#!/usr/bin/env python3
"""
Shared helpers for the CSSI LINT roster (S1 §3.H).

Standard-library only (no pip installs). Every lint imports from this module.

Conventions established by the corpus (see S1 §3.A/3.B and S4 Appendix B):
  - wikilinks are [[Page]] / [[Page#anchor]] / [[Page#^block]] / [[Page|display]]
  - CourtListener opinion URLs look like
        https://www.courtlistener.com/opinion/<id>/<slug>/
  - case tables are GFM markdown tables
  - case names use the party-v-party pattern  "Foo v. Bar"
  - doctrine pages carry  type: doctrine ; case pages carry  type: case

These helpers are tolerant of the PRE-overhaul corpus state (they will report
many violations now — that is informational, not a failure) and keep working
after the S2 folder restructure (all scans are recursive over content/**/*.md).
"""

import glob as _glob
import json
import os
import re
import sys

# --------------------------------------------------------------------------
# repo / content discovery
# --------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
# scripts/lint/_common.py -> repo root is two levels up
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
CONTENT_ROOT = os.path.join(REPO_ROOT, "content")


def iter_markdown_files(paths=None):
    """Yield absolute paths of markdown files to CHECK.

    `paths` may be None (default: every content/**/*.md), or a list of
    glob patterns / files / directories to scope to a subset. Directories
    and bare globs are expanded recursively; only *.md files are returned.
    """
    if not paths:
        pattern = os.path.join(CONTENT_ROOT, "**", "*.md")
        for p in sorted(_glob.glob(pattern, recursive=True)):
            yield p
        return

    seen = set()
    for raw in paths:
        cand = raw
        if not os.path.isabs(cand):
            cand = os.path.join(REPO_ROOT, raw)
        if os.path.isdir(cand):
            for p in sorted(_glob.glob(os.path.join(cand, "**", "*.md"),
                                      recursive=True)):
                if p not in seen:
                    seen.add(p)
                    yield p
        elif os.path.isfile(cand) and cand.endswith(".md"):
            if cand not in seen:
                seen.add(cand)
                yield cand
        else:
            # treat as a glob (relative to repo root if not absolute)
            for p in sorted(_glob.glob(cand, recursive=True)):
                if p.endswith(".md") and p not in seen:
                    seen.add(p)
                    yield p


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def relpath(path):
    try:
        return os.path.relpath(path, REPO_ROOT)
    except ValueError:
        return path


# --------------------------------------------------------------------------
# minimal YAML-subset frontmatter parser (stdlib only — no PyYAML)
# --------------------------------------------------------------------------

