# SPEC S1 — Standards & the Self-Improvement Pass
status: APPROVED
depends-on: []            gates: [S2, S3, S4, S5, S6, S7, S8, S9]
last-updated: 2026-06-29

> This is the **constitution** of the CSSI overhaul. It turns the lessons register
> (L1–L8, N1–N13) into one enforceable standard that every later spec must obey.
> *(L7 added 2026-06-27 during the S2 interview — see Appendix A · SI-6; L8 added
> 2026-06-29 during the S4 interview — see Appendix A · SI-7; SR-5 added 2026-06-29
> during the S5 interview — see Appendix A · SI-8.)* S1
> **designs** the standard; the standard document itself (`docs/STANDARDS.md`) is
> **authored during execution**, not now. Nothing here edits content pages.

---

## 1. Objective

Define a single governing standard — `docs/STANDARDS.md` — that (a) restates every scar
and mechanism lesson as a numbered, **testable** rule with an explicit trigger and check;
(b) fixes the mandatory authority-weight vocabulary; (c) extends the existing D1–D12
reviewer dimensions to absorb the new rules; (d) codifies the research discipline and the
find→adjudicate→fix verification machine; and (e) sets the enforcement model (automated
where cheap + reviewer checklist). `docs/STANDARDS.md` supersedes and absorbs
`docs/FINAL-QA-SPEC.md` and is the top authority for all of S2–S9 and the EXECUTE run.

## 2. Scope

**In:**
- The full rules catalog: L1–L8, N1–N13, plus the new S1-introduced rules SR-1…SR-5.
- The 6-tier authority-weight lexicon as mandatory site-wide vocabulary.
- The check-dimension framework extended: D1–D12 carried (some extended) + new D13, D14, and a rule→dimension mapping.
- The progressive research discipline (N12) with a recursion bound + stop conditions.
- The standing find→adjudicate→fix verification machine (L5/L4).
- The enforcement model: the automated lint roster + the reviewer checklist, and which rule each enforces.
- The canonical template **tables of contents**: the brief-first doctrine page (N8) and a reference to the officer-IRAC case-page skeleton (owned by S4).
- Supremacy + naming of `docs/STANDARDS.md`; the disposition of `FINAL-QA-SPEC.md`.

**Out (owned elsewhere):**
- Authoring `docs/STANDARDS.md` prose, the lint scripts, and the reviewer-checklist form — these are **execution** deliverables built from this spec, not written now.
- The category taxonomy, MOC, and the **project-scope** decision (S2).
- The case data model + per-case page skeleton in detail (S4 — referenced here only).
- Per-page content, ingest, reformatting, term-linking, research pages, and the exhaustive verification *run* itself (S5–S9). S1 sets the rules they must satisfy.

---

## 3. Requirements (the numbered rules catalog)

Every rule below is stated **testable**, with a **Trigger** (when it applies) and a
**Check** (how a reviewer or script verifies it). Enforcement is tagged
`AUTO:<lint>` (deterministic script), `CHECKLIST:<Dn>` (reviewer judgment), or
`PROCESS` (orchestration discipline). `docs/STANDARDS.md` reproduces this catalog.

### 3.A Scar-rules (already paid for — carried from the lessons register)

- **L1 — Two-key rule / paraphrase drift.** Every holding, rule statement, and quotation
  on any page or card traces to the primary opinion via the two-key rule: **(key-1)**
  existence + proposition + verbatim pinpoint where quoted; **(key-2)** good-law status.
  **Decks derive FROM verified pages, never the reverse.**
  *Trigger:* any asserted holding/rule/quote/case anywhere.
  *Check:* the assertion appears in the assertion inventory with a CL-cited verdict;
  quotes are verbatim with a confirmed pinpoint; no card asserts a fact absent from its
  source page. *Enforcement:* AUTO:LINT-2 (quote/pinpoint presence) + AUTO:deck↔page id
  check + CHECKLIST:D1.

- **L2 — Web is discovery-only.** Nothing enters a page until confirmed against the
  primary opinion on CourtListener. **Discovery ≠ assertion.**
  *Trigger:* any content sourced from web/secondary material.
  *Check:* every web-surfaced case/holding/quote has a corresponding CL confirmation in the
  manifest before it appears; unconfirmed items are flagged, never asserted.
  *Enforcement:* PROCESS (§3.F) + CHECKLIST:D1/D3.

- **L3 — cluster-id ≠ opinion-id.** Every CL URL must resolve (HTTP 200) **AND** display
  the **named** case (identity, not just status). Resolve cluster → lead opinion id for
  post-~2015 cases; confirm the case name in returned text before trusting any quote.
  *Trigger:* any CL URL on a page, or any quote read from CL.
  *Check:* link-checker confirms the URL resolves and the returned text contains the case
  name; quote-reads are logged against the confirmed opinion id.
  *Enforcement:* AUTO:LINT-1 (CL-URL identity) + CHECKLIST:D7.

- **L4 — One serial CL lane.** ALL CourtListener calls go through a single serial lane
  (concurrency-1), **always** — writing, review, adjudication, and research alike.
  *Trigger:* any CL call anywhere in execution.
  *Check:* `cl-calls.log` shows a single serial lane with no concurrent timestamps; the
  tier probe was run; STOP-on-old-5/min-tier was honored. *Enforcement:* PROCESS +
  CHECKLIST (audit `cl-calls.log`).

- **L5 — find → adjudicate → fix (no reviewer edits).** Hard separation of the three
  roles. A reviewer never edits; a **legal** assertion never changes without CL evidence
  at adjudication. *Trigger:* any review finding that would change a page.
  *Check:* every change traces to an adjudicated verdict (UPHELD/MODIFIED) with evidence;
  reviewers produced findings only; DISMISSED findings are logged with a reason.
  *Enforcement:* PROCESS (§3.G) + CHECKLIST (audit the findings→adjudications→fixes trail).

- **L6 — "Not found" ≠ "doesn't exist."** Before declaring a case fake/unverifiable,
  run the misspelling-tolerant escalation ladder (reporter cite → name/phonetic variants →
  proposition full-text → web → re-locate in CL). Only then mark `UNVERIFIABLE`, flagged,
  never asserted. *Trigger:* any CL lookup miss on a captured/cited case.
  *Check:* an `UNVERIFIABLE` verdict shows the full ladder was run (logged); no case marked
  fake from a single miss. *Enforcement:* PROCESS (§3.F) + CHECKLIST:D1.

