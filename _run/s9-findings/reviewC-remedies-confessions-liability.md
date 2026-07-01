# S9 Adversarial Dimensional Review — Cluster C (Remedies · Confessions · Liability)

**Reviewer lane:** adversarial S9 dimensional reviewer — **D2 ∧ D4 ∧ D9 ∧ D10 ∧ D14 + SR-2 instructor-grade composite gate**.
**Mode:** FREE (no CL calls), FINDINGS-ONLY (L5 — no page edits). `needs_cl` flagged for any doubted/untraceable asserted holding/quote.
**Date:** 2026-06-30 · branch `overhaul/build` · governed by `docs/STANDARDS.md` (SR-2 = D2 ∧ D4 ∧ D9 ∧ D14, blocking).

Pages reviewed (12 doctrine pages):
- `content/8-exclusionary-rule-remedies/`: The Exclusionary Rule · Standing to Challenge a Search
- `content/9-confessions-interrogation/`: Due-Process Voluntariness of Confessions · Miranda and Custodial Interrogation · Miranda Waiver and Invocation · Sixth Amendment Right to Counsel · Eyewitness Identification · Public-Employee Compelled Statements (Garrity)
- `content/10-use-of-force-liability/`: Use of Force · Section 1983 Liability and Qualified Immunity · Brady and Giglio
- `content/11-adjacent-doctrines/Entrapment`

---

## 0. Verdict summary — per-page SR-2 (D2 ∧ D4 ∧ D9 ∧ D14) + finding counts

| Page | SR-2 | HIGH | MED | LOW/needs_cl |
|---|---|---|---|---|
| The Exclusionary Rule | **PASS** | 1 | 0 | 0 |
| Standing to Challenge a Search | **PASS** | 1 | 1 | 0 |
| Due-Process Voluntariness of Confessions | **FAIL** | 1 | 1 | 0 |
| Miranda and Custodial Interrogation | **PASS** | 0 | 0 | 0 |
| Miranda Waiver and Invocation | **PASS** | 0 | 1 | 0 |
| Sixth Amendment Right to Counsel | **FAIL** | 1 | 1 | 0 |
| Eyewitness Identification | **PASS** | 0 | 0 | 1 |
| Public-Employee Compelled Statements (Garrity) | **PASS** | 0 | 0 | 0 |
| Use of Force | **PASS** | 0 | 1 | 1 |
| Section 1983 Liability and Qualified Immunity | **PASS** | 0 | 0 | 1 |
| Brady and Giglio | **PASS** | 0 | 0 | 1 |
| Entrapment | **PASS** | 0 | 0 | 1 |

**Result: 10 PASS · 2 FAIL.** The two FAILs (Due-Process, Sixth Amendment) fail on a **blocking D10 structural defect** (stray tool-artifact tags rendering as visible text at end of page) compounded by a **self-declared "SR-2 instructor sign-off pending"** marker — the composite teaching content itself is substantively excellent on all four SR-2 dimensions, but the page as it stands cannot ship.

**Cluster-wide guardrail/lexicon sweep (D6):** CLEAN. Zero banned "persuasive, not binding"; 6-tier lexicon used throughout; circuits named; zero inline `## Flashcards`; no apocryphal-trio issues observed.

---

## 1. HIGH-severity findings (page · problem · fix · needs_cl)

### F-DP-1 — Due-Process Voluntariness · **D10 structural (blocking)**
- **Problem:** Stray generation-artifact tags `</content>` (line 119) and `</invoke>` (line 120) leaked into the file body as the final two content lines. These render as literal visible text at the bottom of the published page — an instructor-grade page shipping raw tool-call XML.
- **Fix:** Delete the two trailing lines `</content>` and `</invoke>`. The file should end at the last Sources bullet (`- [United States v. Young ...]`).
- **needs_cl:** No (pure structural artifact).