def split_frontmatter(text):
    """Return (frontmatter_dict, body_text, body_start_line).

    body_start_line is the 1-based line number in the ORIGINAL file where the
    body begins, so lints can report accurate line numbers against the body.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text, 1
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text, 1
    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1:])
    fm = parse_yaml_subset(fm_lines)
    return fm, body, end + 2


def _strip_inline_comment(value):
    # remove a trailing "  # comment" but not a '#' inside quotes
    out = []
    in_s = in_d = False
    i = 0
    while i < len(value):
        c = value[i]
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        elif c == "#" and not in_s and not in_d:
            # only treat as comment if preceded by whitespace or start
            if i == 0 or value[i - 1] in " \t":
                break
        out.append(c)
        i += 1
    return "".join(out).rstrip()


def _scalar(value):
    value = _strip_inline_comment(value).strip()
    if value == "":
        return ""
    # inline flow list  [a, b, c]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_unquote(x.strip()) for x in _split_flow(inner)]
    # inline flow map {a: b} -> keep raw (rare; not needed by lints)
    return _unquote(value)


def _split_flow(inner):
    parts = []
    buf = []
    depth = 0
    in_s = in_d = False
    for c in inner:
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        if c in "[{(" and not in_s and not in_d:
            depth += 1
        elif c in "]})" and not in_s and not in_d:
            depth -= 1
        if c == "," and depth == 0 and not in_s and not in_d:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(c)
    if buf:
        parts.append("".join(buf))
    return parts


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _indent(line):
    return len(line) - len(line.lstrip(" "))


def parse_yaml_subset(lines):
    """Parse a restricted YAML subset sufficient for the case/doctrine schema:
    nested mappings, block sequences (scalars or mappings), and inline flow
    lists. Comments and blank lines are ignored. Good enough for the keys the
    lints read; not a general YAML implementation.
    """
    # drop blanks / pure comments
    cleaned = []
    for ln in lines:
        if ln.strip() == "" or ln.lstrip().startswith("#"):
            continue
        cleaned.append(ln.rstrip("\n"))
    pos = [0]

    def parse_block(min_indent):
        node = None  # could become dict or list
        while pos[0] < len(cleaned):
            line = cleaned[pos[0]]
            ind = _indent(line)
            if ind < min_indent:
                break
            stripped = line.strip()
            if stripped.startswith("- "):
                if ind < min_indent:
                    break
                if node is None:
                    node = []
                if not isinstance(node, list):
                    break
                pos[0] += 1
                rest = stripped[2:]
                if ":" in rest and not rest.startswith("[") \
                        and not rest.startswith("{"):
                    # list item that is itself a mapping; first key inline
                    key, _, val = rest.partition(":")
                    item = {}
                    item[key.strip()] = _scalar(val)
                    # subsequent keys of this mapping are indented deeper than
                    # the dash position
                    child_min = ind + 2
                    sub = parse_block(child_min)
                    if isinstance(sub, dict):
                        item.update(sub)
                    node.append(item)
                else:
                    node.append(_scalar(rest))
            elif ":" in stripped:
                if node is None:
                    node = {}
                if not isinstance(node, dict):
                    break
                key, _, val = stripped.partition(":")
                key = key.strip()
                val = val.strip()
                pos[0] += 1
                if val == "":
                    # could be nested mapping/sequence on following lines
                    child = parse_block(ind + 1)
                    node[key] = child if child is not None else ""
                else:
                    node[key] = _scalar(val)
            else:
                # unrecognized line; skip to avoid infinite loop
                pos[0] += 1
        return node

    result = parse_block(0)
    return result if isinstance(result, dict) else {}


def fm_get(fm, *path, default=None):
    """Safe nested getter:  fm_get(fm, 'treatment', 'status')."""
    cur = fm
    for key in path:
        if isinstance(cur, dict) and key in cur:
            cur = cur[key]
        else:
            return default
    return cur


# --------------------------------------------------------------------------
# regexes shared across lints
# --------------------------------------------------------------------------

# A party token: a capitalized word (may carry internal periods/apostrophes),
# optionally followed by capitalized words or common lowercase connectors.
_PARTY = (r"[A-Z][A-Za-z.&'’\-]*"
          r"(?:\s+(?:[A-Z][A-Za-z.&'’\-]*|of|the|and|for|ex|rel\.|et|al\.|"
          r"de|van|von|la|le|du|dos|in|re)){0,5}")

# party-v-party case name, e.g. "Florida v. Jardines", "United States v. Dunn"
CASE_RE = re.compile(r"(%s)\s+v\.\s+(%s)" % (_PARTY, _PARTY))

# reporter citation (volume Reporter firstpage), with optional pincite ", page"
_REPORTER = (r"U\.?\s?S\.?|S\.?\s?Ct\.?|L\.?\s?Ed\.?(?:\s?2d)?|"
             r"F\.?(?:\s?(?:2d|3d|4th))?|F\.?\s?Supp\.?(?:\s?(?:2d|3d))?|"
             r"F\.?\s?App'?x\.?|So\.?(?:\s?(?:2d|3d))?|P\.?(?:\s?(?:2d|3d))?|"
             r"N\.?[EW]\.?(?:\s?2d)?|A\.?(?:\s?(?:2d|3d))?|S\.?[EW]\.?(?:\s?2d)?|"
             r"Cal\.?(?:\s?(?:App|Rptr)\.?)?(?:\s?(?:2d|3d|4th|5th))?")
REPORTER_RE = re.compile(r"\b\d{1,4}\s+(?:%s)\s+\d" % _REPORTER)

# a pinpoint cite: either "... at <page>"  or  "vol Reporter first, <pin>"
PINCITE_RE = re.compile(
    r"(?:\bat\s+\*?\d{1,4})"                                  # "at 838"
    r"|(?:\b\d{1,4}\s+(?:%s)\s+\d{1,4}\s*,\s*\d{1,4})"        # "569 U.S. 1, 6"
    % _REPORTER)

# U.S. Reports citation (strong SCOTUS signal): "547 U.S. 398"
US_REPORTER_RE = re.compile(r"\b\d{1,4}\s+U\.?\s?S\.?\s+\d{1,4}")
SCT_REPORTER_RE = re.compile(r"\b\d{1,4}\s+S\.?\s?Ct\.?\s+\d{1,4}")

# wikilinks:  [[Target]] | [[Target#anchor]] | [[Target|display]] | [[#anchor]]
WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")

# inline markdown link  [text](url)
MDLINK_RE = re.compile(r"\[([^\[\]]*)\]\(([^()\s]+)[^()]*\)")

# inline code span  `...`
INLINE_CODE_RE = re.compile(r"`[^`]*`")

# CourtListener opinion URL (capture the numeric id)
CL_OPINION_URL_RE = re.compile(
    r"https?://(?:www\.)?courtlistener\.com/opinion/(\d+)/[^\s)\]\"'>]*")
# any CL URL (opinion or otherwise)
CL_ANY_URL_RE = re.compile(
    r"https?://(?:www\.)?courtlistener\.com/[^\s)\]\"'>]+")


# --------------------------------------------------------------------------
# markdown structure helpers
# --------------------------------------------------------------------------

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def fenced_line_numbers(body_lines):
    """Return a set of 0-based line indexes that fall inside ``` code fences."""
    inside = False
    fence = None
    out = set()
    for i, line in enumerate(body_lines):
        s = line.lstrip()
        if not inside and (s.startswith("```") or s.startswith("~~~")):
            inside = True
            fence = s[:3]
            out.add(i)
            continue
        if inside:
            out.add(i)
            if s.startswith(fence):
                inside = False
                fence = None
    return out


