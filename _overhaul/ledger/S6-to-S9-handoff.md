# S6 → S9 Handoff — Consolidated Gate Items for the Exhaustive Verify Pass

> **S6 cleanup/gate pass (FREE · no CourtListener calls) · branch `overhaul/build` · 2026-06-30.**
> All doctrine + narrative pages are reformatted brief-first (S6). The caretaking-split case pages have been re-homed (Job 1), the Case Index regenerated (Job 2), the lint roster run for a post-S6 baseline (Job 3), and the full build validated (Job 4). This file consolidates every flagged item the reformat agents surfaced, plus the residual lint/build findings, for **S9's exhaustive verify + serial-CL gate (R13 / SR-1 live-verify)**.
>
> **Nothing here is a defect in S6 output** — these are the deferred verification and policy decisions S9 owns. S6 stayed strictly within scope (case-page `homes`/"Appears on" + Case Index regen); no doctrine bodies or non-home frontmatter were edited.

---

## 0. S6 gate-pass baseline (the numbers S9 inherits)

**Lint roster (non-CL; LINT-1 excluded — serial-CL lane only), full `content/` corpus:**

| Lint | Check | Pre-overhaul | **Post-S6** | High | Read |
|---|---|---|---|---|---|
| LINT-2 | quote/pinpoint (L1) | 55 | **256** | **0** | ↑ medium-only: brief-first added many pinpoint-cited quotes; S4/reformat case-page items **deferred to S9** |
| LINT-3 | structure / no-SCOTUS-in-recent-dev (N5/N8) | 18 (13 high) | **2** | **0** | near-0 achieved; both **low** (§4 below) |
| LINT-4 | authority lexicon (N2) | 448 (99 high) | **172** | **1** | sweep worked: **99 → 1 high** (§5 below) |
| LINT-5 | link-every-case + wikilink resolution (N7) | 1904 | **2397** | **2** | ↑ medium = page-less named-in-prose (mostly intentional annotate, R6); **2 high = genuine broken links** (§5) |
| LINT-6 | treatment-status presence (N13) | 224 | **0** | 0 | holds at post-S4 = 0 |
| LINT-7 | glossary wiring (N11, auto half) | — | **0** | 0 | clean |
| LINT-8 | guardrails (D6) | — | **1** | 0 | 1 medium |

- **Build:** `npx quartz build` OK — 518 input files parsed, 1859 emitted, 0 filtered. Split targets emitted (`Emergency-Aid`, `Community-Caretaking`, `Securing-the-Scene`); combined-title redirect emitted via alias (owned by **Community Caretaking**).
- **Genuine broken wikilinks: 2** (both pre-existing, unrelated to the re-home) — see §5.
- **Interpretation vs task expectation:** LINT-4 high **99 → 1** and LINT-3 high **13 → 0** confirm the lexicon + structure sweeps landed. The LINT-2 / LINT-5 **totals rose** purely because brief-first authoring added pinpoint-cited quotes (LINT-2) and named circuit cases / annotate clusters (LINT-5) — these are **medium and deferred/intentional**, not regressions.
- **Ingest-gap resolution:** all 8 cases the S6 worklist flagged as **MISSING** now have `content/cases/` pages (*United States v. Garner* [10th], *United States v. Rideau*, *Graham v. Barnette*, *United States v. Walker*, *United States v. Osage*, *United States v. Carloss*, *United States v. Lundin*, *Newman v. Underhill*). S9 must **SR-1 live-verify each asserted holding** (they were ingested during S6 execution waves 3–4).

---

## 1. New framing assertions needing SR-1 live-verify (R13 serial-CL gate)

Authored teaching content (N9 field framing, completeness paragraphs, mnemonics, restatements) that **restates holdings faithfully** but is new prose not yet CL-verified. Route each through the single serial-CL lane at the publish gate.

**Cross-cutting (most doctrine pages):**
- The **burden / standard-of-review / remedy completeness paragraphs** added to most doctrine pages (who bears the burden, de novo vs clear-error vs *Ornelas* mixed review, suppression vs damages remedy). New framing on ~30+ pages.
- The **N9 field-decisive questions** leading each doctrine page — teaching restatements (SR-2 authored, SR-1 verify holdings behind them).