- **L7 — Scope-boundary claims are assertions (no narrow-scope synthesis).** A statement that
  **bounds a doctrine's reach — especially a *negative* bound** ("does not reach X", "only Y",
  "vehicles, not persons") — is an **assertion, not discovery** (L2), and carries the
  **two-key burden**. It must rest on **frontier-level** progressive research (N12 Hop-2:
  circuit/state treatment, splits, first-impression) confirmed against **primary** authority —
  never on secondary-source synthesis alone. Until that research is run, the scope is recorded
  as **"unresolved — research,"** never as the narrow reading. *(Scar: during the S2 interview,
  community caretaking was first framed "vehicles, not persons outside the home" from secondary
  synthesis; the mandated frontier pass then surfaced the controlling person-caretaking line —*
  United States v. Garner *(10th Cir.) 3-part caretaking-detention test;* United States v.
  Rideau *(5th Cir.) impaired-person-in-roadway;* Graham v. Barnette *(8th Cir.) PC-of-
  dangerousness for emergency mental-health seizures — reversing the boundary.)*
  *Trigger:* any who/what/where scope statement; any "only / never / does-not-reach" language.
  *Check:* every scope boundary cites primary authority at the frontier; negative bounds show
  the Hop-2 frontier pass was run (logged); no scope claim rests on secondary synthesis alone.
  *Enforcement:* PROCESS (§3.F — frontier hop mandatory for scope claims) + CHECKLIST:D2/D4.
  Strengthens **N10** (state scope) and **N12** (progressive research); sibling of **L2**.

- **L8 — Restatement, not editorialization (explanatory prose may not move the holding).** Any
  explanatory, practical, "what-this-means," or teaching-*takeaway* paraphrase of a holding or rule —
  especially the **un-anchored blocks that do not quote the opinion** — must **restate** it faithfully and
  may **not add, drop, narrow, or broaden** a condition of the rule it conveys. A takeaway that moves the
  holding is **paraphrase drift (L1)** and, where it bounds reach, a **negative-scope assertion (L7)** —
  carrying the **two-key burden**, not a free-writing license. Operating principle: **case pages *restate*;
  doctrine pages *teach*** — generalized field framing (N9) lives on doctrine pages under the **SR-2**
  instructor gate and is never injected into the canonical case record. *(Scar: during the S4 interview a
  draft "Field-IRAC" takeaway rewrote* Brigham City v. Stuart*'s "objectively reasonable basis to **believe**
  an occupant is injured" into "**see** it," narrowing a source-agnostic standard into a visual-observation
  rule the Court never imposed.)*
  *Trigger:* any practical/takeaway/explanatory paraphrase of a holding or rule (a case-page Application or
  takeaway; a doctrine-brief "what this means"; any "you may / must / need only…" operational line).
  *Check:* the prose adds or drops no element of the pinpointed holding; case pages carry no generalized
  field-advice beyond a faithful restatement; field framing appears on doctrine pages with instructor
  sign-off; spot-check the paraphrase against the opinion. *Enforcement:* CHECKLIST:D2/D4/D9 + PROCESS
  (instructor review of doctrine-page field framing). Strengthens **L1**, **L7**, and **N1**; sibling of **L1**.

### 3.B Mechanism-rules (from the instructor's page-by-page notes)

- **N1 — Placement by holding, not keyword.** A case's home page and key/related status
  is set by the legal proposition it stands for, not surface-keyword overlap.
  *Trigger:* assigning a case to a page or to key/related. *Check:* each placement is
  justified by the case's holding (the proposition supports THIS page's doctrine); e.g.
  *Matlock* = consent/common-authority, not abandonment. *Enforcement:* CHECKLIST:D2/D5.

- **N2 — Authority-weight lexicon.** Use the fixed 6-tier lexicon (§3.D) everywhere;
  **never** "persuasive, not binding"; circuit cases name the circuit; splits flagged.
  *Trigger:* any authority/weight label on any case. *Check:* every weight label is one of
  the 6 tiers; circuit cases carry the circuit; no banned phrasing.
  *Enforcement:* AUTO:LINT-4 (lexicon vocabulary) + CHECKLIST:D6.

- **N3 — Tests stated up front.** Any named test / prongs / elements appear explicitly in
  the Rule/brief at the top — never left for the reader to reconstruct (e.g. the *Dunn*
  4 factors). *Trigger:* a doctrine governed by a named multi-factor/element test.
  *Check:* the test and all its prongs appear in the top brief; reviewer confirms
  completeness. *Enforcement:* CHECKLIST:D14/D4.

- **N4 — Subsequent treatment inline.** Where a case is materially narrowed/limited/
  abrogated, tag **"limited by [linked case]"** at the point of assertion; add a 1–2
  sentence *why* **only when it changes field application** *(user-confirmed threshold).*
  *Trigger:* asserting a case with material negative subsequent treatment.
  *Check:* the inline tag is present wherever the case is asserted; the explanation is
  present iff field application changes; the treatment is stated consistently across every
  page the case appears on. *Enforcement:* CHECKLIST:D3/D5.

- **N5 — Recent-developments is role-based, not recency-based.** That section is for
  circuit/state cases that expand/narrow/split/first-impression vs SCOTUS. **Any SCOTUS
  holding belongs in Key cases regardless of date** (e.g. re-home *Case v. Montana*).
  *Trigger:* placing a case in Recent-developments. *Check:* no SCOTUS case appears there;
  every entry has an expand/narrow/split/first-impression role labeled.
  *Enforcement:* AUTO:LINT-3 (no-SCOTUS-in-recent-developments) + CHECKLIST:D10.

- **N6 — Key-status is non-exclusive.** A case is Key on a page if central to THAT
  doctrine, independent of being key elsewhere; multi-homing is expected and framing is
  page-specific (promote *Herring* on Collective Knowledge; move *Riley* to Related on
  Common Law). *Trigger:* assigning key/related to a multi-homed case. *Check:* key/related
  is decided per-page by centrality to that doctrine; framing differs appropriately across
  homes. *Enforcement:* CHECKLIST:D2/D5.