### F-6A-1 — Sixth Amendment Right to Counsel · **D10 structural (blocking)**
- **Problem:** Identical artifact — stray `</content>` (line 136) and `</invoke>` (line 137) as the final two lines, rendering as visible text.
- **Fix:** Delete the two trailing lines. File should end at the last Sources bullet (`- [Montejo v. Louisiana ...] — pinpoint: 797`).
- **needs_cl:** No.

### F-EXCL-1 — The Exclusionary Rule · **D2 framing / D3 currency (already escalated)**
- **Problem:** The recent-developments apparatus (brief L124; bullets L129–130) frames the geofence / Google-Location-History antecedent-search question as an **open circuit split "now before the Supreme Court" (Chatrie, No. 25-112)**. That question was **decided by SCOTUS on 2026-06-29** — *Chatrie v. United States*, 609 U.S. ___ (2026) holds acquiring geofence Location History **is** a Fourth Amendment search (geofence warrants **not** categorically unconstitutional; PC/particularity remanded). Presenting decided current law as "pending" is a faithful-framing defect on an instructor-grade page.
- **Mitigation:** This is **already logged** as a proper escalation in `_review-needed/chatrie-scotus-2026-correction.md` (a single-finding correction + ingest order) — it is a **logged escalation, not a silent gap**, so it does not by itself sink the release gate under R13/§7.
- **Fix:** Apply the reframe in that correction file (Action B, item 6): search-question **RESOLVED (Chatrie 2026)**; re-tier the controlling authority to Binding — SCOTUS; live `⚖` split becomes PC/particularity on remand. Confirm whether Chatrie touched *Leon* good-faith on remand.
- **needs_cl:** **Yes** — slip-op-sourced; the correction file warns CL has **no clean SCOTUS Chatrie object** and opinion `10881683` is corrupted (resolves to the wrong case). Do not trust CL for Chatrie until a clean `scotus / 25-112` cluster appears.

### F-STAND-1 — Standing to Challenge a Search · **D2 framing / D3 currency (already escalated)**
- **Problem:** Same stale Chatrie framing in Recent developments (intro L76; bullets L80–81) — geofence search question presented as an unresolved 4th-vs-5th-Cir. split. Superseded by *Chatrie* (2026).
- **Mitigation:** Covered by the same logged escalation (`_review-needed/chatrie-scotus-2026-correction.md`, Action B item 5). Not a silent gap.
- **Fix:** Reframe per the correction file; note the geofence cases here are framed on the **search-definition threshold** (not standing holdings), so the reframe is "the threshold search question is now resolved by *Chatrie*."
- **needs_cl:** **Yes** (same CL caveat as F-EXCL-1).

---

## 2. Medium-severity findings

### F-STAND-2 — Standing · **D3/needs_cl (recent circuit anchor)**
- *United States v. Mendoza* (3d Cir. **2026**), hotel-checkout REP, is asserted as a precedential circuit holding (Recent developments L78). A 2026 opinion authored days/weeks before review — the holding, precedential status, and CL object (`10771114`) should be live-verified.
- **Fix:** none to content framing (role-labeled correctly as doctrine-extension, circuit named, no-SCOTUS clean). **needs_cl: Yes** (verify holding + CL identity).

### F-DP-2 — Due-Process Voluntariness · **D9/D14 process (SR-2 sign-off pending)**
- The page carries an explicit authoring comment (L18–23) declaring the N9 field-decisive framing and the synthesized 3-element (coercion · causation · will-overborne) teaching are **"AUTHORED teaching … Instructor-review (SR-2) pending"**, and that the McNabb-Mallory prompt-presentment overlay is **newly-added** cross-material. The composite content is substantively sound (state-action per *Connelly*, coercion-not-reliability per *Rogers*, both correctly restated), but the page self-declares the blocking SR-2 instructor sign-off has **not** occurred.
- **Fix:** Instructor sign-off on the authored synthesis + confirm the McNabb-Mallory overlay is desired on this page (it is correctly framed as a **federal-court evidentiary rule, NOT a constitutional command** — good). Combined with F-DP-1, this page cannot ship as-is → SR-2 FAIL.

