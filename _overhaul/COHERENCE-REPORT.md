# Cross-Spec Coherence Verification — Report

**Date:** 2026-06-30 · **Scope:** all nine specs `S1…S9` read in conjunction + both wrappers + the
context pack + `docs/RUNBOOK.md` + `docs/FINAL-QA-SPEC.md`. **Mode:** spec-level reasoning pass — no
content authored, no CL, no builds. **Method:** the project's hybrid — self-interview every coherence
question; `AskUserQuestion` only for the genuinely user-owned conflicts.

## Verdict: **GO (execution-ready) — after the amendments below, all applied.**

The spec set was already **substantially coherent**: the L7/L8/SR-5 mid-kit amendments propagated
cleanly; the 6-tier lexicon, the 8-role set, and the D1–D14 dimensions are referenced consistently;
the dependency chain is sound. The pass found **1 high-severity gap, 5 medium, and several low** — all
resolved (applied additively, each recorded in the relevant spec's Appendix A / EXECUTE), plus **3
user-owned decisions** taken via interview. With those in, the specs work together as one executable
contract.

---

## User-owned decisions taken (recorded in the specs)

| # | Decision | Choice | Where recorded |
|---|---|---|---|
| **U5-S9** | Flashcards in the overhaul | **None — frozen S1–S9; rebuilt in a SEPARATE later run** after the full content corpus is final | S9·R11 + Appendix A·U5-S9; propagated to S4·R11, S5·R8, S6·R12, S7·§2.2, S8·§2 |
| **U6-S9** | Source of truth + publish | **`content/` becomes canonical; retire the vault→content sync** (publish = commit/push `content/` → Vercel; never `redeploy.sh`) | S9·R14 + §5-P6 + Appendix A·U6-S9; EXECUTE updated |
| **D3-S2** | Garrity / gov-employee 5A scope | **CORE (amends S2 §2.0 OPTIONAL tag now)** | S2·§2.0 ⚠ amendment + Appendix A·D3-S2 |

---

## Findings & resolutions

### HIGH

**H1 — Edit target vs. source of truth (data-loss hazard). [RESOLVED · U6-S9]**
Every overhaul spec edits `content/` (the repo — S3 `git mv`s files, S4 writes `content/cases/`, S6
reformats pages), but `docs/RUNBOOK.md §4` makes `content/` a **copy of the iCloud vault**, synced
**vault→content** by `redeploy.sh`. The original S9 publish ("sync vault→content (redeploy.sh)") —
inherited from FINAL-QA — would have **overwritten the entire rebuilt `content/` with the stale
vault**, and the same clobber would hit any build-validation that ran `redeploy.sh`.
*Resolution (user choice U6-S9 = option B):* **`content/` is canonical**; the **vault→content sync is
retired**. Publish = validate with a direct `npx quartz build`, then commit/push `content/` → Vercel.
S9·R14 / §5-P6 / §7 and the EXECUTE wrapper updated to forbid `redeploy.sh`. *Consequence flagged:* the
`/cssi-ingest` pipeline and the Tailscale `redeploy.sh` server now assume the old vault→content model
and will need reworking — **post-overhaul maintenance, not part of this build** (logged in U6-S9).

### MEDIUM

**M1 — S7 ↔ S8 mutual term-anchor dependency vs. linear order. [RESOLVED]**
S7 wires doctrine-prose citation-mechanics terms to **S8's** `### Term` anchors (S8·R4), and S8 routes
its page-less terms to **S7's** glossary anchors (S8·R10) — a genuine circular dependency that the
linear EXECUTE order (S7 then S8) doesn't capture.
*Resolution:* EXECUTE now sequences S7+S8 as a coordinated pair — **anchorize first (S8 citation
anchors + S7 glossary), then run the term-wiring sweep** — with S9·R9's term re-audit as a back-fill
safety net. (No spec rule changed; the specs already say "route, don't duplicate"; only the execution
sequencing needed making explicit.)

**M2 — Deck-id supersession left stale "preserve deck ids" language. [RESOLVED]**
S4·R11 (with U3-S4) dropped the deck-id-preserving caretaking migration and superseded the FSRS/deck-id
half of D-6 — but S2·§3.4, S2·§6.2, S3·R9, and the EXECUTE "preserve flashcard ids on every rename"
guardrail still asserted it (read alone, they'd direct an executor to preserve deck ids).
*Resolution:* additive **superseded-by-S4·R11 / U5-S9** forward-pointers added to S2·§3.4 R4, S2·§6.2
(SPLIT row), and S3·R9; the EXECUTE guardrail corrected to "no deck work — decks frozen."

**M3 — Garrity OPTIONAL (S2) vs. CORE (S5/S6). [RESOLVED · D3-S2]**
S2·§2.0 still tagged "government-employee Miranda/Garrity" OPTIONAL, but S5·U2-S5/R11 promoted the
cluster to CORE (case pages + a new doctrine page) and only *recommended* a one-line S2 cross-ref "at
execution," leaving a live contradiction in the scope contract S5 reads.
*Resolution (user choice):* S2·§2.0 amended now with a ⚠ note marking the Garrity cluster **CORE**
(homed under #9; case pages + doctrine page per S5·R11 / S6·R9); the rest of Book-IX 5A immunity stays
OPTIONAL. Appendix A·D3-S2 added.

**M4 — "Autonomous" run has mandatory human pauses not enumerated. [RESOLVED]**
S5·R2's **borderline sign-off** is a mid-run human gate (cases parked, surfaced before ingest/drop),
and there's the **final publish go-ahead** — neither was called out in EXECUTE's "full autonomous"
framing.
*Resolution:* EXECUTE now lists the **mandatory human pauses**: (a) S5 borderline sign-off (park +
surface; proceed with clear-ingest cases, apply dispositions in a short follow-up); (b) the publish
go-ahead. (The deck-purge pause is gone — decks are now out of scope, U5-S9.)

**M5 — Final page inventory isn't pinned in any one spec. [RESOLVED]**
The S2·§6.1 tree predates the **S8 three-page split** (Legal Research → Reading & Citing Cases / Legal
Research Tools / Verifying Good Law) and the **new Garrity doctrine page**, and the page count drifts
(43 in the context pack vs. 46 in S2).
*Resolution:* a **final-page-inventory note** added to S2·§6.1 — the S8 three pages home under #2, the
Garrity page under #9, and the canonical post-overhaul list is **assembled at execution** by enumerating
`content/*.md` live (S2·§8 step 1) + the splits + every `content/cases/*` page. No single spec holds the
final count; the executor assembles it.

### LOW (resolved or noted)

- **L1 — TreatmentBadge values drifted from the data model. [RESOLVED]** S3·R4 #1 listed badge values
  "good-law / limited / narrowed / overruled / unpublished-non-precedential," mixing treatment statuses
  with an authority-weight tier and a non-canonical "narrowed." Aligned to S1 §3.D: the badge reads the
  canonical `treatment.status ∈ {good | criticized | limited | abrogated | overruled}`, with the 6-tier
  authority-weight shown as a **separate** orthogonal label.
- **L2 — Page-count drift (43 vs 46).** Folded into M5 (runtime-determined).
- **L3 — `_review-needed/` subfoldering** is inconsistent across specs (`cases/`, `coverage/`, flat) —
  harmless (escalation buckets); noted, not edited.
- **L4 — Cumulative CL load.** SR-1 (no tiering) deliberately re-verifies the same cases at S4
  generation **and** again at S9; combined with S5 ingest + S6 new assertions, the single serial lane is
  the global bottleneck across the whole run. Intentional (the chosen rigor); S9·§9 already flags the CL
  budget + STOP-on-old-tier pacing. The run is multi-session/resumable by design.
- **L5 — CREW mnemonic expansion** (C·RE·W) is an instructor-preference call already flagged in S6·§9
  for execution. Noted.
- **L6 — S8 IA placement circular-defer to S2.** Folded into M5 (S8's 3 pages home under #2).
- **L7 — S9's "Thread P" vs S5's prior "Thread P".** Distinct reference points (S9's Thread P = the
  whole post-build state, which already incorporated S5's reconciliation; S9's Thread N re-derives the
  finished product blind). S9·R5 is clear enough in context; noted, not edited.

---

## Coherence dimensions audited

| Dimension | Result |
|---|---|
| **1. Dependency & ordering** | PASS after M1 (S7↔S8 interleave) + M4 (pauses). Dep graph sound; spec `depends-on` are *authoring* deps — S8's *execution* deps (S2/S3/S4/S6 link targets) are satisfied by EXECUTE's numeric order (S8 at step 8, after S6). |
| **2. Interface / handoff** | PASS. Every producer→consumer handoff is concretely specified (S2 tree/roles → S3/S4/S5/S6; S4 frontmatter/anchors/data-convention → S5/S6/S3/S7/S8; S5 rows/Garrity-flag/ledgers → S6/S9; S6 text → S7; S7 routed terms → S8; all → S9). |
| **3. Conflict / supersession** | PASS after H1, M2, M3. L7/L8/SR-5 propagation verified consistent; the Warrant-Requirement-split deferral chain (S2 WATCH → S6 re-eval → S9 verify) is consistent. |
| **4. Terminology / ID consistency** | PASS after L1. 6-tier lexicon, 8-role set, D1–D14, treatment-status enum referenced identically; L#/N#/SR#/D#/R# resolve; lessons count (21 L/N + SR-1…SR-5) consistent. |
| **5. Per-spec clarifications / missing context** | PASS after H1, H2 (EXECUTE now loads RUNBOOK §3/§3a + FINAL-QA Key-paths for the CL tier protocol, cluster-id gotcha, EPERM, and the Mermaid render command — the mechanics the specs reference but don't restate). |
| **6. Coverage gaps** | PASS. Each deferral is *conscious*: Quartz 4→5 (S3·§9), continuous-glossary cadence (S7·§9/S9·§9), OPTIONAL promotion-on-request (S2), the separate flashcard run (U5-S9), the `_review-needed/` human triage (the user, post-delivery), the cssi-ingest/redeploy rework (U6-S9 consequence). |

**H2 — EXECUTE load-order omitted the operational mechanics. [RESOLVED]** The specs reference "RUNBOOK
§3," "FINAL-QA Key-paths" (Mermaid render), and the EPERM workaround, but EXECUTE only loaded the
context pack + specs. EXECUTE now loads `docs/RUNBOOK.md` + `docs/FINAL-QA-SPEC.md` Key-paths.

---

## Residual open items (flagged for later — not blocking EXECUTE)

1. **Separate flashcard rebuild run** — still owed after the overhaul + full content corpus are final.
   Decks derive FROM the finalized verified pages (L1); D12 verified there; the FSRS-preservation option
   is decided in that run before its irreversible purge. A dedicated wrapper should be authored when
   ready. `FINAL-S9-REPORT.md` must surface this as the required follow-on.
2. **cssi-ingest + Tailscale `redeploy.sh` rework** — both assume the retired vault→content model now
   that `content/` is canonical (U6-S9). Post-overhaul maintenance.
3. **Quartz 4.5.2 → 5 upgrade** — deferred non-blocking (S3·§9), re-evaluate after S9.
4. **Continuous-glossary audit cadence** — S9 runs it once at the gate; the ongoing cadence is a
   maintenance concern (S7·§9 / S9·§9).

---

## Files changed (all additive; specs remain `APPROVED`)

- **S9** — removed the deck-rebuild phase (P5) + the D12 release-gate item + deck artifacts; R11
  rewritten to a deck **non-breakage** check; R14/§5-P6/§7/§2 publish model fixed to `content/`-canonical
  (no `redeploy.sh`); R7 validation reference fixed; Appendix A: **U5-S9** + **U6-S9** added, SI-1/SI-4
  updated.
- **S4** — R11 reframed: deck rebuild is a **separate later run** (U5-S9), not EXECUTE/S9; `last-updated` 06-30.
- **S2** — §2.0 ⚠ **Garrity CORE** amendment; §3.4/§6.2 deck-id supersession forward-pointers;
  final-page-inventory note; Appendix A **D3-S2**; `last-updated` 06-30.
- **S3** — R4 #1 TreatmentBadge values aligned to S1 §3.D; R9 deck-id supersession pointer; `last-updated` 06-30.
- **S5 / S6 / S7 / S8** — deck pointers reframed to "separate later run" (light edits).
- **EXECUTE.wrapper.md** — load order (+RUNBOOK §3/§3a, +FINAL-QA Key-paths); S2 deck-id guardrail
  removed; S7+S8 anchorize-then-wire coordination; flashcards-frozen + `content/`-canonical publish;
  mandatory human pauses; numbering fix; **new mandatory "Orchestration model" section** (thin
  orchestrator holds only ledger/specs/statuses; all substantive work in fresh sub-agents, one unit =
  one job; small on-disk hand-offs; serial-CL concurrency-1; find→adjudicate→fix role separation;
  checkpoint-after-every-sub-phase resumability; loop cap 3 → escalate).

---

## Handoff

All specs are coherent and execution-ready. The next step is the **full autonomous build** via
`_overhaul/wrappers/EXECUTE.wrapper.md` (now corrected). The build is content-only; the **flashcard
rebuild is a deliberate separate run afterward**.
