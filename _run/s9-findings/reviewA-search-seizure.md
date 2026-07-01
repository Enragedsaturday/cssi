# S9 Adversarial Dimensional Review — Cluster A (search-threshold + seizure doctrines)

reviewer: **Review A** — adversarial S9 dimensional reviewer (D2 · D4 · D9 · D10 · D14 + SR-2 instructor-grade gate; D6 guardrail check)
role: **FREE (no CL) — FINDINGS ONLY** (find→adjudicate→fix separation, L5). No page edits made.
branch: `overhaul/build` · date: 2026-06-30
finding schema: `{page · dimension · locator(section + quote) · problem · severity · proposed_fix · needs_cl}`

Pages reviewed (10):
`3-what-is-a-search/`: Two Definitions of Search · The Third-Party Doctrine and Digital Surveillance · Curtilage · Tents · Abandonment
`4-what-is-a-seizure/`: Seizure of the Person · Terry Stops and Reasonable Suspicion · Traffic Stops · Arrest in the Home · Collective Knowledge and the Fellow-Officer Rule

---

## SR-2 verdict summary (D2 ∧ D4 ∧ D9 ∧ D14, blocking)

| # | Page | SR-2 verdict | high | med | low | one-line reason |
|---|------|--------------|------|-----|-----|-----------------|
| 1 | Two Definitions of Search | **PASS** | 2 | 1 | 2 | Instructor-grade brief; but ships with a now-FALSE "Chatrie not yet decided" + a Moore-Bush cross-page contradiction (apparatus, not brief). |
| 2 | The Third-Party Doctrine and Digital Surveillance | **PASS** | 1 | 3 | 1 | Excellent brief w/ *Carpenter*-prong gloss discipline; stale geofence-split framing + stray tool markup in file. |
| 3 | Curtilage | **PASS** | 1 | 0 | 2 | Model brief (Dunn factors up front); Moore-Bush disposition stated backwards & internally contradictory. |
| 4 | Tents | **PASS** | 0 | 1 | 2 | Complete circuit-built REP brief; only recency + lint-anchor noise. |
| 5 | Abandonment | **PASS** | 0 | 2 | 1 | Strong brief; recent circuit cases (Hunt/Small/Crumble) need live confirm. |
| 6 | Seizure of the Person | **PASS** | 0 | 1 | 1 | Excellent two-roads brief; Carter cert-status needs recheck. |
| 7 | Terry Stops and Reasonable Suspicion | **PASS** | 0 | 0 | 3 | Model two-step (stop vs frisk) brief; minor D13/D2 nits. |
| 8 | Traffic Stops | **PASS** | 0 | 1 | 1 | Exhaustive mission/duration brief; *Mayville* flagged in prior build as fabrication-risk — confirm. |
| 9 | Arrest in the Home | **PASS** | 0 | 1 | 2 | Excellent firm-line brief; Case v. Montana (2026 SCOTUS) + Knight cite need confirm/link. |
| 10 | Collective Knowledge and the Fellow-Officer Rule | **PASS** | 0 | 1 | 1 | Best-in-cluster vertical/horizontal brief w/ *Pringle* correctly distinguished; Trent (2026) needs confirm. |

**All 10 briefs are instructor-grade, brief-first, complete, and framed by holding — none is muddled/incomplete, so none FAILS the SR-2 composite gate.** No escalations for brief quality.
**Caveat:** pages #1 and #2 carry HIGH-severity **accuracy/currency** defects (stale *Chatrie*) that are ship-blockers on their own (D3/D1) even though they do not fail the D2∧D4∧D9∧D14 composite. See HIGH findings.

**Cluster-wide D6 guardrail status: CLEAN.** No banned "persuasive, not binding" in any cluster-A page (the 2 LINT-4 highs are on `Case Index.md` and `Verifying Good Law.md`, outside this cluster); the 1 LINT-8 med is on `Exigent Circumstances`, outside this cluster. All authority weights ∈ the 6 tiers; circuits named; splits flagged.

