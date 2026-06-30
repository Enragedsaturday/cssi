# CSSI Overhaul — Orchestration Ledger (resumable)

Thin-orchestrator state for the autonomous build (`_overhaul/wrappers/EXECUTE.wrapper.md`).
Governed by `docs/STANDARDS.md` (S1, SR-3). **Resume from this file, not from scratch.**

- **Branch:** `overhaul/build` (off `main` @ `abefdf3`; baseline commit carries prior FINAL-QA state + specs).
- **Canonical source:** `content/` (U6-S9). **Never run `redeploy.sh`** (retired vault→content sync).
- **CL discipline:** single serial lane (L4), concurrency-1; tier probed before CL work; STOP on old 5/min tier (RUNBOOK §3). Log: `_overhaul/ledger/cl-calls.log`.
- **Orchestration:** thin main thread holds ledger/specs/statuses only; all substantive work in fresh sub-agents; small on-disk hand-offs; find→adjudicate→fix role-separated; loop cap 3 → `_review-needed/`.
- **Decks:** frozen the whole overhaul (U5-S9). No `merge.py`/`make_apkg.py`. Page-derived rebuild is a SEPARATE later run.
- **Mandatory human pauses:** (a) S5 borderline sign-off; (b) final publish go-ahead (before push to `main`/Vercel prod).

## Phase status

| # | Phase | Status | Notes |
|---|---|---|---|
| 0 | Setup (branch, scaffold, ledger) | ✅ done | branch + dirs + task list created |
| — | CL tier probe | ✅ done | **TIER=NEW (≥20/min), MCP auth OK**, cluster→opinion gotcha validated → PROCEED |
| S1 | STANDARDS.md + LINT roster | ✅ done | committed ce6b5cd |
| S2 | IA folder restructure + aliases | ✅ done | committed e3f37ca; 44 moves, 0 broken links |
| S3 | Platform/nav/UX + components | ✅ done | nav b713b2b + components 09cdca8; build ok. S9 flags: CaseBrowser live render, data-island scaling, slug-casing deep-link check |
| S4 | Case pages (BIRAC) + index | ⏳ in progress | 262 pages, serial-CL batches of ~15; batch tracker below |
| S5 | Missed-case ingest + concordance | ⏳ blocked(S4) | borderline → USER PAUSE |
| S6 | Doctrine/narrative reformat | ⏳ blocked(S5) | caretaking split, Garrity page |
| S7+S8 | Research pages + glossary wiring | ⏳ blocked(S6) | anchorize-then-wire |
| S9 | Verification + release gate | ⏳ blocked(S7+S8) | STOP before publish |

## S4 batch tracker (262 pages, idx order, ~15/batch → ~18 batches; serial CL ONE at a time)
- Resumable: each batch updates `S4-worklist.json` status (pending→authored|escalated); skip already-authored. Commit after each batch.
- batch 1: idx 1–15 — ✅ committed 133fcab (15 pages, 0 escalations, ~50 CL calls, no throttle; Gant spot-check = instructor-grade)
- batch 2: idx 16–33 — ⏳ running (18 cases)
- pinpoint-pagination caveats to revisit at gate/S9: Gant star-pag; Bailey/Berghuis slip-op; Benn paragraph-nums (idx 8/12/13/14)

## Artifact locations
- Orchestration: `_overhaul/ledger/` (this file, `cl-calls.log`).
- S5 coverage: `_overhaul/coverage/` (missed-cases, omissions, borderline, thread-P, concordance, prior-reconciliation).
- S9: `_run/` (S9-LEDGER.json, assertion-inventory.json, thread-P.json, s9-concordance.json, findings/adjudications, FINAL-S9-REPORT.md).
- Escalations: `_review-needed/{cases,coverage}/<slug>.md`.
- Lint scripts: `scripts/lint/`.

## CL reference (validated by probe 2026-06-30)
- Tier NEW (≥20/min); pace <20/min (~1 call/3.2s); cached opinion reads are free.
- Carpenter v. United States (2018): cluster 4510032, lead `opinion_id` 4287285, url `https://www.courtlistener.com/opinion/4510032/carpenter-v-united-states/`.

## S4 facts (from Case Index)
- Case Index: 267 data rows; **261 carry a CL opinion URL → 261 case pages to generate** (S4 target). ~6 flagged captions (no CL URL) get NO page (R1: flagged exception rows).
- Columns: Case | Holding | Good law | Home page(s) | CourtListener. Good-law blank = "good" convention (N13 will fill explicit status).
- Worklist: `_overhaul/ledger/S4-worklist.json` (bootstrap). Collisions: `_overhaul/ledger/S4-collisions.md`.

## Decision log (consequential calls, with rationale)
- **2026-06-30 · S4 ∥ S3 parallelization.** S4 generation is file-disjoint from all of S3 (S4 writes content/cases + Case Index + scripts and is the only CL user; S3 writes quartz/ + category stubs). So S4 runs in PARALLEL with S3-components — the serial-CL lane is internal to S4; S3 is free/no-CL. The S4-blockedBy-S3 task dep is therefore advisory only; S4 needs only content/cases/ (created in S2) + the probe (done).
- **2026-06-30 · S4 batch pipeline.** 261 cases generated via SEQUENTIAL serial-CL batch sub-agents (~20/batch, one CL lane at a time — never parallel CL, L4). Each batch: verify identity (cluster→opinion L3) + good-law (analyze_citations batched) + verbatim pinpoint quotes (search_document) → author BIRAC page → checkpoint S4-worklist.json status. Resumable. find→adjudicate→fix gate (review free/parallel) runs after generation; needs_cl adjudication back on the serial lane.
- **2026-06-30 · Baseline carry-forward.** Prior FINAL-QA working tree (modified Curtilage/Miranda-Waiver/Special-Needs/index + new Recalibration & Third-Party pages) carried onto the branch as the canonical `content/` start state (U6-S9). Dogfood/backup junk (`idb-dogfood/`, `app.js.bak`) gitignored.
- **2026-06-30 · S2/S3 split.** Per EXECUTE order: S2 = physical folder restructure (git mv, stems stable, aliases); S3 = Explorer/SCSS/components. Caretaking split + Garrity page CONTENT deferred to S6 (content authoring); S2 only moves the existing combined caretaking file into 7a and S6 splits it.
