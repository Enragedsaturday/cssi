# CSSI Overhaul — Context Pack (read this first)

> This file is the shared grounding for every overhaul interview. It is self-contained
> so that a **fresh context thread** can conduct any interview without re-doing the
> discovery research. Read it in full before running any `interviews/SN-*.md` file.

**Project:** CSSI — a federal search-and-seizure instructor wiki, built on Quartz, for a
police-academy instructor (Anthony Bandiero "Blue to Gold" SCOTUS reference is the
source book). Goal of the overhaul: rebuild content + structure to a **100%-verified,
officer-practical** standard, doctrine-brief-first, with a page for every case.

**Mode:** Spec-driven development. We run one **interview per spec** (this kit), each
producing a written spec in `_overhaul/specs/`. **Execution happens later**, in a
separate full-autonomous run launched by `_overhaul/wrappers/EXECUTE.wrapper.md`.
Interviews DESIGN; they do not edit content pages.

---

## 1. Key paths (don't re-discover these)

| What | Path |
|---|---|
| Repo root (git, → Vercel `cssi-search-and-seizure.vercel.app`) | `/Users/johngalt/Projects/cssi-quartz` |
| Markdown content (Quartz builds only this dir) | `…/content/` (43 pages) |
| Master case list | `…/content/Case Index.md` (~261–329 verified cases) |
| Glossary | `…/content/Common Legal Terms.md` |
| Quartz config / layout | `…/quartz.config.ts`, `…/quartz.layout.ts` |
| Sidebar spacing knobs | `…/quartz/styles/base.scss` (`gap:1.2rem`), `…/quartz/styles/variables.scss` (`$sidePanelWidth:320px`) |
| **Prior self-critique (GOLD)** | `…/docs/FINAL-QA-SPEC.md` — §0 = 15-point failure-mode list; §3 = D1–D12 dimensions |
| Methodology / CL gotchas | `…/docs/RUNBOOK.md` |
| Prior per-page specs (format reference) | vault `…/CSSI/_run/spec/*.spec.md` (41 files) |
| Prior IA spec | vault `…/CSSI/_run/IA-SPEC.md` |
| Prior self-interview decision log (format reference) | vault `…/CSSI/_run/DECISIONS.md` (D-0…D-8) |
| Flashcards | `…/flashcard-src/decks/*.json` (~55 decks, ~1,660 cards) + `merge.py`, `make_apkg.py` |
| Roadmap brief (HTML) | `/Users/johngalt/briefs/2026-06-27-cssi-overhaul-spec-roadmap.html` |
| The book scans | `/Users/johngalt/.orca/drops/Book Jun 26, 2026.pdf` (TOC), `…(1).pdf` (case example) |

Obsidian vault (source of truth; `content/` is a copy) lives under
`~/Library/Mobile Documents/com~apple~CloudDocs/Main/CSSI`.

## 2. Current state (verified by discovery)

- **Quartz 4.5.2, vanilla** (zero custom components). Hover **popovers already ON**
  (`enablePopovers:true`). Search, graph, backlinks, breadcrumbs enabled.
- **No individual case pages** — cases exist only as table rows + Case Index entries.
- **No category taxonomy** — organization is `index.md` narrative sections + `related:`
  frontmatter wikilinks. No parent/child tree, no tag pages.
- **Doctrine page anatomy (confirmed):** Rule → Key cases → Related cases across
  doctrines → Nuances & limits → Common pitfalls → Visual (Mermaid) → Recent
  developments & subsequent treatment → Sources. The "brief" is fragmented across this.
- **Shepardizing sparse** — only ~14 of ~261 Case-Index rows carry a good-law flag.
- **Sidebar "cramped"** = two SCSS values. Not a reason to leave Quartz.
- **Book case example format:** Facts → Issue → Held → Discussion → Citation(topic).
- **Prior process is mature:** D1–D12 review dimensions, two-key rule, single-serial-
  CourtListener-lane rule, find→adjudicate→fix separation, 3,101 assertions tracked /
  ~154 corrections in the last QA pass.

## 3. The lessons register (this is the heart of the overhaul)

Every spec must enforce the relevant rules below. S1 turns this into `docs/STANDARDS.md`.

### Scars the prior build already paid for
- **L1 Paraphrase drift** → every holding/quote traces to the opinion via the **two-key
  rule** (existence + proposition + verbatim pinpoint + good-law). Decks derive FROM
  verified pages, never the reverse.
- **L2 Web-discovery error rate** (a backwards holding; invented frameworks; **4 fake
  cases**) → web is **discovery only**; nothing enters a page until confirmed against the
  primary opinion on CourtListener. Discovery ≠ assertion.
- **L3 cluster-id ≠ opinion-id** (26 wrong CL URLs) → link-check confirms each CL URL
  resolves AND displays the **named** case (identity, not just HTTP 200).
- **L4 Parallel-CL leak** → one **serial CourtListener lane**, always.
- **L5 Reviewer-fixes-in-place** → hard separation **find → adjudicate → fix**.
- **L6 "Not found" ≠ "doesn't exist"** → escalate (reporter cite → name variants →
  proposition full-text → web) before declaring a case fake. Misspelling-tolerant ID.

### Mechanism lessons from the instructor's page-by-page notes
- **N1 Placement by holding, not keyword.** A case's home + key/related status is set by
  the legal proposition it stands for, not surface-keyword overlap. (Matlock = consent/
  common-authority, NOT abandonment.)
- **N2 Authority-weight lexicon.** Replace blunt "persuasive, not binding." Use the fixed
  lexicon in §4 everywhere.
