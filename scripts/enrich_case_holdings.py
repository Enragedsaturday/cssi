#!/usr/bin/env python3
"""
S4 · Job 1 — enrich every case page's frontmatter with a `holding:` field.

The verified one-line holding for each case lives in
`content/2-legal-system-research/Case Index.md` (Holding column). This script
maps each case page (by title, then aliases) to its Case-Index holding and
writes it into the page's frontmatter as

    holding: "<one-line ratio>"

The value is emitted with json.dumps (ensure_ascii=False) so it is a valid
YAML double-quoted scalar (YAML is a superset of JSON) regardless of embedded
quotes/colons, and round-trips losslessly via json.loads in the index builder.

If a page cannot be matched to a Case-Index holding, a concise one-liner is
derived from the page's `## Rule` section and the page is FLAGGED (reported).

Stdlib only. Idempotent: re-running replaces an existing `holding:` line.

Usage: python3 scripts/enrich_case_holdings.py [--dry-run]
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "lint"))
import _common as c  # noqa: E402

INDEX = os.path.join(REPO, "content", "2-legal-system-research", "Case Index.md")
CASES_GLOB = os.path.join(REPO, "content", "cases", "*.md")


def norm(s):
    n = (s or "").strip().lower().replace("’", "'")
    n = re.sub(r"\s+", " ", n)
    return n


def parse_index_holdings():
    """name (normalized) -> verified one-line holding (raw cell text)."""
    out = {}
    for ln in c.read_text(INDEX).split("\n"):
        if not ln.startswith("|") or ln.startswith("|---") or "| Case |" in ln:
            continue
        cells = [p.strip() for p in ln.split("|")[1:-1]]
        if len(cells) != 5:
            continue
        caption, holding = cells[0], cells[1]
        cap = caption.strip().strip("*").strip()
        m = re.search(r",\s*\d", cap)          # cut at the reporter volume
        name = cap[:m.start()].strip() if m else cap
        if holding:
            out[norm(name)] = holding
    return out


def derive_from_rule(body):
    """Fallback one-liner from the ## Rule section (concise, stripped)."""
    lines = body.split("\n")
    grab = []
    in_rule = False
    for ln in lines:
        if re.match(r"^##\s+Rule\b", ln):
            in_rule = True
            continue
        if in_rule:
            if ln.startswith("## "):
                break
            if ln.strip():
                grab.append(ln.strip())
    text = " ".join(grab)
    # strip markdown emphasis, wikilinks, pin anchors, reporter pincite tails
    text = re.sub(r"\^pin-[A-Za-z0-9]+", "", text)
    text = re.sub(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", r"\1", text)
    text = re.sub(r"\*\*?([^*]*)\*\*?", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    # first sentence (up to the first ". " that is not an abbrev like "U.S.")
    m = re.search(r"\.\s+[A-Z]", text)
    if m:
        text = text[:m.start() + 1]
    return text[:300].strip()


def upsert_holding(path, holding):
    text = c.read_text(path)
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise RuntimeError("no frontmatter: %s" % path)
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    new_line = "holding: " + json.dumps(holding, ensure_ascii=False)
    # replace an existing top-level holding: line, else insert before closing ---
    for i in range(1, end):
        if re.match(r"^holding\s*:", lines[i]):
            if lines[i] == new_line:
                return False  # already current
            lines[i] = new_line
            c_write(path, "\n".join(lines))
            return True
    lines.insert(end, new_line)
    c_write(path, "\n".join(lines))
    return True


def c_write(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    dry = "--dry-run" in sys.argv[1:]
    idx = parse_index_holdings()
    pages = sorted(glob.glob(CASES_GLOB))
    matched = derived = changed = 0
    derived_pages = []
    for p in pages:
        fm, body, _ = c.split_frontmatter(c.read_text(p))
        title = fm.get("title", "") or os.path.splitext(os.path.basename(p))[0]
        aliases = fm.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        keys = [norm(title)] + [norm(a) for a in aliases]
        holding = next((idx[k] for k in keys if k in idx), None)
        if holding is not None:
            matched += 1
        else:
            holding = derive_from_rule(body)
            derived += 1
            derived_pages.append(title)
        if not dry:
            if upsert_holding(p, holding):
                changed += 1
    print("pages:            %d" % len(pages))
    print("index-matched:    %d" % matched)
    print("rule-derived:     %d" % derived)
    print("frontmatter changed: %d" % changed)
    if derived_pages:
        print("\nFLAGGED (rule-derived, verify):")
        for t in derived_pages:
            print("  -", t)


if __name__ == "__main__":
    main()