- **N7 — Link every named case.** Every case named anywhere links to its own case page;
  passage-specific discussion → deep-link to the pinpoint/highlighted span; whole-case
  reference → link the case page. *Trigger:* any case name in prose/tables.
  *Check:* no bare unlinked case name; passage discussions deep-link; link targets resolve.
  *Enforcement:* AUTO:LINT-5 (link-every-named-case) + CHECKLIST:D13.

- **N8 — Brief-first.** The full teaching brief (rule + limits + nuance + pitfalls,
  integrated) reads top-to-bottom first; tables + recent developments follow as supporting
  apparatus. *Trigger:* any doctrine page. *Check:* the brief is the first substantive
  content and is self-contained; apparatus follows it.
  *Enforcement:* CHECKLIST:D14/D10.

- **N9 — Frame around the officer's field-decisive question.** Frame each doctrine around
  the operational question an officer must answer, not "what is the exception." For
  misunderstood topics (e.g. knock-and-talk) be exhaustive on line-drawing.
  *Trigger:* authoring/reformatting any doctrine brief. *Check:* the brief leads with the
  field-decisive question and draws the lines; reviewer (instructor lens) confirms.
  *Enforcement:* CHECKLIST:D9/D14.

- **N10 — State scope explicitly.** State what/who/where a doctrine covers; split bundled
  doctrines; research, never assume (e.g. community caretaking: persons vs vehicles —
  resolved in S2). *Trigger:* a doctrine with ambiguous or bundled scope.
  *Check:* scope is stated explicitly; bundled doctrines split or boundary-noted; scope
  claims are authority-backed. *Enforcement:* CHECKLIST:D4/D2.

- **N11 — Wire the glossary.** Non-vernacular terms link to the glossary (hover-preview +
  click-through); the glossary is audited continuously from live page text.
  *Trigger:* any non-vernacular legal term in prose. *Check:* terms link to the glossary;
  the glossary covers all terms used; no orphan terms.
  *Enforcement:* AUTO:LINT-7 (glossary wiring, best-effort) + CHECKLIST:D13/D11.

- **N12 — Progressive research.** narrow issue → doctrine/keyword → expand → learn →
  expand, **bounded**. Assume nothing; web discovers, CL confirms (protocol + bound in
  §3.F). *Trigger:* rounding out any page beyond captured seed cases.
  *Check:* research followed the bounded protocol; a stop condition was met; all additions
  are CL-verified. *Enforcement:* PROCESS (§3.F) + CHECKLIST:D4.

- **N13 — No blank treatment status.** Every case carries an explicit, verified good-law
  treatment status; "good as of <date>" only after a check.
  *Trigger:* any case asserted on any page or in the Case Index. *Check:* every case row/
  assertion carries a non-blank treatment status with a check date; no "good" without a
  logged check. *Enforcement:* AUTO:LINT-6 (treatment-status presence) + CHECKLIST:D3.

### 3.C New standard rules introduced by S1 (the five user-owned decisions; SR-5 added later — Appendix A · SI-8)

- **SR-1 — Exhaustive live re-verification (USER DECISION).** Every asserted case is
  re-verified **live against the primary opinion** through the serial CL lane — **including
  manifest-grade cases** — for proposition, every verbatim quote + pinpoint, and good-law
  currency. No case is exempt by prior verification grade; prior manifests are a starting
  reference, not a substitute for the live re-check.
  *Trigger:* the S9 exhaustive pass; any page authored/reformatted in S5/S6.
  *Check:* the assertion inventory shows a fresh live-CL verdict for **every** case;
  `cl-calls.log` evidences the re-check; zero cases pass on manifest alone.
  *Enforcement:* PROCESS (S9, serial lane, RUNBOOK §3) + CHECKLIST:D1 + audit (inventory
  completeness). *Note:* this is the heaviest CL load in the project; it runs patiently in
  the single serial lane, checkpointed; if the CL tier regresses to 5/min, RUNBOOK §3
  STOP-and-notify governs.

- **SR-2 — Instructor-grade framing gate (USER DECISION; blocking).** Citation accuracy is
  necessary but **not sufficient**. Every doctrine page must also pass an instructor-grade
  gate: the rule/test is stated correctly and up front (N3); the doctrine is **complete**
  (black-letter rule · elements/prongs · burden + who bears it · standard of review ·
  remedy · controlling authority + progeny by role · limits · nuances · pitfalls · the
  operational "apply it" angle — the D4 checklist); and it **actually teaches** (D9). A page
  with perfect cites but a muddled or incomplete brief **FAILS** and is escalated, not
  shipped. *Trigger:* every doctrine page at review/sign-off.
  *Check:* the page passes the composite gate **D2 ∧ D4 ∧ D9 ∧ D14**; the completeness
  checklist has no unlogged gap; a reviewer signs off teachability.
  *Enforcement:* CHECKLIST (composite, blocking).

- **SR-3 — STANDARDS.md supremacy (USER DECISION).** `docs/STANDARDS.md` is the single
  top-authority contract. It **absorbs** `FINAL-QA-SPEC.md`'s §0 self-critique and the
  D1–D12 dimensions (now extended). On any conflict, STANDARDS.md governs;
  `FINAL-QA-SPEC.md` is retained as historical reference with a pointer header. Every later
  spec (S2–S9) and the EXECUTE run obey it. *Trigger:* any cross-doc conflict or later-spec
  authoring. *Check:* STANDARDS.md exists and is cited as governing in S2–S9;
  `FINAL-QA-SPEC.md` carries the pointer header; no later spec contradicts STANDARDS.md.
  *Enforcement:* PROCESS + CHECKLIST.

- **SR-4 — Enforcement model (USER DECISION).** Enforce **automated where cheap + reviewer
  checklist** for judgment. The automated lint roster (§3.H, LINT-1…8) runs at pre-publish
  (`redeploy.sh` validation gate) / CI; the reviewer checklist (the D-dimensions) covers
  framing, completeness, pedagogy, placement, and Mermaid doctrinal accuracy. A page ships
  only when **both** pass (or escalations are logged in `_review-needed/`).
  *Trigger:* pre-publish and per-page review. *Check:* the lint roster is green; the
  reviewer checklist is signed; escalations are logged.
  *Enforcement:* AUTO (roster) + CHECKLIST.

