# CSSI — STANDARDS (the governing contract)

status: GOVERNING · authority: TOP
supersedes: `docs/FINAL-QA-SPEC.md` (authority absorbed; retained as history)
derived-from: `_overhaul/specs/S1-standards.spec.md` §3 (this document is the prose realization of S1 §3)
last-updated: 2026-06-30

---

## 0. Supremacy clause (SR-3)

**`docs/STANDARDS.md` is the single top-authority contract for the CSSI overhaul.**

It **absorbs** `docs/FINAL-QA-SPEC.md`'s §0 adversarial self-critique (the 15-point
failure-mode register) and the D1–D12 reviewer dimensions — now **carried, extended, and
expanded to D1–D14** in §4 below. `docs/FINAL-QA-SPEC.md` is retained only as historical
reference and carries a pointer header transferring its authority here.

On **any conflict** between this document and any other document — a spec, a runbook, a
prior manifest, the QA spec, a page convention — **STANDARDS.md governs.** Every later
spec (**S2 through S9**) and the autonomous **EXECUTE** run are bound by it: each must cite
STANDARDS.md as governing and may extend it, but may never contradict or weaken it.

This document is written to be read **top-to-bottom** as a reference and **grepped** by
rule ID (`L1`…`L8`, `N1`…`N13`, `SR-1`…`SR-5`), by dimension (`D1`…`D14`), and by lint
(`LINT-1`…`LINT-8`). Nothing here edits content pages; it states the rules every page,
deck, card, and verification pass must satisfy.

**The catalog at a glance:** 8 scar-rules (L1–L8) + 13 mechanism-rules (N1–N13) + 5
S1-introduced standard rules (SR-1…SR-5) = **26 enforceable rules**, mapped onto **14**
reviewer dimensions and **8** automated lints.

---

## 1. How to read a rule

Every rule is stated **testable**, with:

- **Rule statement** — what is required.
- **Trigger** — when the rule applies (the condition that puts a page/assertion in scope).
- **Check** — how a reviewer or script verifies compliance.
- **Enforcement** — one or more tags:
  - `AUTO:LINT-n` — a deterministic script in the lint roster (§7) decides it.
  - `CHECKLIST:Dn` — reviewer judgment against dimension *Dn* (§4) decides it.
  - `PROCESS` — orchestration discipline (the research protocol §5, the
    find→adjudicate→fix machine §6) decides it.

A rule may carry more than one tag (e.g. an `AUTO` guard plus a `CHECKLIST` backstop).

---

## 2. The rules catalog

### 2.A Scar-rules (already paid for — carried from the lessons register)

These eight are failure modes the prior build actually hit. They are non-negotiable.

#### L1 — Two-key rule / paraphrase drift
Every holding, rule statement, and quotation on any page or card traces to the primary
opinion via the **two-key rule**: **(key-1)** existence + proposition + verbatim pinpoint
where quoted; **(key-2)** good-law status. **Decks derive FROM verified pages, never the
reverse.**
- **Trigger:** any asserted holding / rule / quote / case anywhere.
- **Check:** the assertion appears in the assertion inventory with a CL-cited verdict;
  quotes are verbatim with a confirmed pinpoint; no card asserts a fact absent from its
  source page.
- **Enforcement:** `AUTO:LINT-2` (quote/pinpoint presence) + `AUTO:` deck↔page id check +
  `CHECKLIST:D1`.

#### L2 — Web is discovery-only
Nothing enters a page until confirmed against the primary opinion on CourtListener.
**Discovery ≠ assertion.**
- **Trigger:** any content sourced from web / secondary material.
- **Check:** every web-surfaced case/holding/quote has a corresponding CL confirmation in
  the manifest before it appears; unconfirmed items are flagged, never asserted.
- **Enforcement:** `PROCESS` (§5) + `CHECKLIST:D1/D3`.

#### L3 — cluster-id ≠ opinion-id
Every CL URL must resolve (HTTP 200) **AND** display the **named** case (identity, not just
status). Resolve cluster → lead opinion id for post-~2015 cases; confirm the case name in
returned text before trusting any quote.
- **Trigger:** any CL URL on a page, or any quote read from CL.
- **Check:** the link-checker confirms the URL resolves and the returned text contains the
  case name; quote-reads are logged against the confirmed opinion id.
- **Enforcement:** `AUTO:LINT-1` (CL-URL identity) + `CHECKLIST:D7`.

#### L4 — One serial CL lane
**ALL** CourtListener calls go through a single serial lane (concurrency-1), **always** —
writing, review, adjudication, and research alike.
- **Trigger:** any CL call anywhere in execution.
- **Check:** `cl-calls.log` shows a single serial lane with no concurrent timestamps; the
  tier probe was run; the STOP-on-old-5/min-tier rule was honored.
