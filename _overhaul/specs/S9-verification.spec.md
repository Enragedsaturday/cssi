# SPEC S9 — Full Independent Verification & Adjudication

status: APPROVED
depends-on: [S1, S2, S3, S4, S5, S6, S7, S8]          gates: []
last-updated: 2026-06-30

> Governed by `docs/STANDARDS.md` (S1, SR-3 supremacy). S9 **designs the final, whole-product
> verification pass** that makes the deliverable *100%-verified, complete, and correct*:
> exhaustive live re-verification (SR-1) + uniform N-of-3 dimensional review across D1–D14 +
> a **whole-corpus conclusion-blind re-derivation** reconciled against the build (SR-5) +
> adjudication (editorial lane + the single serial-CL legal lane) + fix + visual/Mermaid +
> link-identity check + glossary/tool/nav sweeps + a literal **release-gate** sign-off +
> publish/verify-live. **Flashcard decks are entirely out of scope here** — frozen/untouched
> through S1–S9; the page-derived deck rebuild is a **separate later flashcard run** after the
> overhaul + vault are finalized (USER, U5-S9), so S9 does **not** rebuild decks or gate on deck
> integrity. S9 is the **successor to
> `docs/FINAL-QA-SPEC.md`** (its P0–P5 / D1–D12 pass), extended by the S1 constitution
> (D1–D14, the 6-tier lexicon, SR-1, SR-2, SR-5) and by everything S2–S8 produce. S9
> **designs** the pass; it **runs later** under `EXECUTE.wrapper.md`, after S1–S8 content
> exists. Every CourtListener call goes through the **single serial lane (L4)**; the
> find→adjudicate→fix roles stay **hard-separated (L5)**; nothing is guessed (two-key, L1).

---

## 1. Objective

Define the exhaustive, orchestrator-led, serial-CL verification pass that takes the built CSSI
wiki to a **release-gateable** standard: every asserted case/holding/quote/pinpoint live-re-verified
against the primary opinion (SR-1); every page reviewed across **D1–D14** by **N-of-3** independent
reviewers; the build's conclusions **independently re-derived conclusion-blind and reconciled**
(SR-5, whole corpus); every finding **adjudicated** (legal findings on the single serial CL lane,
editorial findings free) and every UPHELD/MODIFIED fix applied (L5); every Mermaid visually
inspected; every wikilink + CL URL + deep-link anchor identity-checked; the glossary/term-wiring,
the legal-research tool facts, the category nav, and the Case Index swept; and the whole thing
measured against a single **definition-of-done release gate** (§7) that is the literal ship
condition — pass, or a **logged `_review-needed/` escalation**, never a silent gap. **Flashcard
decks are out of scope** — frozen through the overhaul and rebuilt from the finalized pages in a
**separate later run** (S4·R11 as amended; U5-S9), so neither the deck rebuild nor deck↔page↔index
integrity (D12) is part of S9 or its gate.

## 2. Scope

### 2.1 In scope (S9 designs)
- The **coverage universe** — every object the pass verifies, at full depth (R1).
- The **extended dimension set D1–D14** + the N/L/SR-rule→dimension map + the final per-object
  **reviewer checklist** (R2).
- The **exhaustive live re-verification (SR-1)** + the **assertion inventory** + the proactive
  serial-CL sweeps (R3).
- The **find→adjudicate→fix machine with uniform N-of-3 review** (L5), the editorial lane + the
  single serial-CL legal lane (L4), refutation semantics, loop cap 3 (R4).
- The **whole-corpus conclusion-blind re-derivation + concordance reconciliation (SR-5)** — Thread-P
  freeze, Thread-N blind, reconcile, double-verified/escalate, the no-regression floor (R5).
- The **Mermaid / visual-accuracy pass (D8)** (R6).
- The **link & identity check** (wikilinks, CL-URL identity L3, deep-link/term anchors, alias
  redirects) + the **automated lint roster LINT-1…8 / LINT-7-AUTO** as the pre-publish gate (R7).
- The **cross-page coherence audit (D5)** (R8).
- The **glossary/term-wiring re-audit (S7)** + the **legal-research tool-fact currency re-vet (S8)** (R9).
- The **Case-Index regeneration (S4·R10) + category-nav/Explorer/alias integrity (S2/S3)** (R10).
- The **decks-out-of-scope contract** — decks stay frozen through S9; the rebuild is a separate run (R11).
- The **ledger + reporting artifacts** (R12).
- The **release gate (§7) as the literal definition of done** + the escalation policy (R13).
- **Publish & verify-live** (R14).
- The **self-audit of the pass itself** — false-positive logging, adjudication sampling re-checks,
  blindness audit (§8).

### 2.2 Out of scope (owned elsewhere)
- **Authoring/standards/lexicon/the verification-machine definition** → **S1** (`docs/STANDARDS.md`);
  S9 *runs* the machine, it does not redefine it.
- **The category tree / homes / role set / scope contract** → **S2**; **platform/nav/components/
  config** → **S3**; **the case object + BIRAC template + anchors + Case-Index generator** → **S4**;
  **ingest/coverage** → **S5**; **doctrine-page reformat + field framing + the structural authoring
  (caretaking split, Garrity page)** → **S6**; **glossary wiring** → **S7**; **legal-research pages**
  → **S8**. S9 **verifies** these outputs; it does not re-design or re-author them, except to **apply
  adjudicated fixes** through the standing machine.
- **The flashcard decks** — **frozen/untouched through the entire overhaul; the page-derived deck
  rebuild + deck↔page↔index (D12) verification is a SEPARATE later flashcard run** (after the overhaul
  and the full content corpus are finalized — USER U5-S9). S9 does **not** rebuild decks, does **not**
  gate on deck integrity, and verifies only that the existing frozen deck is not *broken* by page
  moves/renames (the published `flashcards.json` still loads, via stable stems + S3 aliases).
- **Re-opening settled decisions** (the 6-tier lexicon, BIRAC, the field-relevance gate, the deck-id
  supersession). S9 enforces them; it does not relitigate them.

---

## 3. Requirements (numbered, testable)

### R1 — The coverage universe (whole corpus, full depth) **[USER U3-S9; SR-1]**
S9 verifies **every** content object the overhaul produced, at **full depth** (no sanity-only tier —
the user chose whole-corpus rigor). The universe, enumerated so the pass has an exhaustive worklist:
1. **Every case page** `content/cases/*` (the ~261 verified + every S5 ingest) — BIRAC template
   (S4·R3), frontmatter schema (S4·R2), restate-not-editorialize (S4·R4 / L8).
2. **Every doctrine page** in the S2 tree (incl. the two caretaking-split pages and the new Garrity
   page) — brief-first template (S6·R1), the SR-2 composite gate.
3. **The narrative/reference pages** S6 reformatted (`index.md` MOC, Fourth Amendment Framework /
   Analysis Checklist / Recalibration, CREW, Three Golden Rules, Instructor Development, The Federal
   Court System).
4. **The glossary** `Common Legal Terms.md` (S7) — entries, anchors, term-wiring across all pages.
5. **The three legal-research pages** (S8) — Reading & Citing Cases, Legal Research Tools, Verifying
   Good Law — incl. the ten citation-mechanics term anchors and the vetted tool facts.
6. **The Case Index** (S4·R10, generated) — regeneration fidelity + every row's links/treatment.
7. **The category nav** — the S2/S3 Explorer tree, folder pages, breadcrumbs, alias redirects.
- **Out of scope: the flashcard decks** — frozen through the overhaul; their rebuild + deck↔page↔index
  (D12) verification is a **separate later run** (R11). S9 confirms only that the *frozen* deck still
  loads (not broken by page moves); it does not verify deck *content* freshness.