---

## HIGH-severity findings (page · problem · fix · needs_cl)

### H1 — Two Definitions of Search · **STALE: *Chatrie* asserted as "not yet decided"** · D3/D1/N5 · needs_cl=Y
- **Locator:** `## Recent developments`, L74: *"The geofence question is now before the Supreme Court (United States v. Chatrie, cert. granted, No. 25-112, argued Apr. 27, 2026, not yet decided)"*; and L77 bullet "Split (narrowing) — geofence" + Sources L125–126.
- **Problem:** Per `_review-needed/chatrie-scotus-2026-correction.md`, **SCOTUS decided *Chatrie v. United States*, No. 25-112, on 2026-06-29** — holding that acquiring Google Location History (geofence) data **IS a Fourth Amendment search**. As of the review date the page asserts a **factually false** statement of current law ("not yet decided") on this page's **anchor doctrine**. Secondary defects: caption should be ***Chatrie v. United States*** (Chatrie is SCOTUS petitioner — the page's own oral-arg URL says "okello-t-chatrie-petitioner-v-united-states"), and once decided the SCOTUS holding must move to **Key cases** (N5 — no SCOTUS in Recent developments).
- **Proposed fix:** Execute the queued correction (`_review-needed/chatrie-scotus-2026-correction.md` Action B #2): reframe geofence search-question as **RESOLVED — *Chatrie* (2026) = it is a search; geofence warrants NOT categorically unconstitutional; PC/particularity remanded to 4th Cir.**; add the *Chatrie* holding in full (this is its anchor page); re-tier to **Binding — SCOTUS** and home in Key cases; keep the live `⚖` split as PC/particularity-on-remand.
- **needs_cl:** Y — confirm holding, vote (reported 6–3 Kagan, J.), disposition (vacated/remanded), and cite against the slip op; **do not** ingest corrupted CL opinion `10881683` (resolves to *Harmon v. ABC 2 News*).

### H2 — Two Definitions of Search ∧ Curtilage · **Cross-page CONTRADICTION on *Moore-Bush* disposition** · D5/D2/D1 · needs_cl=Y
- **Locator:**
  - Two Definitions `## Recent developments` L79: *"United States v. Moore-Bush (1st Cir. 2022, en banc) **admitted** eight months of pole-camera evidence … good-faith reliance on circuit precedent saved it either way."*
  - Curtilage `## Recent developments` L82: *"the tie **affirmed suppression below** … (resolved on Leon good faith)."*
- **Problem:** The two pages state **opposite outcomes** for the same en-banc case. Curtilage is also **internally contradictory** ("affirmed suppression below" AND "resolved on Leon good faith" cannot both be the disposition — good faith admits the evidence). This is exactly the scar documented in FINAL-QA §0.3 ("backwards holding (*Moore-Bush*)"). The en-banc First Circuit **reversed** the district court's suppression order (evidence **admitted** on good faith), so **Two Definitions is correct and Curtilage is backwards.**
- **Proposed fix:** Correct Curtilage L82 to state the en-banc court **reversed the suppression order / admitted the evidence** on *Leon* good faith while splitting 3-3 on the search question; harmonize wording across both pages (and the neutral Third-Party Doctrine L58 mention).
- **needs_cl:** Y — confirm *United States v. Moore-Bush*, 36 F.4th 320 (1st Cir. 2022) (en banc) disposition + good-faith rationale against the opinion before the fix is applied.

### H3 — The Third-Party Doctrine and Digital Surveillance · **STALE geofence-split framing (Chatrie)** · D3/D1 · needs_cl=Y
- **Locator:** `## Recent developments` L58: *"Geofence warrants & long-term pole-camera surveillance — an open circuit split (post-Carpenter) … United States v. Chatrie (4th Cir.) runs in the contra direction — accessing geofence location data was not treated as a search on those facts."*
- **Problem:** Presents the geofence **search question** as an open circuit split, which SCOTUS **resolved** in *Chatrie* (2026-06-29). Same stale-law defect as H1 on a page whose whole subject is the third-party doctrine's digital limit. Caption/party-order (US v. Chatrie → Chatrie v. US at SCOTUS) also needs the SCOTUS entry.
- **Proposed fix:** Per correction file §4 "Also check": relabel the geofence search-question split **resolved (Chatrie 2026)**; the live split becomes **PC/particularity on remand**; add *Chatrie* as **Binding — SCOTUS** authority (cross-linked to the new case page). Keep *Smith* (5th Cir.) as the reframed foil (its "categorically unconstitutional" holding was **not** adopted).
- **needs_cl:** Y — as H1 (slip-op sourced; CL-confirm pending).

---

## Per-page findings

### 1 — Two Definitions of Search — SR-2 **PASS**
- **D14 (brief-first):** PASS. `## The Brief` is first substantive content, self-contained, top-to-bottom. Both threshold tests stated **up front** (N3): Test A trespass (2 elements) + Test B *Katz* (2 prongs, correctly attributed to **Harlan's concurrence**). Nuances/pitfalls folded in as bolded paragraphs ("Where the lines fall", "Pitfalls to avoid") — no `## Nuances`/`## Common pitfalls` headings. 
- **D4 (completeness):** PASS. Black-letter · elements · burden+who ("Who bears what") · SoR (de novo / clear error) · remedy (exclusion) · authority+progeny by role · limits · nuances · pitfalls · "where the lines fall" apply-it angle — no unlogged gap.
- **D9 (pedagogy):** PASS. Rule-first, teaches the either-theory-suffices logic and the technology recalibration well.
- **D2 (framing / L8):** mostly faithful (Carpenter "declining to mechanically extend", Kyllo "not in general public use", Olmstead revived-not-dead). Exceptions = **H1** (stale Chatrie) and **H2** (Moore-Bush).
- **H1** (see above) — high, needs_cl=Y.
- **H2** (see above) — high, needs_cl=Y.
- **[med] D10/N6:** `## Related cases across doctrines`, *Hudson v. Palmer* row lists "Primary home: [[Two Definitions of Search]]" (this page) yet sits in the *Related-across-doctrines* table rather than **Key cases**. Fix: move Hudson to Key cases (it's homed here) or relabel its home. needs_cl=N.
- **[low] D10:** frontmatter has no `amendment:` field (encodes it in `jurisdiction:`), unlike 6 of the other cluster pages — cosmetic single-controlling-amendment inconsistency (N5/LINT-3). needs_cl=N.
- **[low] D7:** *Gooch* appears in the brief as "6 F.3d 673 (9th Cir.)" with weight inline — fine; but note the brief's several block quotes rely on `#^pin-NNN` anchors (pinpoint encoded in the wikilink), which the LINT-2 heuristic reads as "no nearby pinpoint" → largely **false positives**; genuine pinpoints are present. Flag so the adjudicator does not over-de-quote. needs_cl=N.

### 2 — The Third-Party Doctrine and Digital Surveillance — SR-2 **PASS**
- **D14:** PASS. Brief-first; black-letter third-party rule + *Carpenter* limit + ordered "How to apply it" up front. **Exemplary L8 discipline:** the "*Carpenter* prongs" are explicitly labeled **"instructor framing, not the Court's holding"** — a model gloss-vs-holding disclaimer.
- **D4:** PASS. Rule · two-track dividing line · apply-it · burden/SoR/remedy · limits/nuances/pitfalls (mosaic scale, Kyllo/Dow contrast, Berger baseline, drone/ALPR watch-outs) — complete.
- **D9:** PASS. Strong "which track does the data sit on" operational teaching.
- **D2:** faithful except **H3** (stale geofence split).
- **H3** (see above) — high, needs_cl=Y.
- **[med] D10 — stray tool-call markup committed into the file:** file **lines 90–91 literally contain `</content>` and `</invoke>`** (verified: `wc -l` = 91; tail shows both tags after the last Sources bullet). These will render as visible garbage. **Fix: delete lines 90–91.** Non-CL editor fix. needs_cl=N.
- **[med] D7/L1 — quotes in the brief lack point-of-use pinpoints:** e.g. L17 *"a person has no legitimate expectation of privacy in information he voluntarily turns over to third parties"* (Smith), L19 *"maintains a legitimate expectation of privacy in the record of his physical movements as captured through CSLI"* (Carpenter), L19 *"an intimate window into a person's life"* — pinpoints exist only in `## Sources`, and the anchors used are `#Rule` (not `#^pin-NNN`), so unlike the other cluster pages the pinpoint is not carried to the quote. Add inline pincites (Smith 743–44; Carpenter slip op. at 11–15). needs_cl=N (pincites already in Sources; hygiene only).
- **[med] needs_cl — Leaders of a Beautiful Struggle:** Sources L89 self-flags *"CourtListener URL not verified in this pass (no-CL); confirm at the serial-CL gate."* Also confirm the **2024/2026 circuit/state entries** (*Hay* 10th; *Porter* 5th Cir. Mar. 2026; *Robinson* Va. Apr. 2026) exist + holdings. needs_cl=Y.
- **[low] D10:** no `amendment:` frontmatter field (as page 1). needs_cl=N.

### 3 — Curtilage — SR-2 **PASS**
- **D14:** PASS. Model brief-first. The **four *Dunn* factors are enumerated up front** (N3) with the "not a mechanical checklist / centrally-relevant" qualifier; open-fields, implied-license scope, lawful-vantage-vs-entry, commercial-privacy, and tent-has-no-curtilage all woven in. Pitfalls folded in.
- **D4:** PASS. Rule · named test + prongs · open-fields boundary · Collins (auto-exception ≠ curtilage entry) · Ciraolo/Riley/Kyllo vantage line · burden/SoR/remedy · pitfalls — comprehensive.
- **D9:** PASS. Excellent "same officer, same patch of marijuana" framing.
- **D2:** faithful throughout **except H2** (Moore-Bush disposition backwards + internally contradictory).
- **H2** (see above) — high, needs_cl=Y.
- **[low] D6/N2:** *May-Shaw* (6th Cir.) and *Lundin* (9th Cir.) in Recent developments and the state-illustrative trio in Sources are correctly tiered/circuited — no defect; noted only to confirm D6 clean.
- **[low] D10:** no `amendment:` frontmatter field (as pages 1–2). needs_cl=N.

### 4 — Tents — SR-2 **PASS**
- **D14:** PASS. Brief-first; the *Katz* two-part test stated up front (N3), then a clean three-factor application (dwelling-not-vehicle / subjective-closure / location-right-to-be). Limits/pitfalls + the ⚖ *Ruckman* split woven in.
- **D4:** PASS. Rule · test · three factors · burden/SoR/remedy · trespasser limit · closed-tent arrest-warrant rule · guest standing (Olson/Carter) · pitfalls — complete for a circuit-built doctrine; correctly states **no SCOTUS on tents**.
- **D9:** PASS.
- **D2:** faithful (Gooch "more like a house than a car"; Basher no-curtilage; Sandoval permission-irrelevant).
- **[med] needs_cl:** the tent line is entirely circuit-built (9th Cir. *LaDuke → Gooch → Sandoval → Basher*; 10th Cir. *Ruckman*) with multiple block quotes; confirm the *Sandoval* 661 and *Basher* 1169 quotes/pincites and the split characterization live. needs_cl=Y.
- **[low] D7:** many LINT-2 "no nearby pinpoint" flags on this page are **false positives** — pinpoints are carried in `#^pin-NNN` anchors + Sources. Do not over-de-quote. needs_cl=N.
- **[low] D13:** *Ruckman* and *LaDuke* are page-less (declared in Sources as intentional) — acceptable; both named with circuit. needs_cl=N.

### 5 — Abandonment — SR-2 **PASS**
- **D14:** PASS. Brief-first; black-letter rule + the four totality factors up front (N3), three "lines to know" (Greenwood/Abel/Hester), bailment contrast, abandonment≠consent distinction, burden/SoR/remedy, pitfalls, field-framing — all in-brief.
- **D4:** PASS. Notably strong on the **abandonment-vs-consent** doctrinal separation and the voluntariness (unlawful-police-conduct) limit.
- **D9:** PASS. "Anything to do with it" field framing is good instructor voice.
- **D2:** faithful; *Matlock* correctly homed to Consent and distinguished (N1); *Jones v. United States* shown as **overruled by Salvucci** (N4 treatment inline). 
- **[med] needs_cl:** Recent developments asserts three recent circuit holdings — **United States v. Hunt (9th Cir. 2025)**, **United States v. Small (4th Cir. 2019)**, **United States v. Crumble (8th Cir. 2018)** — with specific facts/holdings (device-vs-data separate inquiry). *Small* is on the FINAL-QA §0.3 prior-build watch-list ("invented frameworks (… Small)"). Confirm existence + holdings live. needs_cl=Y.
- **[med] D2:** the page asserts a device-vs-data "first-impression/refinement" **frontier** and that there is "**no recognized circuit split**" on these points — a scope/negative-bound claim (L7). Confirm the no-split characterization at the frontier. needs_cl=Y.
- **[low] D10:** order/structure correct; `amendment:` present. needs_cl=N.

### 6 — Seizure of the Person — SR-2 **PASS**
- **D14:** PASS. Brief-first; the **four named tests stated up front** (N3): *Mendenhall* free-to-leave, *Hodari D.* submission, *Torres* force, *Brower* means-intentionally-applied — plus the consensual→Terry→arrest continuum. Pitfalls + field-framing in-brief.
- **D4:** PASS. Force branch vs show-of-authority kept separate; burden/SoR/remedy; back-end Gerstein/McLaughlin 48-hour rule; Brendlin passenger reach — complete.
- **D9:** PASS. "Am I applying force / is there submission" ordered field test is excellent.
- **D2:** faithful; *Barnes v. Felix* (2025) correctly framed as the reasonableness step, homed to Use of Force.
- **[med] needs_cl:** Recent developments L101 — **Carter v. United States (D.C. Ct. App. 2025)**, "cert petition (No. 25-885) … no Supreme Court holding yet — not settled law." The correction file's §7 watch-item flags this exact marker to re-poll. Framing is defensible if cert is still pending, but confirm current status (granted/denied/decided) as of review date. needs_cl=Y.
- **[low] needs_cl:** *Barnes v. Felix* "has no time limit" quote (605 U.S. 73, 80 (2025)) — recent SCOTUS quote; confirm verbatim + pinpoint. needs_cl=Y (low).
- **[low] D2:** *Torres* 10th-Cir.-on-remand entry cites *Heck v. Humphrey* — fine, but *Heck* is unlinked/page-less (civil-procedure cross-ref); acceptable. needs_cl=N.

### 7 — Terry Stops and Reasonable Suspicion — SR-2 **PASS**
- **D14:** PASS. Brief opens with the **two-call framing (stop RAS vs. separate armed-and-dangerous RAS to frisk)** — the named two-step stated up front (N3). Tip-reliability spectrum, scope/duration, stop-and-identify, flight, pitfalls, field-framing all in-brief.
- **D4:** PASS. RAS-vs-PC middle rung; frisk-for-weapons-not-evidence; particularity (Ybarra); burden/SoR/remedy — complete.
- **D9:** PASS. Best-in-class "make the two calls separately, in order."
- **D2:** faithful; *Peters* correctly framed as the stop→arrest line and companion to *Sibron* (shared 392 U.S. 40 opinion, noted in Sources).
- **[low] D13:** `## Related`, *Kolender v. Lawson* row — the "Primary home" column holds a doctrine **label** ("Due Process — void-for-vagueness (stop-and-identify)") rather than a page wikilink; no home-page link. Acceptable (no S&S home) but inconsistent with the column's purpose. needs_cl=N.
- **[low] D2:** Recent developments *Daniels* (10th Cir.) is tagged "⚖ Circuit split" yet the parenthetical says it is a "doctrinal-tightening signal … rather than recognizing an opinion-level conflict" — the ⚖ marker slightly overstates; consider relabeling role-only. needs_cl=N.
- **[low] needs_cl:** the three Recent-developments circuit cases (*Daniels* 10th 2024; *Robinson* 4th en banc 2017; *Black* 4th 2013) carry block quotes with pincites — confirm live (esp. the 2024 *Daniels*). needs_cl=Y (low).

### 8 — Traffic Stops — SR-2 **PASS**
- **D14:** PASS. Brief-first; field-decisive "what may I do / how long." Black-letter + *Rodriguez* mission rule + control-measures ladder (Mimms/Wilson/Johnson/Long) + checkpoints cross-doctrine + pitfalls + the 5A/Miranda clarifier flagged as **not a 4A holding** — clean scoping.
- **D4:** PASS. Pretext (Whren/Sullivan), mistake-of-law (Heien), mission/diligence (Rodriguez/Sharpe/Caballes), frisk thresholds, burden/SoR/remedy, Strieff attenuation — thorough.
- **D9:** PASS. "Multitasking OK; adding time is not" is a precise operational teaching.
- **D2:** faithful; **N5 handled explicitly** — *Barnes v. Felix* row notes "A SCOTUS holding — homed in the case tables, **not** Recent developments (N5)."
- **[med] needs_cl:** Recent developments — **United States v. Mayville (10th Cir. 2020)**. *Mayville* is named in the FINAL-QA §0.3 prior-build watch-list ("invented frameworks (Mayville/…)") as web-discovery that serial CL had to re-check. It now carries a specific "Triple-I criminal-history check … negligibly burdensome … within the mission" holding + CL URL — confirm existence + that the holding is not the prior-build's invented framing. Also confirm **United States v. Cole (7th Cir. 2021 en banc)** travel-plan holding. needs_cl=Y.
- **[low] D6/N2:** *Vinton* labeled "Binding in-circuit — D.C. Cir. (persuasive elsewhere)" — correct tier-2 usage with the footnote caveat that its protective-search point sits in a footnote (paired with binding *Long*). No defect. needs_cl=N.

### 9 — Arrest in the Home — SR-2 **PASS**
- **D14:** PASS. Brief-first; *Payton* firm-line rule + the two predicates (resides + present) up front, the *Steagald* third-party flip, the four-line exigency gate (Santana/Welsh/King/Lange run "at the same time"), the "reason to believe" quantum split, and the three-protected-interests pitfall map — all in-brief (N3/N9).
- **D4:** PASS. Rule · third-party flip · remedy bound (New York v. Harris) · exigency factors · quantum split · burden/SoR/remedy · emergency-aid boundary (Caniglia no-caretaking) — complete.
- **D9:** PASS. "Whose home / what authority" decision map is strong.
- **D2 / D10 / N5:** faithful; **N5 handled correctly** — *Case v. Montana*, 607 U.S. ___ (2026), a SCOTUS holding, is placed in the **Related-cases table (not Recent developments)**, consistent with the "re-home Case v. Montana" directive.
- **[med] needs_cl:** *Case v. Montana*, 607 U.S. ___ (2026) (No. 24-624) is a **very recent SCOTUS** case asserted with pincites (slip op. at 7–11); under SR-1 confirm existence, holding (emergency-aid "objectively reasonable basis," not PC), and pincites live against the slip op. Also confirm the constructive-entry split cases (*Maez* 10th, *Berkowitz* 7th, *Knight v. Jacobson* 11th, *Brinkley* 4th, *Vasquez-Algarin* 3d). needs_cl=Y.
- **[low] D7/D13:** Recent developments names **Knight v. Jacobson (11th Cir.), 300 F.3d 1272** in prose but provides **no CL link** for it (only Maez + Berkowitz are linked) and it is **absent from `## Sources`**. Add the CL link + a Sources line. needs_cl=N.
- **[low] D10:** no `amendment:` frontmatter field (as pages 1–3). needs_cl=N.

### 10 — Collective Knowledge and the Fellow-Officer Rule — SR-2 **PASS**
- **D14:** PASS. Brief-first; the **vertical vs. horizontal** two-mode distinction stated up front (N3) as the doctrine's "central trap," then Whiteley/Hensley (vertical, settled), horizontal (unsettled), Herring (mistaken pooled knowledge), burden/SoR/remedy, pitfalls — all in-brief.
- **D4:** PASS. Notably strong: separates the settled vertical prong from the split horizontal prong and states the *Hensley* **intrusiveness ceiling** — complete.
- **D9:** PASS. "Pools knowledge, never manufactures it" is a crisp instructor line.
- **D2 (framing / N1):** **exemplary.** *Maryland v. Pringle* is **expressly distinguished** as aggregate-PC-as-to-a-person, **NOT** horizontal pooling ("contains no collective-knowledge … reasoning") — a textbook N1 placement-by-holding correction. *Herring* correctly **promoted to Key** here (matches the STANDARDS.md N6 example).
- **[med] needs_cl:** Recent developments — **United States v. Trent (6th Cir. 2026)** (unpublished, tier-5 "Persuasive only — non-precedential"), plus *Massenburg* (4th 2011), *Chavez* (10th 2008), *Ramirez* (9th 2007) with block-quote pincites. Confirm the 2026 *Trent* existence + unpublished status and the split-characterization quotes live. needs_cl=Y.
- **[low] D6/N2:** tier-5 "Persuasive only — non-precedential" used correctly for the unpublished *Trent*; circuits named on all; ⚖ split flagged. D6 clean. needs_cl=N.

---

## Cross-cutting observations (for the adjudicator)

- **Stale-SCOTUS currency sweep (D3/SR-1):** the two HIGH stale-*Chatrie* findings (H1, H3) and the *Carter* cert-status med (page 6) all stem from decisions/petitions moving **after** the digital-frontier research pass. Recommend running the correction file's grep before ship:
  `grep -rniE "pending before the supreme court|not yet decided|cert. granted|now before the supreme court" content/3-what-is-a-search content/4-what-is-a-seizure`.
- **LINT-2 anchor false positives:** pages using `[[Case#^pin-NNN|...]]` anchors (Two Definitions, Curtilage, Tents, Abandonment, Seizure, Terry, Traffic, Arrest, Collective) carry the pinpoint **inside the wikilink**; the LINT-2 proximity heuristic still flags them "no nearby pinpoint." These are largely **dismiss-worthy** — do not de-quote. The **genuine** point-of-use pinpoint gap is on **The Third-Party Doctrine** page (uses `#Rule` anchors + bare quotes) — fix there.
- **Prior-build fabrication-risk cases resurfacing (FINAL-QA §0.3):** *Moore-Bush* (H2 — confirmed backwards on Curtilage), *Mayville* (page 8), *Small* (page 5) all appear in cluster-A pages and were on the prior "backwards/invented" watch-list. All three are flagged needs_cl for live re-confirmation of holding direction.
- **D6 guardrails:** CLEAN across all 10 cluster-A pages (no banned phrasing, all 6-tier weights, circuits named, splits flagged, no apocryphal trio, no inline `## Flashcards`).
- **`amendment:` frontmatter:** absent on Two Definitions, Third-Party, Curtilage, Arrest in the Home (encoded in `jurisdiction:` instead); present on the other 6. Low-severity D10 consistency nit — add for uniformity if the template requires the explicit field.

*End of Review A findings.*
