"""Thin HTTP client for the Higgsfield API (https://api.higgsfield.ai).

Implements the documented request lifecycle: submit -> poll status_url with
backoff -> terminal state; plus cancel, estimate, presigned uploads, SOUL styles,
Marketing Studio presets and Soul ID character references.
"""
from __future__ import annotations

import asyncio
import mimetypes
import os
import random
import uuid
from pathlib import Path
from typing import Any

import httpx

BASE_URL = "https://api.higgsfield.ai"
TERMINAL = {"completed", "failed", "nsfw", "canceled"}
UPLOAD_TYPES = {
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp",
    ".gif": "image/gif", ".wav": "audio/wav", ".mp4": "video/mp4",
}


class HiggsfieldError(RuntimeError):
    def __init__(self, status: int, detail: Any, correlation_id: str | None = None):
        self.status, self.detail, self.correlation_id = status, detail, correlation_id
        super().__init__(f"HTTP {status}: {detail} (X-Correlation-ID={correlation_id})")


def load_dotenv(path: Path) -> None:
    """Minimal .env loader; never overrides variables already set in the environment."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _validate_path(p: str) -> Path:
    path = Path(p).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"not a file: {p}")
    return path


class HiggsfieldClient:
    def __init__(self, key_id: str | None = None, key_secret: str | None = None, base_url: str = BASE_URL):
        key_id = key_id or os.environ.get("HF_API_KEY_ID")
        key_secret = key_secret or os.environ.get("HF_API_KEY_SECRET")
        if not key_id or not key_secret:
            combo = os.environ.get("HF_KEY") or os.environ.get("HF_CREDENTIALS") or ""
            if ":" in combo:
                key_id, key_secret = combo.split(":", 1)
        if not key_id or not key_secret:
            raise RuntimeError("Set HF_API_KEY_ID and HF_API_KEY_SECRET (env or .env)")
        self.base_url = base_url.rstrip("/")
        self._auth = {"Authorization": f"Key {key_id}:{key_secret}"}
        self._http = httpx.AsyncClient(timeout=httpx.Timeout(60.0, connect=15.0))

    async def aclose(self) -> None:
        await self._http.aclose()

    # ---- low level -------------------------------------------------------
    async def _req(self, method: str, url: str, *, json: Any = None, params: dict | None = None,
                   headers: dict | None = None, retries: int = 3) -> Any:
        if url.startswith("/"):
            url = self.base_url + url
        h = {**self._auth, **(headers or {})}
        delay = 1.0
        for attempt in range(retries + 1):
            try:
                r = await self._http.request(method, url, json=json, params=params, headers=h)
            except (httpx.TransportError,) as e:
                if attempt == retries:
                    raise HiggsfieldError(0, f"network error: {e}")
                await asyncio.sleep(delay + random.uniform(0, 0.5)); delay *= 2
                continue
            cid = r.headers.get("X-Correlation-ID")
            if r.status_code >= 500 and attempt < retries:
                await asyncio.sleep(delay + random.uniform(0, 0.5)); delay *= 2
                continue
            if r.status_code >= 400:
                try:
                    detail = r.json().get("detail", r.text)
                except Exception:
                    detail = r.text
                raise HiggsfieldError(r.status_code, detail, cid)
            if r.status_code == 202 or not r.content:
                return {"ok": True, "http_status": r.status_code, "correlation_id": cid}
            data = r.json()
            if isinstance(data, dict):
                data.setdefault("correlation_id", cid)
            return data
        raise HiggsfieldError(0, "unreachable")

    # ---- generation lifecycle -------------------------------------------
    async def submit(self, endpoint_id: str, params: dict, *, webhook_url: str | None = None,
                     idempotency_key: str | None = None) -> dict:
        headers = {"Content-Type": "application/json",
                   "Idempotency-Key": idempotency_key or str(uuid.uuid4())}
        query = {"hf_webhook": webhook_url} if webhook_url else None
        res = await self._req("POST", "/" + endpoint_id.strip("/"), json=params, params=query, headers=headers)
        res["idempotency_key"] = headers["Idempotency-Key"]
        return res

    async def status(self, request_id: str) -> dict:
        return await self._req("GET", f"/requests/{request_id}/status")

    async def cancel(self, request_id: str) -> dict:
        return await self._req("POST", f"/requests/{request_id}/cancel")

    async def wait(self, request_id: str, *, timeout: float = 600.0, status_url: str | None = None) -> dict:
        """Poll until terminal, following the documented 2s -> 10s backoff with jitter."""
        loop = asyncio.get_event_loop()
        deadline = loop.time() + timeout
        delay = 2.0
        url = status_url or f"/requests/{request_id}/status"
        while True:
            res = await self._req("GET", url)
            if res.get("status") in TERMINAL:
                return res
            if loop.time() >= deadline:
                res["timed_out"] = True
                res["hint"] = f"still {res.get('status')} after {timeout}s; call hf_status/hf_wait again with this request_id"
                return res
            await asyncio.sleep(min(delay + random.uniform(0, 0.5), max(0.0, deadline - loop.time())))
            delay = min(delay * 1.5, 10.0)

    async def estimate(self, endpoint_id: str, params: dict) -> dict:
        return await self._req("POST", "/estimate/" + endpoint_id.strip("/"), json=params,
                               headers={"Content-Type": "application/json"})

    # ---- uploads ---------------------------------------------------------
    async def upload_file(self, local_path: str, content_type: str | None = None) -> dict:
        path = _validate_path(local_path)
        ct = content_type or UPLOAD_TYPES.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0]
        if not ct:
            raise ValueError(f"cannot infer content type for {path.name}; pass content_type")
        info = await self._req("POST", "/files/generate-upload-url", json={"content_type": ct},
                               headers={"Content-Type": "application/json"})
        up_headers = info.get("upload_headers") or {"Content-Type": ct}
        with path.open("rb") as fh:
            r = await self._http.put(info["upload_url"], content=fh.read(), headers=up_headers, timeout=300)
        if r.status_code >= 300:
            raise HiggsfieldError(r.status_code, f"upload failed: {r.text[:300]}")
        return {"public_url": info["public_url"], "content_type": ct, "bytes": path.stat().st_size,
                "source": str(path)}

    async def download(self, url: str, dest_dir: str, filename: str | None = None) -> str:
        d = Path(dest_dir).expanduser().resolve()
        d.mkdir(parents=True, exist_ok=True)
        name = filename or Path(httpx.URL(url).path).name or f"output-{uuid.uuid4().hex[:8]}"
        name = Path(name).name  # strip any directory components
        target = d / name
        async with self._http.stream("GET", url, timeout=300) as r:
            r.raise_for_status()
            with target.open("wb") as fh:
                async for chunk in r.aiter_bytes():
                    fh.write(chunk)
        return str(target)

    # ---- helper catalogs -------------------------------------------------
    async def soul_styles(self, version: str = "v2") -> Any:
        path = "/v1/text2image/soul-styles" + ("/v2" if version == "v2" else "")
        return await self._req("GET", path)

    async def marketing_presets(self, search: str | None = None, size: int = 50, cursor: int = 0) -> Any:
        params: dict[str, Any] = {"size": size, "cursor": cursor}
        if search:
            params["search"] = search
        return await self._req("GET", "/marketing-studio/image/presets", params=params)

    async def create_character(self, name: str, image_urls: list[str], model_version: str = "v1") -> dict:
        body = {"name": name, "model_version": model_version,
                "input_images": [{"type": "image_url", "image_url": u} for u in image_urls]}
        return await self._req("POST", "/v1/custom-references", json=body,
                               headers={"Content-Type": "application/json"})

    async def get_character(self, reference_id: str) -> dict:
        return await self._req("GET", f"/v1/custom-references/{reference_id}")
