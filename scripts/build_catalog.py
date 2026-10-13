"""Build src/higgsfield_mcp/catalog.json from the Mintlify markdown pages in docs/pages.

Re-run after refreshing docs/pages (see scripts/fetch_docs.sh) so every model
endpoint documented by Higgsfield becomes an MCP tool.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "docs" / "pages"
OUT = ROOT / "src" / "higgsfield_mcp" / "catalog.json"

RE_TITLE = re.compile(r"^# (.+)$", re.M)
RE_DESC = re.compile(r"^> (.+)$", re.M)
RE_ENDPOINT = re.compile(r"\*\*Endpoint:\*\* `(POST|GET) https://api\.higgsfield\.ai(/[^`]+)`")
RE_ENDPOINT_ID = re.compile(r"\*\*(?:Endpoint|Catalog) ID:\*\* `([^`]+)`")
RE_FAMILY = re.compile(r"^\[← (.+?)\]\(/docs/models/([^)]+)\)", re.M)
RE_SCHEMA = re.compile(r'<Accordion title="Complete JSON schema">\s*```json\s*(\{.*?\})\s*```\s*</Accordion>', re.S)
RE_NOTES = re.compile(r"^## Usage notes\s*\n(.*?)(?=^## )", re.S | re.M)
RE_OUTPUT = re.compile(r'"status": "completed",\s*"request_id": "REQUEST_ID",(?:\s*"status_url"[^\n]*\n\s*"cancel_url"[^\n]*\n)?\s*"(images|video|audio|audios)"')
RE_CURL_BODY = re.compile(r"```bash cURL.*?--data '(\{.*?\})'\s*```", re.S)
RE_PARAM = re.compile(r'<ParamField body="([^"]+)" type="([^"]+)"( required)?(?: default="([^"]*)")?>\s*(.*?)\s*</ParamField>', re.S)


def tool_name(endpoint_id: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9]+", "_", endpoint_id).strip("_")
    return name[:64]


def clean_notes(block: str) -> list[str]:
    notes = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("* "):
            notes.append(line[2:].replace("\\_", "_").replace("\\{", "{").replace("\\}", "}"))
    return notes


def parse_params_fallback(md: str) -> dict:
    """Build a JSON schema from <ParamField> tags when no accordion schema exists."""
    props, required = {}, []
    for name, typ, req, default, body in RE_PARAM.findall(md):
        if "[]" in name:
            continue  # nested fields are described in parent description
        t = typ.split("|")[0].strip()
        jt = {"string": "string", "integer": "integer", "number": "number", "boolean": "boolean", "array": "array", "object": "object"}.get(t, "string")
        desc = re.sub(r"<[^>]+>", "", body)
        desc = " ".join(l.strip() for l in desc.splitlines() if l.strip())
        p: dict = {"type": jt, "description": desc.replace("\\_", "_")}
        if "null" in typ:
            p["type"] = [jt, "null"]
        if jt == "array":
            p["items"] = {"type": "string"}
        m = re.search(r"Allowed values: (.+?)\.", desc)
        if m:
            vals = re.findall(r"`([^`]+)`", m.group(1))
            if vals:
                try:
                    p["enum"] = [json.loads(v) for v in vals]
                except json.JSONDecodeError:
                    p["enum"] = vals
        if default is not None and default != "":
            try:
                p["default"] = json.loads(default)
            except json.JSONDecodeError:
                p["default"] = default
        props[name] = p
        if req:
            required.append(name)
    return {"type": "object", "properties": props, "required": required}


def parse_page(path: Path) -> dict | None:
    md = path.read_text()
    m_ep = RE_ENDPOINT.search(md)
    if not m_ep:
        return None
    method, api_path = m_ep.groups()
    m_id = RE_ENDPOINT_ID.search(md)
    endpoint_id = m_id.group(1) if m_id else api_path.strip("/")
    title = RE_TITLE.search(md).group(1).strip()
    desc_m = RE_DESC.search(md)
    fam = RE_FAMILY.search(md)
    schema_m = RE_SCHEMA.search(md)
    if schema_m:
        schema = json.loads(schema_m.group(1))
    else:
        schema = parse_params_fallback(md)
    notes_m = RE_NOTES.search(md + "\n## END")
    out_m = RE_OUTPUT.search(md)
    curl_m = RE_CURL_BODY.search(md)
    example = None
    if curl_m:
        try:
            example = json.loads(curl_m.group(1))
        except json.JSONDecodeError:
            example = None
    slug = path.stem.replace("models_", "", 1).replace("_", "/")
    is_training = api_path.startswith("/v1/custom-references")
    if out_m:
        output = out_m.group(1)
    elif is_training:
        output = "character_reference"
    else:
        output = "video" if "video" in path.stem else "images"
    category = "training" if is_training else ("image" if output == "images" else ("video" if output == "video" else "audio"))
    return {
        "tool": tool_name(endpoint_id),
        "endpoint_id": endpoint_id,
        "method": method,
        "path": api_path,
        "title": title,
        "description": desc_m.group(1).strip() if desc_m else "",
        "family": fam.group(1) if fam else None,
        "family_slug": fam.group(2) if fam else None,
        "category": category,
        "output": output,
        "docs_url": f"https://docs.higgsfield.ai/docs/models/{slug}",
        "docs_page": path.name,
        "usage_notes": clean_notes(notes_m.group(1)) if notes_m else [],
        "example": example,
        "schema": schema,
    }


def main() -> None:
    entries = []
    for p in sorted(PAGES.glob("models_*.md")):
        e = parse_page(p)
        if e:
            entries.append(e)
    names = [e["tool"] for e in entries]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        sys.exit(f"duplicate tool names: {dupes}")
    catalog = {
        "source": "https://docs.higgsfield.ai/docs/llms.txt",
        "base_url": "https://api.higgsfield.ai",
        "count": len(entries),
        "models": entries,
    }
    OUT.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")
    cats = {}
    for e in entries:
        cats[e["category"]] = cats.get(e["category"], 0) + 1
    print(f"wrote {OUT} with {len(entries)} endpoints: {cats}")
    missing_req = [e["endpoint_id"] for e in entries if "properties" not in e["schema"]]
    if missing_req:
        print("WARNING schema without properties:", missing_req)


if __name__ == "__main__":
    main()
