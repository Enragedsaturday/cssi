#!/bin/zsh
# Redeploy the CSSI site after editing the Obsidian vault.
# Syncs vault pages -> Quartz content, re-applies the site-only Flashcards link, rebuilds.
# The launchd server serves public/ live, so NO restart is needed — just refresh the browser.
set -e
VAULT="/Users/johngalt/Library/Mobile Documents/com~apple~CloudDocs/Main/CSSI"
PROJ="/Users/johngalt/Projects/cssi-quartz"

echo "syncing vault pages -> content/ (excluding internal _conventions.md)…"
for f in "$VAULT"/*.md; do
  b="$(basename "$f")"
  [ "$b" = "_conventions.md" ] && continue
  cp "$f" "$PROJ/content/$b"
done

# Re-apply the site-only 'Study / Flashcards' section to the home page (not in the vault).
/opt/homebrew/bin/python3 - "$PROJ/content/index.md" "$PROJ/quartz/static/flashcards/flashcards.json" <<'PY'
import sys, json
p = sys.argv[1]; s = open(p, encoding="utf-8").read()
try:
    n = len(json.load(open(sys.argv[2], encoding="utf-8")).get("cards", []))
except Exception:
    n = 0
count = f"{n}-card " if n else ""
if "[[flashcards" not in s:
    s = s.rstrip() + (f"\n\n## Study\n- [[flashcards|Flashcards]] — a {count}spaced-repetition deck (FSRS) "
        "covering every case and doctrine on these pages: holdings, verbatim tests, key facts, distinctions, "
        "and pitfalls. Flip with **Space**, grade **1–4**; progress saves on your device.\n")
    open(p, "w", encoding="utf-8").write(s)
    print(f"  re-added Flashcards link to home ({n} cards)")
PY

echo "building…"
cd "$PROJ" && npx quartz build
echo "done — refresh http://johns-mac-studio.tail2e4945.ts.net:8787/  (no server restart needed)"
