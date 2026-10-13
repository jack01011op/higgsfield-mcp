"""Higgsfield MCP server.

Exposes:
  * shared lifecycle tools  (hf_submit, hf_status, hf_wait, hf_cancel, hf_estimate, hf_upload_file, hf_download)
  * helper catalogs         (hf_list_models, hf_describe_model, hf_soul_styles, hf_marketing_presets,
                             hf_create_character, hf_get_character)
  * documentation           (hf_docs_read, hf_docs_search, hf_docs_index)
  * ONE TOOL PER MODEL ENDPOINT generated from catalog.json (84 at build time), each accepting the exact
    documented parameters plus hf_wait / hf_timeout_seconds / hf_webhook_url / hf_idempotency_key / hf_download_dir.
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any

import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server

from . import docs
from .client import TERMINAL, HiggsfieldClient, HiggsfieldError, load_dotenv

PKG_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PKG_DIR.parents[1]
CATALOG: dict = json.loads((PKG_DIR / "catalog.json").read_text())
MODELS: dict[str, dict] = {m["tool"]: m for m in CATALOG["models"]}
BY_ENDPOINT: dict[str, dict] = {m["endpoint_id"]: m for m in CATALOG["models"]}

CONTROL_FIELDS = {
    "hf_wait": {"type": "boolean", "default": True,
                "description": "Poll until the request is terminal (completed/failed/nsfw/canceled). False returns the request handle immediately."},
    "hf_timeout_seconds": {"type": "number", "default": 600,
                           "description": "Max seconds to wait when hf_wait is true. On timeout the current status is returned; resume with hf_wait/hf_status."},
    "hf_webhook_url": {"type": "string", "description": "Optional HTTPS webhook URL (sent as the hf_webhook query parameter)."},
    "hf_idempotency_key": {"type": "string", "description": "Optional Idempotency-Key. A fresh UUID is generated when omitted; reuse only to retry the identical request."},
    "hf_download_dir": {"type": "string", "description": "If set and the request completes, download every output file into this local directory and return the paths."},
}

_client: HiggsfieldClient | None = None


def client() -> HiggsfieldClient:
    global _client
    if _client is None:
        load_dotenv(PROJECT_DIR / ".env")
        _client = HiggsfieldClient()
    return _client


# --------------------------------------------------------------------------- schema helpers
def _model_tool(m: dict) -> types.Tool:
    schema = json.loads(json.dumps(m["schema"]))  # deep copy
    schema.setdefault("type", "object")
    props = schema.setdefault("properties", {})
    if m["category"] != "training":
        for k, v in CONTROL_FIELDS.items():
            props.setdefault(k, v)
    schema.pop("title", None)
    notes = "\n".join(f"- {n}" for n in m["usage_notes"][:6])
    desc = (f"{m['title']}. {m['description']} Endpoint: {m['method']} {m['path']} (id `{m['endpoint_id']}`). "
            f"Output: {m['output']}. Docs: {m['docs_url']}")
    if notes:
        desc += "\nUsage notes:\n" + notes
    return types.Tool(name=m["tool"], description=desc[:4000], input_schema=schema)


def _obj(props: dict, required: list[str] | None = None) -> dict:
    return {"type": "object", "properties": props, "required": required or []}


GENERIC_TOOLS: list[types.Tool] = [
    types.Tool(name="hf_list_models", description=(
        f"List the {CATALOG['count']} Higgsfield model endpoints available as tools (tool name, endpoint id, family, "
        "category image/video/training, output type, required params). Filter by category or free-text search."),
        input_schema=_obj({"category": {"type": "string", "enum": ["image", "video", "training", "all"], "default": "all"},
                          "search": {"type": "string", "description": "Substring match on tool name, endpoint id, title or family."}})),
    types.Tool(name="hf_describe_model", description="Full documented input JSON schema, usage notes, example body and docs URL for one model endpoint (by tool name or endpoint id).",
               input_schema=_obj({"model": {"type": "string", "description": "Tool name (e.g. kling_video_v3_0_pro_image_to_video) or endpoint id (e.g. kling-video/v3.0/pro/image-to-video)."}}, ["model"])),
    types.Tool(name="hf_submit", description="Submit a generation to ANY endpoint id with a raw params object (use when a model is not in the catalog). Returns the request handle (request_id, status_url, cancel_url).",
               input_schema=_obj({"endpoint_id": {"type": "string"}, "params": {"type": "object"},
                                 "webhook_url": {"type": "string"}, "idempotency_key": {"type": "string"},
                                 "wait": {"type": "boolean", "default": False}, "timeout_seconds": {"type": "number", "default": 600}}, ["endpoint_id", "params"])),
    types.Tool(name="hf_status", description="GET /requests/{request_id}/status — current state and output URLs of a request.",
               input_schema=_obj({"request_id": {"type": "string"}}, ["request_id"])),
    types.Tool(name="hf_wait", description="Poll a request with documented backoff (2s→10s + jitter) until terminal or timeout.",
               input_schema=_obj({"request_id": {"type": "string"}, "timeout_seconds": {"type": "number", "default": 600},
                                 "download_dir": {"type": "string"}}, ["request_id"])),
    types.Tool(name="hf_cancel", description="POST /requests/{request_id}/cancel — cancel a request that is still queued (202 on success, 400 if already processing).",
               input_schema=_obj({"request_id": {"type": "string"}}, ["request_id"])),
    types.Tool(name="hf_estimate", description="POST /estimate/{endpoint_id} — credits and USD cost estimate for given params, without generating.",
               input_schema=_obj({"endpoint_id": {"type": "string"}, "params": {"type": "object"}}, ["endpoint_id", "params"])),
    types.Tool(name="hf_upload_file", description="Upload a local image/audio/video file via a presigned URL (jpeg/png/webp/gif/wav/mp4) and return a public_url usable as image_url/video_url/audio_url.",
               input_schema=_obj({"path": {"type": "string"}, "content_type": {"type": "string"}}, ["path"])),
    types.Tool(name="hf_download", description="Download an output URL to a local directory (outputs are retained ~7 days). Returns the saved path.",
               input_schema=_obj({"url": {"type": "string"}, "dest_dir": {"type": "string", "description": "Defaults to $HF_DOWNLOAD_DIR"},
                                 "filename": {"type": "string"}}, ["url"])),
    types.Tool(name="hf_soul_styles", description="GET SOUL style_id catalog (v1 or v2) for the soul text-to-image endpoints.",
               input_schema=_obj({"version": {"type": "string", "enum": ["v1", "v2"], "default": "v2"}})),
    types.Tool(name="hf_marketing_presets", description="GET /marketing-studio/image/presets — preset_id values for Marketing Studio enhanced requests (search, size, cursor).",
               input_schema=_obj({"search": {"type": "string"}, "size": {"type": "integer", "default": 50}, "cursor": {"type": "integer", "default": 0}})),
    types.Tool(name="hf_create_character", description="Soul ID: POST /v1/custom-references — train a reusable character from 1–100 public image URLs. Poll with hf_get_character, then pass id as custom_reference_id to a SOUL endpoint.",
               input_schema=_obj({"name": {"type": "string", "maxLength": 100}, "image_urls": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 100},
                                 "model_version": {"type": "string", "enum": ["v1", "v2", "cinema"], "default": "v1"}}, ["name", "image_urls"])),
    types.Tool(name="hf_get_character", description="GET /v1/custom-references/{id} — training status (not_ready/queued/in_progress/completed/failed) of a Soul ID character.",
               input_schema=_obj({"reference_id": {"type": "string"}}, ["reference_id"])),
    types.Tool(name="hf_docs_index", description="List all bundled Higgsfield documentation pages (offline copy of docs.higgsfield.ai).", input_schema=_obj({})),
    types.Tool(name="hf_docs_read", description="Read one documentation page by slug or URL path, e.g. 'authentication', 'concepts/polling', 'models/kling-3/pro-image-to-video'.",
               input_schema=_obj({"page": {"type": "string"}}, ["page"])),
    types.Tool(name="hf_docs_search", description="Full-text search across all documentation pages; returns matching snippets.",
               input_schema=_obj({"query": {"type": "string"}, "max_hits": {"type": "integer", "default": 20}}, ["query"])),
]


def all_tools() -> list[types.Tool]:
    return GENERIC_TOOLS + [_model_tool(m) for m in CATALOG["models"]]


TOOL_INDEX: dict[str, types.Tool] = {t.name: t for t in all_tools()}


# --------------------------------------------------------------------------- execution
def _summary(m: dict) -> dict:
    return {"tool": m["tool"], "endpoint_id": m["endpoint_id"], "title": m["title"], "family": m["family"],
            "category": m["category"], "output": m["output"], "required": m["schema"].get("required", []),
            "params": sorted(m["schema"].get("properties", {}).keys())}


def _find_model(key: str) -> dict:
    m = MODELS.get(key) or BY_ENDPOINT.get(key.strip("/"))
    if not m:
        close = [k for k in MODELS if key.lower().replace("-", "_").replace("/", "_").replace(".", "_") in k]
        raise ValueError(f"unknown model '{key}'. Close matches: {close[:10]} — use hf_list_models")
    return m


async def _download_outputs(res: dict, dest: str) -> dict:
    urls: list[str] = []
    for img in res.get("images") or []:
        if img.get("url"):
            urls.append(img["url"])
    for key in ("video", "audio", "zip", "mov", "jsx", "fbx", "ply"):
        if isinstance(res.get(key), dict) and res[key].get("url"):
            urls.append(res[key]["url"])
    for a in res.get("audios") or []:
        if a.get("url"):
            urls.append(a["url"])
    paths = []
    for u in urls:
        try:
            paths.append(await client().download(u, dest))
        except Exception as e:  # keep going; report per-file failure
            paths.append(f"ERROR downloading {u}: {e}")
    res["downloaded_files"] = paths
    return res


async def _run_generation(endpoint_id: str, params: dict, *, wait: bool, timeout: float,
                          webhook: str | None, idem: str | None, download_dir: str | None) -> dict:
    handle = await client().submit(endpoint_id, params, webhook_url=webhook, idempotency_key=idem)
    if not wait:
        return handle
    res = await client().wait(handle["request_id"], timeout=timeout, status_url=handle.get("status_url"))
    res["idempotency_key"] = handle.get("idempotency_key")
    if download_dir and res.get("status") == "completed":
        await _download_outputs(res, download_dir)
    return res


async def _dispatch(name: str, a: dict) -> Any:
    if name in MODELS:
        m = MODELS[name]
        if m["category"] == "training":
            return await client()._req("POST", m["path"], json=a, headers={"Content-Type": "application/json"})
        ctrl = {k: a.pop(k, None) for k in CONTROL_FIELDS}
        return await _run_generation(
            m["endpoint_id"], a, wait=ctrl["hf_wait"] is not False,
            timeout=float(ctrl["hf_timeout_seconds"] or 600), webhook=ctrl["hf_webhook_url"],
            idem=ctrl["hf_idempotency_key"], download_dir=ctrl["hf_download_dir"])
    c = client
    match name:
        case "hf_list_models":
            cat, q = a.get("category", "all"), (a.get("search") or "").lower()
            out = [_summary(m) for m in CATALOG["models"]
                   if (cat in ("all", None) or m["category"] == cat)
                   and (not q or q in f"{m['tool']} {m['endpoint_id']} {m['title']} {m['family']}".lower())]
            return {"count": len(out), "models": out}
        case "hf_describe_model":
            m = _find_model(a["model"])
            return {k: m[k] for k in ("tool", "endpoint_id", "method", "path", "title", "family", "category",
                                      "output", "docs_url", "usage_notes", "example", "schema")}
        case "hf_submit":
            return await _run_generation(a["endpoint_id"], a["params"], wait=bool(a.get("wait")),
                                         timeout=float(a.get("timeout_seconds") or 600),
                                         webhook=a.get("webhook_url"), idem=a.get("idempotency_key"), download_dir=None)
        case "hf_status":
            return await c().status(a["request_id"])
        case "hf_wait":
            res = await c().wait(a["request_id"], timeout=float(a.get("timeout_seconds") or 600))
            if a.get("download_dir") and res.get("status") == "completed":
                await _download_outputs(res, a["download_dir"])
            return res
        case "hf_cancel":
            return await c().cancel(a["request_id"])
        case "hf_estimate":
            return await c().estimate(a["endpoint_id"], a["params"])
        case "hf_upload_file":
            return await c().upload_file(a["path"], a.get("content_type"))
        case "hf_download":
            dest = a.get("dest_dir") or os.environ.get("HF_DOWNLOAD_DIR") or str(PROJECT_DIR / "downloads")
            return {"path": await c().download(a["url"], dest, a.get("filename"))}
        case "hf_soul_styles":
            return await c().soul_styles(a.get("version", "v2"))
        case "hf_marketing_presets":
            return await c().marketing_presets(a.get("search"), int(a.get("size", 50)), int(a.get("cursor", 0)))
        case "hf_create_character":
            return await c().create_character(a["name"], a["image_urls"], a.get("model_version", "v1"))
        case "hf_get_character":
            return await c().get_character(a["reference_id"])
        case "hf_docs_index":
            return {"pages": docs.list_pages(), "hint": "hf_docs_read(page) for content; model pages are models_<family>_<workflow>"}
        case "hf_docs_read":
            return docs.read_page(a["page"])
        case "hf_docs_search":
            return docs.search(a["query"], int(a.get("max_hits", 20)))
    raise ValueError(f"unknown tool {name}")


async def call_tool(name: str, arguments: dict | None) -> types.CallToolResult:
    is_error = False
    try:
        result = await _dispatch(name, dict(arguments or {}))
    except HiggsfieldError as e:
        is_error = True
        result = {"error": True, "http_status": e.status, "detail": e.detail, "correlation_id": e.correlation_id}
    except (ValueError, FileNotFoundError, RuntimeError, KeyError) as e:
        is_error = True
        result = {"error": True, "detail": f"{type(e).__name__}: {e}"}
    text = result if isinstance(result, str) else json.dumps(result, indent=2, ensure_ascii=False, default=str)
    return types.CallToolResult(content=[types.TextContent(type="text", text=text)], is_error=is_error)


# --------------------------------------------------------------------------- MCP wiring (mcp>=2 low-level API)
async def _on_list_tools(ctx: Any, params: Any) -> types.ListToolsResult:
    return types.ListToolsResult(tools=list(TOOL_INDEX.values()))


async def _on_call_tool(ctx: Any, params: types.CallToolRequestParams) -> types.CallToolResult:
    return await call_tool(params.name, params.arguments)


def _tool_input_schema(name: str) -> dict | None:
    t = TOOL_INDEX.get(name)
    return None if t is None else t.input_schema


server = Server(
    name="higgsfield",
    version="0.1.0",
    instructions=(f"Higgsfield API as tools. {CATALOG['count']} model endpoints are exposed one-per-tool; call hf_list_models "
                  "to browse, hf_describe_model for a schema, and hf_docs_search/hf_docs_read for the full docs. Generation "
                  "is async: model tools wait by default (hf_wait=true) and return output URLs; set hf_download_dir to save "
                  "files locally. Upload local inputs with hf_upload_file first."),
    get_tool_input_schema=_tool_input_schema,
    on_list_tools=_on_list_tools,
    on_call_tool=_on_call_tool,
)


async def _serve() -> None:
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


def main() -> None:
    try:
        asyncio.run(_serve())
    except KeyboardInterrupt:
        pass
    finally:
        if _client is not None:
            try:
                asyncio.run(_client.aclose())
            except Exception:
                pass


if __name__ == "__main__":
    sys.exit(main())
