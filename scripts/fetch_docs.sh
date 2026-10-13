#!/usr/bin/env bash
# Refresh docs/ from docs.higgsfield.ai (Mintlify serves every page as .md) then rebuild the catalog.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/docs"
curl -sL https://docs.higgsfield.ai/docs/llms.txt -o llms.txt
curl -sL https://docs.higgsfield.ai/docs/llms-full.txt -o llms-full.txt
curl -sL https://docs.higgsfield.ai/docs/openapi.json -o openapi.json
mkdir -p pages
curl -sL https://docs.higgsfield.ai/docs/sitemap.xml | grep -oE '<loc>[^<]+' | sed 's/<loc>//' | while read -r u; do
  p="${u#https://docs.higgsfield.ai/docs}"; p="${p#/}"; [ -z "$p" ] && p=index
  curl -sL "$u.md" -o "pages/$(echo "$p" | tr '/' '_').md"
done
echo "fetched $(ls pages | wc -l | tr -d ' ') pages"
python3 -I "$ROOT/scripts/build_catalog.py"