- **SR-5 — Independent-replication concordance (build-time cross-verification) [Added
  2026-06-29 during the S5 interview — Appendix A · SI-8].** Where conclusions already produced and
  verified by a **prior thread** (a prior research manifest, a prior build, an independent reviewer) are
  re-derived by a **new pass**, the new pass runs **conclusion-blind** to the prior result — forming and
  **recording its own conclusions first** — and is then **reconciled** against the prior thread.
  **Concordance** (same case set · holding/ratio · home-by-holding (N1) · role · treatment/good-law · split
  call) raises the assertion to **double-verified** (a stronger grade than a single pass). **Fundamental
  discordance** — any of those axes differ; cosmetic wording/ordering does **not** count — **escalates** to
  the find→adjudicate→fix machine (§3.G), is **adjudicated against primary authority** (serial CL, L4), and
  the verdict must state **what diverged** (prior wrong / new wrong / scope-or-framing shift) and **which
  conclusion stands**. Independence is **conclusion-blind** (both threads may use the same primary sources;
  the new thread must **not** be seeded with the prior thread's conclusions) and is **enforced by
  orchestration** (freeze prior → run new with prior withheld → reconcile). **No prior verified conclusion may
  be silently absent** from the reconciliation. Strengthens **SR-1** (adds a cross-source *agreement* axis to
  live re-verification) and feeds **L5** (discordances are findings).
  *Trigger:* any pass that re-derives conclusions a prior verified thread already produced (S5 ingest vs. the
  prior manifests; the S9 final verification vs. the build).
  *Check:* the prior conclusion set was **frozen before** the new pass began; the new pass **recorded its
  conclusions before** reconciliation; every item carries a concordant/discordant disposition; fundamental
  discordances were adjudicated with primary-authority evidence + a logged verdict; no prior verified
  conclusion is silently dropped.
  *Enforcement:* PROCESS (orchestration: blind-then-reconcile) + CHECKLIST:D1/D5 + AUTO (concordance diff
  where the conclusion sets are structured).

### 3.D The authority-weight lexicon (mandatory vocabulary)

These six tiers are the **only** permitted authority labels site-wide. The blunt phrase
"persuasive, not binding" is **banned**.

1. **Binding — SCOTUS** (nationwide).
2. **Binding in-circuit** (a circuit holding, within its own circuit, on a case heard there).
3. **Persuasive (outside circuit)** — replaces "persuasive, not binding".
4. **Persuasive — state, illustrative** (paired with the federal rule).
5. **Persuasive only — non-precedential** (unpublished; the only "not binding even at home" tier).
6. **Historical** (English/colonial origins; or overruled cases shown as history).

**Separate, orthogonal metadata:** every case **also** carries a good-law **treatment
status** — `good | criticized | limited | abrogated | overruled` — with a check date
(N13). Authority-weight (the six tiers) describes the case's *precedential weight*;
treatment status describes its *current validity*. An overruled US case is shown under
tier 6 (Historical) **and** carries `overruled` treatment everywhere it appears (D5).

### 3.E The check dimensions, extended

The existing D1–D12 reviewer framework is **carried**, three dimensions are **extended**,
and two new dimensions are **added**. Each dimension maps to the rules it enforces; every
rule maps to ≥1 dimension (the no-orphan invariant, verified in §8).

| Dim | Name | Status | Rules it enforces |
|---|---|---|---|
| D1 | Accuracy / two-key (exhaustive) | **extended → exhaustive-live (SR-1)** | L1, L2, L6, SR-1, SR-5 |
| D2 | Framing | carried | N1, N6, N10, L7, L8 |
| D3 | Shepardize + new frontier | **extended (N4, N13)** | N4, N13, L2 |
| D4 | Completeness | carried | N3, N9, N10, N12, SR-2, L7, L8 |
| D5 | Internal consistency & cross-page coherence | carried | N1, N4, N6, SR-5 |
| D6 | Guardrails | **extended (N2 lexicon)** | N2 + fed/state, apocryphal trio, mnemonics, no inline flashcards |
| D7 | Citation hygiene | carried | L3 |
| D8 | Visual accuracy (Mermaid) | carried | (render + doctrinal faithfulness) |
| D9 | Pedagogy / teachability | carried | N9, SR-2, L8 |
| D10 | Structure / spec compliance | carried | N5, N8 |
| D11 | Practical/reference/history pages | carried | N11 (glossary accuracy) + guardrails |
| D12 | Deck ↔ page ↔ index integrity | carried | L1 (decks derive from pages) |
| **D13** | **Linking & glossary wiring** | **NEW** | **N7, N11** |
| **D14** | **Brief-first architecture & teachability-up-front** | **NEW** | **N3, N8, N9** |

- **D13 — Linking & glossary wiring (NEW).** Every named case links to its case page;
  passage discussions deep-link to the pinpoint span; non-vernacular terms link to the
  glossary; all link targets resolve. *Acceptance:* no bare case name; no orphan glossary
  term; deep-links point to the correct span; zero broken wikilinks.
- **D14 — Brief-first architecture & teachability-up-front (NEW).** The integrated teaching
  brief reads top-to-bottom and self-contained as the first content; named tests/prongs
  appear up front; the page is framed around the field-decisive question; tables and
  recent-developments follow as apparatus. *Acceptance:* brief-first order holds on every
  doctrine page; tests are stated, not reconstructed.

### 3.F The research discipline (N12 — progressive, bounded)

For each page, seed = the captured cases **plus** the controlling foundational SCOTUS
authority the doctrine rests on, added even if uncaptured (*Chimel* for SITA, *Schneckloth*
for consent). Then expand progressively:

- **Hop 0 (seed):** the proposition the capture/page states.
- **Hop 1 (doctrine/keyword):** the named test, its elements, the controlling authority +
  significant progeny by role.
- **Hop 2 (frontier):** circuit splits, recent developments, weak-but-overused field cases
  officers rely on, issues of first impression.

**Recursion bound:** at most **2 expansion hops beyond the seed** per page.
**Division of labor:** web search (free, parallel) **discovers** candidates; the **single
serial CL lane** (L4) **confirms** existence + proposition + verbatim quote before anything
is asserted (L2). **Stop conditions (any one):** (a) the D4 completeness checklist for the
doctrine is fully covered; (b) a full hop surfaces no new load-bearing authority; (c) the
page would exceed the ½–1 page digestible budget — then cut to load-bearing authority only.
**Case identification:** misspelling-tolerant (L6 / RUNBOOK §3a) — never declare a case fake
from one miss; run the escalation ladder. **cluster-id ≠ opinion-id (L3)** guard on every
read. **Scope claims (L7):** any boundary on a doctrine's reach — and especially a *negative*
one ("only X" / "does not reach Y") — is treated as an assertion: the **Hop-2 frontier pass is
mandatory** (circuit/state treatment, splits, first-impression) **plus** primary confirmation
before the boundary may appear; until then the page records the scope as *unresolved —
research*, never the narrow reading.

### 3.G The find → adjudicate → fix machine (L5/L4 — adopted)

The standing verification machine is **adopted from `FINAL-QA-SPEC.md` §2 unchanged**, now
governed by STANDARDS.md. Three separated roles; a legal assertion never changes on a
reviewer's opinion alone.

1. **REVIEW** (parallel, free, **NO CL**). Per page, dimensional reviewers emit structured
   findings: `{id, page, dimension(D1–D14), locator(section + verbatim text), problem,
   severity, proposed_fix, needs_cl, confidence}`. Reviewers **may not edit pages.**
2. **ADJUDICATE.** Every finding → a verdict in the set
   **{UPHELD, MODIFIED, DISMISSED, ESCALATE}** with `adjudicated_fix` + `evidence`.
   - `needs_cl=true` findings (good-law, proposition, quote/pinpoint, case existence,
     CL-URL, new-frontier) → adjudicated by the **single serial CL lane**; the verdict
     **must cite CL evidence**. No CL evidence → cannot UPHOLD a change to a legal
     assertion (→ DISMISS or ESCALATE).
   - Non-legal findings (formatting, structure, missing cross-link, internal contradiction,
     pedagogy, corpus-supported completeness gap) → a free editor-adjudicator.
   - **DISMISSED findings are logged with the reason** (a dismissed false-positive is a
     successful outcome — guards against over-correction).
3. **FIX** (parallel, free). Per page, a fixer applies **only** UPHELD/MODIFIED adjudicated
   fixes, verbatim; ESCALATE → `_review-needed/`. The fixer introduces no new content.

**Loop cap 3**, then escalate to `_review-needed/<slug>.md`. Checkpoint the ledger after
every sub-phase (resumable). Surface consequential calls in the final report.

### 3.H Enforcement model (SR-4 — automated where cheap + checklist)

**Automated lint roster** (deterministic; runs at pre-publish via `redeploy.sh` validation
and/or CI; the CL-touching lint reuses the serial lane):

| Lint | What it checks | Enforces |
|---|---|---|
| LINT-1 | Every CL URL resolves (200) **and** returned text contains the named case | L3, D7 |
| LINT-2 | Every block/inline quote has an accompanying pinpoint cite (else de-quote/pin) | L1, D7 |
| LINT-3 | Doctrine-page section order present; **no SCOTUS case in Recent-developments**; single controlling amendment in frontmatter | N5, N8, D10 |
| LINT-4 | Every authority label is one of the 6 tiers; banned "persuasive, not binding"; circuit cases name the circuit | N2, D6 |
| LINT-5 | Every named case resolves to a case-page wikilink (no bare case names) | N7, D13 |
| LINT-6 | Every asserted case carries a non-blank treatment status with a check date | N13, D3 |
| LINT-7 | Non-vernacular terms link to the glossary (best-effort; checklist-primary — see §9) | N11, D13 |
| LINT-8 | Guardrails: no apocryphal Holiday/McCall/Smith trio; mnemonics uncited; no inline `## Flashcards` | D6 |

**Reviewer checklist (judgment — the D-dimensions):** framing correctness (D2), placement-
by-holding (N1/D2), completeness vs the D4 checklist (D4), cross-page coherence (D5),
Mermaid doctrinal accuracy (D8), pedagogy/teachability (D9), brief-first architecture (D14),
and the **SR-2 instructor-grade composite gate**. A page ships only when the roster is green
**and** the checklist is signed (or escalations are logged).

### 3.I Canonical template tables of contents

**Brief-first doctrine page (N8) — section order:**
1. **Frontmatter** — single controlling amendment; aliases (renamed pages); `related:`.
2. **The Brief** (top, integrated, self-contained, reads top-to-bottom): field-decisive
   question (N9) → black-letter rule + named test/prongs stated up front (N3) →
   elements / burden + who bears it / standard of review / remedy → limits & nuances →
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

**Officer-IRAC case page (N7 home target) — skeleton owned by S4; referenced here.**
Reference order: Facts → Issue → Held → Discussion/Reasoning → Rule/Holding (with pinpoint)
→ authority weight (6-tier) + treatment status → Citation (topic) → backlinks to doctrine
pages. The **detailed** skeleton (anchors for deep-linking per N7, frontmatter, aliases) is
defined in **S4**; S1 states only the cross-cutting rules it must honor: tests-up-front
(N3), link-every-case (N7), two-key (L1), lexicon (N2), treatment-status (N13).

---

## 4. Lessons enforced

S1 **is** the lessons register turned into an enforceable contract. It restates L1–L8 and
N1–N13 as testable rules (§3.A/3.B), each with a trigger, a check, and an enforcement tag;
adds the mandatory lexicon (§3.D, enforcing N2); extends the reviewer dimensions to D1–D14
(§3.E); codifies the research discipline (§3.F = N12 + L2/L4/L6) and the find→adjudicate→fix
machine (§3.G = L5/L4); and sets the enforcement model (§3.H). The five user decisions
become SR-1…SR-4 + §3.D. No prior lesson is dropped or weakened; SR-1 and SR-2 **strengthen**
D1 (exhaustive live re-verify) and the framing gate (instructor-grade, blocking). **L7** (a
scar discovered during the S2 interview) strengthens N10/N12 by making narrow/negative scope
boundaries two-key assertions, not free synthesis. **L8** (a scar discovered during the S4
interview) strengthens L1/L7/N1 by making any explanatory or practical *takeaway* that narrows or
broadens a holding a two-key assertion — **case pages restate, doctrine pages teach.** **SR-5** (added during
the S5 interview) adds an *independent-replication* axis to verification: a new pass runs conclusion-blind and
reconciles against the prior thread, so **agreement double-verifies and fundamental disagreement escalates** —
strengthening SR-1 with a cross-source agreement signal.

## 5. Method (how execution authors the standard from this spec)

1. **Author `docs/STANDARDS.md`** from §3: the full rules catalog (L/N/SR with
   trigger·check·enforcement), the §3.D lexicon, the §3.E dimensions + mapping table, the
   §3.F research discipline, the §3.G machine, the §3.H enforcement roster, and the §3.I
   template TOCs. STANDARDS.md opens with a supremacy clause (SR-3).
2. **Stub `docs/FINAL-QA-SPEC.md`** with a pointer header ("Superseded by `docs/STANDARDS.md`;
   retained for history") — content retained, authority transferred.
3. **Build the automated lint roster** (LINT-1…8) as scripts where cheap, wired into
   `redeploy.sh`'s validation gate and/or CI; LINT-1 reuses the serial CL lane for identity.
4. **Produce the reviewer checklist** (the D1–D14 dimensions + the SR-2 composite gate) as a
   per-page sign-off form (a section of STANDARDS.md or `docs/REVIEWER-CHECKLIST.md`).
5. **Self-consistency pass** (§8): no rule contradicts `DECISIONS.md` D-0…D-8; every rule has
   a check; every dimension maps to ≥1 rule and vice-versa.
6. All later specs (S2–S9) **cite STANDARDS.md as governing**.

## 6. Deliverables

- `docs/STANDARDS.md` — **NEW**, the governing contract (the §3 catalog authored as prose).
- `docs/FINAL-QA-SPEC.md` — **EDIT**, pointer/supremacy header; content retained as history.
- The automated lint roster scripts (LINT-1…8), wired to `redeploy.sh` validation / CI —
  exact filenames chosen at execution (e.g. `scripts/lint/*`).
- The reviewer checklist (the D1–D14 + SR-2 sign-off form) — standalone or a STANDARDS.md
  section.
- `_overhaul/specs/S1-standards.spec.md` — **this spec** (the design of the above).

## 7. Acceptance criteria (definition of done)

- [ ] `docs/STANDARDS.md` exists and contains the full **L1–L8, N1–N13, SR-1…SR-5** catalog,
      each rule carrying a non-empty **Trigger + Check + Enforcement** tag.
- [ ] The **6-tier lexicon** is present, declared mandatory, and lists "persuasive, not
      binding" as banned; the orthogonal treatment-status metadata is defined.
- [ ] The dimensions **D1–D14** are present with the rule→dimension mapping table; D1 is
      extended to exhaustive-live (SR-1), D3 extended (N4/N13), D6 extended (N2 lexicon);
      **D13** and **D14** are defined with acceptance lines.
- [ ] The **research discipline** states an explicit recursion bound (≤2 hops), ≥1 stop
      condition, the web-discovers/CL-confirms split, the one-serial-lane rule, and the
      L6/§3a escalation ladder.
- [ ] The **find→adjudicate→fix machine** states the three roles, the no-reviewer-edit rule,
      the 4-verdict set, serial-CL-for-`needs_cl`, DISMISSED-logged-with-reason, the
      escalation path, and the loop cap 3.
- [ ] The **enforcement model** lists the automated lint roster (each lint → the rule it
      enforces) **and** the reviewer checklist; both are required pre-ship.
- [ ] The **two template TOCs** (brief-first doctrine; officer-IRAC case → S4) are present
      with their cross-cutting rules.
- [ ] **SR-3 supremacy** is declared in STANDARDS.md; `FINAL-QA-SPEC.md` carries the pointer
      header.
- [ ] **No rule contradicts** `DECISIONS.md` D-0…D-8 (verified in §8).
- [ ] **All 5 user-owned decisions** are reflected (SR-1 full live re-verify; SR-2 framing
      gate; SR-3 supremacy; SR-4 enforcement; §3.D lexicon-as-written) and **all 21 lessons**
      (L1–L8, N1–N13) appear in the catalog; **SR-5** (independent-replication concordance) is
      present as an additive amendment from the S5 interview (Appendix A · SI-8).

## 8. Verification plan (how S1 itself is checked)

S1 is verified by a **free (no-CL) internal review** at the end of execution Stage 5;
failures escalate to `_review-needed/S1-*`.

1. **Completeness:** all 21 lessons (L1–L8, N1–N13) + SR-1…SR-5 appear in the catalog; all
   5 user-owned decisions are represented; SR-5 is present as the S5-interview amendment; no
   lesson silently dropped.
2. **Well-formedness:** every rule has a non-empty Trigger + Check + Enforcement; every
   AUTO-tagged rule's Check is implementable by a deterministic script (spot-check LINT-1
   identity, LINT-5 link-every-case, LINT-6 treatment-status — if a Check is not
   deterministic, demote it to CHECKLIST).
3. **No-orphan invariant:** every dimension D1–D14 maps to ≥1 rule, and every rule maps to
   ≥1 dimension or PROCESS lane (the §3.E table is the proof).
4. **Internal non-contradiction:** no two rules conflict (e.g. SR-1 exhaustive-live does not
   contradict L4 one-lane — it *runs through* it; N4 inline-tag does not contradict N8
   brief-first — the tag lives in the brief).
5. **Non-regression vs `DECISIONS.md`:** cross-check each S1 rule against D-0…D-8; confirm
   D-3 (slug stability / naming), D-5 (two-key + circuit-split policy), and D-6 (lossless
   deck) remain satisfied; flag any contradiction (expected: none — S1 extends, never
   reverses, prior rulings).
6. **Consistency with carried docs:** the §3.G machine matches `FINAL-QA-SPEC.md` §2; the
   §3.F protocol matches RUNBOOK §3/§3a; the lexicon matches context-pack §4.

## 9. Open items / escalations

- **LINT-7 (glossary wiring, N11)** is only *best-effort* automatable — term detection is
  fuzzy. Flagged checklist-primary; final automatability is decided in **S7** (Legal-Term
  Linking).
- **Deep-link-to-pinpoint-span (N7)** depends on the case-page anchor scheme, which **S4**
  defines. S1 states the requirement; S4 supplies the mechanism; LINT-5's deep-link check is
  finalized once S4 lands.
- **SR-1 CL budget** is large (the heaviest pass). **S9** owns pacing/checkpointing; if the
  CL tier regresses to 5/min, RUNBOOK §3 STOP-and-notify governs. S1 sets only the policy.
- **`FINAL-QA-SPEC.md` retention form** — recommend full-retain-with-pointer-header;
  execution may stub to a one-line pointer if preferred. Non-blocking.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. User-owned decisions are
marked **[USER]** and record the user's actual choice; the rest are self-interviewed.*

### [USER] U-1 — "100%-verified" gate strictness → **Full live re-verify of every case (no tiering) + a blocking instructor-grade framing gate.**
- *Options:* (a) trust the two-key'd catalog, re-verify only deltas + all quotes/pinpoints;
  (b) full live re-verify of every assertion, no tiering.
- *Discussion:* The user leaned to full rigor and, on follow-up, **rejected tiering by
  evidence grade** — every case (including the ~99 manifest-grade) is re-read live against
  the opinion — and added that "verified" must include the holding/rule being **correctly
  framed and teachably explained (instructor-grade)**, not merely citation-accurate.
- *Adjudication:* **SR-1** (exhaustive live re-verification, every case) **+ SR-2**
  (instructor-grade framing gate, blocking). Honors the user's "all about verification"
  stance; the heavy CL load is S9's to pace through the single serial lane (L4 + RUNBOOK §3).

### [USER] U-2 — Authority-weight lexicon → **Adopt the 6 tiers as written.**
- *Options:* (a) the 6 tiers verbatim; (b) split "Historical" into origins vs. overruled (7 tiers).
- *Red-team (6 as-is):* "Historical" bundles English/colonial origins with overruled US cases.
- *Steel-man (6 as-is):* the separate good-law **treatment status** (`overruled`/`abrogated`)
  already captures dead-law currency orthogonally, so the weight lexicon stays lean and the
  two axes don't blur. *Adjudication:* **6 tiers as written** (§3.D), with the orthogonal
  treatment-status metadata doing the overruled/abrogated work. Mandatory site-wide; banned
  phrasing: "persuasive, not binding".

### [USER] U-3 — Enforcement model → **Automated where cheap + reviewer checklist.**
- *Adjudication:* **SR-4** + the §3.H lint roster (LINT-1…8) and the D1–D14 reviewer
  checklist; both required pre-ship. (User selected the recommended option.)

### [USER] U-4 — N4 subsequent-treatment depth → **Tag everywhere; explain inline only when field application changes.**
- *Adjudication:* **N4** threshold confirmed (§3.B): inline "limited by [case]" wherever
  asserted; 1–2 sentence *why* only when it changes what an officer may do in the field.

### [USER] U-5 — Where the standard lives & supremacy → **`docs/STANDARDS.md` supersedes & absorbs `FINAL-QA-SPEC.md`.**
- *Adjudication:* **SR-3** — single top-authority contract; FINAL-QA-SPEC retained with a
  pointer header; all of S2–S9 + EXECUTE obey it.

### SI-1 — Rule-ID scheme: keep L#/N# or renumber into a unified catalog?
- *Options:* (a) keep L1–L6 + N1–N13 as canonical IDs and add SR-# for new rules; (b) renumber
  everything into a single R-# catalog.
- *Red-team (a):* three ID prefixes (L/N/SR) is slightly less uniform.
- *Steel-man (a):* L#/N# are referenced across the context pack and **all nine interview
  files**; renumbering would orphan every cross-reference and break traceability to the
  lessons register. *Adjudication:* **(a)** — keep L#/N# stable; new rules are SR-#. Traceability
  beats cosmetic uniformity.

### SI-2 — How to extend D1–D12 for the new N-rules.
- *Options:* (a) map N-rules onto existing dimensions only; (b) add new dimensions where no
  existing one fits.
- *Red-team (b):* dimension proliferation dilutes the framework.
- *Steel-man (b):* N7 (link-every-case) and N11 (glossary) have **no** home — D7 is CL-URL
  hygiene, D12 is deck/index — and brief-first (N3/N8/N9) is the overhaul's central structural
  thrust, deserving a first-class dimension. *Adjudication:* extend D1 (→exhaustive-live), D3
  (→N4/N13), D6 (→N2 lexicon); **add D13** (linking & glossary, N7/N11) and **D14** (brief-first
  & teachability-up-front, N3/N8/N9). Everything else maps onto carried dimensions (§3.E table).

### SI-3 — Research recursion bound & stop condition (N12).
- *Options:* (a) unbounded "research until satisfied"; (b) a hard hop bound + explicit stop
  conditions.
- *Red-team (a):* unbounded research blows the CL budget and balloons pages past the ½–1-page
  budget. *Steel-man (b):* a bound makes "done" testable and protects the digestibility rule.
- *Adjudication:* **(b)** — **≤2 expansion hops beyond seed**; stop on any of {D4 checklist
  covered · a full hop adds no load-bearing authority · page hits the ½–1-page budget}; web
  discovers, the one serial CL lane confirms; L6/§3a misspelling-tolerant ID throughout (§3.F).

### SI-4 — The find→adjudicate→fix machine: adopt or redesign?
- *Options:* (a) adopt `FINAL-QA-SPEC.md` §2 unchanged; (b) redesign.
- *Red-team (a):* it was authored for the QA pass specifically.
- *Steel-man (a):* it is exactly the L5/L4 discipline, already battle-tested (3,101 assertions
  / ~154 corrections), with the verdict set, the no-edit rule, serial-CL adjudication, and
  DISMISSED-logging. *Adjudication:* **(a)** — adopt §2 verbatim as the standing machine (§3.G),
  now governed by STANDARDS.md. Reuse beats reinvention.

### SI-5 — Automated vs checklist split (the SR-4 roster).
- *Options:* (a) automate everything; (b) automate only the deterministic, cheap checks and
  leave judgment to the checklist. *Red-team (a):* framing correctness, completeness, pedagogy,
  placement-by-holding, and Mermaid doctrinal accuracy are **not** mechanically decidable —
  forcing them into scripts yields false confidence. *Steel-man (b):* lint the deterministic
  guards (CL identity, quote/pinpoint presence, lexicon vocabulary, no-SCOTUS-in-recent-dev,
  link-every-case, treatment-status, guardrails) and reserve human review for judgment.
- *Adjudication:* **(b)** — the §3.H roster (LINT-1…8) for the cheap/deterministic rules; the
  D-dimension checklist for judgment; **SR-2** is the blocking composite gate. LINT-7 (glossary)
  is best-effort/checklist-primary (§9).

### SI-6 — [Added 2026-06-27 during the S2 interview] A scope-framing miss → new scar-rule **L7**.
- *Trigger:* While running S2's mandated community-caretaking research, the doctrine was first
  framed too narrowly — "caretaking reaches vehicles, not persons outside the home" — from
  **secondary-source synthesis** (*Caniglia* explainers), before the Hop-2 frontier pass was run.
- *Options:* (a) treat it as a one-off S2 correction; (b) generalize it into a standing rule in
  the lessons register.
- *Red-team (b):* the scars were "frozen" at L1–L6; adding L7 mid-kit risks register churn and a
  third ID under the L/N/SR scheme.
- *Steel-man (b):* this is a genuine, repeatable failure mode — a **negative scope claim asserted
  from discovery-grade material** — that N10 ("state scope") and L2 ("discovery ≠ assertion") each
  *imply* but neither makes explicit; the lessons register exists precisely to capture such scars.
  The frontier research (*Garner* 10th Cir.; *Rideau* 5th Cir.; *Graham v. Barnette* 8th Cir.)
  **reversed** the boundary, proving the cost is real, not hypothetical.
- *Adjudication:* **(b)** — add **L7** (§3.A, additive; L1–L6 unchanged): scope boundaries,
  especially negative ones, are two-key assertions requiring the Hop-2 frontier pass + primary
  confirmation; until then scope is recorded "unresolved — research." Mapped to D2/D4 (no-orphan
  preserved); enforcement wired into §3.F. **Routed here from the S2 interview** per the user's
  instruction to home the fix in the spec where it belongs (the standards constitution), not in
  S2. S2 records the caretaking *scope* recalibration in its own decision log and cross-references
  L7. *(S1 remains APPROVED; this is an additive amendment, lessons count 19 → 20.)*

### SI-7 — [Added 2026-06-29 during the S4 interview] R4 generalized into new scar-rule **L8**.
- *Trigger:* While drafting the S4 per-case page format, a "Field-IRAC" practical *takeaway* block rewrote
  *Brigham City v. Stuart*'s holding — "objectively reasonable **basis to believe** an occupant is injured" —
  into "**see** violence/injury," silently converting a source-agnostic standard (dispatch, 911, a witness,
  sounds all suffice) into a visual-observation requirement the Court never imposed. The user caught it and
  questioned whether agent-authored field takeaways belong on the canonical case record at all.
- *Options:* (a) treat it as a one-off S4 template constraint (R4) only; (b) generalize it into a standing
  scar-rule in the lessons register.
- *Red-team (b):* a third interview-discovered scar (after L7) risks register churn and a further ID under the
  L/N/SR scheme. *Steel-man (b):* it is a genuine, repeatable failure mode — **explanatory/practical paraphrase
  silently moving a holding** — that **L1** (paraphrase drift), **L7** (negative-scope-by-implication), and
  **N1** (framing tracks the holding) each *imply* but none states for explanatory prose; the un-anchored
  "what this means" block is precisely where the scar recurs. The fix (BIRAC: case pages **restate**; doctrine
  pages **teach** under the SR-2 instructor gate) earns a first-class rule.
- *Adjudication:* **(b)** — add **L8** (§3.A, additive; L1–L7 unchanged): any explanatory/practical/takeaway
  paraphrase must restate the holding faithfully and may not add, drop, narrow, or broaden a condition; such
  drift is a two-key assertion (L1/L7), not a writing license. Mapped to **D2/D4/D9** (no-orphan preserved);
  enforcement = CHECKLIST:D2/D4/D9 + PROCESS (instructor review for doctrine-page field framing). **Routed
  here from the S4 interview** per the user's instruction to elevate R4. S4 · R4 is the case-template
  application of L8; S4 · §9's elevation open item is thereby resolved. *(S1 remains APPROVED; additive
  amendment, lessons count 20 → 21.)*