**Specific overlays / mnemonics / restatements:**
- **McNabb–Mallory overlay** (prompt-presentment / §3501; *McNabb* / *Mallory* / *Corley*) on **Due-Process Voluntariness** and **Miranda** pages.
- **Bandiero "hot on the tail / fresh on the trail"** mnemonic + the hot-vs-fresh-pursuit distinction on **Exigent Circumstances and Hot Pursuit**.
- **Ziglar v. Abbasi / Egbert v. Boule** Bivens-contraction restatements on **§1983 Liability and Qualified Immunity**.
- Pinpoints flagged by reformat agents for live-verify: **Wade 240**, **Barnes v. Felix** (2025), **Torres 325**, **Salinas** (v. Texas), and the other page-specific pins surfaced in the S4 worklist.
- The **Garrity** field framing on the new **Public-Employee Compelled Statements (Garrity)** page (all 6 cluster pages exist; framing restates verified holdings — standard R13 path).

**Newly-ingested case holdings (pages now exist — verify before publish):**
- *United States v. Garner* (10th, 3-part caretaking-detention test **stated up front** on Community Caretaking), *United States v. Rideau* (5th), *Graham v. Barnette* (8th, PC-of-dangerousness) — **Community Caretaking** persons-in-public strand (load-bearing).
- *United States v. Osage* (10th, general-consent-≠-destruction rule) — **Consent Searches** (anchored to *Jimeno*).
- *United States v. Carloss* (10th), *United States v. Lundin* (9th), *United States v. Walker* (11th) — **Knock and Talk** circuit split (split annotated, not resolved).
- *Newman v. Underhill* (9th 2025, 9-min-gap fresh-pursuit illustration) — **Exigent Circumstances**.

**NOT new assertions (resolved/verified — standard re-verify only):** *Pringle* horizontal-pooling prose fix (op. 131150); *Herring* Key-promotion + *Riley* Related-demotion (re-homes; holdings on existing pages); *Santana* "limited by *Lange*" consistency tag.

---

## 2. Page-less named circuit cases in Recent-developments (S9: Case-Index-row vs de-name vs accept-as-annotation)

These drive the **LINT-5 medium** bulk. Most are **intentional annotate-only** (R6 — circuit named in prose, no standalone page by design); the rest are recurring bare-name references S9 must dispose.

**Intentional annotate-clusters (R6 — keep as annotation, confirm N7 satisfied or add index rows):**
- **Cluster 1 — geofence / long-term pole-camera:** *United States v. Smith* (5th), *United States v. Chatrie* (4th), *United States v. Moore-Bush* (1st en banc), *May-Shaw* → **Third-Party Doctrine** + **Curtilage**.
- **Cluster 2a — digital over-retention / computer-search particularity:** *United States v. Ganias* (2d), *United States v. Burgess* (10th) → **Plain View**.
- **Cluster 2b — border-device forensic / RS split:** *United States v. Aigbekaen* (4th), *United States v. Kolsuz* (4th), *Alasaad v. Mayorkas* (1st) → **Border Searches**.

**Recurring page-less named cases (grounded to their host doctrine page):**
| Named case(s) | Host doctrine page |
|---|---|
| *Hunt* (9th), *Small* (4th), *Crumble* (8th) | Abandonment |
| *Massenburg*, *Chavez*, *Ramirez* (collective-knowledge sense — distinct from existing *Chavez v. Martinez* / *Groh v. Ramirez*) | Collective Knowledge and the Fellow-Officer Rule |
| *Maez*, *Berkowitz* | Arrest in the Home |
| *Camou* | Automobile Exception |
| *Cole*, *Mayville* | Traffic Stops |
| *Daniels* | Probable Cause and Reasonable Suspicion + Terry Stops |
| *Young* | (frontier annotate — confirm host page) |
| *Liddell* | Miranda and Custodial Interrogation |
| *Capers*, *Williams*, *Wint* | Miranda Waiver and Invocation |
| *Alvarez* | Brady and Giglio |
| *Jimerson* | Section 1983 Liability and Qualified Immunity |
| *Hanapel* | Entrapment |

> Policy per case: (a) **Case-Index brief-mention row** (resolves N7/LINT-5), (b) **de-name** to a generic circuit reference, or (c) **accept as annotation** (R6 — already the default for the two named clusters). Load-bearing holdings should get an index row at minimum.

---

## 3. D5 cross-page role divergences (case-page `homes[].role` vs doctrine-page placement)

S9 reconcile each so a case's tier/role reads consistently on its page and on the doctrine page that hosts it:

- **French v. Merrill / Florida v. Bostick / United States v. Drayton** — on **Knock and Talk** (case-page role vs doctrine-page Key/Related placement).
- **LaChance v. Erickson / NASA v. FLRA** — on **Public-Employee Compelled Statements (Garrity)** (Related on case pages vs body placement).
- **Bobby v. Dixon** — on **Miranda Waiver and Invocation** (Related vs body use).
- **Graham v. Connor / Tennessee v. Garner** — split treatment across **§1983 Liability** vs **Use of Force** (which is the home, which is Related).
- **People v. Hughes** — Key on **Plain View** (state case as Key — confirm tier).