- *Check:* the assertion inventory (R3) enumerates every object in classes 1–7; no object class is
  unaddressed; each object carries a per-dimension verdict or a logged escalation.

### R2 — The extended dimension set D1–D14 + the final reviewer checklist **[S1 §3.E]**
S9 reviews against the **D1–D14** framework S1 §3.E defines (D1 extended to exhaustive-live; D3
extended N4/N13; D6 extended N2-lexicon; **D13** linking & glossary; **D14** brief-first &
teachability) and the **rule→dimension map** (every L#/N#/SR# maps to ≥1 dimension; the no-orphan
invariant). The N-rules the S9 interview names map as: **N1** homing → D2/D5; **N5** recent-dev
placement → D10; **N7** link-every-case → D13; **N8** brief-first → D14; **N13** no-blank-status →
D3; **N4** subsequent-treatment → D3/D5; **N2** lexicon → D6; **N9/N3** field-framing/tests-up-front
→ D9/D14; **L8** restate-not-editorialize → D2/D4/D9; **SR-1** → D1; **SR-5** → D1/D5. S9 produces the
**final per-object reviewer checklist** (§6.2) — which dimensions apply to a case page vs. a doctrine
page vs. a reference page vs. the glossary vs. the Case Index — so a reviewer signs a complete,
object-appropriate form.
- *Check:* the §6.2 checklist exists; every dimension D1–D14 has a reviewer prompt + an acceptance
  line; the object→dimensions matrix covers all R1 classes; no rule is orphaned (cross-checked vs.
  S1 §3.E).

### R3 — Exhaustive live re-verification + the assertion inventory **[SR-1, L1, L4; USER U1-S4/U2-S4]**
**P0 builds the assertion inventory** (deterministic, free): extract from every object every tracked
assertion — `(case-cite, stated holding/proposition, quoted passage + pinpoint, CL opinion URL +
opinion_id, authority-weight label, treatment status + as_of, cross-list framing, home + role, Mermaid
block, glossary definition, tool-fact)`. This inventory is the **exhaustive target list and the
completeness gate**. Then **every asserted case is re-read live against the primary opinion through the
single serial CL lane (SR-1, no tiering, including manifest-grade cases)** for: identity (L3:
cluster→lead opinion resolved, named case present in returned text), proposition match, every verbatim
quote + pinpoint, and good-law currency (N13). The proactive serial-CL sweeps that run **regardless of
findings**: good-law re-confirm on every case (batch via `analyze_citations` where possible), confirm
every unconfirmed quote/pinpoint, confirm every CL URL resolves to the right case (L3), and the
**new-frontier check** (D3 — splits/first-impression surfaced since the build).
- *Check:* every inventory item has a fresh **live-CL verdict**; `cl-calls.log` evidences a live
  re-check for **every** case; zero cases pass on manifest/prior grade alone; zero unverified legal
  claims asserted as settled; the inventory has no item without a verdict (the exhaustiveness proof).