### SI-8 — [Added 2026-06-29 during the S5 interview] Independent-replication concordance → new standard rule **SR-5**.
- *Trigger:* Designing S5 (case ingest), the user asked that the prior verified research be kept as a **separate
  thread** rather than merged in as a head start: if a fresh pass reaches the **same** conclusion that is a
  **built-in extra verifier**, and if it reaches a **fundamentally different** one, that divergence must trigger
  investigation ("we need to figure out what's going on").
- *Options:* (a) keep it an **S5-local** mechanism (dual-thread reconciliation in S5 only); (b) generalize it
  into a **standing verification rule** in the constitution so S9 (and any later independent pass) inherits it.
- *Red-team (b):* a fifth SR-rule + more S1 surface; risks over-formalizing a method. *Steel-man (b):* it is a
  **general verification primitive** — independent replication, where *agreement carries information only if the
  threads are blind to each other* — that **S9's whole mandate** (independent verification) wants by design;
  homing it in S1 (which S9 reads) guarantees inheritance, exactly as L7/L8 were routed here from later
  interviews. The first S5 draft's **seed-from-prior** approach would have **destroyed** the independence that
  gives agreement its weight; SR-5 makes the **blind-then-reconcile** discipline explicit and mandatory.
- *Adjudication:* **(b)** — add **SR-5** (§3.C): conclusion-blind re-derivation + reconciliation; concordance
  → **double-verified**; fundamental discordance (presence · holding · home-by-holding · role · treatment ·
  split; not wording/order) → **escalate** to §3.G, adjudicated against primary authority. Mapped to **D1/D5**
  (no-orphan preserved); enforcement = PROCESS (blind-then-reconcile orchestration) + CHECKLIST + AUTO.
  **Applied** in **S5 · R12** (the dual-thread ingest gate; the R6 seed walked back); **inherited** by **S9**.
  **Routed here from the S5 interview** per the user's delegation to home the fix where it belongs. *(S1 remains
  APPROVED; additive amendment; standard rules SR-1…SR-4 → SR-1…SR-5.)*