**Surfaced by the S6 re-home (new — S9 reconcile):**
- **Thompson v. Louisiana / Flippo v. West Virginia** — case-page homes now point to **Securing the Scene** only (crime-scene holding; the redundant combined-caretaking home was removed to avoid a duplicate). The **Emergency Aid** doctrine body (per the split plan) lists both as Related "no crime-scene exception." Decide whether Emergency Aid should carry them as Related cross-refs (body-only, no case-page home) or drop them.
- **Combined-title alias routing:** the legacy alias `Community Caretaking and Emergency Aid` resolves to the **Community Caretaking** page, but 8 of the 9 re-homed caretaking cases (the emergency-aid share) now live on **Emergency Aid**. Any lingering prose `[[Community Caretaking and Emergency Aid]]` link lands on Community Caretaking by design — confirm that is the intended target for each legacy reference.

---

## 4. LINT-3 single-amendment frontmatter (dual-amendment doctrines)

**Actual post-S6 LINT-3 flags (both low, 0 high):**
- **Tents** (`content/3-what-is-a-search/Tents.md`) — *no controlling amendment found* in frontmatter [D10]. S9: add `amendment: IV`.
- **Due-Process Voluntariness of Confessions** (`content/9-confessions-interrogation/…`) — *multiple amendments* `['V','XIV']` [D10]. S9: declare single controlling (V, incorporated via XIV) or accept dual.

**Task-presupposed dual-amendment doctrines that did NOT trigger LINT-3** (they already declare a single controlling amendment): **Eyewitness Identification** (VI & XIV), **Brady and Giglio** (V & XIV), **§1983 Liability**. S9: confirm the single declared value is the correct controlling amendment, or intentionally accept dual and adjust the lint's D10 allow-list.

---

## 5. Residual lint/build items (S9 cleanup)

- **LINT-4 — 1 remaining high:** `content/cases/United States v. August.md` `holding` field opens *"(5th Cir. — persuasive, not binding)…"* — banned N2 phrasing; the Case Index copies it verbatim (line ~378). S9: replace with a six-tier label (e.g. **"Persuasive (outside circuit)"**), then regen the index. (Out of S6's "frontmatter homes only" scope.)
- **Genuine broken wikilinks — 2 (LINT-5 high; pre-existing, not from the re-home):**
  - `[[Chapman v. California]]` in **Arizona v. Fulminante** (harmless-error standard, 386 U.S. 18 — no page).
  - `[[Fisher v. United States]]` in **Boyd v. United States** (act-of-production, 425 U.S. 391 — no page).
  - S9: create a page, add a Case-Index brief-mention row, or de-link.
- **LINT-2 — 256 medium (0 high):** brief-first pinpoint/quote items across doctrine + case pages — the S4 case-page quote/pinpoint backlog **deferred to S9's exhaustive quote/pin verify**.
- **LINT-8 — 1 medium** guardrail (D6) — review at gate.

---

## Appendix — Job 1 re-home record (audit trail)

Split of the consumed parent *Community Caretaking and Emergency Aid* (alias retained on **Community Caretaking**). Each case kept its existing role; only the `homes[].page` + matching "Appears on" line changed.

| Case | New home | Role (unchanged) |
|---|---|---|
| Brigham City v. Stuart | Emergency Aid | Key — Anchor |
| Michigan v. Fisher | Emergency Aid | Key — Progeny / Refinement |
| Mincey v. Arizona | Emergency Aid | Key — Progeny / Refinement |
| Ryburn v. Huff | Emergency Aid | Key — Progeny / Refinement |
| Case v. Montana | Emergency Aid | Key — Progeny / Refinement |
| Caniglia v. Strom | Emergency Aid | Key — Progeny / Refinement |
| Michigan v. Tyler | Emergency Aid | Key — Progeny / Refinement (fire-scene) |
| Michigan v. Clifford | Emergency Aid | Key — Limiting (fire-scene) |
| Cady v. Dombrowski | Community Caretaking | Key — Anchor (vehicles) |
| Thompson v. Louisiana | Securing the Scene *(already homed; redundant combined home removed)* | Related (cross-doctrine) |
| Flippo v. West Virginia | Securing the Scene *(already homed; redundant combined home removed)* | Related (cross-doctrine) |

**Assignment counts:** Emergency Aid ← 8 · Community Caretaking ← 1 · Securing the Scene ← 2 (dedup). **11 case pages touched; 0 remaining `[[Community Caretaking and Emergency Aid]]` in any case-page `homes`/"Appears on".**
