import asyncio
import json
import re
from pathlib import Path

from higgsfield_mcp import server

NAME_RE = re.compile(r"^[a-zA-Z0-9_-]{1,64}$")


def test_catalog_shape():
    assert server.CATALOG["count"] == len(server.CATALOG["models"]) >= 80
    for m in server.CATALOG["models"]:
        assert NAME_RE.match(m["tool"]), m["tool"]
        assert m["path"].startswith("/")
        assert m["schema"]["type"] == "object"
        assert "properties" in m["schema"]


def test_tools_unique_and_serializable():
    import asyncio
    tools = server.all_tools()
    names = [t.name for t in tools]
    assert len(names) == len(set(names))
    assert "hf_submit" in names and "kling_video_v3_0_pro_image_to_video" in names
    json.dumps([t.model_dump() for t in tools])


def test_control_fields_injected_only_for_generation():
    m = server.MODELS["higgsfield_ai_soul_v2_standard"]
    t = server._model_tool(m)
    assert "hf_wait" in t.input_schema["properties"] and "prompt" in t.input_schema["required"]
    soul_id = server._model_tool(server.MODELS["soul_id"])
    assert "hf_wait" not in soul_id.input_schema["properties"]


def test_docs_read_and_search():
    from higgsfield_mcp import docs
    assert "Authorization: Key" in docs.read_page("authentication")
    assert "Kling 3.0" in docs.read_page("models/kling-3/pro-image-to-video")
    assert docs.search("422 Unprocessable")
    assert docs.search("Idempotency-Key")[0]["page"]


def test_dispatch_list_and_describe_offline():
    res = asyncio.run(server.call_tool("hf_list_models", {"category": "image"}))
    data = json.loads(res.content[0].text)
    assert data["count"] >= 15 and not res.is_error
    res = asyncio.run(server.call_tool("hf_describe_model", {"model": "kling-video/v3.0/pro/image-to-video"}))
    assert "image_url" in json.loads(res.content[0].text)["schema"]["required"]
    res = asyncio.run(server.call_tool("hf_describe_model", {"model": "nope"}))
    assert res.is_error