### F-6A-2 — Sixth Amendment · **D9/D14 process (SR-2 sign-off pending)**
- Same self-declared marker (L18–24): "AUTHORED teaching … Instructor-review (SR-2) pending." Combined with the F-6A-1 artifact → SR-2 FAIL. (Content note: the N5 fix here is executed **correctly** — see §4.)

### F-MW-1 — Miranda Waiver and Invocation · **D10 structural**
- Orphan triple-backtick code fence (` ``` `) at EOF (line 158), after the last Sources bullet. An unterminated fence with no opener — renders as an empty/broken code block at the page foot.
- **Fix:** Delete the trailing ` ``` ` line. **needs_cl:** No. (Content composite fully passes SR-2; this is a lint fix, not a gate failure.)

### F-UOF-1 — Use of Force · **D10 structural**
- The page is **missing its `# Use of Force` H1 heading** — it jumps straight from frontmatter close to `## The Brief` (line 14). It is the **only** doctrine page in the cluster without an H1 (every sibling has `# Title` before `## The Brief`, matching the S6 brief-first template). Cosmetically Quartz may render the title from frontmatter, but this breaks template/anchor consistency across the corpus.
- **Fix:** Insert `# Use of Force` between the frontmatter and `## The Brief`. **needs_cl:** No.

---

## 3. Low-severity / needs_cl-only findings

- **F-EW-1 — Eyewitness Identification (D4 minor / needs_cl):** the appellate standard-of-review sentence (L44) carries a self-flag `[FLAG — completeness add: the appellate standard-of-review line is not pinpointed to an ingested case page; route to the R13 serial-CL gate]`, and the Recent-developments frontiers (L75) are explicitly deferred to serial-CL. Both are **logged** completeness flags, not silent gaps. **needs_cl: Yes** (pinpoint a source for the clear-error/de-novo split on ID rulings). Core two-track brief (DP suggestiveness/reliability + 6A lineup) is complete and excellent.
- **F-UOF-2 — Use of Force (needs_cl):** *Barnes v. Felix*, 605 U.S. 73 (**2025**) is a very recent SCOTUS anchor (correctly homed to Key — see §4). Flag the 2025 cite + "no time limit / moment-of-threat rejected, vacated & remanded, unanimous" holding for live CL re-verify. **needs_cl: Yes.**
- **F-1983-1 — Section 1983 (needs_cl, self-flagged):** four asserted holdings carry self-flags or are very recent and page-less — *Zorn v. Linton*, 606 U.S. ___ (2026) (**"restated from the prior verified page, not independently CL-re-verified here"**); *Ziglar v. Abbasi* (**"new assertion, not yet CL-re-verified"**); *Martin v. United States*, 605 U.S. 371 (2025) (FTCA §2680(h) proviso holding); *Jimerson v. Lewis* (5th Cir. 2024) (wrong-house-raid QI split, cert. denied). **needs_cl: Yes** for each. Core §1983/Monell/QI teaching is complete and correctly framed (elements · Monell 3 routes · QI two-step · clearly-established at high specificity · obvious-case route · Bivens · Heck bar).
- **F-BG-1 — Brady and Giglio (needs_cl):** *Glossip v. Oklahoma*, 604 U.S. 226 (**2025**) — the *Napue* application ordering a new trial — flag the 2025 cite + holding for live CL re-verify (recent). Placement is **correct** (Key cases, not Recent developments — see §4). **needs_cl: Yes.**
- **F-ENT-1 — Entrapment (needs_cl):** recent circuit applications *United States v. Hanapel* (8th Cir. 2024) and *United States v. Perez-Rodriguez* (1st Cir. 2021) — role-labeled, circuit-named, no-SCOTUS clean; flag holdings for CL verify. **needs_cl: Yes.** Core subjective 2-element test + *Jacobson* timing + objective-minority + outrageous-conduct DP branch all stated up front and complete.
- **Section 1983 (D2, note only, no action):** *Monroe v. Pape* carries treatment `limited` with inline tag "Limited by *Monell* (municipal-immunity holding overruled)." Accurate as framed; the partial overruling is on the municipal-person point only. No finding.

---

## 4. Task-mandated confirmations

### ✅ Garrity page (`Public-Employee Compelled Statements (Garrity)`) — ALL checks PASS
- **NASA v. FLRA framed as STATUTORY (not 5A): CONFIRMED.** Labeled "**Statutory companion (not 5A)**" in the Key-cases table (L49); a dedicated brief paragraph "A statutory companion, not a Fifth Amendment rule — the representation right (NASA v. FLRA)" (L32) construes the FSLMRS, 5 U.S.C. § 7114(a)(2)(B); Pitfall #5 (L38) warns "**Treating NASA v. FLRA as constitutional authority** … do not cite it for *Garrity* immunity"; the Mermaid node labels it "**FSLMRS, NOT 5A**" (L79).
- **Audience-relevance / S2-supersession note: CONFIRMED.** The "Why this page is CORE (provenance)" callout (L18) records the OPTIONAL→CORE promotion on audience-relevance grounds (U2-S5 / D3-S2), states it **supersedes S2 §2.0's OPTIONAL tag** for this cluster, and recommends the one-line S2 §2.0 cross-ref be added at execution (S2 not edited here).
- **All 6 cluster cases homed: CONFIRMED.** Key-cases table contains all six — *Garrity v. New Jersey*, *Gardner v. Broderick*, *Lefkowitz v. Turley*, *Kalkines v. United States* (Binding in-circuit — Fed. Cir.), *LaChance v. Erickson*, *NASA v. FLRA*.
- **Named tests up front: CONFIRMED.** Garrity immunity + Gardner/Lefkowitz "compel only under immunity, never a waiver" limit + the Kalkines two-part warning (discharge-for-silence AND no-criminal-use-of-replies-and-fruits) + the LaChance silence-not-falsehood limit — all stated in the brief before the tables. Exemplary page; SR-2 PASS.

### ✅ Overruled / recent-SCOTUS placement (Jackson / Glossip / Barnes) — ALL correct
- **Montejo overrules Jackson → Historical: CONFIRMED (Sixth Amendment page).** *Michigan v. Jackson* is carried at **tier-6 Historical**, treatment `overruled` "*overruled by* [[Montejo v. Louisiana]]" (Key-cases L78), with a dedicated "**Historical — *Michigan v. Jackson* is no longer law**" callout (L40) and pitfall "Do not cite *Michigan v. Jackson* as live law" (L57). The N5 fix is executed correctly: the SCOTUS subsequent-treatment content (Montejo-overrules-Jackson; Massiah-line vitality) was **moved into the brief**, and Recent developments is now circuit/state-only (correctly empty, with the deferral logged).
- **Glossip → Key cases: CONFIRMED (Brady and Giglio page).** *Glossip v. Oklahoma* (2025) sits in **Key cases** (L68, Progeny — *Napue*), and Recent developments explicitly states "including the 2025 *Glossip* application of *Napue*, home to **Key cases** regardless of date." No SCOTUS in Recent-developments. (Cite flagged needs_cl per F-BG-1.)
- **Barnes → Key cases: CONFIRMED (Use of Force page).** *Barnes v. Felix* (2025) is in **Key cases** (L54); it also appears correctly framed in Related-cases on the §1983 page. Recent-developments on both pages is circuit-only. (Cite flagged needs_cl per F-UOF-2.)

### ✅ N5 no-SCOTUS-in-Recent-developments — CLEAN across all 12 pages
Every Recent-developments section contains only circuit/state authority with expand/narrow/split/first-impression roles labeled; all controlling SCOTUS cases home to Key regardless of date. Spot-confirmed: Exclusionary (Soto-Peguero 1st, Neugin 10th, Mitcham Ariz, Chatrie 4th, Smith 5th, Carpenter-remand 6th — a pending SCOTUS *cert* is mentioned but no SCOTUS *holding* is placed there); Standing (Mendoza 3d, Lyle 2d, Chatrie 4th, Smith 5th); Miranda-Custody (Liddell 8th); Miranda-Waiver (Capers 2d / Williams 9th, Wint N.J.); 6A (correctly none); Eyewitness (correctly none — deferred); Garrity (correctly none — deferred); Use of Force (Wright 6th); §1983 (Wright 6th, Jimerson 5th); Brady (Alvarez 5th en banc); Entrapment (Hanapel 8th, Perez-Rodriguez 1st).

---

## 5. Dimension notes (what passed strongly)

- **D14 brief-first / named-tests-up-front:** Every page leads with a field-decisive question and states its named test(s) in the brief before any table. The mandated tests are all present up front: the exclusionary **four escape hatches** (independent source · inevitable discovery · attenuation w/ *Brown* factors · good faith w/ *Leon*'s four fail-situations); the Miranda **custody + interrogation** two-trigger gate; the **Edwards** rule (+ *Davis* unambiguity, *Shatzer* 14-day break, the two invocation tracks); the **Biggers** five reliability factors + the *Wade/Gilbert* 6A lineup rule; **Graham** objective-reasonableness + three non-exclusive factors + **Garner** deadly-force PC test (+ *Barnes* totality-no-time-limit); the **§1983** two elements + **Monell** policy/custom + **QI** two-step + clearly-established-at-specificity + obvious-case; the **Brady** three elements (favorable · suppressed · material) + **Giglio** impeachment + **Napue** false-testimony sister duty; the **entrapment** subjective two-element test + *Jacobson* timing; the **Garrity** immunity + Gardner/Lefkowitz limit + **Kalkines** warning.
- **D4 completeness:** all pages carry the full checklist (black-letter rule · elements/prongs · burden + who bears it · standard of review · remedy · controlling authority + progeny by role · limits · nuances · pitfalls · recent developments · cross-links · apply-it angle). Only logged gap: F-EW-1.
- **D9 teachability:** instructor-voice pitfalls, "keep the two tracks straight" framing (Miranda 5A vs 6A; Garrity vs Miranda; DP-reliability vs 6A-counsel; §1983 vs Leon good-faith), and worked field framing are consistent and strong.
- **D2 faithful framing / L8:** case framing is doctrine-appropriate and restated, not editorialized; multi-homed cases (Perkins, Brewer, Chavez, Cobb, Roberson, Kirby, Wade/Gilbert/Ash, Connick, Graham/Garner/Barnes) are framed per-page without contradiction. Only D2 defects: the two already-escalated Chatrie currency items (F-EXCL-1 / F-STAND-1).

---

## 6. Release-gate action list (blocking items before ship)

| # | Page | Blocking? | Action |
|---|---|---|---|
| 1 | Due-Process Voluntariness | **YES** | Delete trailing `</content>` + `</invoke>` (F-DP-1); obtain SR-2 instructor sign-off (F-DP-2) |
| 2 | Sixth Amendment R2C | **YES** | Delete trailing `</content>` + `</invoke>` (F-6A-1); obtain SR-2 instructor sign-off (F-6A-2) |
| 3 | Miranda Waiver | lint | Delete trailing orphan ` ``` ` fence (F-MW-1) |
| 4 | Use of Force | lint | Add `# Use of Force` H1 (F-UOF-1) |
| 5 | Exclusionary Rule + Standing | escalated | Apply `_review-needed/chatrie-scotus-2026-correction.md` reframe (F-EXCL-1 / F-STAND-1) — needs_cl, slip-op sourced |
| 6 | (multiple) | serial-CL | Clear needs_cl flags: Chatrie(2026), Mendoza(3d 2026), Barnes(2025), Glossip(2025), Zorn(2026), Abbasi, Martin(2025), Jimerson(2024), Hanapel(2024), Perez-Rodriguez(2021), Eyewitness SoR pinpoint |

*End of Cluster C findings.*