def slugify(heading_text):
    """GitHub/Quartz-style heading slug: lowercase, strip markdown emphasis &
    punctuation, spaces -> hyphens."""
    t = heading_text.strip().lower()
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*?([^*]*)\*\*?", r"\1", t)
    t = re.sub(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("&", " and ")
    t = re.sub(r"[^\w\s\-]", "", t)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-+", "-", t)
    return t


def iter_headings(body_lines, skip_fenced=True):
    """Yield (line_index, level, text) for ATX headings outside code fences."""
    fenced = fenced_line_numbers(body_lines) if skip_fenced else set()
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        m = HEADING_RE.match(line)
        if m:
            yield i, len(m.group(1)), m.group(2).strip()


def sections(body_lines):
    """Split body into sections keyed by H2 headings.
    Returns a list of dicts: {title, slug, level, start, end} (line indexes).
    """
    heads = [(i, lvl, txt) for (i, lvl, txt) in iter_headings(body_lines)
             if lvl == 2]
    out = []
    for idx, (i, lvl, txt) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(body_lines)
        out.append({"title": txt, "slug": slugify(txt), "level": lvl,
                    "start": i, "end": end})
    return out


def mask_links_and_code(line):
    """Return the line with [[wikilinks]] and `code` spans blanked to spaces
    (same length), so bare-text scanners don't match inside them. Markdown
    links [text](url) are NOT masked (a CL link is not a case-page wikilink)."""
    def blank(m):
        return " " * (m.end() - m.start())
    line = INLINE_CODE_RE.sub(blank, line)
    line = WIKILINK_RE.sub(blank, line)
    return line


# --------------------------------------------------------------------------
# corpus index (pages + anchors + aliases) for link resolution
# --------------------------------------------------------------------------

class CorpusIndex:
    def __init__(self):
        self.page_by_norm = {}     # normalized name -> stem
        self.anchors = {}          # stem -> set(anchor slugs incl. ^blocks)
        self.alias_by_norm = {}    # normalized alias -> stem

    @staticmethod
    def norm(name):
        n = name.strip().lower()
        n = re.sub(r"\.md$", "", n)
        n = n.replace("’", "'")
        n = re.sub(r"\s+", " ", n)
        return n

    def resolve(self, target):
        """Resolve a wikilink target (page part, no #anchor) to a stem, or
        None. Tries basename, full relative path, alias, and slug forms."""
        if not target:
            return None
        cand = target.strip()
        # strip any leading path; Quartz resolves by basename for [[..]]
        base = cand.split("/")[-1]
        for key in (cand, base):
            n = self.norm(key)
            if n in self.page_by_norm:
                return self.page_by_norm[n]
            if n in self.alias_by_norm:
                return self.alias_by_norm[n]
        # slug fallback (e.g. [[two-definitions-of-search]])
        sl = slugify(base)
        return self._slug_lookup.get(sl)

    def has_anchor(self, stem, anchor):
        if stem not in self.anchors:
            return False
        a = anchor.strip()
        if a.startswith("^"):
            return a.lower() in self.anchors[stem]
        return slugify(a) in self.anchors[stem]


def build_corpus_index(root=None):
    """Index every page in content/ (always the FULL corpus, regardless of any
    scoping arg) so link/anchor resolution is correct even when a lint is
    scoped to a subset of files."""
    root = root or CONTENT_ROOT
    idx = CorpusIndex()
    idx._slug_lookup = {}
    for path in _glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
        stem = os.path.splitext(os.path.basename(path))[0]
        try:
            text = read_text(path)
        except OSError:
            continue
        fm, body, _ = split_frontmatter(text)
        idx.page_by_norm[idx.norm(stem)] = stem
        idx._slug_lookup[slugify(stem)] = stem
        # title / topic as additional resolvable names
        for key in ("title", "topic"):
            val = fm.get(key)
            if isinstance(val, str) and val.strip():
                idx.alias_by_norm.setdefault(idx.norm(val), stem)
        aliases = fm.get("aliases")
        if isinstance(aliases, list):
            for al in aliases:
                if isinstance(al, str) and al.strip():
                    idx.alias_by_norm.setdefault(idx.norm(al), stem)
        elif isinstance(aliases, str) and aliases.strip():
            idx.alias_by_norm.setdefault(idx.norm(aliases), stem)
        # anchors: heading slugs + ^block ids
        anchors = set()
        body_lines = body.split("\n")
        for _, _, txt in iter_headings(body_lines):
            anchors.add(slugify(txt))
        for m in re.finditer(r"\s(\^[A-Za-z0-9\-]+)\s*$",
                             body, flags=re.MULTILINE):
            anchors.add(m.group(1).lower())
        idx.anchors[stem] = anchors
    return idx


# --------------------------------------------------------------------------
# violation emission + CLI runner scaffold
# --------------------------------------------------------------------------

HIGH = "high"
MEDIUM = "medium"
LOW = "low"


def make_violation(lint, path, line, severity, message):
    return {
        "lint": lint,
        "file": relpath(path),
        "line": line,
        "severity": severity,
        "message": message,
    }


def emit(violations, stream=None):
    stream = stream or sys.stdout
    for v in violations:
        stream.write(json.dumps(v, ensure_ascii=False) + "\n")


def exit_code_for(violations):
    return 1 if any(v.get("severity") == HIGH for v in violations) else 0


def cli_main(run_fn, lint_name):
    """Standard CLI entrypoint: scope args -> run_fn(paths) -> JSON lines.
    Exits non-zero iff any high-severity violation is found."""
    args = sys.argv[1:]
    paths = args if args else None
    violations = run_fn(paths)
    emit(violations)
    n_high = sum(1 for v in violations if v["severity"] == HIGH)
    sys.stderr.write(
        "[%s] %d violation(s): %d high, %d medium, %d low\n" % (
            lint_name, len(violations), n_high,
            sum(1 for v in violations if v["severity"] == MEDIUM),
            sum(1 for v in violations if v["severity"] == LOW)))
    sys.exit(exit_code_for(violations))
