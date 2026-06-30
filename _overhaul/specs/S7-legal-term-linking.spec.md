# SPEC S7 — Legal-Term Linking (glossary wiring)

status: APPROVED
depends-on: [S3, S6]          gates: [S9]
last-updated: 2026-06-29

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S7 **designs the inclusion test** for
> what counts as a linkable legal term, the **term-audit method** that finds candidates and
> produces the add-to-glossary list + the term→pages occurrence map, the **wiring mechanism**
> (wikilink → glossary anchor so Quartz's popover fires), the **authoring rule** for new glossary
> entries, and the **find→adjudicate→fix gate**. S7 **runs against the finalized S6 page text** —
> S6 explicitly **deferred glossary/term wiring (N11) and the `Common Legal Terms` page to S7**
> (S6 §2.2, R11, §6.3 leave the glossary untouched) — so the brief-first doctrine prose S6 produced
> is the **live text the continuous glossary audit runs against** (N11). S7 **uses the popover/anchor
> mechanism S3 already locked** (S3 · R6: `enablePopovers:true` + `[[Common Legal Terms#anchor]]` +
> the glossary-popover style); it builds no component and changes no config. S7 **finalizes LINT-7**,
> which S1 §9 left **best-effort / checklist-primary** pending this interview. S7 **designs**; the
> sweep executes later under `EXECUTE.wrapper.md` through the standing gate (L5), serial CL (L4) only
> where a definition asserts a case-tied proposition (L1).

---

## 1. Objective

Make every **non-vernacular legal term of art** a hover-preview link to its definition, so a reader
hovering the word sees a plain-English definition + a concrete search-and-seizure example and a click
lands on it — **without going overly broad**. S7 (a) fixes the **inclusion test** as a testable rule
(term-of-art only; route terms that have their own page to that page; skip the page's own subject term
and the officer-audience's known field vocabulary; first occurrence per page only); (b) specifies the
**term-audit method** (controlled-vocabulary match + a fuzzy discovery pass) producing the
**glossary-additions list** and the **term→pages occurrence map**; (c) fixes the **wiring mechanism**
(anchorize the glossary into addressable headings, then link `[[Common Legal Terms#term]]`); (d) sets
the **authoring rule** for new entries; and (e) defines the **gate** that catches over-linking, broken
anchors, and inaccurate definitions. S7 **finalizes LINT-7**.

## 2. Scope

### 2.1 In scope (S7 designs)
- The **inclusion test** for a glossary-linkable term, as a testable rule with explicit exclusion sets
  (§3 · R1–R5).
- The **link-target routing** rule: a term with its own doctrine/case page links to **that page**
  (N7, S6's job — not duplicated here); only term-of-art words with **no page home** are glossary-wired
  (R2).
- The **officer-audience vernacular exclusion set** — the field-operational vocabulary skipped as
  "vernacular for this audience" (R3), seeded here and instructor-editable.
- The **term-audit method** over the finalized S6 page text (R6): build the candidate inventory, dedupe
  against the glossary, emit the **add-to-glossary list** + the **term→pages occurrence map**.
- The **glossary anchorization** — promote each entry to an addressable heading so S3's popover anchor
  mechanism resolves (R7), satisfying S3 · R6's "addressable `## Term` heading" prerequisite.
- The **wiring mechanism** — first-occurrence-per-page wikilink to the glossary anchor (R8).
- The **authoring rule** for new glossary entries (plain-English definition + concrete S&S example;
  two-key only where a definition asserts a case-tied proposition) (R9).
- The **LINT-7 finalization** (what is automatable vs. checklist-primary) (R10).
- The **per-page find→adjudicate→fix gate** for the sweep (§8; R11).

### 2.2 Out of scope (owned elsewhere)
- The **popover/anchor mechanism + the glossary-popover style** → **S3** (R6); S7 only **uses and
  verifies** it and supplies the anchors it points at.
- The **`enablePopovers`/`markdownLinkResolution`/`AliasRedirects` config** → unchanged (S3); S7 edits
  no config.
- **Case-name → `[[Case]]` linking (N7), doctrine-page prose, the lexicon sweep, field framing** →
  **S6** (S7 layers term links onto the finalized prose; it disturbs no case link and rewrites no brief).
- **Legal-research / citation-mechanics pages and terms** (supra, id., pinpoint cite, reporter,
  parallel citation, en banc, certiorari, slip opinion) → **S8** authors/defines those; S7 routes such
  terms to the S8 page rather than re-defining them in the glossary (coordination, §9).
- The **case object / anchor scheme** → **S4**; the **standards/lexicon/verification machine** → **S1**;
  the **final exhaustive independent verification** → **S9**.
- **Flashcard decks** → frozen through the entire overhaul; the page-derived rebuild is a **separate
  later run** (S4 · R11 as amended by U5-S9 — **not** an S9 step); S7 touches no deck.

---

## 3. Requirements (numbered, testable)

### R1 — The inclusion test (the core rule) **[N11; USER U1/U2]**
A word/phrase in a page's prose is a **glossary-linkable term** **iff ALL** of the following hold:
1. **Term of art.** It is **outside common lay vernacular and primarily used by legal professionals**
   (e.g. *curtilage* — when not its own page —, *attenuation*, *inevitable discovery*, *independent
   source*, *dicta*, *stare decisis*, *mens rea*, *prima facie*, *in limine*, *voir dire*,
   *fruit of the poisonous tree*). (U1: **term-of-art only** — not the "legal-meaning-differs" breadth.)
2. **No page home.** It does **not** have its own doctrine page or case page. (If it does, it links to
   **that page**, per **R2** — not the glossary.)
3. **Not the page's own subject.** It is **not** the term the current page is itself teaching as its
   subject (no self-referential link on the page that defines it).
4. **Not officer-audience vernacular.** It is **not** in the **R3 officer-known field-operational set**
   (terms the police/instructor audience knows cold). (U2: **skip officer-known**.)
5. **First occurrence only.** Only the **first** qualifying occurrence on a given page is wired (U3;
   density rule, R8). (This is a wiring condition, not a term-eligibility condition, but it is part of
   "what gets a link.")
- *Check (CHECKLIST:D13 + AUTO:LINT-7):* a sampled qualifying term is linked exactly once per page on
  first occurrence; no plain-English word, no page-subject term, no R3-set term, and no term-with-a-page
  is glossary-linked; every glossary-linked target resolves.

### R2 — Link-target routing (term with a page links to the page) **[N7, S6, D13]**
The destination a term points to is fixed by what exists for it:
- **Has a doctrine/case page** → link the **page** (`[[Probable Cause and Reasonable Suspicion]]`,
  `[[Curtilage]]`, `[[Plain View Doctrine]]`). This is **N7/D13 doctrine-linking already executed by
  S6**; S7 does **not** re-route these to the glossary and does **not** duplicate the link.
- **Taught as a labeled section of a doctrine page** (a sub-doctrine — e.g. attenuation / inevitable
  discovery / independent source under **[[The Exclusionary Rule]]**) → if S6 already deep-links the
  section, leave it; otherwise S7 may deep-link the section (`[[The Exclusionary Rule#attenuation]]`).
  The glossary is the **fallback** only when the term has **no** such home.
- **No page home, term-of-art (R1)** → link **`[[Common Legal Terms#term]]`** (the S7 wiring job).
- *Check:* no term that has its own page is wired to the glossary; glossary wiring covers only
  page-less terms-of-art; section deep-links resolve under SPA nav.

### R3 — The officer-audience vernacular exclusion set **[USER U2; N11 "don't go overly broad"]**
Skip — site-wide, as **vernacular for this audience** — the **field-operational vocabulary** the
police/instructor audience uses daily. **Seed set** (instructor-editable at execution, §9):
*probable cause, reasonable suspicion, exigent circumstances, custody, detention, arrest, stop, frisk /
pat-down, search, seizure, consent, warrant, plain view, contraband, Miranda, suspect, officer,
evidence*. **Note:** most of these also have a doctrine page and are therefore already excluded by **R2**
(routed to the page, not the glossary); R3 catches the rest. **Counter-note:** courtroom/suppression
terms of art that are **not** daily field vocabulary — *attenuation, inevitable discovery, independent
source, good-faith exception, standing, totality of the circumstances, particularity* — are **NOT** in
this set and remain **included** (subject to R2 routing).
- *Check:* no R3-set term is glossary-linked anywhere; the set is recorded in the spec deliverable and
  was reviewed by the instructor; courtroom terms-of-art outside the set are still wired.

### R4 — Plain-English / lay exclusion **[N11]**
Never link ordinary English words a lay reader uses correctly without help (*car, house, night, money,
door, knock, statement, question, mistake*) even when they appear in a legal sentence. Surface meaning
that matches lay meaning ⇒ not a term of art ⇒ not linked (this is the inverse of the rejected
"legal-meaning-differs" breadth, U1).
- *Check:* zero links on plain-English words; the audit's exclusion log shows lay words filtered out.

### R5 — No self-link on the defining/teaching page **[N11]**
On the page that **is** the glossary, and on any page **whose subject is the term**, the term is **not**
glossary-linked (no circular/self-referential popover). The glossary page itself carries **cross-links
between related entries** where useful, but never a self-link.
- *Check:* `Common Legal Terms.md` contains no `[[Common Legal Terms#self]]` self-link; a doctrine page
  about term *X* does not glossary-link *X*.

### R6 — The term-audit method (find → list + map) **[N11 continuous audit; L5 find-phase]**
Run **against the finalized S6 page text** (every live `content/` page except the S7/S8/S4-owned pages
per §2.2). Two-pass detection, because LINT-7 is best-effort (R10):
1. **Controlled-vocabulary pass (deterministic).** Match each page's prose against a **maintained term
   lexicon** = the current glossary terms **+** a curated term-of-art list (R1 #1). Every match is a
   candidate occurrence. This pass is **automatable** (R10).
2. **Fuzzy discovery pass (checklist-primary).** Flag likely-missed terms of art — italicized Latin,
   capitalized doctrine phrases, words matching a legal-term pattern — for **human/checklist review**;
   confirmed novel terms are added to the lexicon for the next continuous audit (N11).
**Dedupe** every candidate against the glossary, splitting into **(a) already-in-glossary** (→ wire
only) and **(b) needs-adding** (→ author + wire). Emit the two §6 artifacts: the **glossary-additions
list** and the **term→pages occurrence map**.
- *Check:* every in-scope page is scanned; the candidate set is deduped against the glossary; both
  artifacts are produced; the lexicon is updated with confirmed discoveries (audit is repeatable).

### R7 — Glossary anchorization (make every entry addressable) **[S3 · R6 prerequisite]**
Restructure `Common Legal Terms.md` so **every entry is an addressable anchor**, satisfying S3 · R6
("each glossary entry must be an addressable `## Term` heading or `^block`"). Mechanism: **promote each
`**Term** —` entry to a heading** (`### Term`) **under its existing category `## Heading`**, keeping the
definition + example as the heading body. The four current categories (Criminal-law terms · Evidence &
procedure · Opinions & precedent · Latin shorthand) **stay as `##` section dividers**; entries become
`###`. Quartz auto-slugs each heading, so `[[Common Legal Terms#stare-decisis]]` resolves to it.
- **Multi-lemma / parenthetical entries** (e.g. *Dicta (obiter dictum)*, *De facto vs. de jure*,
  *Subpoena duces tecum / ad testificandum*, *Probable cause vs. reasonable suspicion*): set a **canonical
  heading per linkable term** (split a paired entry into two headings, or pick the canonical lemma and
  note alternates in the body) so each linkable term has a clean, stable anchor (§9).
- *Check:* every glossary entry is a heading with a resolvable slug; a wikilink to each anchor resolves;
  no entry is left as bold-only inline (unaddressable); paired entries expose one anchor per linkable term.

### R8 — The wiring mechanism (first-occurrence hover-link) **[S3 · R6; USER U3]**
On each page, replace the **first** qualifying occurrence (R1) of a term with a **wikilink to its
glossary anchor** — `[[Common Legal Terms#curtilage|curtilage]]` (piped so the visible text stays the
inflected word in context). Under `enablePopovers:true` (S3, confirmed), hover fetches the target and
**scrolls the preview to the anchor**, showing the definition + example; click navigates to it. The
**glossary-popover style** (S3 · R6 #3) constrains the preview to definition size — S7 keeps entries
short (R9) so the preview **is** the whole definition. Confirm the popover content (Quartz's
`.popover-hint` container) renders the anchored entry's body.
- *Check:* a wired term shows its definition on hover (preview scrolled to the anchor) and lands on it
  on click; only the first occurrence per page is a link; piped display text reads naturally in the
  sentence; the popover is definition-sized, not a full-page dump.

### R9 — Authoring rule for new glossary entries **[L1 two-key; D11 glossary accuracy; voice match]**
Each **needs-adding** term (R6 b) gets an entry **matching the existing glossary's voice**: a
**plain-English definition** (≤ ~2 sentences) **+ one concrete search-and-seizure `*Example:*`**. Entries
are **established legal definitions, stated plainly without citations** (as the glossary preamble says) —
**except**: where a definition **asserts a legal proposition tied to a specific case/holding**, it is a
**two-key (L1) event** — verify against the primary opinion via the **serial CL lane (L4)** **or**, better,
**don't restate the holding in the glossary at all** — give the generic definition and **link the
doctrine/case page** for the proposition (keeps the glossary definitional, not assertional). New entries
slot into the **existing category** that fits, or add a new `##` category only if a cluster genuinely has
no home.
- *Check:* every new entry has a definition + an S&S example in the glossary voice; pure definitions
  carry no citation; any case-tied proposition either cites CL evidence (two-key) or is replaced by a
  link to the page that owns it; entries are short enough to preview whole.

### R10 — LINT-7 finalization (automatable vs. checklist-primary) **[S1 §9 closes here]**
S1 §9 deferred LINT-7's automatability to S7. **Decision:**
- **Automatable (AUTO):** (a) **anchor resolution** — every `[[Common Legal Terms#x]]` target exists
  (a build-time/link-check assertion, same engine as LINT-5); (b) **density** — no term linked more than
  once per page; (c) **no-banned-link** — no R3-set term, no plain-English-stoplist word, and no
  term-with-its-own-page is glossary-wired (checked against the maintained lexicon + page index);
  (d) **known-term coverage** — every controlled-vocabulary term that occurs on a page is wired on first
  occurrence.
- **Checklist-primary (CHECKLIST):** (e) **novel-term discovery** (the fuzzy pass, R6 #2) and
  (f) **definition accuracy / voice** (R9) — both remain human-reviewed; term detection beyond the
  controlled vocabulary is fuzzy (S1 §9 confirmed).
- *Check:* the AUTO sub-checks run in the lint gate and pass; the CHECKLIST sub-checks are signed per
  audit cycle; S1 §9's open item is marked resolved by this requirement.

### R11 — The find→adjudicate→fix gate **[L5, L4, L1, §8]**
The sweep runs the standing machine (S1 §3.G): **REVIEW** (parallel, free, no-CL — over-linking/density
R8, banned-link/own-subject R1/R3/R4/R5, anchor resolution R7, definition accuracy/voice R9) →
**ADJUDICATE** (a finding that a **definition asserts a case-tied proposition** is `needs_cl=true` → the
**single serial CL lane** for two-key verification (L1/L4); pure-definition and link-mechanics findings →
a free editor-adjudicator; DISMISSED logged with reason) → **FIX** (apply only UPHELD/MODIFIED; introduce
no new prose into doctrine pages beyond the term link itself; ESCALATE → `_review-needed/<slug>.md`).
**Loop cap 3**, checkpointed/resumable.
- *Check:* every wired term + new entry traces to an adjudicated verdict; case-tied definitions show CL
  evidence in `cl-calls.log`; reviewers produced findings only; escalations logged.

---

## 4. Lessons enforced

- **N11 (wire the glossary; hover-preview + click-through; audited continuously from live page text)** →
  the whole spec: R1 inclusion test, R6 audit over the **finalized S6 text**, R7/R8 wiring, R9 authoring.
- **N7 (link the right target)** → R2 routing: a term with its own page links to the **page**, not the
  glossary; only page-less terms-of-art are glossary-wired (no duplication of S6's case/doctrine links).
- **L1 (two-key)** → R9/R11: a definition that asserts a case-tied proposition is a live-verify event
  (serial CL) or is replaced by a link to the owning page. **L4 (serial CL lane)** → R11. **L5
  (find→adjudicate→fix)** → R11 gate.
- **D13 (linking & glossary wiring)** → R1/R7/R8 (no orphan term; all anchors resolve). **D11
  (practical/reference page accuracy)** → R9 (glossary accuracy + voice). **SR-3 (`docs/STANDARDS.md`
  supremacy)** → every execution step cites S1; LINT-7 keys to S1's lint roster.
- **S3 · R6** (popover/anchor mechanism + glossary-popover style) → R7/R8 (S7 supplies the anchors S3's
  mechanism points at). **S6** (finalized brief-first prose; glossary deferred to S7) → R6 (the audit's
  input text) + R2 (S6's case/doctrine links are the routing targets). **S1 §9** (LINT-7 best-effort) →
  R10 (finalized here).

## 5. Method (how execution proceeds against this spec)

Runs **after S6** (finalized page text), through the standing gate, serial CL only where R9 triggers it:

1. **Audit (R6).** Controlled-vocabulary pass + fuzzy discovery pass over every in-scope page; dedupe
   against the glossary; emit the **glossary-additions list** + the **term→pages occurrence map** (§6).
2. **Anchorize (R7).** Promote glossary entries to `###` headings under the existing `##` categories;
   split paired entries into one anchor per linkable term; confirm every anchor slug resolves.
3. **Author additions (R9).** Write each new entry (definition + S&S example, glossary voice); case-tied
   propositions → two-key via serial CL or replaced by a page link.
4. **Wire (R8/R1/R2).** For each page, link the **first** qualifying occurrence of each eligible term to
   its glossary anchor (piped display text); route page-having terms to their pages (R2 — confirm S6
   already did so, don't duplicate); skip R3/R4/R5 exclusions.
5. **Gate (R11).** find→adjudicate→fix per page; serial CL (L4) for case-tied definitions; run the
   **LINT-7 AUTO sub-checks** (R10) + sign the CHECKLIST sub-checks; escalate to `_review-needed/`.
6. **Touch no deck, no config, no component** (S3/S4 own those). Hand to **S9** for final verification.

## 6. Deliverables (what execution produces or changes)

### 6.1 — The inclusion test
The **R1 rule + the R3 officer-known set + the R4 plain-English stoplist + the maintained term-of-art
lexicon** (R6), recorded as the audit's machine-usable input. (The rule itself is §3; the lexicon/sets
are the data the sweep consumes and the continuous audit maintains.)

### 6.2 — The term→pages occurrence map (format)

A table the EXECUTE run applies without re-deciding:

| Term | Destination (anchor/page) | In glossary? | Pages to wire (first occurrence) | Notes |
|---|---|---|---|---|
| curtilage | `[[Curtilage]]` *(has page → R2)* | n/a | *(handled by S6 doctrine link)* | not glossary-wired |
| attenuation | `[[The Exclusionary Rule#attenuation]]` *or* `[[Common Legal Terms#attenuation]]` | add if no section home | Exclusionary Rule, Fruit-of-the-tree mentions, … | R2 fallback; courtroom term, not R3 |
| stare decisis | `[[Common Legal Terms#stare-decisis]]` | yes | Federal Court System, Common Law Origins, … | first occurrence each |
| voir dire | `[[Common Legal Terms#voir-dire]]` | yes | (where it occurs) | — |

*Columns:* **Term** · **Destination** (glossary anchor, or page/section per R2) · **In glossary?**
(yes / add / n/a) · **Pages to wire** (each page where the *first* occurrence gets the link) · **Notes**
(routing/exclusion rationale). Rows are produced by the R6 audit against finalized S6 text.

### 6.3 — The glossary-additions list (format)

For each **needs-adding** term, an authored entry ready to drop into `Common Legal Terms.md` under its
category, in the glossary voice:

```
### <Term>            ← becomes the addressable anchor (R7)
<plain-English definition, ≤ ~2 sentences, no citation unless a two-key case-tied proposition (R9)>
*Example:* <one concrete search-and-seizure example>
```

Plus, per entry: **target category** (existing `##` or a justified new one), and a **two-key flag** if
the definition asserts a case-tied proposition (→ serial CL, R9/R11).

### 6.4 — The anchorized glossary
`content/Common Legal Terms.md` restructured so every entry is a `###` heading anchor under its `##`
category (R7), with new entries (6.3) merged in. Preamble note retained ("established legal definitions
… stated plainly without citations"), adjusted for any two-key entry.

### 6.5 — The wired pages
Every in-scope page with its first-occurrence term links inserted (R8), routed per R2, exclusions per
R3/R4/R5. No other prose change (S6's briefs/case-links untouched).

### 6.6 — LINT-7 finalization note
The R10 split (AUTO sub-checks a–d; CHECKLIST sub-checks e–f) recorded in/aligned with the S1 lint
roster, closing S1 §9's open item.

## 7. Acceptance criteria (definition of done)

- [ ] **Inclusion test (R1):** the rule is stated testably (term-of-art only; no page-home; not the
      page's subject; not officer-known; first occurrence only); a sample sweep obeys all five conjuncts.
- [ ] **Routing (R2):** no term with its own doctrine/case page is glossary-wired; page-less terms-of-art
      go to `[[Common Legal Terms#anchor]]`; S6's case/doctrine links are not duplicated.
- [ ] **Officer-known set (R3):** the seed set is recorded, instructor-reviewed; no set-term is
      glossary-linked; courtroom terms-of-art outside the set remain wired.
- [ ] **Plain-English / self-link (R4/R5):** zero links on lay words; no self-referential link on the
      glossary or on a page whose subject is the term.
- [ ] **Audit (R6):** every in-scope page scanned; candidates deduped against the glossary; the
      **term→pages map** and the **glossary-additions list** are produced; the lexicon is updated.
- [ ] **Anchorization (R7):** every glossary entry is an addressable `###` heading under its `##`
      category; every anchor slug resolves; paired entries expose one anchor per linkable term.
- [ ] **Wiring (R8):** first qualifying occurrence per page is a piped wikilink to the glossary anchor;
      hover previews the definition (scrolled to the anchor), click lands on it; popover is
      definition-sized.
- [ ] **Authoring (R9):** every new entry has a plain-English definition + a concrete S&S example in the
      glossary voice; pure definitions carry no citation; case-tied propositions are two-key-verified or
      replaced by a page link.
- [ ] **LINT-7 (R10):** AUTO sub-checks (anchor resolution, density, no-banned-link, known-term coverage)
      run and pass; CHECKLIST sub-checks (novel-term discovery, definition accuracy) signed; S1 §9 closed.
- [ ] **Gate (R11):** every wired term + new entry traces to an adjudicated verdict; case-tied
      definitions show CL evidence; escalations logged; loop cap 3; no deck/config/component touched.

## 8. Verification plan (how S7's output gets verified — the audit gate)

The sweep runs through the standing **find → adjudicate → fix** machine (S1 §3.G), serial CL (L4),
checkpointed/resumable:

1. **REVIEW (parallel, free, NO CL).** Per page, reviewers emit findings
   `{id, page, term, locator, problem, severity, proposed_fix, needs_cl, confidence}` against:
   over-linking/density (R8), banned-link / own-subject / officer-known / plain-English (R1/R3/R4/R5),
   anchor resolution (R7), routing (R2 — a page-having term wrongly sent to the glossary), and
   definition accuracy + voice (R9). **Reviewers do not edit.**
2. **ADJUDICATE.** Each finding → {UPHELD, MODIFIED, DISMISSED, ESCALATE} with `adjudicated_fix` +
   `evidence`. **`needs_cl=true`** only for a **definition asserting a case-tied proposition** →
   the **single serial CL lane** (two-key, L1); verdict cites CL evidence (or the proposition is
   replaced by a page link). All link-mechanics + pure-definition findings → a **free
   editor-adjudicator**. **DISMISSED logged with reason.**
3. **FIX (parallel, free).** Apply only UPHELD/MODIFIED; insert no doctrine-page prose beyond the term
   link itself; **ESCALATE → `_review-needed/<slug>.md`**. **Loop cap 3.**
4. **Automated lint gate (pre-publish) — LINT-7 AUTO (R10):** (a) every `[[Common Legal Terms#x]]`
   resolves (engine shared with LINT-5); (b) no term linked >1× per page; (c) no R3-set / plain-English
   / has-a-page term glossary-wired; (d) every controlled-vocabulary term occurring on a page is wired on
   first occurrence. Ships only when green **and** the CHECKLIST sub-checks (novel-term discovery,
   definition accuracy) are signed.
5. **Popover spot-check (S3 · R6):** sample wired terms across page types — hover previews the anchored
   definition; click lands on the anchor under SPA nav; the popover is definition-sized (the
   glossary-popover style applies).
6. **No-orphan / coverage (D13):** every glossary entry is reachable (has an anchor and ≥1 inbound link
   or is intentionally reference-only); no qualifying recurring term is left entirely unwired site-wide
   (best-effort, R10).
7. **Non-regression:** S6's briefs, case-links, lexicon, and field framing are unchanged except for the
   inserted term links; no config/component/deck changed; the build succeeds and popovers fire.

## 9. Open items / escalations

- **The officer-known vernacular set (R3) is a judgment about *this* audience.** S7 seeds it; the
  **instructor confirms/edits** it at execution (e.g. is *attenuation* known cold, or does it stay
  wired? — S7's default keeps it **wired** as a courtroom term, not field vocabulary). Non-blocking;
  the set is data the audit consumes.
- **S8 boundary on citation-mechanics terms.** Terms whose home is the **Legal Research & Case
  Citations** page (S8) — *supra, id., pinpoint cite, reporter, parallel citation, en banc, certiorari,
  slip opinion, on remand, vacated* — should link to **that page**, not be re-defined in the glossary.
  Coordinate at execution so S7 and S8 don't double-define; if S8 lands after S7, leave those terms
  unwired and let S8's sweep claim them (route, don't duplicate).
- **Anchor-slug stability for paired/parenthetical entries (R7).** *Dicta (obiter dictum)*, *De facto
  vs. de jure*, *Subpoena duces tecum / ad testificandum*, *Probable cause vs. reasonable suspicion*:
  decide the canonical anchor per linkable term at execution (split vs. canonical-lemma-with-alternates);
  add `aliases`/heading-id stability if a slug would otherwise be ambiguous. The
  *Probable-cause/reasonable-suspicion* entry overlaps the **doctrine page** — keep the definitional
  glossary entry but route prose mentions to **[[Probable Cause and Reasonable Suspicion]]** (R2).
- **Continuous-audit cadence (N11).** N11 says the glossary is "audited continuously from live page
  text." S7 defines the audit; **S9** (and post-overhaul maintenance) re-runs it whenever page text
  changes so the term lexicon and wiring stay current. Flagged, not scheduled here.
- **Two-key load (R9/R11).** Only case-tied definitions hit the serial CL lane; the load is small
  relative to S5/S6/S9, but it shares the single lane (L4) — paced/checkpointed; RUNBOOK §3
  STOP-and-notify governs if the CL tier regresses.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual
choice; the rest are self-interviewed.*

### [USER] U1-S7 — Inclusion test breadth ("don't go overly broad") → **Term-of-art only.**
- *Options:* (a) **term-of-art only** — outside lay vernacular, primarily professional use, exclude the
  page's own subject; (b) **Latin/opaque only** — narrowest; (c) **legal-meaning-differs** — also link
  familiar words (search, seizure, consent) whose legal meaning differs from lay meaning.
- *Red-team (a):* still requires a judgment call on what's "lay" for this audience (resolved by U2/R3).
  *Steel-man (c):* the lay/legal gap is a real teaching point. *Red-team (c):* it would link the very
  words the doctrine pages exist to teach — the over-linking the wrapper warns against; and those words
  mostly have their own pages anyway (R2). *Steel-man (b):* maximally conservative. *Red-team (b):* drops
  genuinely opaque English-form terms of art (attenuation, standing, particularity).
- *Adjudication:* **(a)** (R1). User confirmed. Calibrated by R2 (page-having terms route to pages) and
  R3 (officer-known terms skipped), which together keep it from "going overly broad."

### [USER] U2-S7 — Audience calibration for officer-known terms → **Skip officer-known field vocabulary.**
- *Options:* (a) **skip** terms the officer/instructor audience knows cold (treat as vernacular *for this
  audience*); (b) **link them too** for completeness/newer students.
- *Red-team (a):* a brand-new student might not know "exigent"; *Steel-man (a):* the audience is
  practitioners — linking their daily vocabulary is noise, and the wrapper's whole steer is "don't go
  overly broad"; the few that a novice needs mostly have **doctrine pages** that teach them in full
  (better than a glossary blurb). *Red-team (b):* densened pages, diluted signal.
- *Adjudication:* **(a)** (R3). User confirmed. Recorded as an **instructor-editable seed set** (§9) so
  the audience call stays the instructor's; courtroom terms-of-art outside the set remain wired.

### [USER] U3-S7 — Link density → **First occurrence per page.**
- *Options:* (a) **first occurrence per page**; (b) **every occurrence**.
- *Red-team (a):* a reader who lands mid-page past the first mention misses the link; *Steel-man (a):*
  one definitional touch where the term is introduced is the clean teaching pattern and keeps long
  doctrine briefs readable. *Red-team (b):* repetitive, visually noisy, and the popover repeats the same
  definition every paragraph.
- *Adjudication:* **(a)** (R8). User confirmed. (Full-text **search** + the glossary page itself cover
  the "landed mid-page" case.)

### [USER] U4-S7 — Glossary granularity → **Single page + anchors.**
- *Options:* (a) **single `Common Legal Terms` page + heading anchors**; (b) **page per term**.
- *Red-team (a):* one long page; *Steel-man (a):* S3 · R6 **already built the popover mechanism around
  single-page anchors** (`[[Common Legal Terms#term]]`); the categorized reference read is valuable; the
  popover scrolls to the anchor so a long page is invisible to the hover user. *Red-team (b):* dozens of
  tiny files, fragments a cohesive reference, no popover benefit (anchors already work), maintenance
  churn; S4's per-case pages are per-page only because a case is a full BIRAC brief, not a 1–2-sentence
  definition — no precedent to match here.
- *Adjudication:* **(a)** (R7/R8). User confirmed.

### SI-1-S7 — Link-target routing: where does a term that *also* has a page point? → **The page, not the glossary.**
- *Question:* "probable cause," "curtilage," "plain view" are terms of art **and** have doctrine pages.
  Glossary or page?
- *Red-team (glossary):* uniform — every term goes to the glossary. *Red-team:* but it would send a
  reader to a one-line blurb instead of the full doctrine, and it **duplicates** the case/doctrine links
  S6 already wired (N7). *Steel-man (page):* N7 already says discuss-a-doctrine → link the doctrine; a
  glossary is the **fallback for terms with no page home**.
- *Adjudication:* **route to the page** (R2). The glossary wiring (S7's actual job) covers **only**
  page-less terms-of-art; S7 does not re-point or duplicate S6's doctrine/case links. This also shrinks
  the S7 sweep to exactly the gap N11 exists to fill.

### SI-2-S7 — Anchorization mechanism: headings vs. block ids? → **Promote entries to `###` headings under the `##` categories.**
- *Options:* (a) make each term a `### Term` heading (categories stay `##`); (b) keep bold-inline entries
  and append `^block-id` to each; (c) one `## Term` per entry (flat, no categories).
- *Red-team (b):* block ids are uglier to author/link and the popover-to-block scroll is less obviously
  reliable than heading anchors; *Red-team (c):* flattening loses the four useful categories and bloats
  the page TOC. *Steel-man (a):* heading anchors are Quartz-auto-slugged, are exactly what S3 · R6
  anticipated ("addressable `## Term` heading"), keep the category grouping (`##`) **and** give every
  term a clean anchor (`###`).
- *Adjudication:* **(a)** (R7). Headings under categories; paired entries split to one anchor per
  linkable term.

### SI-3-S7 — LINT-7 automatability (S1 §9 finalization) → **AUTO for anchors/density/banned-link/known-coverage; CHECKLIST for discovery + accuracy.**
- *Question:* S1 §9 left LINT-7 "best-effort, checklist-primary, decide automatability in S7."
- *Findings:* matching a **controlled vocabulary** of known terms against page text is deterministic and
  scriptable (anchor resolution, density, banned-link, known-term coverage). **Detecting *novel* terms
  of art** is fuzzy, and **judging definition accuracy/voice** is editorial — neither fully automatable.
- *Adjudication:* split LINT-7 (R10): **AUTO** sub-checks (a–d) run in the lint gate; **CHECKLIST**
  sub-checks (e novel-term discovery, f definition accuracy) stay human-reviewed. This **confirms** S1's
  "best-effort/checklist-primary" call while making the deterministic half hard-gated. S1 §9 closed.

### SI-4-S7 — Two-key for glossary definitions? → **Pure definitions need no cite; case-tied propositions are two-key, or link the page.**
- *Question:* the glossary preamble says entries are "established legal definitions … stated plainly
  without citations." Does N11/L1 force citations onto glossary entries?
- *Red-team (cite everything):* over-applies L1 to non-assertional definitions and clutters the glossary.
  *Steel-man:* L1 (two-key) governs **asserted legal propositions tied to authority**, not generic
  definitions of a term. A definition that *states a holding* ("X held that …") **is** an assertion.
- *Adjudication:* (R9) pure definitions = no citation (preserve the glossary's plain voice); a definition
  that asserts a case-tied proposition is **two-key-verified via serial CL** **or**, preferably, kept
  generic with the proposition moved to a **link to the owning page** — keeping the glossary definitional,
  not a second place holdings live (avoids the L1 drift the overhaul exists to kill).

### SI-5-S7 — S8 / overlapping-entry boundary → **Route citation-mechanics terms to S8; keep overlapping glossary entries but route prose to pages.**
- *Question:* citation terms (supra, id., en banc, certiorari) and entries that overlap doctrine pages
  (probable-cause/reasonable-suspicion).
- *Adjudication:* (§9) citation-mechanics terms link to the **S8 Legal Research page** (their home), not
  a duplicate glossary entry — coordinate so S7/S8 don't double-define; if S8 lands after S7, leave them
  unwired for S8 to claim. Overlapping definitional entries **stay** in the glossary (useful contrast)
  but **prose mentions route to the doctrine page** (R2). No entry is retired without the instructor's
  say-so.
