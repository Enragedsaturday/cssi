#!/usr/bin/env python3
"""
S9 P0 — deterministic assertion inventory over content/ (FREE, no CL).

Extracts every tracked assertion (R3 / §5-P0) from every content object and
writes _run/assertion-inventory.json. Each item carries a stable id + source
object + kind. Report counts by class/kind at the end.

Tracked assertions:
  case page   : holding | cl_url | authority_weight | treatment | home | quote(^pin)
  doctrine    : case_row | quote(#^pin deep-link) | mermaid | flag(html-comment) | recent_dev
  glossary    : term_def
  research    : term_anchor | tool_fact
  case_index  : index_row
  nav/index   : (object recorded; no tracked legal assertion)
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # _run/ -> repo root
CONTENT = os.path.join(ROOT, "content")


def rel(p):
    return os.path.relpath(p, ROOT)


def split_fm(txt):
    if txt.startswith("---"):
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
        if m:
            return m.group(1), m.group(2)
    return "", txt


def fm_scalar(fm, key):
    m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % re.escape(key), fm, re.M)
    return m.group(1).strip() if m else None


def classify(path, fm):
    base = os.path.basename(path)
    t = (fm_scalar(fm, "type") or "").strip('"')
    if "/cases/" in path.replace(os.sep, "/"):
        return "case"
    if base == "Case Index.md":
        return "case_index"
    if base == "Common Legal Terms.md":
        return "glossary"
    if base in ("Legal Research Tools.md", "Reading and Citing Cases.md",
                "Verifying Good Law.md"):
        return "research"
    if base == "index.md":
        return "moc" if path.replace(os.sep, "/").endswith("content/index.md") else "nav"
    if t == "doctrine":
        return "doctrine"
    # practical/reference narrative pages (CREW, Three Golden Rules, Federal
    # Court System, Instructor Development, 4A Analysis Checklist)
    return "narrative"


PIN_ANCHOR = re.compile(r"\^(pin-[A-Za-z0-9]+)")
PIN_DEEPLINK = re.compile(r"\[\[[^\]]*#\^(pin-[A-Za-z0-9]+)[^\]]*\]\]")
MERMAID = re.compile(r"^```mermaid\s*$", re.M)
# a case-table data row: first cell contains a [[wikilink]] and row has >= 4 cols
CASEROW = re.compile(r"^\|\s*\*?\[\[")
HEADING3 = re.compile(r"^###\s+(.*)$", re.M)
HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.S)
FLAG_KEYS = re.compile(r"NEW-ASSERTION|new-assertion|field.fram|S6-REFORMAT|"
                       r"new assertion|route through", re.I)


def strip_header_comment(c):
    # ignore the ubiquitous "header line; TreatmentBadge..." render comment
    return "header line" not in c.lower() and "treatmentbadge" not in c.lower()


items = []
counts = {}
per_class_files = {}


def add(cls, kind, path, ident, extra=None):
    d = {"id": ident, "class": cls, "kind": kind, "object": rel(path)}
    if extra:
        d.update(extra)
    items.append(d)
    counts[(cls, kind)] = counts.get((cls, kind), 0) + 1


def slug(path):
    return os.path.splitext(os.path.basename(path))[0]


def in_recent_dev(body, line_idx, lines):
    # walk up to nearest H2; True if it is a Recent-developments section
    for i in range(line_idx, -1, -1):
        if lines[i].startswith("## "):
            return "recent develop" in lines[i].lower()
    return False


for path in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
    if os.path.basename(path) == "flashcards.md":
        continue
    txt = open(path, encoding="utf-8").read()
    fm, body = split_fm(txt)
    cls = classify(path, fm)
    per_class_files[cls] = per_class_files.get(cls, 0) + 1
    s = slug(path)
    lines = body.splitlines()

    if cls == "case":
        add("case", "holding", path, f"case:{s}:holding",
            {"citation": fm_scalar(fm, "citation"),
             "title": fm_scalar(fm, "title")})
        cl_url = None
        m = re.search(r'opinion_url:\s*"?(\S+?)"?\s*$', fm, re.M)
        oid = re.search(r"opinion_id:\s*(\d+)", fm)
        idc = re.search(r"identity_checked:\s*(\w+)", fm)
        if m:
            cl_url = m.group(1)
        add("case", "cl_url", path, f"case:{s}:cl_url",
            {"opinion_url": cl_url,
             "opinion_id": int(oid.group(1)) if oid else None,
             "identity_checked": (idc.group(1) if idc else None)})
        add("case", "authority_weight", path, f"case:{s}:weight",
            {"authority_weight": fm_scalar(fm, "authority_weight")})
        tstatus = re.search(r"treatment:\s*\n(?:.*\n)*?\s*status:\s*(\S+)", fm)
        tas = re.search(r"as_of:\s*(\S+)", fm)
        add("case", "treatment", path, f"case:{s}:treatment",
            {"status": tstatus.group(1) if tstatus else None,
             "as_of": tas.group(1) if tas else None})
        # homes + roles
        hm = re.search(r"^homes:\s*\n((?:\s+-.*\n(?:\s+\w+:.*\n)*)+)", fm, re.M)
        if hm:
            block = hm.group(1)
            pages = re.findall(r"page:\s*\"?(.*?)\"?\s*$", block, re.M)
            roles = re.findall(r"role:\s*\"?(.*?)\"?\s*$", block, re.M)
            for i, pg in enumerate(pages):
                add("case", "home", path, f"case:{s}:home{i+1}",
                    {"page": pg, "role": roles[i] if i < len(roles) else None})
        # quoted passages keyed by ^pin anchor
        for a in PIN_ANCHOR.findall(body):
            add("case", "quote", path, f"case:{s}:{a}", {"anchor": a})

    elif cls in ("doctrine", "narrative", "moc"):
        # case-table rows
        row_n = 0
        for ln in lines:
            if CASEROW.match(ln) and ln.count("|") >= 4:
                row_n += 1
                first = ln.split("|")[1].strip()
                add(cls, "case_row", path, f"{cls}:{s}:row{row_n}",
                    {"cell": first[:120]})
        # verbatim quotes via pinpoint deep-links
        for i, a in enumerate(PIN_DEEPLINK.findall(body)):
            add(cls, "quote", path, f"{cls}:{s}:q{i+1}", {"anchor": a})
        # recent-developments circuit entries (named-in-prose page-less cases)
        for idx, ln in enumerate(lines):
            if re.match(r"^\s*-\s+\*\*[A-Z].*\(\d?\w*\s*Cir\.", ln) and \
               in_recent_dev(body, idx, lines):
                add(cls, "recent_dev", path,
                    f"{cls}:{s}:rd{idx}", {"entry": ln.strip()[:120]})
        # html-comment flags
        for c in HTML_COMMENT.findall(body):
            if strip_header_comment(c) and FLAG_KEYS.search(c):
                add(cls, "flag", path, f"{cls}:{s}:flag{len(items)}",
                    {"snippet": c.strip()[:160]})

    elif cls == "glossary":
        for i, term in enumerate(HEADING3.findall(body)):
            add("glossary", "term_def", path,
                f"glossary:{s}:t{i+1}", {"term": term.strip()})

    elif cls == "research":
        heads = HEADING3.findall(body)
        for i, term in enumerate(heads):
            add("research", "term_anchor", path,
                f"research:{s}:t{i+1}", {"term": term.strip()})
        # tool facts: bullet lines that assert a fact (only on the tool pages)
        if os.path.basename(path) in ("Legal Research Tools.md",
                                      "Verifying Good Law.md"):
            tf = 0
            for ln in lines:
                if re.match(r"^\s*[-*]\s+\S", ln) and len(ln.strip()) > 25:
                    tf += 1
                    add("research", "tool_fact", path,
                        f"research:{s}:tf{tf}", {"fact": ln.strip()[:140]})

    elif cls == "case_index":
        row_n = 0
        for ln in lines:
            if ln.startswith("|") and ln.count("|") >= 3 and "[[" in ln \
               and not re.match(r"^\|\s*-", ln):
                # skip header separator rows
                if re.search(r"\|\s*:?-{3,}", ln):
                    continue
                row_n += 1
                add("case_index", "index_row", path,
                    f"case_index:row{row_n}",
                    {"cell": ln.split('|')[1].strip()[:80]})

    elif cls == "nav":
        add("nav", "folder_page", path, f"nav:{s}:{len(items)}")

    # universal Mermaid pass (D8 worklist parity across every page)
    for i, _ in enumerate(MERMAID.findall(body)):
        add(cls, "mermaid", path, f"{cls}:{s}:mermaid{i+1}")


out = {
    "generated": "2026-06-30",
    "phase": "S9-P0",
    "root": "content/",
    "total_items": len(items),
    "objects_by_class": per_class_files,
    "counts_by_class_kind": {f"{c}.{k}": n for (c, k), n in sorted(counts.items())},
    "items": items,
}
os.makedirs(os.path.join(ROOT, "_run"), exist_ok=True)
outp = os.path.join(ROOT, "_run", "assertion-inventory.json")
json.dump(out, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# summary to stderr
w = sys.stderr.write
w("\n=== ASSERTION INVENTORY (S9 P0) ===\n")
w("objects by class: %s\n" % json.dumps(per_class_files, sort_keys=True))
w("total tracked assertions: %d\n" % len(items))
w("-" * 50 + "\n")
byclass = {}
for (c, k), n in counts.items():
    byclass.setdefault(c, {})[k] = n
for c in sorted(byclass):
    w("%-12s total=%d\n" % (c, sum(byclass[c].values())))
    for k in sorted(byclass[c]):
        w("    %-16s %d\n" % (k, byclass[c][k]))
w("-" * 50 + "\n")
w("written: %s\n" % rel(outp))
