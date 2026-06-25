#!/usr/bin/env python3
"""Validate + merge the per-page flashcard decks into the published flashcards.json.
Durable home for the CSSI deck source. Run after adding/editing decks in ./decks/.
  python3 flashcard-src/merge.py
Auto-bumps the deck version (YYYY-MM-DD.N) so the in-browser app migrates by id
(keeps study progress for surviving card ids, adds new ids as New)."""
import os, json, sys, collections, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DECKS = os.path.join(HERE, "decks")
OUT = os.path.normpath(os.path.join(HERE, "..", "quartz", "static", "flashcards", "flashcards.json"))
REQUIRED = {"id", "page", "topic", "type", "front", "back", "tags"}
TYPES = {"qa", "cloze", "definition"}


def next_version():
    today = datetime.date.today().isoformat()
    try:
        cur = json.load(open(OUT, encoding="utf-8")).get("version", "")
    except Exception:
        cur = ""
    if cur.startswith(today + "."):
        try:
            return f"{today}.{int(cur.split('.')[-1]) + 1}"
        except ValueError:
            pass
    return f"{today}.1"


def main():
    errors, all_cards, ids = [], [], set()
    per_page, per_type = collections.Counter(), collections.Counter()
    files = sorted(f for f in os.listdir(DECKS) if f.endswith(".json"))
    print(f"decks: {len(files)}")
    for fn in files:
        try:
            data = json.load(open(os.path.join(DECKS, fn), encoding="utf-8"))
        except Exception as e:
            errors.append(f"{fn}: JSON parse error: {e}"); continue
        if not isinstance(data, list):
            errors.append(f"{fn}: top-level is not an array"); continue
        slug, n = fn[:-5], 0
        for i, c in enumerate(data):
            miss = REQUIRED - set(c)
            if miss: errors.append(f"{fn}#{i}: missing {miss}"); continue
            if c["type"] not in TYPES: errors.append(f"{fn}#{i} {c.get('id')}: bad type {c['type']!r}")
            if not isinstance(c["tags"], list): errors.append(f"{fn}#{i} {c.get('id')}: tags not list")
            if c["id"] in ids: errors.append(f"{fn}: DUPLICATE id {c['id']}"); continue
            if not c["id"].startswith(slug): errors.append(f"{fn}: id {c['id']} not prefixed with {slug!r}")
            ids.add(c["id"]); per_page[c["page"]] += 1; per_type[c["type"]] += 1
            card = {k: c[k] for k in ["id", "page", "topic", "type", "front", "back", "tags"]}
            if c.get("cite"): card["cite"] = c["cite"]
            if c.get("source"): card["source"] = c["source"]
            all_cards.append(card); n += 1
        print(f"  {fn}: {n}")
    for p, n in sorted(per_page.items()): print(f"    {p}: {n}")
    print("types:", dict(per_type), "| TOTAL:", len(all_cards))
    if errors:
        print("\n!!! ERRORS:"); [print("  " + e) for e in errors]; sys.exit(1)
    version = sys.argv[1] if len(sys.argv) > 1 else next_version()
    deck = {"version": version, "title": "CSSI — Search & Seizure", "cards": all_cards}
    json.dump(deck, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nWROTE {OUT}  ({len(all_cards)} cards, version {version})")


if __name__ == "__main__":
    main()