- **Enforcement:** `PROCESS` + `CHECKLIST` (audit `cl-calls.log`).

#### L5 — find → adjudicate → fix (no reviewer edits)
Hard separation of the three roles. A reviewer never edits; a **legal** assertion never
changes without CL evidence at adjudication.
- **Trigger:** any review finding that would change a page.
- **Check:** every change traces to an adjudicated verdict (UPHELD/MODIFIED) with evidence;
  reviewers produced findings only; DISMISSED findings are logged with a reason.
- **Enforcement:** `PROCESS` (§6) + `CHECKLIST` (audit the findings→adjudications→fixes trail).

#### L6 — "Not found" ≠ "doesn't exist"
Before declaring a case fake/unverifiable, run the **misspelling-tolerant escalation
ladder** (reporter cite → name/phonetic variants → proposition full-text → web → re-locate
in CL). Only then mark `UNVERIFIABLE`, flagged, never asserted.
- **Trigger:** any CL lookup miss on a captured/cited case.
- **Check:** an `UNVERIFIABLE` verdict shows the full ladder was run (logged); no case
  marked fake from a single miss.
- **Enforcement:** `PROCESS` (§5) + `CHECKLIST:D1`.

#### L7 — Scope-boundary claims are assertions (no narrow-scope synthesis)
A statement that **bounds a doctrine's reach — especially a *negative* bound** ("does not
reach X", "only Y", "vehicles, not persons") — is an **assertion, not discovery** (L2), and
carries the **two-key burden**. It must rest on **frontier-level** progressive research
(N12 Hop-2: circuit/state treatment, splits, first-impression) confirmed against
**primary** authority — never on secondary-source synthesis alone. Until that research is
run, the scope is recorded as **"unresolved — research,"** never as the narrow reading.
*(Scar: in the S2 interview, community caretaking was first framed "vehicles, not persons
outside the home" from secondary synthesis; the mandated frontier pass then surfaced the
controlling person-caretaking line —* United States v. Garner *(10th Cir.) 3-part
caretaking-detention test;* United States v. Rideau *(5th Cir.) impaired-person-in-roadway;*
Graham v. Barnette *(8th Cir.) PC-of-dangerousness for emergency mental-health seizures —
reversing the boundary.)*
- **Trigger:** any who/what/where scope statement; any "only / never / does-not-reach"
  language.
- **Check:** every scope boundary cites primary authority at the frontier; negative bounds
  show the Hop-2 frontier pass was run (logged); no scope claim rests on secondary synthesis
  alone.
- **Enforcement:** `PROCESS` (§5 — frontier hop mandatory for scope claims) + `CHECKLIST:D2/D4`.
- *Relation:* strengthens **N10** (state scope) and **N12** (progressive research); sibling
  of **L2**.

