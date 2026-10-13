"""Offline access to the Higgsfield docs bundled in docs/ (refresh with scripts/fetch_docs.sh)."""
from __future__ import annotations

import re
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parents[2] / "docs"
PAGES_DIR = DOCS_DIR / "pages"
_STRIP = [
    (re.compile(r"^> ## Documentation Index.*?^> Use this file.*?$\n", re.S | re.M), ""),
    (re.compile(r' theme=\{"theme":\{"light":"github-light","dark":"github-dark"\}\}'), ""),
    (re.compile(r"\n## Related topics.*", re.S), ""),
    (re.compile(r'<div className="models-color-scope"[^>]*/>\n?'), ""),
    (re.compile(r"<a className=\"model-playground-card\".*?</a>\n?", re.S), ""),
]


def clean(md: str) -> str:
    for rx, rep in _STRIP:
        md = rx.sub(rep, md)
    return md.strip()


def list_pages() -> list[str]:
    return sorted(p.stem for p in PAGES_DIR.glob("*.md"))


def read_page(name: str) -> str:
    """name = page slug like 'authentication', 'concepts_polling', 'models_kling-3_pro-image-to-video'
    or a docs URL path like 'concepts/polling'."""
    slug = name.strip().removeprefix("https://docs.higgsfield.ai").removeprefix("/docs/").removeprefix("docs/").strip("/")
    slug = slug.replace("/", "_").removesuffix(".md") or "index"
    path = (PAGES_DIR / f"{slug}.md").resolve()
    if PAGES_DIR not in path.parents or not path.exists():
        hits = [p for p in list_pages() if slug.lower() in p.lower()]
        raise FileNotFoundError(f"no page '{name}'. Close matches: {hits[:15]}")
    return clean(path.read_text())


def search(query: str, max_hits: int = 20) -> list[dict]:
    """Case-insensitive search across all pages. All terms must appear within one paragraph
    (block separated by blank lines); returns the matching paragraphs."""
    terms = [t for t in re.split(r"\s+", query.strip().lower()) if t]
    hits: list[dict] = []
    for p in sorted(PAGES_DIR.glob("*.md")):
        text = clean(p.read_text())
        for para in re.split(r"\n\s*\n", text):
            low = para.lower()
            if all(t in low for t in terms):
                hits.append({"page": p.stem, "snippet": para.strip()[:1200]})
                if len(hits) >= max_hits:
                    return hits
    return hits