- **N3 Tests stated up front.** Any named test/prongs/elements appear explicitly in the
  Rule/brief at top — never left for the reader to reconstruct (e.g. the *Dunn* 4 factors).
- **N4 Subsequent treatment inline.** Where a case is materially narrowed, say "limited by
  [linked cases]" at the point of assertion (brief why when it changes field application).
  (e.g. *Santana*.)
- **N5 Recent-developments is role-based, not recency-based.** That section is for
  circuit/state cases that expand/narrow/split/first-impression vs SCOTUS. **Any SCOTUS
  holding belongs in Key cases regardless of date.** (Re-home *Case v. Montana*.)
- **N6 Key-status is non-exclusive.** A case is Key on a page if central to THAT doctrine,
  independent of being key elsewhere. Multi-homing expected; framing page-specific.
  (Promote *Herring* on Collective Knowledge; move *Riley* to Related on Common Law.)
- **N7 Link every named case.** Every case named anywhere links to its own case page;
  discussing a specific passage → deep-link to the pinpoint/highlighted span; whole-case
  reference → link the case page.
- **N8 Brief-first.** The full teaching brief (rule + limits + nuance + pitfalls, integrated)
  reads top-to-bottom first; tables + recent developments follow as supporting apparatus.
- **N9 Frame around the officer's field-decisive question**, not "what is the exception."
  For misunderstood topics (knock-and-talk) be exhaustive on line-drawing.
- **N10 State scope explicitly** (what/who/where); split bundled doctrines. Research, never
  assume. (Community caretaking: persons vs vehicles?)
- **N11 Wire the glossary.** Non-vernacular terms link to glossary (hover-preview +
  click-through); glossary audited continuously from live page text.
- **N12 Progressive research.** narrow issue → doctrine/keyword → expand → learn →
  expand (bounded). Assume nothing; web discovers, CourtListener confirms.
- **N13 No blank treatment status.** Every case carries an explicit, verified status;
  "good as of <date>" only after a check.

## 4. Proposed authority-weight lexicon (confirm/adjust in S1)

- **Binding — SCOTUS** (nationwide)
- **Binding in-circuit** (a circuit holding within its own circuit, and on a case heard there)
- **Persuasive (outside circuit)** — replaces "persuasive, not binding"
- **Persuasive — state, illustrative** (paired with the federal rule)
- **Persuasive only — non-precedential** (unpublished; the only "not binding even at home" tier)
- **Historical** (English/colonial origins; or overruled cases shown as history)

## 5. The spec roadmap (9 specs, 4 waves)

```
Wave A Foundations : S1 Standards/Self-Improvement → S2 Information Architecture & Categories
Wave B Substrate   : S3 Platform & Nav/UX          → S4 Case Data Model & Per-Case Pages
Wave C Content     : S5 Case Ingest/Coverage → S6 Doctrine & Page Re-format → S7 Legal-Term
                     Linking → S8 Legal-Research Pages
Wave D Assurance   : S9 Full Independent Verification & Adjudication

Deps: S1→S2→S3→S4→S5→S6→S7→S9 ; S8 depends on S1 only ; S9 depends on all.
```

**The scope question (settle in S2, gates S5):** the book runs I–XIII (4A, 5A/Miranda,
6A, Use of Force, Liability). The site is "search & seizure" but already carries Miranda,
6A right-to-counsel, due-process voluntariness, eyewitness ID, use-of-force, Brady/Giglio,
entrapment. Decide the target: (a) 4A-complete, (b) **current scope + its existing
adjacencies (recommended)**, or (c) whole book I–XIII.

## 6. How to run an interview (method)

This is a **hybrid interview**, mirroring the project's established self-interview pattern:

1. **Ask the user only the genuinely user-owned decisions** — the ones flagged in each
   interview file. Use the `AskUserQuestion` tool for these, in focused batches, and always
   lead with your recommendation. Do **not** ask things you can decide or verify yourself.
2. **For everything else, self-interview:** Options → Red-team → Steel-man → Adjudication,
   and propose the answer. Log each in the spec's Decision log appendix.
3. **Use web search + CourtListener (serial, per L2/L4) only to resolve spec-level
   questions** (e.g. the community-caretaking person/vehicle question; opencase.com vetting).
   Do not start building content.
4. **Keep it tight.** A good interview is a few focused question batches + a written spec,
   not an interrogation.

## 7. Spec output format (every interview writes this)

Write to `_overhaul/specs/SN-<slug>.spec.md`:

```
# SPEC SN — <Title>
status: APPROVED
depends-on: [S…]   gates: [S…]
last-updated: <date from session context>

## 1. Objective              (1–3 sentences)
## 2. Scope                  (in / out — explicit)
## 3. Requirements           (numbered, each testable)
## 4. Lessons enforced       (which L#/N# rules this spec honors, and how)
## 5. Method                 (how the autonomous execution will proceed; stages)
## 6. Deliverables           (files/paths the execution will produce or change)
## 7. Acceptance criteria    (definition of done — testable checklist)
## 8. Verification plan       (how this spec's output gets independently verified)
## 9. Open items / escalations
## Appendix A — Decision log (each: Question · Options · Red-team · Steel-man · Adjudication)
```

## 8. Handoff at the end of every interview

1. Write the spec file. 2. Update `_overhaul/README.md` status table (mark SN ✅ written).
3. Give the user a 5–8 line recap. 4. **Hand the user the contents of the next wrapper**
(`_overhaul/wrappers/S(N+1).wrapper.md`) to paste into a **new context thread**; after S9,
hand `EXECUTE.wrapper.md`. Do not auto-start the next interview.
