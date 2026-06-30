# S5 Phase A — Partition-Completeness Check + Cross-Phase Flags

> Proves the R3 four-way partition is **complete and disjoint**: every candidate resolves to exactly one of
> `already-covered ⊎ confirmed-miss ⊎ excluded ⊎ borderline`. FREE pass (no CourtListener calls — identity is
> confirmed at Phase-B ingest, R3.4/R9). Written 2026-06-30 on branch `overhaul/build`.

## 1. Candidate pool (R3.1 — the union, R5)

| Source | What was harvested | Result |
|---|---|---|
| **Book roster (spine)** | Full I–XIII TOC, 14 pages, OCR-extracted (the PDF is a scanned image — **no text layer**; read visually) | **394 TOC case-entries** (incl. cross-listed cases like Chadwick, Schmerber, Abel) → **197 distinct not-covered** |
| **Named-in-prose** | Regex `X v. Y` + `[[wikilink]]`/`related:` scan over **all** `content/**/*.md` (doctrine + 262 case pages) | 220 raw uncovered names triaged (foundational/SCOTUS → misses; circuit/state illustrative → omissions B) |
| **Thread-P corpus** | 327-key `verified-cases-catalog.json` + 41 prior per-page specs + COVERAGE-MATRIX | Frozen to `thread-P.md`; 89 catalog keys not in the covered set triaged (substantive → misses; pinpoint/caption artifacts → covered-alias) |
| **Seed (S4 forward-refs)** | The 37 named-in-prose / class-2/3 forward-refs from `ORCHESTRATION.md` | All 37 placed (35 → confirmed-miss; Fisher → omission OPTIONAL act-of-production; all others miss) |

## 2. The four-way partition (R3.3)

| Disposition | Count | File |
|---|---|---|
| **already-covered** | 262 case pages (+ 3 flagged page-less captions correctly excluded) | `content/cases/*` + `Case Index.md` |
| **confirmed-miss** (→ Phase-B ingest) | **185** (incl. the 6-case Garrity CORE cluster) | `missed-cases.md` |
| **excluded** (→ omissions) | **105** = 38 scoped-out/OPTIONAL/out-of-remit/UNVERIFIABLE/duplicate (A) + 67 persuasive-only illustrative (B) | `omissions.md` |
| **borderline** (→ user sign-off) | **11** (9 individual cases + 2 frontier clusters) | `borderline.md` |

## 3. Completeness + disjointness (the proof)

- **Book roster:** all **197 not-covered** book cases are placed in exactly one partition (verified by normalized-caption reconciliation; the single "unmatched" — *Pembaur v. Cincinnati* — is placed under its full caption *Pembaur v. City of Cincinnati*). **0 unplaced, 0 overlaps.**
- **Seed-37:** all 37 reconciled (covered or placed). **0 unresolved.**
- **Catalog-327:** every key is covered, placed, or a confirmed covered-alias/pinpoint artifact (e.g. `Lange 594 U.S. at 297`, `Olson 495 U.S. at 96`, `Brower v. County of Inyo` = `Brower v. Inyo County`). **0 silent drops.**
- **No false-merge:** holding-identity matching kept name-collisions distinct — *Henry v. United States* ≠ *United States v. Henry*; *Mathis v. United States* ≠ *United States v. Mathis*; *Davis v. United States* 2011 ≠ 1994; the *Harris* quartet and *Smith* cluster split out (R4 class 5; see `missed-cases.md`).
- **Identity NOT yet CL-confirmed** (Phase A is FREE): every confirmed-miss is `Status: pending`; CL cluster→opinion identity is resolved at Phase-B ingest before any page is authored (R3.4/R7.2/R9). Two flagged for special identity care at ingest: **Case v. Montana** (possible 2025) and **NASA v. FLRA** (confirm exact holding).

**Partition identity:** candidate-pool = already-covered (262) ⊎ confirmed-miss (185) ⊎ excluded (105) ⊎ borderline (11). No gaps, no overlaps.

## 4. R12 / SR-5 status (Thread-P frozen; Thread-N NOT run here)

- **`thread-P.md` is FROZEN** (41 doctrines: prior case-set-by-role + split calls; + 327-case catalog floor). This is the **no-regression floor + reconciliation reference**, to be **WITHHELD** from the later blind Thread-N discovery.
- **Not done in Phase A (by design):** `concordance.md` (Thread-N vs Thread-P reconciliation) and `prior-reconciliation.md` (no-regression ledger). These require the **blind Thread-N pass** (separate sub-agent, P withheld) — a Phase-B/EXECUTE orchestration step, not this freeze.
- **No-regression sanity:** the 3 page-less flagged captions (the `Cruz/West/Jackson` trio, stolen-vehicle `White`, `self-help doctrine`) are carried as **flagged omissions** (R9/R10), not silently re-lost. Prior SR-5 finding **State v. Mitcham** (prior=independent-source vs live=inevitable-discovery) is logged in `thread-P.md`/ORCHESTRATION for the Phase-B concordance gate.

## 5. Cross-phase flags

- **R11 / Garrity → S6:** the 6-case Garrity cluster (Garrity, Gardner, Kalkines, Lefkowitz, LaChance, NASA v. FLRA) is on `missed-cases.md` as **CORE** ingests, provisional home = **NEW doctrine page "Public-Employee Compelled Statements (Garrity)"** under category #9. **S6 must author that doctrine page.** S2 §2.0 already carries the OPTIONAL→CORE amendment (D3-S2) — no S2 edit needed.
- **N1 re-homes → S6:** class-4 surfaced as re-home decisions on already-covered pages (Anchondo→SITA, Braxton→inevitable-discovery, Morton→good-faith) — S6 reweaves, no new ingest.
- **S4 · R5 collisions:** the 10 class-5 collision pairs feed the year-suffix disambiguation list (`missed-cases.md` §class-5).
- **Phase-B (R6/R7) deferred work:** the class-6 date-bounded CL sweep and class-7 frontier pass (web-first→serial CL), plus all ingest live-verify, run in Phase B. Borderline frontier clusters await user sign-off before any page.
- **Decks (R8):** untouched — zero deck artifacts produced.