### R4 — The find→adjudicate→fix machine, uniform N-of-3 review **[USER U2-S9; L5, L4, S1 §3.G]**
S9 runs the standing machine (S1 §3.G), with **uniform N-of-3 review** (the user's max-rigor choice):
1. **REVIEW (parallel, free, NO CL).** Per object, **three independent reviewers per dimension** emit
   structured findings `{id, object, dimension(D1–D14), locator(section + verbatim text), problem,
   severity, proposed_fix, needs_cl, confidence}`. For the **legal-assertion dimensions (D1, D3, D7)**
   the three are **adversarial refuters** — each prompted to *try to REFUTE* the assertion (default to
   refuted on uncertainty); a **majority-refute (≥2 of 3) kills/flags** the assertion. For **editorial
   dimensions** the three are **independent reviewers**; their findings are **unioned + deduped** into
   the finding set. **Reviewers may not edit.** N-of-3 review is FREE/NO-CL, so the fan-out does **not**
   touch the serial lane (L4 preserved).
2. **ADJUDICATE.** Every finding → a verdict in **{UPHELD, MODIFIED, DISMISSED, ESCALATE}** with
   `adjudicated_fix` + `evidence`. **`needs_cl=true` findings** (good-law, proposition, quote/pinpoint,
   case existence, CL-URL, new-frontier, a re-homing's holding basis, an SR-5 discordance) → the
   **single serial CL lane**; the verdict **must cite CL evidence**; no CL evidence → cannot UPHOLD a
   change to a legal assertion (→ DISMISS or ESCALATE). **Non-legal findings** (structure, fold-in,
   links, role labels, pedagogy, corpus-supported completeness, tool-fact) → a **free
   editor-adjudicator** (tool-fact findings adjudicated against the **live tool + a current source** —
   the tool analog of CL evidence, S8·R12). **DISMISSED findings are logged with the reason** (a
   dismissed false-positive is a successful outcome — guards over-correction).
3. **FIX (parallel, free).** A fixer applies **only** UPHELD/MODIFIED adjudicated fixes, verbatim;
   introduces no new content; **ESCALATE → `_review-needed/<slug>.md`**. **Loop cap 3**, then escalate;
   **checkpoint the ledger after every sub-phase** (resumable).
- *Check:* every legal-assertion dimension shows a 3-reviewer refutation tally; every editorial
  dimension shows ≥1 independent review deduped; every change traces to an adjudicated UPHELD/MODIFIED
  verdict with evidence; reviewers produced findings only; DISMISSED carry reasons; `cl-calls.log`
  shows a single serial lane; loop cap honored; escalations logged.

### R5 — Whole-corpus conclusion-blind re-derivation + concordance reconciliation **[USER U3-S9; SR-5]**
S9 inherits SR-5 (S1 §3.C) as its final-gate instrument and applies it to the **whole corpus**:
- **Thread P (the build), frozen up front (P0).** Extract the build's conclusion set — per case:
  existence, holding/ratio, home-by-holding (N1), role, treatment/good-law, split call; per doctrine:
  case set + split calls — from the finalized pages + the S4/S5 manifests/ledgers. Held aside;
  **withheld** from Thread N's context (§6.4 `thread-P.json`).
- **Thread N (new), conclusion-blind (P1b).** A fresh pass **re-derives** each case's and each
  doctrine's conclusions **from primary authority** and **records its conclusions before** Thread P is
  revealed to the reconciliation step. **Efficiency that makes whole-corpus tractable:** Thread N
  forms its conclusions from the **same live opinion reads** SR-1 already performs (SR-5 permits shared
  primary sources; only the *conclusions* must be blind) — so the marginal cost over SR-1 is "withhold
  P's answer + record N's reading first + compare," **not** a duplicate CL sweep. Blindness is enforced
  by **orchestration** (freeze P → run N with P withheld from its context → reconcile via a separate
  step/sub-agent); one agent holding both threads at once voids the check.
- **Reconciliation gate.** Diff N vs P at **two levels** — *coverage* (same case set per doctrine?)
  and *judgment* (same holding/home/role/treatment/split per shared case?) — tagging each:
  **Concordant → `double-verified`** (a stronger grade than single-pass); **Fundamentally discordant**
  (presence/absence · holding/ratio · home-by-holding · role Key↔Related · treatment/good-law · split
  direction differ — cosmetic wording/order does **not**) → **escalate to the find→adjudicate→fix
  machine (R4.2)**: adjudicate against the **primary opinion** (serial CL), the verdict stating **what
  diverged** (prior wrong / new wrong / scope-or-framing shift) and **which conclusion stands**;
  **Cosmetic → reconcile freely**.
- **No-regression floor.** Any Thread-P item **absent** from Thread N is a coverage-discordance that
  **must** be investigated → `re-surfaced` / `re-verified` / `dropped-with-prior-reason` (the 4 fakes /
  UNVERIFIABLE / flagged bare-name captures → carried as flagged omissions, never silently re-lost) /
  `regression → re-ingest`. **No prior verified conclusion is silently absent** from both the live wiki
  and the omissions register.
- *Check:* Thread P was frozen before Thread N ran (blindness audited, §8); N recorded its conclusions
  before reconciliation; every case/split carries a concordant/discordant disposition at **both**
  levels; concordant items are `double-verified`; **every** fundamental discordance carries a
  CL-adjudicated verdict naming what diverged and which stands; zero prior verified conclusions are
  silently absent; `thread-P.json` / `s9-concordance.json` evidence the pass.

### R6 — Visual / Mermaid accuracy pass **[D8]**
**Render EVERY Mermaid diagram** (mermaid-cli + system Chrome → PNG, per FINAL-QA Key-paths) and
**visually inspect each** by reading the PNG: every node/branch matches the page's stated rule; the
correct cases are labeled; compact + legible. This covers the new S6 interactive-flowchart diagrams
**and** every pre-existing diagram (the prior pass left ~25 un-re-inspected — D8 closes that). A
diagram whose nodes contradict the page's brief is a **finding** (→ adjudicate → fix the diagram or
the brief, whichever the holding supports).
- *Check:* every diagram renders; every diagram has a logged visual-inspection verdict; zero diagrams
  contradict their page's stated rule; cross-checked against the (now re-verified) brief.

### R7 — Link & identity check + the automated lint roster (pre-publish gate) **[L3, N7; S1 §3.H; SR-4]**
The deterministic gate, run pre-publish (via the **`npx quartz build` validation step / CI** — *not*
`redeploy.sh`, which is retired with the vault→content sync, R14), the CL-touching lint reusing the
serial lane:
- **Wikilink integrity:** zero broken `[[Page]]` / `[[Case]]` / `[[Case#anchor]]` links across the
  corpus (after the S2 folder move + the S4 case linking + the S6 reformat).
- **CL-URL identity (LINT-1 / L3):** every CL URL resolves (200) **and** the returned text contains
  the **named** case; cluster→lead opinion resolved.
- **Deep-link / term anchors:** every `#rule` / `#^pin-N` case anchor (S4·R6) and every glossary
  `### Term` (S7·R7) / legal-research `### Term` (S8·R4) anchor resolves under SPA nav.
- **Alias redirects (S3):** the caretaking-split old slug, the S8 old slug, and every path-changed
  page's `aliases:` redirect resolves; no broken inbound link.
- **The lint roster LINT-1…8** (S1 §3.H) **+ LINT-7-AUTO sub-checks** (S7·R10 a–d) all green:
  LINT-1 CL-identity · LINT-2 quote↔pinpoint · LINT-3 section-order + no-SCOTUS-in-recent-dev +
  single controlling amendment · LINT-4 6-tier lexicon (no "persuasive, not binding"; circuits named)
  · LINT-5 link-every-named-case · LINT-6 non-blank treatment status + as_of · LINT-7 glossary wiring
  (AUTO half) · LINT-8 guardrails (no apocryphal trio; mnemonics uncited; no inline `## Flashcards`).
- *Check:* the roster runs green at the gate; a hand-sample of LINT-1/LINT-5 results is spot-verified
  (the lint isn't trusted blind — §8); zero broken links/anchors/aliases corpus-wide.

### R8 — Cross-page coherence audit **[D5, N4, N6]**
A **shared-case audit** over every multi-homed case: page-specific **framing** may differ (N6), but
**treatment status + the N4 "limited by [[case]]" tag are identical across every home**, overruled
cases are shown as **Historical** everywhere they appear, and **no two pages contradict** each other
(boundary sentences where doctrines overlap). The audit reconciles the case-page record (S4, the
canonical source) against every doctrine-page mention of that case.
- *Check:* the shared-case audit shows zero treatment/tag conflicts across homes; zero cross-page
  contradictions; overruled cases are Historical + carry `overruled` treatment everywhere; each
  multi-homed case's doctrine mentions agree with its case page.

### R9 — Glossary/term-wiring re-audit + legal-research tool-fact currency re-vet **[S7, S8; N11, L2, N13]**
- **Glossary/term-wiring (S7·§9 continuous audit):** re-run the S7 term audit against the **final**
  page text (page text changed through S6); confirm every qualifying term-of-art is wired on first
  occurrence to the correct target (page per R2-S7, glossary anchor otherwise), no over-linking, no
  banned/own-subject/officer-known/plain-English link, every glossary anchor resolves, every new
  glossary definition accurate + in-voice (D11), and case-tied glossary propositions two-keyed (L1).
- **Tool-fact currency (S8·R8 / §8.5):** **re-vet every legal-research tool fact live** against a
  current source (the tool analog of CL evidence) — specifically re-confirm OpenCase's free-tier
  limits, the neutral-cite state list, vLex Fastcase bar terms, and that no retired tool (Casetext,
  Ravel) is asserted live; refresh the "verified current as of <date>" stamp.
- *Check:* the term-wiring audit passes against final text; the LINT-7 AUTO sub-checks are green and
  the CHECKLIST sub-checks signed; every tool fact traces to a current source dated at S9; the
  currency stamp is refreshed; the two S8 corrections (OpenCase≠OpenJurist; Casetext-retired) hold.

### R10 — Case-Index regeneration + category-nav/Explorer/alias integrity **[S4·R10, S2, S3; D12]**
- **Case Index (S4·R10):** **regenerate `Case Index.md` from the final `content/cases/*` frontmatter**;
  regeneration is **byte-diff-clean** vs. the committed index (it cannot drift from the pages); every
  Case cell is a resolving `[[wikilink]]`; no blank treatment cell; the human-readable header prose is
  preserved.
- **Category nav (S2/S3):** the Explorer renders the 12 S2 categories in book-spine order, collapsible,
  with the active page's folder auto-expanded/highlighted; exactly one 3-level branch (the exceptions
  cluster); breadcrumbs + folder pages resolve; `cases/` segregated from the doctrine nav; the
  sidebar de-cramp (380px / 1.6rem) is in effect; components degrade correctly with JS disabled
  (S3·R5 portability spot-check on sample pages).
- *Check:* the regenerated Case Index diff-cleans against the pages; the rendered Explorer matches the
  S2 tree + depth invariant; zero broken nav/alias links; components degrade legibly when disabled.

### R11 — Decks out of scope: frozen through the overhaul; rebuild is a SEPARATE later run **[USER U5-S9; S4·R11 as amended; L1; D12 deferred]**
**S9 does NOT rebuild the flashcard decks and does NOT gate on deck↔page↔index integrity (D12).** Per
the user's decision (U5-S9), **no flashcard work happens anywhere in the overhaul (S1–S9)** — the decks
stay **frozen/untouched**, and the page-derived purge-and-regenerate (decks derive **FROM** the
finalized, verified pages — L1; existing taxonomy preserved; no per-case decks; FSRS progress resets)
runs as a **separate flashcard run AFTER** the overhaul and the full content corpus are finalized. S9's
only deck obligation is a **non-breakage check**: confirm the existing, frozen `flashcards.json` still
**loads** and is not broken by the S2 folder moves / S6 reformats / the caretaking split — stable file
stems (D-3) + the S3 caretaking alias keep deck `page:` references resolving until the separate rebuild
(S4·R11). The decks will carry **stale content** (old cards vs. rebuilt pages) by design until that run;
that is expected, not a finding. **D12 (deck↔page↔index integrity) is deferred to the separate run.**
- *Check:* **zero deck files modified by S9**; the published frozen `flashcards.json` still loads (the
  study app opens, the caretaking-split alias resolves the dangling `page:`); S9 emits **no** deck
  artifact and runs **no** `merge.py`/`make_apkg.py`; the separate flashcard run (owning D12) is flagged
  in `FINAL-S9-REPORT.md` as the required follow-on.

### R12 — The ledger + reporting artifacts **[L5; FINAL-QA §7]**
S9 keeps a resumable, checkpointed ledger and produces the durable trail (in `_run/` mirrored, per the
project pattern):
- `S9-LEDGER.json` — per object: dimension verdicts, findings, adjudications, fixes, escalations,
  status. **Resumable** (checkpoint after every sub-phase).
- `s9-findings.json` / `s9-adjudications.json` — the full find→adjudicate trail incl. **DISMISSED +
  reasons** and the N-of-3 refutation tallies.
- `assertion-inventory.json` — every tracked assertion + its final verdict (the exhaustiveness proof).
- `thread-P.json` / `s9-concordance.json` — the SR-5 frozen build conclusion set + the reconciliation
  ledger (per item: concordant→`double-verified` / discordant→adjudicated verdict + CL evidence /
  cosmetic; the no-regression dispositions).
- `s9-false-positives.json` — the §8 self-audit log (DISMISSED findings, over-corrections caught,
  sampling re-check results, per-dimension false-positive rates).
- `cl-calls.log` — the single serial CL lane log (tier-probe result; pace; no concurrent timestamps).
- `FINAL-S9-REPORT.md` — accuracy summary; **every negatively-treated case** (limited/abrogated/
  overruled, with the limiting case); **every split/frontier** surfaced; the completeness sign-off vs.
  the assertion inventory; the **flag that the page-derived flashcard rebuild is a required separate
  follow-on run** (decks were frozen, not rebuilt, in the overhaul); the release-gate checklist with
  each box ticked or escalated; everything parked in `_review-needed/`.
- *Check:* every artifact exists and is internally consistent (counts reconcile across findings →
  adjudications → fixes → inventory); the ledger is resumable; the report enumerates negative
  treatments + splits + escalations.

### R13 — The release gate (the literal definition of done) + escalation policy **[USER U1-S9, U4-S9; SR-2, SR-4]**
**Done == the §7 release-gate checklist passes.** It is the **full composite gate** (the user's
choice): the legal/citation/structural checks **and** the **blocking SR-2 instructor-grade gate**
(D2 ∧ D4 ∧ D9 ∧ D14) on every doctrine page must pass — a page with perfect cites but a muddled or
incomplete brief **FAILS** and is escalated, not shipped. A page/object ships only when its automated
lint roster is **green** **and** its N-of-3 reviewer checklist is **signed**. **Escalation policy
(U4-S9):** anything unresolved after **loop cap 3** goes to a `_review-needed/<slug>.md` human queue
with the open issue stated; **no legal assertion is ever guessed or changed without CL evidence**
(two-key). **"100% verified" tolerates logged escalations, not silent gaps** — the gate is satisfied
when every object **passes OR carries a logged `_review-needed` escalation**, and zero assertions in
the inventory lack a verdict.
- *Check:* the §7 checklist is evaluated object-by-object; every box is ticked or maps to a logged
  escalation; zero silent gaps; the SR-2 composite gate is signed on every doctrine page; no
  `_review-needed` item is a guessed legal assertion.

### R14 — Publish & verify live **[FINAL-QA P5; EXECUTE guardrail; USER U6-S9 source-of-truth]**
**`content/` is the canonical source** post-overhaul (USER U6-S9): the overhaul rebuilt `content/`
directly, so the legacy **vault→content sync is RETIRED** — **do NOT run `redeploy.sh`** (it would
overwrite the rebuilt `content/` with the stale iCloud vault) for publish *or* build-validation.
On gate pass, **prepare** the outward step but **stop before pushing to `main` / triggering a Vercel
production deploy** (the EXECUTE guardrail — surface for the user's go-ahead). The prepared step:
**validate with a direct `npx quartz build`** (no vault sync) succeeds, then (on go-ahead) **commit +
push `content/` → origin main → Vercel** (Vercel builds the repo); **verify live**: pages 200, no
internal 404s, internal dirs unpublished,
Mermaid renders, CL links resolve, the **existing frozen flashcard deck still loads** (not rebuilt —
R11), popovers/Explorer/components work.
Deliver the **served HTML brief** (per the `/brief` flow) summarizing changes + the verification ledger
+ `_review-needed/` + the review/deploy commands; hand the link; wait for go-ahead.
- *Check:* the local build succeeds pre-push; the pass stops before the production deploy and surfaces
  the brief + commands; on go-ahead, the live checks pass; the brief link is delivered.

---

## 4. Lessons enforced

- **SR-1** (exhaustive live re-verify, no tiering) → **R3** (every case re-read live) + R1 (whole
  corpus). **SR-2** (blocking instructor-grade gate) → **R13** + R2 (the composite D2∧D4∧D9∧D14 on
  every doctrine page). **SR-5** (independent-replication concordance) → **R5** (whole-corpus
  blind-then-reconcile; agreement double-verifies, fundamental disagreement escalates). **SR-3**
  (STANDARDS.md supremacy) → every phase cites S1. **SR-4** (automated-where-cheap + checklist) → R7
  roster + R2 checklist, both required pre-ship.
- **L1** (two-key / no paraphrase drift) → R3 + R4 (no legal change without CL evidence). **L2** (web
  discovers, CL confirms) → R3 frontier + R9 tool re-vet (AI/web is discovery, the primary opinion /
  live source confirms). **L3** (cluster-id ≠ opinion-id) → R3 + R7 (CL-URL identity). **L4** (one
  serial CL lane) → R3/R4/R5 (N-of-3 review is free/no-CL; all CL through the one lane). **L5**
  (find→adjudicate→fix) → R4 machine. **L6** (not-found ≠ fake; escalation ladder) → R3 (UNVERIFIABLE
  only after the ladder) + R5 no-regression. **L7** (scope-boundary = assertion) → R4 (negative-scope
  framings are `needs_cl`). **L8** (restate, not editorialize) → R2 (case pages restate; D2/D4/D9) +
  R8 (cross-page framing).
- **N1** homing → D2/D5 in R2/R5/R8. **N2** lexicon → R7 LINT-4. **N3/N9** tests-up-front / field
  framing → R2 D14/D9 + R13 SR-2. **N4** subsequent-treatment → R8 (consistent across homes). **N5**
  no-SCOTUS-in-recent-dev → R7 LINT-3. **N6** non-exclusive key-status → R8. **N7** link-every-case →
  R7 LINT-5. **N8** brief-first → R2 D14. **N10** state scope → R2 D4 (caretaking strands). **N11**
  glossary wiring → R9. **N13** no-blank-status → R7 LINT-6 + R3.
- **D1–D14** (S1 §3.E) → R2 reviewer framework; **D8** Mermaid → R6. **D12** deck↔page↔index → **deferred
  to the separate flashcard run** (R11); S9 verifies only deck non-breakage.
- **The find→adjudicate→fix machine** = `FINAL-QA-SPEC.md` §2, now governed by STANDARDS.md and run
  with uniform N-of-3 review (R4). S9 is the **successor** to FINAL-QA-SPEC §0–§8 (its P0–P5 / D1–D12
  pass), extended by every S1 rule above.

## 5. Method (how the autonomous execution runs the pass — phases, each ends with a gate + ledger checkpoint)

S9 runs **after S1–S8** content exists. Orchestrator stays thin (ledger/specs/statuses only); all work
in fresh sub-agents; **all CL through the single serial lane** (re-probe the tier first, STOP on the
old 5/min tier per RUNBOOK §3); checkpoint after every sub-phase (resumable).

- **P0 — Bootstrap, inventory & Thread-P freeze.** Timestamped backup. Re-probe CL tier. Load
  `docs/STANDARDS.md` + all specs + prior ledgers/manifests. **Build the assertion inventory** (R3,
  deterministic, free) over the whole corpus (R1). **Freeze Thread P** (R5) — the build's conclusion
  set — and withhold it from the Thread-N context. *Gate:* inventory built; tier OK; Thread P frozen.
- **P1 — Dimensional review (parallel, free, NO CL) + Thread-N blind re-derivation.** Per object,
  **N-of-3** reviewers across the object's applicable D1–D14 (R2/R4): adversarial refuters on D1/D3/D7,
  independent reviewers on editorial dimensions. **In parallel, Thread N** re-derives every case's +
  doctrine's conclusions **conclusion-blind** (R5), forming them from the same live opinion reads SR-1
  performs, and **records them before** reconciliation. *Gate:* every object reviewed (3×/dimension);
  Thread N's conclusions recorded; findings collected.
- **P2 — Adjudication (editorial lane + the single serial-CL legal lane) + SR-5 reconciliation.**
  (a) Serial-CL adjudication of all `needs_cl` findings **+** the proactive sweeps (R3: good-law
  re-confirm every case; quotes/pinpoints; CL-URL identity; new-frontier). (b) Free editor-adjudication
  of non-legal findings (incl. tool-fact vs. live source, R9). (c) **Reconcile Thread N vs Thread P**
  (R5): concordant→`double-verified`; fundamental discordance→adjudicate against the primary opinion
  (serial CL), verdict states what diverged + which stands; the no-regression floor accounts for every
  Thread-P item. *Gate:* every finding + every discordance has a verdict + evidence; CL log shows no
  old-tier throttle; no prior verified conclusion silently absent.
- **P3 — Fix (parallel, free).** Apply UPHELD/MODIFIED per object; ESCALATE → `_review-needed/`. Loop
  cap 3. *Gate:* all UPHELD/MODIFIED applied; escalations logged.
- **P4 — Final sweeps.** Render + visually inspect ALL Mermaid (R6/D8); the link & identity check +
  lint roster (R7); cross-page coherence (R8/D5); glossary/term re-audit + tool-fact re-vet (R9);
  Case-Index regeneration + nav/alias integrity (R10); completeness sign-off vs. the inventory (every
  item has a verdict). *Gate:* all sweeps pass or escalate.
  *(No deck-rebuild phase — decks are out of scope; the page-derived rebuild is a separate later run,
  R11. S9's only deck step is the non-breakage check folded into the P4 sweeps.)*
- **P5 — Release-gate sign-off + self-audit.** Evaluate the §7 release gate object-by-object (R13);
  run the §8 self-audit (false-positive logging, adjudication sampling re-checks, blindness audit).
  *Gate:* every box ticked or escalated; the self-audit passes.
- **P6 — Publish & verify live & report.** Validate with a direct **`npx quartz build`** (no
  `redeploy.sh`/vault sync — `content/` is canonical, R14); **stop before the production push**;
  deliver the served HTML brief + review/deploy commands **+ the flag that a separate flashcard rebuild
  run is still owed**; on the user's go-ahead, **commit + push `content/`** → Vercel → verify live.
  *Gate:* live checks pass; brief delivered.

## 6. Deliverables (what the execution produces)

### 6.1 — The artifacts (R12)
`S9-LEDGER.json` · `s9-findings.json` · `s9-adjudications.json` · `assertion-inventory.json` ·
`thread-P.json` · `s9-concordance.json` · `s9-false-positives.json` · `cl-calls.log` ·
`FINAL-S9-REPORT.md` · the `_review-needed/<slug>.md` queue · the regenerated `Case Index.md` · the
served **HTML brief**. *(No deck artifacts — decks are frozen; the rebuilt deck set is produced by the
separate later flashcard run, not S9.)*

### 6.2 — The final reviewer checklist (the object→dimensions matrix) **[R2]**

| Object class | Applies | Notes |
|---|---|---|
| **Case page** (S4 BIRAC) | D1 (two-key, live), D2 (restate-not-editorialize / placement-by-holding), D3 (treatment + N4), D6 (lexicon weight), D7 (citation/pinpoint + CL identity), D10 (BIRAC structure), D13 (linking + anchors) | **No** D14/D9 doctrine-brief gate (case pages restate; L8). The Application must be case-fact-bound. |
| **Doctrine page** (S6 brief-first) | **D1–D14 (full)**, incl. the **SR-2 composite D2∧D4∧D9∧D14** (blocking), D8 (Mermaid) | The instructor-grade gate (R13) blocks shipping a muddled/incomplete brief. |
| **Reference/narrative page** (S6/R11) | D1 (accuracy), D6 (lexicon/guardrails), D7 (citation where present), D11 (reference accuracy), D13 (links) | Not bound by the doctrine TOC (S1 §3.I); leads with the field-decisive question (N9). |
| **Glossary** (S7) | D11 (definition accuracy/voice), D13 (anchors + wiring), D1 (two-key on any case-tied definition) | Term-of-art-only; routing per S7·R2; first-occurrence wiring. |
| **Legal-research pages** (S8) | D1 (any asserted holding), D6 (lexicon), D7 (citation-mechanics), D11 (tool-fact accuracy + currency), D13 (term anchors + links) | Tool-fact adjudicated vs. a **live source** (the CL analog). |
| **Case Index** (S4·R10) | D7 (links), D12 (regeneration fidelity), D13 (every cell resolves), N13 (no blank treatment) | Regenerated from frontmatter; diff-clean. |
| **Category nav** (S2/S3) | D10 (tree/depth), D13 (links/aliases) | Explorer order + depth invariant + alias redirects. |
| **Decks** | *(out of scope — non-breakage check only)* | Frozen through the overhaul; D12 + the page-derived rebuild are a **separate later run** (R11). |

Each form carries, per dimension, the reviewer prompt + the acceptance line from S1 §3.E and the
N-of-3 disposition (refutation tally for D1/D3/D7; deduped findings otherwise).

### 6.3 — The release-gate checklist (= §7, the literal ship condition).
### 6.4 — The self-audit design (= §8).

## 7. Acceptance criteria (the release gate — the literal definition of done)

> *Done == every box ticked OR mapped to a logged `_review-needed/` escalation. No silent gaps;
> zero inventory items without a verdict; no guessed legal assertion (two-key).*

- [ ] **Exhaustive accuracy (D1/SR-1):** every asserted case/holding/fact/quote/pinpoint in the
      assertion inventory has a **fresh live-CL verdict**; zero cases passed on prior grade alone; zero
      unverified legal claims asserted as settled.
- [ ] **Adjudication completeness (L5):** every finding (N-of-3) has a verdict {UPHELD/MODIFIED/
      DISMISSED/ESCALATE} with evidence; every UPHELD/MODIFIED fix is **applied**; DISMISSED logged with
      reason; **zero open UPHELD/MODIFIED findings unapplied**.
- [ ] **Concordance (SR-5, whole corpus):** Thread P frozen before Thread N (blindness audited); every
      case/split has a concordant/discordant disposition at coverage + judgment levels; concordant →
      `double-verified`; **every** fundamental discordance carries a CL-adjudicated verdict; **zero**
      prior verified conclusions silently absent (no-regression floor satisfied).
- [ ] **Case pages:** every verified case has a BIRAC page (S4); **two-key'd + `identity_checked: true`
      + non-blank treatment + as_of**; the Application is case-fact-bound (no editorial street takeaway,
      L8); every quote verbatim + pinpointed.
- [ ] **No blank treatment status anywhere** (N13/LINT-6); every case carries a 6-tier authority-weight
      **and** a treatment status with a check date.
- [ ] **No SCOTUS in Recent-developments** (N5/LINT-3) on any doctrine page; every recent-dev entry is
      circuit/state with an expand/narrow/split/first-impression role.
- [ ] **Every named case linked** (N7/LINT-5); zero bare case names; passage discussions deep-link;
      every `[[Case]]`/`[[Case#anchor]]`/glossary/term anchor + alias redirect resolves.
- [ ] **All named tests stated up front** (N3/D14) on every doctrine page (the *Dunn* factors, the
      consent prongs, the *Garner* 3-part test, etc.).
- [ ] **Instructor-grade gate (SR-2, blocking):** every doctrine page passes the composite
      **D2 ∧ D4 ∧ D9 ∧ D14**; no muddled/incomplete brief shipped (escalated instead).
- [ ] **Lexicon (N2/LINT-4):** every authority label is one of the 6 tiers; zero "persuasive, not
      binding"; circuits named; splits flagged.
- [ ] **Cross-page coherence (D5):** shared/multi-homed cases carry identical treatment + N4 tag across
      homes; overruled cases shown as Historical everywhere; zero cross-page contradictions.
- [ ] **Every Mermaid visually inspected (D8)** and doctrinally faithful to its page's stated rule
      (new + pre-existing diagrams).
- [ ] **CL-URL identity (L3/LINT-1):** every CL URL resolves AND shows the named case.
- [ ] **Glossary + term wiring (S7):** re-audited against final text; term-of-art-only; first-occurrence;
      anchors resolve; case-tied definitions two-keyed; AUTO sub-checks green, CHECKLIST signed.
- [ ] **Legal-research tool facts (S8):** re-vetted live; currency stamp refreshed; OpenCase≠OpenJurist
      + Casetext-retired corrections hold; no defunct tool asserted live.
- [ ] **Case Index (S4·R10):** regenerated from frontmatter, **diff-clean**; every cell resolves; no
      blank treatment cell.
- [ ] **Category nav (S2/S3):** Explorer in spine order + depth invariant; sidebar de-cramped;
      components degrade legibly when disabled; zero broken nav/alias links.
- [ ] **Decks (R11) — non-breakage only:** **zero deck files modified by S9**; the existing frozen
      `flashcards.json` still loads (study app opens; the caretaking-split alias resolves the dangling
      `page:`). **D12 + the page-derived rebuild are a separate later run** and are **not** gated here;
      `FINAL-S9-REPORT.md` flags that run as the required follow-on.
- [ ] **Ledger reconciles (R12):** findings → adjudications → fixes → inventory counts reconcile; the
      `FINAL-S9-REPORT.md` enumerates every negative treatment, every split/frontier, the completeness
      sign-off, and every `_review-needed/` escalation.
- [ ] **Self-audit (§8) passes:** false-positive log populated; adjudication sampling re-check clean;
      blindness audit confirms Thread-P-before-Thread-N.
- [ ] **Published + verified live (R14):** direct `npx quartz build` succeeds (no `redeploy.sh`/vault
      sync — `content/` is canonical); on the user's go-ahead, **commit + push `content/`** → pages 200,
      no internal 404s, internal dirs unpublished, Mermaid renders, CL links resolve, the frozen deck
      still loads; the served HTML brief (incl. the separate-flashcard-run flag) is delivered.

## 8. Verification plan (how the verification pass itself is audited — false-positive logging, sampling re-checks)

S9 is the verifier; this section is the **meta-verification** that keeps the verifier honest. The
guarantee is not "S9 ran" but "S9's own findings, adjudications, and blindness are themselves checked."

1. **False-positive logging (over-correction defense).** Every **DISMISSED** finding is logged with
   its reason in `s9-false-positives.json`; a dismissed false-positive is a **successful** outcome. The
   **N-of-3 refutation tally** for each legal assertion is recorded (a 1-of-3 refute that was overruled
   is logged, not silently dropped). Per-dimension/per-reviewer **false-positive rate** (DISMISSED ÷
   total) is surfaced; a reviewer or dimension producing mostly-dismissed noise is flagged for prompt
   tuning — but **no finding is auto-suppressed**.
2. **Adjudication sampling re-check (the adjudicator can err too).** A **random sample** of
   **UPHELD/MODIFIED legal adjudications** gets an **independent second serial-CL confirmation** (a
   different sub-agent, same single lane) — catching a bad UPHELD before it ships a wrong "fix." Any
   sampled adjudication that fails re-check escalates the **whole dimension** for a re-sweep, not just
   the one item.
3. **Pass-sample re-read (the exhaustive pass isn't trusted blind).** A **random sample of "passed"
   case pages** is independently **re-read against the CL opinion** (proposition + every quote +
   pinpoint) — the FINAL-QA Phase-8-style sample, now a **meta-check on** the exhaustive pass, **not a
   substitute** for it. A failure in the sample means the exhaustive pass missed something → re-open.
4. **Blindness audit (SR-5 independence is verified, not assumed).** Confirm from the orchestration log
   that **Thread P was frozen before Thread N ran** and **Thread N recorded its conclusions before
   reconciliation** — and that no single agent held both threads. If blindness cannot be evidenced, the
   concordance result is **void** (agreement carries information only if the threads were blind) and the
   re-derivation is re-run.
5. **Inventory-completeness audit (no silent skips).** Re-confirm **every** assertion-inventory item
   has a verdict and every R1 object class is represented; an item without a verdict is a gate failure,
   not a pass.
6. **Lint spot-verification (no false confidence from green checks).** Hand-verify a **sample** of
   LINT-1 (CL identity) and LINT-5 (link-every-case) results — a green lint that a hand-check
   contradicts means the lint is broken, which is itself a finding.
7. **Escalation audit (nothing dropped at the loop cap).** Confirm every item that hit **loop cap 3**
   is in `_review-needed/` with a stated open issue; **zero** loop-capped items silently dropped; no
   `_review-needed` item is a guessed legal assertion.
8. **Drift re-check before publish (R9/R14).** The tool-fact currency and the new-frontier good-law
   checks are **re-confirmed at the gate** (not just mid-pass), since law and third-party tools move
   during a long pass.

*Failures of this self-audit are themselves findings*: they re-open the relevant phase rather than
ship. The self-audit result is recorded in `FINAL-S9-REPORT.md` and is a release-gate box (§7).

## 9. Open items / escalations

- **CL budget — the heaviest pass, now heaviest-squared.** Whole-corpus SR-1 (every case live) +
  whole-corpus SR-5 blind re-derivation + N-of-3 legal-refutation adjudication all funnel through the
  **single serial CL lane (L4)**. The cost-controlling facts: **N-of-3 review is free/no-CL** (only
  adjudication touches CL), and **Thread N shares SR-1's primary-source reads** (only conclusions are
  blind), so the marginal CL cost of "whole corpus" over SR-1-alone is reconciliation, not a duplicate
  sweep. Even so this is the project's largest CL load — run it **patiently in serial batches,
  checkpointed/resumable**; **RUNBOOK §3 STOP-and-notify governs** if the tier regresses to 5/min. If
  the user later wants to bound it, the lever is R5 scope (whole-corpus → high-stakes+changed+sample);
  flagged, not taken.
- **Flashcards are a SEPARATE later run (USER U5-S9) — NOT part of S9.** No deck work happens anywhere
  in the overhaul; the page-derived purge-and-regenerate (decks derive FROM the finalized verified
  pages, L1; D12 verified there) runs **after** the overhaul + the full content corpus are finalized.
  S9 only confirms the frozen deck is not *broken* (R11). The detailed regeneration design (card-type
  mix, cloze coverage, Name-That-Case sourcing) and any **FSRS-progress-preservation** option (id-stable
  rebuild + app-side id-alias map) are decided in **that run**, before its irreversible purge.
  **`FINAL-S9-REPORT.md` must surface "flashcard rebuild run still owed" as a required follow-on**, and a
  dedicated wrapper for it should be authored when the user is ready.
- **`The Warrant Requirement` possible split (S2·§6.2 / S6·§9).** If S6's reformat pushed it past the
  ½–1-page budget and knock-&-announce was split out, S9 verifies the split page like any other; if it
  was kept whole, S9 confirms the budget call was logged. Non-blocking.
- **Open S6 execution items to confirm resolved (not re-decided):** the *Osage* consent-destruction
  illustrative case (identity + pinpoint confirmed live), the knock-and-talk circuit split (annotated,
  not resolved), the CREW "RE" mnemonic fix. S9 confirms each was resolved/logged, not whether the
  decision was right.
- **Garrity OPTIONAL→CORE S2 cross-ref (S5·R11 / S6·§9).** S9 confirms the one-line S2 §2.0 cross-ref
  was added at execution (the conscious supersession is recorded), and that the Garrity doctrine page +
  case pages verify like everything else.
- **Borderline sign-off (S5·R2).** S9 confirms the coverage borderline list was **dispositioned by the
  user** and that no borderline case was ingested/dropped without a recorded disposition.
- **Continuous-audit cadence (S7·§9 / N11).** S9 runs the glossary/term re-audit once at the gate;
  the **post-overhaul maintenance cadence** (re-run whenever page text changes) is flagged for the
  maintenance phase, not scheduled here.
- **iCloud EPERM (FINAL-QA §1).** The Read tool fails on the vault path; `cp` vault files to scratch to
  read, write in scratch + `cp` back. Files under `~/Projects/cssi-quartz/` read fine. An execution
  detail carried forward.

---

## Appendix A — Decision log

*Format: Question · Options · Red-team · Steel-man · Adjudication. **[USER]** = the user's actual
choice; the rest are self-interviewed.*

### [USER] U1-S9 — Definition of done / release gate → **Full composite gate.**
- *Options:* (a) **full composite gate** — the entire checklist incl. the **blocking SR-2
  instructor-grade gate**, dual-thread concordance, deck integrity, published+verified; "done" = passes
  or logged escalation; (b) **accuracy-hard, teachability-advisory** — hard-gate the legal/citation/
  structural checks but make SR-2 advisory (would relax S1's blocking rule).
- *Red-team (a):* the heaviest, slowest gate; SR-2 can block a page on a judgment call. *Steel-man (a):*
  it is exactly the S1·U-1 standard ("verified" must include correctly-framed + teachably-explained, not
  merely citation-accurate); option (b) would contradict S1·SR-2 and require an amendment.
- *Adjudication:* **(a)** (R13/§7). The full composite gate; SR-2 stays blocking; "100% verified"
  tolerates **logged** escalations, never silent gaps. User selected (a).

### [USER] U2-S9 — Adversarial intensity vs. cost → **Uniform N-of-3 everywhere.**
- *Options:* (a) **tiered** — 1 reviewer for editorial dimensions, N-of-3 adversarial refutation only on
  high-stakes legal assertions + novel/first-impression cases; (b) **uniform N-of-3 everywhere** — three
  independent reviewers on every dimension of every object; (c) **single-pass + serial-CL only**.
- *Red-team (b):* ~3× the review fan-out on the largest pass. *Steel-man (b):* maximum independent-error
  reduction; and because **N-of-3 review is free/no-CL** (R4.1), the fan-out does **not** load the serial
  CL lane (L4) — the cost is reviewer agents, not CL calls. *Red-team (a/c):* cheaper but leaves
  single-reviewer blind spots on editorial dimensions the user wants caught.
- *Adjudication:* **(b)** (R4). Uniform N-of-3; adversarial-refute framing on the legal-assertion
  dimensions (D1/D3/D7, majority-refute kills), independent-and-deduped on editorial dimensions. User
  selected (b).

### [USER] U3-S9 — SR-5 clean-room scope in S9 → **Whole corpus.**
- *Options:* (a) **high-stakes + changed + sample** (bounded blind re-derivation); (b) **whole corpus**
  (every case + every doctrine conclusion re-derived blind and reconciled); (c) **reconcile-only** (no
  fresh blind thread; lean on S5's concordance).
- *Red-team (b):* roughly doubles the already-heaviest pass — in principle. *Steel-man (b):* SR-5's
  agreement-as-verifier is strongest when applied **everywhere**, and the cost is contained by the
  **shared-primary-source** efficiency (R5) — Thread N forms blind conclusions from the **same** live
  reads SR-1 already does, so the marginal cost is reconciliation, not a duplicate CL sweep. (c) would
  weaken the final-gate guarantee the whole pass exists to provide.
- *Adjudication:* **(b)** (R5). Whole-corpus conclusion-blind re-derivation + reconciliation; shared
  CL reads keep it tractable; pacing/STOP-on-old-tier per RUNBOOK §3. User selected (b).

### [USER] U4-S9 — Escalation policy → **`_review-needed/` queue; never guessed.**
- *Options:* (a) **`_review-needed/` queue, never guessed** — unresolved-after-loop-cap-3 → human queue;
  no legal assertion changed without CL evidence (two-key); (b) **auto-resolve low-stakes, queue the
  rest**.
- *Red-team (b):* a low-stakes auto-resolution could slip an unreviewed editorial change through; the
  line between "low-stakes" and "legal" is itself a judgment that can err. *Steel-man (a):* the standing
  FINAL-QA / S1 §3.G pattern; "done" tolerates logged escalations, not silent drops, and the two-key
  guarantee is absolute.
- *Adjudication:* **(a)** (R13). User selected (a).

### SI-1-S9 — Pipeline shape: redesign or extend FINAL-QA P0–P5? → **Extend FINAL-QA, governed by STANDARDS.md.**
- *Options:* (a) design a fresh pipeline; (b) **adopt FINAL-QA's P0–P5 phase/gate/checkpoint shape and
  extend it** with the new objects (case pages, glossary, research pages) and the new instruments
  (N-of-3, SR-5).
- *Red-team (b):* FINAL-QA was authored for the prior corpus shape. *Steel-man (b):* the
  backup-first/thin-orchestrator/serial-CL/checkpoint-resumable spine is battle-tested (3,101 assertions
  / ~154 corrections) and is exactly what S1 §3.G adopts; reuse beats reinvention, and S9 is FINAL-QA's
  declared successor.
- *Adjudication:* **(b)** — P0–P6 (§5) extend P0–P5: P0 adds the inventory + Thread-P freeze; P1 adds
  N-of-3 + the blind Thread N; P2 adds the SR-5 reconciliation; P4 adds glossary/tool/nav sweeps; P5 the
  release gate + self-audit; P6 publish/verify. *(The deck-rebuild phase was removed by U5-S9 — decks
  are a separate later run.)*

### SI-2-S9 — Adopt S1's D1–D14 verbatim, or re-derive an S9 dimension set? → **Adopt D1–D14 (S1 §3.E) verbatim.**
- *Red-team (adopt):* none — S1 is the governing contract. *Steel-man (adopt):* S1 §3.E already extended
  D1–D12 → D1–D14 with the rule→dimension map and the no-orphan invariant precisely so S9 inherits it;
  re-deriving a parallel set would risk orphaning rules and contradicting SR-3.
- *Adjudication:* **adopt D1–D14 verbatim** (R2); S9's contribution is the **object→dimensions matrix**
  (§6.2) — which dimensions apply to each object class — and the N-of-3 disposition recorded per
  dimension.

### SI-3-S9 — Whole-corpus SR-5: does it double the CL load? → **No — shared primary-source reads; only conclusions are blind.**
- *Question:* U3-S9 chose whole-corpus blind re-derivation; does Thread N require a second full CL sweep
  on top of SR-1's?
- *Finding (SR-5 text):* independence is **conclusion-blind** — "both threads may use the same primary
  sources; the new thread must not be seeded with the prior thread's conclusions." So Thread N forms its
  conclusions from the **same** live opinion reads SR-1 already performs; the orchestration withholds
  **P's conclusions** from N's context, not the opinion text.
- *Adjudication:* (R5) Thread N reads no duplicate CL; the marginal cost is "record N's reading first +
  reconcile." This is the efficiency that makes U3-S9's whole-corpus choice tractable on the single
  serial lane. Recorded so the EXECUTE run does not naively double the sweep.

### SI-4-S9 — Where does the deck rebuild live? → ~~S9 phase P5~~ **SUPERSEDED by U5-S9: a separate later run, not S9.**
- *Original adjudication (self-interview):* run the terminal deck rebuild as an S9 phase (P5) after the
  content gate and before publish, with D12 verified on the rebuilt set.
- *Superseded (2026-06-30, during the cross-spec coherence pass):* the **user decided (U5-S9) that no
  flashcard work happens anywhere in the overhaul** — decks are frozen through S1–S9 and the page-derived
  rebuild is a **separate later run** after the full content corpus is finalized. The P5 deck-rebuild
  phase is **removed**; S9 keeps only a deck **non-breakage** check (R11); D12 + the rebuild move to that
  separate run. See **U5-S9** below.

### SI-5-S9 — How is tool-fact (S8) adjudicated, given there's no opinion to CL-check? → **Live source = the CL analog.**
- *Question:* S8's tool facts (free tiers, ownership, live/dead) aren't holdings; the serial CL lane
  doesn't verify them.
- *Adjudication:* (R9/§6.2) a tool-fact finding is adjudicated against the **live tool + a current
  source** (web re-vet), which is the **tool analog of CL evidence** (S8·R12) — same find→adjudicate→fix
  discipline, different evidence lane; the verdict cites the dated source. This keeps L2 (web discovers,
  primary/live source confirms) applied to the reference pages.

### SI-6-S9 — How is the verifier itself kept honest? → **A self-audit: false-positive logging + sampling re-checks + a blindness audit (§8).**
- *Question:* The interview's §8 asks how the **pass itself** is audited; an exhaustive verifier can
  still over-correct, mis-adjudicate, or fake independence.
- *Options:* (a) trust the N-of-3 + serial-CL adjudication as sufficient; (b) add an explicit
  **meta-verification** layer.
- *Red-team (b):* more process on the heaviest pass. *Steel-man (b):* the prior pass's own scars
  (reviewers over-correcting; a parallel-CL leak; sampling-not-exhaustiveness) prove the verifier needs
  its own guards; and SR-5's agreement signal is **meaningless if blindness isn't verified**.
- *Adjudication:* **(b)** (§8) — DISMISSED-with-reason false-positive logging; a random **adjudication
  sampling re-check** (independent second serial-CL confirmation of UPHELD/MODIFIED legal fixes); a
  **pass-sample re-read** as a meta-check on exhaustiveness; a **blindness audit** that voids the
  concordance result if Thread-P-before-Thread-N can't be evidenced; inventory-completeness + lint
  spot-verification + escalation audits. The self-audit result is itself a release-gate box.

### [USER] U5-S9 — Flashcards in the overhaul → **None. Frozen through S1–S9; rebuilt in a separate later run.** *(Added 2026-06-30, cross-spec coherence pass.)*
- *Question:* S4·R11 (and S5/S6/S7/S8) deferred the page-derived deck rebuild to "EXECUTE/S9," and the
  original S9 carried it as phase P5 + a D12 release-gate item. Keep the rebuild inside the overhaul, or
  defer it entirely?
- *Options:* (a) **rebuild at S9** (terminal P5, D12 gated — the original draft); (b) **no deck work in
  the overhaul at all** — decks frozen S1–S9; purge + regenerate from the finalized verified pages in a
  **separate run** once the full content corpus is final.
- *Discussion:* The user: "we're not doing anything with the flashcards. Once we have the full vault and
  everything, we'll do a separate flashcard run." *Red-team (b):* the new/renamed pages aren't drillable
  until that run, and the published deck carries **stale content** in the interim. *Steel-man (b):* it
  cleanly separates a 100%-verified **content** gate from a later **deck** rebuild (decks still derive
  FROM the final pages, L1), removes the heaviest non-content step from S9, and lets the FSRS-preservation
  question be decided in its own run. The interim staleness is acceptable (the frozen deck still loads via
  stable stems + the S3 alias).
- *Adjudication:* **(b)** — **removed the P5 deck-rebuild phase, the D12 release-gate item, and the deck
  artifacts from S9** (R11 rewritten to a non-breakage check; §2/§5/§6/§7 updated). The page-derived
  rebuild + D12 are a **separate later run**, flagged as the required follow-on in `FINAL-S9-REPORT.md`.
  Propagated to S4·R11 / S5·R8 / S6·R12 / S7 / S8 (deck pointers → "separate later run"). User chose (b).

### [USER] U6-S9 — Source of truth + publish, after the overhaul rebuilt `content/` directly → **`content/` is canonical; retire the vault→content sync.** *(Added 2026-06-30, cross-spec coherence pass.)*
- *Question:* The overhaul edits `content/` (repo) directly, but RUNBOOK §4 makes `content/` a **copy of
  the iCloud vault** synced **vault→content** via `redeploy.sh` — so the original S9 publish ("sync
  vault→content") would **overwrite the rebuilt `content/` with the stale vault** (data-loss hazard).
- *Options:* (a) `content/` is the working tree, reconcile **content/→vault** after the overhaul (keep
  Obsidian as the editing surface); (b) **`content/` becomes canonical; retire the vault→content sync**
  (re-point Obsidian at `content/` or drop the iCloud vault); (c) re-target the overhaul to edit the
  vault (needs major S2/S3/S4/S6 rework — the folder restructure can't `git mv` iCloud files).
- *Red-team (b):* departs from the established Obsidian + `/cssi-ingest` workflow (which reads
  `vault/_inbox/` and writes the vault). *Steel-man (b):* the overhaul's IA folder restructure is
  inherently a repo operation; making `content/` canonical removes the clobber hazard entirely and the
  publish path is simply commit/push `content/` → Vercel.
- *Adjudication:* **(b)** — **`content/` is the canonical source post-overhaul**; the **vault→content
  sync (`redeploy.sh`) is retired**. Publish = validate with a direct `npx quartz build`, then commit +
  push `content/` → Vercel; **never** run `redeploy.sh` (it would clobber). S9·R14/§5-P6 updated; the
  EXECUTE wrapper's publish/validation guidance updated to match. User chose (b). *(Note: the `/cssi-ingest`
  pipeline + the Tailscale `redeploy.sh` server are now out of step with `content/`-canonical and will
  need reworking — flagged for the separate post-overhaul maintenance, not handled in this build.)*
