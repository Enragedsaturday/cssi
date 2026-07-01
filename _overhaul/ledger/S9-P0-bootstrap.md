# S9 · P0 Bootstrap Checkpoint (FREE · no CourtListener) — 2026-06-30

> Branch `overhaul/build`. Deterministic bootstrap for the S9 verification pass per
> `_overhaul/specs/S9-verification.spec.md` R1/R3/§5-P0, R7, R12. **No content changed.**
> Artifacts written to `_run/` + this ledger only. All CL work (LINT-1, SR-1 live re-verify,
> SR-5 adjudication) is deferred to the single serial-CL lane in the later phases.

## Gate result: PASS (P0 objectives met)
- [x] Assertion inventory built (`_run/assertion-inventory.json`) — exhaustive target list.
- [x] Deterministic lint roster (LINT-2..8) run; HIGH triage complete; LINT-1 deferred to serial lane.
- [x] Thread-P frozen set confirmed (inherits S5's 0-regression audit).
- [x] Build baseline: `npx quartz build` OK; alias redirects emit.
- [x] Mermaid D8 worklist enumerated (42 diagrams / 42 files).

## 1. Assertion inventory — `_run/assertion-inventory.json`
Generator: `_run/build_assertion_inventory.py` (stdlib only, free).

**Objects by class:** case 456 · doctrine 38 · narrative 5 · glossary 1 · research 3 ·
case_index 1 · MOC 1 · nav (folder) 14 = **519 assertion-bearing objects** (+ `flashcards.md`
excluded — decks frozen/out of scope, R11).

**Total tracked assertions: 5076.**

| Class | Total | Breakdown |
|---|---|---|
| case | 3356 | holding 456 · cl_url(+opinion_id+identity_checked) 456 · authority_weight 456 · treatment(status+as_of) 456 · home+role 562 · quote(^pin) 970 |
| doctrine | 1152 | case_row 648 · quote(#^pin deep-link) 396 · recent_dev(page-less circuit) 67 · mermaid 38 · html-flag 3 |
| case_index | 467 | index_row 467 (matches the regenerated 467-row index) |
| research | 46 | term_anchor 21 · tool_fact 24 · mermaid 1 |
| glossary | 37 | term_def 37 (### anchors) |
| nav | 14 | folder_page 14 (no tracked legal assertion) |
| narrative | 4 | case_row 1 · mermaid 3 |

Every item carries a stable `id`, `class`, `kind`, and `object` (source path). This is the
exhaustiveness gate: each item must carry a live-CL or editorial verdict before the release gate.

## 2. Lint roster (LINT-2..8; LINT-1 = serial-CL-gate-only, deferred) — `_run/lint-summary.txt`
| Lint | total | high | med | low |
|---|---|---|---|---|
| LINT-2 quote/pinpoint | 260 | 0 | 260 | 0 |
| LINT-3 structure/no-SCOTUS-in-recent-dev | 2 | 0 | 0 | 2 |
| LINT-4 authority lexicon | 173 | **2** | 171 | 0 |
| LINT-5 link-every-case + wikilink resolution | 2403 | **0** | 2403 | 0 |
| LINT-6 treatment-status presence | 0 | 0 | 0 | 0 |
| LINT-7 glossary wiring (AUTO) | 0 | 0 | 0 | 0 |
| LINT-8 guardrails | 1 | 0 | 1 | 0 |
| **TOTAL** | **2839** | **2** | 2835 | 2 |

Delta vs S6 baseline: LINT-5 HIGH **2 → 0** — the 2 S6 genuine broken wikilinks
(`[[Chapman v. California]]`, `[[Fisher v. United States]]`) are **gone** (de-linked; no dangling
ref remains corpus-wide). LINT-4 HIGH now surfaces on the Case Index row + a Verifying-Good-Law
false positive (see triage). LINT-2/LINT-5 medium totals drifted up slightly (brief-first
pinpoints + page-less circuit names) — deferred/intentional, not regressions.

### HIGH-severity triage (all 2 HIGH)
1. **fixable-now (structural / N2 lexicon — NO CL):** `content/2-legal-system-research/Case Index.md:378`
   — the *United States v. August* index row carries banned `"(5th Cir. — persuasive, not binding)"`.
   **Root:** `content/cases/United States v. August.md:29` `holding:` field (frontmatter — not
   body-scanned, so lint flags the index copy). Fix = replace with a six-tier label
   (e.g. `Binding in-circuit — 5th Cir.; Persuasive (outside circuit)`) on the case page, then
   regenerate the index. Pre-authorized by S6→S9 handoff §5. No legal adjudication needed.
2. **intentional / accepted (lint false-positive):** `content/2-legal-system-research/Verifying Good Law.md:47`
   — the line *instructs readers never to use* the phrase: `…six-tier authority lexicon — never the
   vague "persuasive, not binding"`. The banned string appears **in quotes as the prohibited
   anti-pattern**; correct pedagogy. Known LINT-4 limitation (literal-string match). No fix.

**No HIGH requires CL adjudication.** LINT-1 (CL-URL identity, L3) is NOT in this roster — it runs
once on the serial CL lane at the adjudication phase (S1 L4).

## 3. Thread-P freeze (SR-5) — confirmed frozen
- `_overhaul/coverage/thread-P.md` (686 ln) — FROZEN 2026-06-30 (S5 Phase A). Per-doctrine prior
  case-by-role sets (41 SPECs) + prior split calls; 327-key catalog floor. Withheld from Thread-N.
- `_overhaul/coverage/prior-reconciliation.md` (371 ln) — 346 Thread-P cases reconciled;
  **0 regressions**; dispositions: re-verified 271 · re-surfaced 64 · annotate-cluster 3 ·
  dropped-with-prior-reason 8 (5 omissions + 3 flagged non-case artifacts).
- `_overhaul/coverage/concordance.md` (55 ln) — SR-5 Thread-N-vs-Thread-P divergences (holding/ratio,
  home re-homes N1, treatment N4, caption fixes) resolved home-by-holding / treatment-by-opinion;
  no prior conclusion silently absent/overwritten.
- **S9 inherits the S5 0-regression audit.** These are the frozen prior-conclusion reference set for
  the S9 SR-5 reconciliation (Thread-N blind re-derivation is a later phase).

## 4. Build baseline — `_run/build.log`
`npx quartz build` → **exit 0**. Quartz v4.5.2: 520 input files, 0 filtered, **1866 emitted** in ~27s.
Clean log (no broken-link warnings). **Genuine broken wikilinks: 0** (authoritative source = LINT-5
HIGH = 0; the 2403 LINT-5 mediums are page-less named-in-prose circuit cases, intentional annotate per
R6 — not build breaks). Alias redirects emit + resolve:
- `public/Community-Caretaking-and-Emergency-Aid.html` → `…/7a-pc-needed/Community-Caretaking` (canonical + meta-refresh).
- `public/Legal-Research-and-Case-Citations.html` → `…/2-legal-system-research/Reading-and-Citing-Cases`.

## 5. Mermaid D8 worklist — 42 diagrams in 42 files
One ```mermaid block per file; render+visual-inspect pass (R6/D8) is a SEPARATE later pass — NOT
rendered here. Files: 38 doctrine + 3 narrative (CREW, Three Golden Rules, The Federal Court System) +
1 research (Reading and Citing Cases). Full list mirrored in `_run/assertion-inventory.json`
(kind=`mermaid`).

## Artifacts written this phase
- `_run/assertion-inventory.json` · `_run/lint-summary.txt` · `_run/lint-stdout.json` · `_run/build.log`
- `_run/build_assertion_inventory.py` (generator)
- this ledger checkpoint

## For the orchestrator (before dimensional review + CL adjudication)
- 1 fixable-now HIGH (August holding label → six-tier + index regen) — free/structural, hold for the P3
  fix lane or clear now; the paired root is the case-page frontmatter, not just the index symptom.
- 1 accepted HIGH is a LINT-4 false-positive — recommend a lint refinement to ignore the quoted
  anti-pattern context, so the roster can gate green.
- Deferred to serial CL: LINT-1 identity, the 260 LINT-2 quote/pinpoint mediums, all 5076 inventory
  items' live verdicts, SR-5 Thread-N.