#### L8 — Restatement, not editorialization (explanatory prose may not move the holding)
Any explanatory, practical, "what-this-means," or teaching-*takeaway* paraphrase of a
holding or rule — especially the **un-anchored blocks that do not quote the opinion** — must
**restate** it faithfully and may **not add, drop, narrow, or broaden** a condition of the
rule it conveys. A takeaway that moves the holding is **paraphrase drift (L1)** and, where
it bounds reach, a **negative-scope assertion (L7)** — carrying the **two-key burden**, not a
free-writing license. **Operating principle: case pages *restate*; doctrine pages *teach*.**
Generalized field framing (N9) lives on doctrine pages under the **SR-2** instructor gate and
is never injected into the canonical case record. *(Scar: in the S4 interview a draft
"Field-IRAC" takeaway rewrote* Brigham City v. Stuart*'s "objectively reasonable basis to
**believe** an occupant is injured" into "**see** it," narrowing a source-agnostic standard
into a visual-observation rule the Court never imposed.)*
- **Trigger:** any practical/takeaway/explanatory paraphrase of a holding or rule (a
  case-page Application or takeaway; a doctrine-brief "what this means"; any "you may / must /
  need only…" operational line).
- **Check:** the prose adds or drops no element of the pinpointed holding; case pages carry
  no generalized field-advice beyond a faithful restatement; field framing appears on
  doctrine pages with instructor sign-off; spot-check the paraphrase against the opinion.
- **Enforcement:** `CHECKLIST:D2/D4/D9` + `PROCESS` (instructor review of doctrine-page field
  framing).
- *Relation:* strengthens **L1**, **L7**, and **N1**; sibling of **L1**.

### 2.B Mechanism-rules (from the instructor's page-by-page notes)

#### N1 — Placement by holding, not keyword
A case's home page and key/related status is set by the legal proposition it stands for, not
surface-keyword overlap.
- **Trigger:** assigning a case to a page or to key/related.
- **Check:** each placement is justified by the case's holding (the proposition supports
  THIS page's doctrine); e.g. *Matlock* = consent/common-authority, not abandonment.
- **Enforcement:** `CHECKLIST:D2/D5`.

#### N2 — Authority-weight lexicon
Use the fixed **6-tier lexicon** (§3) everywhere; **never** "persuasive, not binding";
circuit cases name the circuit; splits flagged.
- **Trigger:** any authority/weight label on any case.
- **Check:** every weight label is one of the 6 tiers; circuit cases carry the circuit; no
  banned phrasing.
- **Enforcement:** `AUTO:LINT-4` (lexicon vocabulary) + `CHECKLIST:D6`.

#### N3 — Tests stated up front
Any named test / prongs / elements appear explicitly in the Rule/brief at the top — never
left for the reader to reconstruct (e.g. the *Dunn* 4 factors).
- **Trigger:** a doctrine governed by a named multi-factor/element test.
- **Check:** the test and all its prongs appear in the top brief; reviewer confirms
  completeness.
- **Enforcement:** `CHECKLIST:D14/D4`.

#### N4 — Subsequent treatment inline
Where a case is materially narrowed/limited/abrogated, tag **"limited by [linked case]"** at
the point of assertion; add a 1–2 sentence *why* **only when it changes field application**
*(user-confirmed threshold).*
- **Trigger:** asserting a case with material negative subsequent treatment.
- **Check:** the inline tag is present wherever the case is asserted; the explanation is
  present iff field application changes; the treatment is stated consistently across every
  page the case appears on.
- **Enforcement:** `CHECKLIST:D3/D5`.

#### N5 — Recent-developments is role-based, not recency-based
That section is for circuit/state cases that expand/narrow/split/first-impression vs SCOTUS.
**Any SCOTUS holding belongs in Key cases regardless of date** (e.g. re-home *Case v.
Montana*).
- **Trigger:** placing a case in Recent-developments.
- **Check:** no SCOTUS case appears there; every entry has an
  expand/narrow/split/first-impression role labeled.
- **Enforcement:** `AUTO:LINT-3` (no-SCOTUS-in-recent-developments) + `CHECKLIST:D10`.

#### N6 — Key-status is non-exclusive
A case is Key on a page if central to THAT doctrine, independent of being key elsewhere;
multi-homing is expected and framing is page-specific (promote *Herring* on Collective
Knowledge; move *Riley* to Related on Common Law).
- **Trigger:** assigning key/related to a multi-homed case.
- **Check:** key/related is decided per-page by centrality to that doctrine; framing differs
  appropriately across homes.
- **Enforcement:** `CHECKLIST:D2/D5`.

#### N7 — Link every named case
Every case named anywhere links to its own case page; passage-specific discussion →
deep-link to the pinpoint/highlighted span; whole-case reference → link the case page.
- **Trigger:** any case name in prose/tables.
- **Check:** no bare unlinked case name; passage discussions deep-link; link targets resolve.
- **Enforcement:** `AUTO:LINT-5` (link-every-named-case) + `CHECKLIST:D13`.

#### N8 — Brief-first
The full teaching brief (rule + limits + nuance + pitfalls, integrated) reads top-to-bottom
first; tables + recent developments follow as supporting apparatus.
- **Trigger:** any doctrine page.
- **Check:** the brief is the first substantive content and is self-contained; apparatus
  follows it.
- **Enforcement:** `CHECKLIST:D14/D10`.

#### N9 — Frame around the officer's field-decisive question
Frame each doctrine around the operational question an officer must answer, not "what is the
exception." For misunderstood topics (e.g. knock-and-talk) be exhaustive on line-drawing.
- **Trigger:** authoring/reformatting any doctrine brief.
- **Check:** the brief leads with the field-decisive question and draws the lines; reviewer
  (instructor lens) confirms.
- **Enforcement:** `CHECKLIST:D9/D14`.

#### N10 — State scope explicitly
State what/who/where a doctrine covers; split bundled doctrines; research, never assume (e.g.
community caretaking: persons vs vehicles — resolved in S2).
- **Trigger:** a doctrine with ambiguous or bundled scope.
- **Check:** scope is stated explicitly; bundled doctrines split or boundary-noted; scope
  claims are authority-backed.
- **Enforcement:** `CHECKLIST:D4/D2`.

#### N11 — Wire the glossary
Non-vernacular terms link to the glossary (hover-preview + click-through); the glossary is
audited continuously from live page text.
- **Trigger:** any non-vernacular legal term in prose.
- **Check:** terms link to the glossary; the glossary covers all terms used; no orphan terms.
- **Enforcement:** `AUTO:LINT-7` (glossary wiring, best-effort) + `CHECKLIST:D13/D11`.

#### N12 — Progressive research
narrow issue → doctrine/keyword → expand → learn → expand, **bounded**. Assume nothing; web
discovers, CL confirms (protocol + bound in §5).
- **Trigger:** rounding out any page beyond captured seed cases.
- **Check:** research followed the bounded protocol; a stop condition was met; all additions
  are CL-verified.
- **Enforcement:** `PROCESS` (§5) + `CHECKLIST:D4`.

#### N13 — No blank treatment status
Every case carries an explicit, verified good-law treatment status; "good as of <date>" only
after a check.
- **Trigger:** any case asserted on any page or in the Case Index.
- **Check:** every case row/assertion carries a non-blank treatment status with a check date;
  no "good" without a logged check.
- **Enforcement:** `AUTO:LINT-6` (treatment-status presence) + `CHECKLIST:D3`.

### 2.C New standard rules introduced by S1 (the five user-owned decisions)

#### SR-1 — Exhaustive live re-verification (USER DECISION)
Every asserted case is re-verified **live against the primary opinion** through the serial CL
lane — **including manifest-grade cases** — for proposition, every verbatim quote + pinpoint,
and good-law currency. No case is exempt by prior verification grade; prior manifests are a
starting reference, not a substitute for the live re-check.
- **Trigger:** the S9 exhaustive pass; any page authored/reformatted in S5/S6.
- **Check:** the assertion inventory shows a fresh live-CL verdict for **every** case;
  `cl-calls.log` evidences the re-check; zero cases pass on manifest alone.
- **Enforcement:** `PROCESS` (S9, serial lane, RUNBOOK §3) + `CHECKLIST:D1` + audit
  (inventory completeness).
- *Note:* this is the heaviest CL load in the project; it runs patiently in the single serial
  lane, checkpointed; if the CL tier regresses to 5/min, RUNBOOK §3 STOP-and-notify governs.

#### SR-2 — Instructor-grade framing gate (USER DECISION; blocking)
Citation accuracy is necessary but **not sufficient**. Every doctrine page must also pass an
instructor-grade gate: the rule/test is stated correctly and up front (N3); the doctrine is
**complete** (black-letter rule · elements/prongs · burden + who bears it · standard of
review · remedy · controlling authority + progeny by role · limits · nuances · pitfalls · the
operational "apply it" angle — the D4 checklist); and it **actually teaches** (D9). A page
with perfect cites but a muddled or incomplete brief **FAILS** and is escalated, not shipped.
- **Trigger:** every doctrine page at review/sign-off.
- **Check:** the page passes the composite gate **D2 ∧ D4 ∧ D9 ∧ D14**; the completeness
  checklist has no unlogged gap; a reviewer signs off teachability.
- **Enforcement:** `CHECKLIST` (composite, blocking).

#### SR-3 — STANDARDS.md supremacy (USER DECISION)
`docs/STANDARDS.md` is the single top-authority contract. It **absorbs**
`FINAL-QA-SPEC.md`'s §0 self-critique and the D1–D12 dimensions (now extended). On any
conflict, STANDARDS.md governs; `FINAL-QA-SPEC.md` is retained as historical reference with a
pointer header. Every later spec (S2–S9) and the EXECUTE run obey it.
- **Trigger:** any cross-doc conflict or later-spec authoring.
- **Check:** STANDARDS.md exists and is cited as governing in S2–S9; `FINAL-QA-SPEC.md`
  carries the pointer header; no later spec contradicts STANDARDS.md.
- **Enforcement:** `PROCESS` + `CHECKLIST`.
- *(This rule is declared operatively in §0 above.)*

#### SR-4 — Enforcement model (USER DECISION)
Enforce **automated where cheap + reviewer checklist** for judgment. The automated lint
roster (§7, LINT-1…8) runs at pre-publish (`redeploy.sh` validation gate) / CI; the reviewer
checklist (the D-dimensions) covers framing, completeness, pedagogy, placement, and Mermaid
doctrinal accuracy. A page ships only when **both** pass (or escalations are logged in
`_review-needed/`).
- **Trigger:** pre-publish and per-page review.
- **Check:** the lint roster is green; the reviewer checklist is signed; escalations are
  logged.
- **Enforcement:** `AUTO` (roster) + `CHECKLIST`.

#### SR-5 — Independent-replication concordance (build-time cross-verification)
*(Added 2026-06-29 during the S5 interview — S1 Appendix A · SI-8.)*
Where conclusions already produced and verified by a **prior thread** (a prior research
manifest, a prior build, an independent reviewer) are re-derived by a **new pass**, the new
pass runs **conclusion-blind** to the prior result — forming and **recording its own
conclusions first** — and is then **reconciled** against the prior thread. **Concordance**
(same case set · holding/ratio · home-by-holding (N1) · role · treatment/good-law · split
call) raises the assertion to **double-verified** (a stronger grade than a single pass).
**Fundamental discordance** — any of those axes differ; cosmetic wording/ordering does
**not** count — **escalates** to the find→adjudicate→fix machine (§6), is **adjudicated
against primary authority** (serial CL, L4), and the verdict must state **what diverged**
(prior wrong / new wrong / scope-or-framing shift) and **which conclusion stands**.
Independence is **conclusion-blind** (both threads may use the same primary sources; the new
thread must **not** be seeded with the prior thread's conclusions) and is **enforced by
orchestration** (freeze prior → run new with prior withheld → reconcile). **No prior verified
conclusion may be silently absent** from the reconciliation. Strengthens **SR-1** (adds a
cross-source *agreement* axis to live re-verification) and feeds **L5** (discordances are
findings).
- **Trigger:** any pass that re-derives conclusions a prior verified thread already produced
  (S5 ingest vs. the prior manifests; the S9 final verification vs. the build).
- **Check:** the prior conclusion set was **frozen before** the new pass began; the new pass
  **recorded its conclusions before** reconciliation; every item carries a
  concordant/discordant disposition; fundamental discordances were adjudicated with
  primary-authority evidence + a logged verdict; no prior verified conclusion is silently
  dropped.
- **Enforcement:** `PROCESS` (orchestration: blind-then-reconcile) + `CHECKLIST:D1/D5` +
  `AUTO` (concordance diff where the conclusion sets are structured).

---

## 3. The authority-weight lexicon (mandatory vocabulary)

These six tiers are the **only** permitted authority labels site-wide. The blunt phrase
**"persuasive, not binding" is BANNED.**

| # | Tier label | Meaning |
|---|---|---|
| 1 | **Binding — SCOTUS** | Nationwide binding authority. |
| 2 | **Binding in-circuit** | A circuit holding, within its own circuit, on a case heard there. |
| 3 | **Persuasive (outside circuit)** | Replaces the banned "persuasive, not binding." |
| 4 | **Persuasive — state, illustrative** | Paired with the federal rule. |
| 5 | **Persuasive only — non-precedential** | Unpublished; the only "not binding even at home" tier. |
| 6 | **Historical** | English/colonial origins; or overruled cases shown as history. |

Circuit cases must **name the circuit** (e.g. "Binding in-circuit — 9th Cir."); genuine
splits are flagged. This is enforced by `AUTO:LINT-4` + `CHECKLIST:D6` (N2).

### 3.1 The orthogonal treatment-status axis

Authority-weight is **separate from** good-law currency. Every case **also** carries a
good-law **treatment status** drawn from a fixed set, with an `as_of` check date (N13):

```
treatment-status ∈ { good | criticized | limited | abrogated | overruled }   as_of <date>
```

- **Authority-weight (the six tiers)** describes the case's *precedential weight*.
- **Treatment status** describes its *current validity*.

The two axes are **orthogonal** and must both be present. An overruled US case is shown under
**tier 6 (Historical)** **and** carries `overruled` treatment everywhere it appears (D5). No
case carries a blank treatment status, and no case is marked `good` without a logged check
(N13 / `AUTO:LINT-6`).

---

## 4. The check dimensions (D1–D14)

The existing D1–D12 reviewer framework is **carried**; three dimensions are **extended**; two
new dimensions (**D13, D14**) are **added**. Each dimension maps to the rules it enforces;
every rule maps to ≥1 dimension or PROCESS lane (the **no-orphan invariant**).

### 4.1 The rule → dimension mapping

| Dim | Name | Status | Rules it enforces |
|---|---|---|---|
| D1 | Accuracy / two-key (exhaustive) | **extended → exhaustive-live (SR-1)** | L1, L2, L6, SR-1, SR-5 |
| D2 | Framing | carried | N1, N6, N10, L7, L8 |
| D3 | Shepardize + new frontier | **extended (N4, N13)** | N4, N13, L2 |
| D4 | Completeness | carried | N3, N9, N10, N12, SR-2, L7, L8 |
| D5 | Internal consistency & cross-page coherence | carried | N1, N4, N6, SR-5 |
| D6 | Guardrails | **extended (N2 lexicon)** | N2 + fed/state, apocryphal trio, mnemonics, no inline flashcards |
| D7 | Citation hygiene | carried | L3, L1 (quote/pinpoint) |
| D8 | Visual accuracy (Mermaid) | carried | (render + doctrinal faithfulness) |
| D9 | Pedagogy / teachability | carried | N9, SR-2, L8 |
| D10 | Structure / spec compliance | carried | N5, N8 |
| D11 | Practical/reference/history pages | carried | N11 (glossary accuracy) + guardrails |
| D12 | Deck ↔ page ↔ index integrity | carried | L1 (decks derive from pages) |
| **D13** | **Linking & glossary wiring** | **NEW** | **N7, N11** |
| **D14** | **Brief-first architecture & teachability-up-front** | **NEW** | **N3, N8, N9** |

Process-lane rules (no dedicated dimension, enforced by orchestration discipline and audit):
**L4** (one serial lane — `cl-calls.log` audit), **L5** (find→adjudicate→fix trail audit),
**SR-3** (supremacy — cross-doc audit), **SR-4** (enforcement model — roster + checklist
audit). Every rule therefore maps to at least one dimension **or** a PROCESS lane; no rule is
orphaned, and every dimension carries at least one rule.

### 4.2 The extended and new dimensions (acceptance lines)

- **D1 — Accuracy / two-key (exhaustive → exhaustive-live, SR-1).** Every asserted case,
  holding, fact, quote, and pinpoint traces to the opinion; under SR-1 every case is
  re-verified **live** against the primary opinion, not on a prior manifest. *Acceptance:*
  every assertion in the inventory has a fresh CL verdict; zero unverified legal claims
  asserted as settled.
- **D3 — Shepardize + new frontier (extended: N4, N13).** Still-valid-law check plus
  subsequent-treatment-inline (N4) and no-blank-treatment-status (N13); genuine
  splits/restrictions/frontiers surfaced and labeled. *Acceptance:* current good-law status
  recorded for every case; inline treatment tags present and consistent; nothing stale
  asserted as current.
- **D6 — Guardrails (extended: N2 lexicon).** The federal/state guardrails plus the mandatory
  6-tier lexicon (N2): every authority label is one of the six tiers, circuit cases name the
  circuit, no banned "persuasive, not binding," no apocryphal trio, mnemonics uncited, no
  inline flashcards. *Acceptance:* fed/state never blurred; lexicon-clean; guardrail-clean.
- **D13 — Linking & glossary wiring (NEW).** Every named case links to its case page; passage
  discussions deep-link to the pinpoint span; non-vernacular terms link to the glossary; all
  link targets resolve. *Acceptance:* no bare case name; no orphan glossary term; deep-links
  point to the correct span; zero broken wikilinks.
- **D14 — Brief-first architecture & teachability-up-front (NEW).** The integrated teaching
  brief reads top-to-bottom and self-contained as the first content; named tests/prongs
  appear up front; the page is framed around the field-decisive question; tables and
  recent-developments follow as apparatus. *Acceptance:* brief-first order holds on every
  doctrine page; tests are stated, not reconstructed.

### 4.3 The carried dimensions (reference)

- **D2 — Framing.** Each case framed correctly *for the doctrine of THIS page*; nuances and
  pitfalls explained, not just named.
- **D4 — Completeness.** Full per-doctrine checklist: black-letter rule · elements/prongs ·
  burden + who bears it · standard of review · remedy · controlling authority + progeny by
  role · limits · nuances · pitfalls · recent developments · cross-links · the operational
  "apply it" angle.
- **D5 — Internal consistency & cross-page coherence.** Shared cases framed and treated
  consistently across pages; overruled cases shown as history everywhere; no contradictions.
- **D7 — Citation hygiene.** Bluebook consistency; pinpoint present wherever a quote appears;
  every CL URL resolves (200) and shows the named case.
- **D8 — Visual accuracy (Mermaid).** Render every diagram and visually inspect; every
  node/branch matches the page's stated rule.
- **D9 — Pedagogy / teachability.** Rule-first clarity, the "why," operational application,
  instructor voice, digestible.
- **D10 — Structure / spec compliance.** Template sections present + ordered; frontmatter
  correct (single controlling amendment; aliases for renamed pages); in the MOC.
- **D11 — Practical/reference/history pages.** The non-case pages: mnemonics verbatim,
  glossary accurate, court-system/research facts correct, history framed as history, no rot.
- **D12 — Deck ↔ page ↔ index integrity.** No orphaned deck cards; card `page`/`source`
  valid; Case Index regenerated and correct; decks derive from verified pages.

---

## 5. The research discipline (N12 — progressive, bounded)

For each page, **seed = the captured cases plus the controlling foundational SCOTUS authority
the doctrine rests on**, added even if uncaptured (*Chimel* for SITA, *Schneckloth* for
consent). Then expand progressively through at most three hops:

- **Hop 0 (seed):** the proposition the capture/page states.
- **Hop 1 (doctrine/keyword):** the named test, its elements, the controlling authority +
  significant progeny by role.
- **Hop 2 (frontier):** circuit splits, recent developments, weak-but-overused field cases
  officers rely on, issues of first impression.

**Recursion bound:** at most **2 expansion hops beyond the seed** per page.

**Division of labor — web discovers, CL confirms:** web search (free, parallel)
**discovers** candidates; the **single serial CL lane** (L4) **confirms** existence +
proposition + verbatim quote before anything is asserted (L2).

**Stop conditions (any one ends the research for a page):**
1. the D4 completeness checklist for the doctrine is fully covered;
2. a full hop surfaces no new load-bearing authority;
3. the page would exceed the ½–1-page digestible budget — then cut to load-bearing authority
   only.

**Case identification (L6 / RUNBOOK §3a):** misspelling-tolerant — never declare a case fake
from one miss; run the escalation ladder (reporter cite → name/phonetic variants →
proposition full-text → web → re-locate in CL). The **cluster-id ≠ opinion-id (L3)** guard
applies on every read.

**Scope claims (L7) — frontier mandate:** any boundary on a doctrine's reach — and especially
a *negative* one ("only X" / "does not reach Y") — is treated as an assertion: the **Hop-2
frontier pass is mandatory** (circuit/state treatment, splits, first-impression) **plus**
primary confirmation before the boundary may appear. Until then the page records the scope as
**"unresolved — research,"** never the narrow reading.

---

## 6. The find → adjudicate → fix machine (L5/L4 — adopted verbatim from FINAL-QA §2)

The standing verification machine is **adopted from `FINAL-QA-SPEC.md` §2 unchanged** (S1
SI-4), now governed by STANDARDS.md. Three separated roles; a legal assertion never changes
on a reviewer's opinion alone.

1. **REVIEW** (parallel, free, **NO CL**). Per page, dimensional reviewers emit structured
   findings:
   `{id, page, dimension(D1–D14), locator(section + verbatim text), problem, severity(high|med|low), proposed_fix, needs_cl, confidence}`.
   **Reviewers may not edit pages.** They surface, they don't decide.

2. **ADJUDICATE.** Every finding → a verdict in the set
   **{UPHELD, MODIFIED, DISMISSED, ESCALATE}** with `adjudicated_fix` + `evidence`.
   - `needs_cl=true` findings (good-law, proposition, quote/pinpoint, case existence, CL-URL,
     new-frontier) → adjudicated by the **single serial CL lane**; the verdict **must cite CL
     evidence** (a confirmed pinpoint/quote or treatment). **No CL evidence → cannot UPHOLD a
     change to a legal assertion** (→ DISMISS or ESCALATE).
   - Non-legal findings (formatting, structure, missing cross-link, internal contradiction,
     pedagogy, corpus-supported completeness gap) → a free editor-adjudicator.
   - **DISMISSED findings are logged with the reason** (a dismissed false-positive is a
     successful outcome — it guards against over-correction).

3. **FIX** (parallel, free). Per page, a fixer applies **only** UPHELD/MODIFIED adjudicated
   fixes, verbatim from the adjudication; **ESCALATE → `_review-needed/`**. The fixer
   introduces no new content of its own.

**Loop cap 3**, then escalate to `_review-needed/<slug>.md` with the open issue. **Checkpoint
the ledger after every sub-phase** (resumable). Surface consequential calls in the final
report.

---

## 7. The enforcement model (SR-4 — automated where cheap + reviewer checklist)

A page ships only when **both** gates pass (or escalations are logged in `_review-needed/`):
(1) the automated lint roster is green, **and** (2) the D1–D14 reviewer checklist is signed.

### 7.1 Automated lint roster (deterministic)

Runs at pre-publish via `redeploy.sh` validation and/or CI; the CL-touching lint reuses the
single serial lane (L4).

| Lint | What it checks | Enforces |
|---|---|---|
| **LINT-1** | Every CL URL resolves (200) **and** returned text contains the named case | L3, D7 |
| **LINT-2** | Every block/inline quote has an accompanying pinpoint cite (else de-quote/pin) | L1, D7 |
| **LINT-3** | Doctrine-page section order present; **no SCOTUS case in Recent-developments**; single controlling amendment in frontmatter | N5, N8, D10 |
| **LINT-4** | Every authority label is one of the 6 tiers; banned "persuasive, not binding"; circuit cases name the circuit | N2, D6 |
| **LINT-5** | Every named case resolves to a case-page wikilink (no bare case names) | N7, D13 |
| **LINT-6** | Every asserted case carries a non-blank treatment status with a check date | N13, D3 |
| **LINT-7** | Non-vernacular terms link to the glossary (**best-effort; checklist-primary** — see §8) | N11, D13 |
| **LINT-8** | Guardrails: no apocryphal Holiday/McCall/Smith trio; mnemonics uncited; no inline `## Flashcards` | D6 |

### 7.2 Reviewer checklist (judgment — the D-dimensions)

The reviewer checklist covers what scripts cannot decide: framing correctness (D2),
placement-by-holding (N1/D2), completeness vs the D4 checklist (D4), cross-page coherence
(D5), Mermaid doctrinal accuracy (D8), pedagogy/teachability (D9), brief-first architecture
(D14), and the **SR-2 instructor-grade composite gate (D2 ∧ D4 ∧ D9 ∧ D14, blocking)**.

**Both required pre-ship.** A page ships only when the roster is green **and** the checklist
is signed (or escalations are logged in `_review-needed/`).

> **Open item (S1 §9):** LINT-7 (glossary wiring, N11) is only *best-effort* automatable —
> term detection is fuzzy. It is flagged **checklist-primary**; its final automatability is
> decided in **S7** (Legal-Term Linking). LINT-5's deep-link-to-span check is finalized once
> **S4** defines the case-page anchor scheme.

---

## 8. Canonical template tables of contents (§3.I)

### 8.1 Brief-first doctrine page (N8) — section order

1. **Frontmatter** — single controlling amendment; aliases (renamed pages); `related:`.
2. **The Brief** (top, integrated, self-contained, reads top-to-bottom):
   field-decisive question (N9) → black-letter rule + named test/prongs stated up front (N3)
   → elements / burden + who bears it / standard of review / remedy → limits & nuances →
   common pitfalls.
3. **Key cases** — table: *case · holding · authority-weight (6-tier) · treatment status ·
   CL link · case-page link*; non-exclusive key-status (N6); placement-by-holding (N1).
4. **Related cases across doctrines** — framed for THIS page's doctrine.
5. **Recent developments** — role-based (circuit/state expand/narrow/split/first-impression;
   **no SCOTUS** — N5).
6. **Visual (Mermaid)** — where a multi-factor/branching test exists.
7. **Sources.**

*Cross-cutting on every doctrine page:* link every named case (N7); subsequent-treatment
inline (N4); glossary-wired terms (N11); authority lexicon (N2); two-key (L1).

### 8.2 Officer-IRAC case page (N7 home target) — skeleton owned by S4, referenced here

Reference order: **Facts → Issue → Held → Discussion/Reasoning → Rule/Holding (with pinpoint)
→ authority weight (6-tier) + treatment status → Citation (topic) → backlinks to doctrine
pages.**

The **detailed** skeleton (anchors for deep-linking per N7, frontmatter, aliases) is defined
in **S4**. S1/STANDARDS states only the **cross-cutting rules the case page must honor**:
tests-up-front (N3), link-every-case (N7), two-key (L1), lexicon (N2), treatment-status
(N13). Per L8, **case pages *restate*; doctrine pages *teach*** — no generalized field-advice
on the canonical case record.

---

## 9. Consistency with prior rulings (DECISIONS.md D-0…D-8)

This document **extends, never reverses** the prior self-interview decision log (S1 §8):

- **D-3 (slug stability / naming):** preserved — renamed pages carry aliases (template
  frontmatter §8.1/§8.2); no slug is silently changed.
- **D-5 (two-key + circuit-split policy):** preserved and strengthened — the two-key rule
  (L1) governs every assertion, circuit cases name the circuit and flag splits (N2 / §3),
  and SR-1 adds exhaustive live re-verification on top.
- **D-6 (lossless deck):** preserved — decks derive FROM verified pages and never the reverse
  (L1); deck↔page↔index integrity is D12; flashcard ids are preserved.

No rule in this catalog contradicts D-0…D-8.

---

*End of STANDARDS.md — the governing contract. On any conflict, this document governs.*
