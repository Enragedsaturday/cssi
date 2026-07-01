# S9 Reviewer B — Cluster B (Levels of Suspicion + Warrants + Exceptions)

**Reviewer:** Adversarial S9 dimensional reviewer B — D2 / D4 / D9 / D10 / D14 + SR-2 instructor-grade composite gate.
**Mode:** FREE (no CL). **FINDINGS ONLY (L5) — no page edits.**
**Date:** 2026-06-30 · branch `overhaul/build`.
**Scope reviewed (13 pages):**
`5-levels-of-suspicion/Probable Cause and Reasonable Suspicion` ·
`6-warrant-requirement/The Warrant Requirement` ·
`7a-pc-needed/{Plain View Doctrine, Automobile Exception, Exigent Circumstances and Hot Pursuit, Emergency Aid, Community Caretaking}` ·
`7b-pc-not-needed/{Search Incident to Arrest, Consent Searches, Knock and Talk, Special Needs and Administrative Searches, Border Searches, Securing the Scene}`

> **Gate legend.** SR-2 = the blocking instructor-grade composite **D2 ∧ D4 ∧ D9 ∧ D14** (framing faithful ∧ complete ∧ teaches ∧ brief-first). D10/N5 (structure, no-SCOTUS-in-recent-dev, single-amendment frontmatter) is **not** part of SR-2 — a D10 finding does not fail the SR-2 gate. `needs_cl=true` items are routed to the single serial CL lane; on this FREE pass they are **flagged, not adjudicated**.

---

## Headline result

**All 13 cluster-B pages PASS the SR-2 composite gate (D2 ∧ D4 ∧ D9 ∧ D14).** Every page is genuinely brief-first, self-contained, complete on rule/elements/burden/SoR/remedy/limits/pitfalls, faithfully framed, and teaches rather than dumps. No page ships a muddled or incomplete brief.

The findings are **peripheral to SR-2**: one HIGH visible leftover process marker (SITA), one MEDIUM invisible unresolved gate comment (PC&RS), a LOW systemic frontmatter inconsistency (6 pages lack a dedicated `amendment:` field — degrades gracefully via `jurisdiction:` fallback, confirmed against `lint3_structure.py`), and a set of `needs_cl` routing flags for circuit/state quotes + a recurring slip-op-pinpoint-for-published-reporter citation pattern.

**The exhaustive-treatment set is genuinely exhaustive; the caretaking split honors the spec in full** (see §Confirmations).

---

## Per-page SR-2 verdict + finding counts

| Page | SR-2 | HIGH | MED | LOW | needs_cl items |
|---|---|---|---|---|---|
| Probable Cause and Reasonable Suspicion | **PASS** | 0 | 1 | 0 | In re Winship (comment); Case v. Montana; Daniels 10th |
| The Warrant Requirement | **PASS** | 0 | 1 | 0 | Smith/Chatrie/Holcomb geofence circuit quotes |
| Plain View Doctrine | **PASS** | 0 | 1 | 0 | Tarantino/Herlth/Volle/Mansor/Burgess/Loera/Morton/Tuggle/Loines/Ganias/Smith |
| Automobile Exception | **PASS** | 0 | 1 | 1 | Camou/Morley/Gastiaburo |
| Exigent Circumstances and Hot Pursuit | **PASS** | 0 | 1 | 1 | Newman/Meyer; Mitchell S.Ct. pinpoint |
| Emergency Aid | **PASS** | 0 | 1 | 0 | Case v. Montana slip-op quotes (2026, high-stakes) |
| Community Caretaking | **PASS** | 0 | 1 | 0 | Garner/Rideau/Graham (persons-in-public strand) |
| Search Incident to Arrest | **PASS** | **1** | 1 | 1 | Davis/Perez/Braxton; Trupiano/Rabinowitz history |
| Consent Searches | **PASS** | 0 | 1 | 1 | **Osage** destruction quotes+pinpoints; Lewis(6th)/Williams(3d) |
| Knock and Talk | **PASS** | 0 | 1 | 1 | Walker/Lundin/Carloss/French; **Carloss Gorsuch-attribution** |
| Special Needs and Administrative Searches | **PASS** | 0 | 0 | 1 | Payne/Oliveras |
| Border Searches | **PASS** | 0 | 1 | 0 | Cotterman/Cano/Kolsuz/Aigbekaen/Touset/Alasaad |
| Securing the Scene | **PASS** | 0 | 1 | 0 | August (4-part test); Conner |
| **Cross-cutting** | — | 0 | 1 | 1 | slip-op-pinpoint-for-published pattern (CC-2) |

**Totals:** 1 HIGH · 13 MED · 8 LOW. **SR-2: 13/13 PASS.**

---

## HIGH-severity findings

### B-H1 · Search Incident to Arrest · visible leftover process marker in body prose
- **Dimension:** D10 (structure / shipping cleanliness). Does **not** fail SR-2.
- **Locator (brief, "immediate-control limit" para):** `*[FLAG — new history note]* The older, broader premises-search line (e.g., *Trupiano v. United States*, 334 U.S. 699 (1948), abrogated by *Rabinowitz*) was superseded by *Chimel*'s immediate-control limit …`
- **Problem:** `*[FLAG — new history note]*` is an **italic markdown marker that renders visibly** to students on a page whose frontmatter is `status: verified`. It is an unfinished-edit annotation left in shipped prose (distinct from an HTML comment). Unprofessional on an instructor-grade product.
- **Fix:** Delete the literal `*[FLAG — new history note]*` token. The sentence it annotates is substantively correct (teach SITA scope through *Chimel*, not the dead pre-*Chimel* premises line) and should remain, unmarked.
- **needs_cl:** No (editorial; the underlying *Trupiano*/*Rabinowitz*/*Chimel* history is standard). The *Trupiano* (334 U.S. 699) / *Rabinowitz* good-law history may be spot-confirmed opportunistically, but the fix is a pure deletion.

---

## MEDIUM-severity findings

### B-M1 · Probable Cause and Reasonable Suspicion · unresolved gate comment + unverified assertion embedded in the page
- **Dimension:** D10 (cleanliness) + D1/D4 (unresolved `needs_cl`). Does not fail SR-2.
- **Locator (ladder rung 4):** the HTML comment `<!-- NEW-ASSERTION (gate/R13): "beyond a reasonable doubt" = the conviction standard (In re Winship, 397 U.S. 358 (1970)); … Route to serial-CL confirmation if retained. -->`
- **Problem:** A raw build/gate comment survives in the published markdown. It is invisible when rendered but (a) is a leftover process artifact, and (b) **self-documents an unfinished `needs_cl`** — the *In re Winship*, 397 U.S. 358 (1970) proposition ("beyond a reasonable doubt = the conviction standard") was never CL-confirmed per the comment's own instruction. The visible rung-4 text ("Proof beyond a reasonable doubt — the trial/conviction standard") depends on it.
- **Fix:** Route *In re Winship*, 397 U.S. 358 (1970) through the serial CL lane to confirm the conviction-standard proposition; on confirmation, **delete the HTML comment** (keep rung 4). If unconfirmable, escalate. Either way the comment must not ship.
- **needs_cl:** **Yes** — *In re Winship*, 397 U.S. 358 (1970), proposition only (no verbatim quote asserted).

### B-M2 · Emergency Aid · *Case v. Montana* (2026) is quote-heavy and high-stakes — live-verify the slip-op quotes
- **Dimension:** D2 (framing faithfulness) + D1. SR-2 framing PASSES on its face (the quotes support "no further gloss," neither RS nor PC), but the case is a 2026 decision carrying the doctrinal load of the whole page.
- **Locator:** brief para "The quantum is *Brigham City* reasonableness" — four slip-op quotes at slip op. 7, 8, 9; also the same case is Key on PC&RS (Related table) and drives the split-resolution in Recent developments.
- **Problem:** *Case v. Montana*, 607 U.S. ___ (2026) (opinion id 10774335) is the single most quote-dependent, most recent, highest-stakes authority in the cluster; the framing ("basis to believe," not PC, not RS; scope-limited) is faithful **as written**, but every quote + slip-op pinpoint must be live-confirmed against the primary opinion (SR-1). A 2026 slip-op is exactly where pagination/quote drift risk is highest.
- **Fix:** none to page framing (it is L8-faithful). Confirm each quote + slip-op pinpoint on the serial lane; reconcile the "with no further gloss" and "decline … probable-cause spin" passages verbatim.
- **needs_cl:** **Yes** — *Case v. Montana*, 607 U.S. ___ (2026), all quotes + slip-op pinpoints 7/8/9 (and the identical PC&RS Related-table framing).

### B-M3 · Community Caretaking · persons-in-public strand (Garner / Rideau / Graham) — live-verify the circuit quotes + pinpoints
- **Dimension:** D4/D2 (the strand is the spec's marquee content) + D1. Framing PASSES; this is a `needs_cl` routing flag, per the review brief's explicit callout of "the caretaking persons-in-public strand Garner/Rideau/Graham."
- **Locator:** Strand (b) — *Garner* 3-part test (416 F.3d 1208, 1213); *Rideau* (969 F.2d 1572, 1574, 1576); *Graham v. Barnette* (5 F.4th 872, quotes at "slip op., at 10, 10–11").
- **Problem:** Three circuit anchors carry verbatim quotes and pinpoints. **Note the pinpoint form on *Graham*:** the page cites "slip op., at 10 / 10–11" for a case with a **published F.4th reporter cite** (5 F.4th 872) — the pinpoint should be to the reporter page (e.g., 5 F.4th at 88x), not a slip-op page. See CC-2.
- **Fix:** confirm each quote verbatim on the serial lane; reconcile *Graham*'s pinpoint to its published 5 F.4th pagination (the "probable cause of dangerousness" standard + "at least nine of our sister circuits" line).
- **needs_cl:** **Yes** — *United States v. Garner* (10th Cir.), *United States v. Rideau* (5th Cir. en banc), *Graham v. Barnette* (8th Cir.).

### B-M4 · Consent Searches · the *Osage* destruction rule — live-verify quotes + pinpoints
- **Dimension:** D4 (exhaustive scope) + D1. Framing PASSES; `needs_cl` flag per the review brief's explicit callout of "the Osage destruction rule."
- **Locator:** brief para "Scope has a hard outer edge" — *United States v. Osage*, 235 F.3d 518, 521–522 (10th Cir. 2000): "[h]owever, we do not read that authority to permit the destruction of such containers" and "before an officer may actually destroy or render completely useless a container … the officer must obtain explicit authorization …".
- **Problem:** The S6 spec (§9 open item) required *Osage* identity + pinpoint to be confirmed live at execution; on a FREE pass this remains unadjudicated. The framing (general consent ≠ authority to destroy; anchored to *Jimeno*'s locked-briefcase dictum) is faithful and correctly lexicon-labeled ("Binding in-circuit — 10th Cir.; Persuasive (outside circuit)").
- **Fix:** confirm *Osage* (235 F.3d 518) existence, both quotes, and pinpoints 521/522 on the serial lane.
- **needs_cl:** **Yes** — *United States v. Osage*, 235 F.3d 518 (10th Cir. 2000).

### B-M5 · Knock and Talk · possible citation-attribution error on *Carloss* pinpoint
- **Dimension:** D7-adjacent / D1 (citation hygiene). Does not fail SR-2.
- **Locator:** Sources line — `*United States v. Carloss*, 818 F.3d 988 (10th Cir. 2016) — … — pinpoints: slip op. at 10–11 (Gorsuch, J., dissenting).`
- **Problem:** The brief quotes slip-op 10–11 for the **majority's** holding ("what an objective officer would have perceived"; signs lack "talismanic" revoking power). The Sources pinpoint attributes "slip op. at 10–11" to **"(Gorsuch, J., dissenting)"** — but Gorsuch **dissented** (the page itself says so in Recent developments). Attributing the majority-holding pinpoint to the dissent is internally contradictory and likely an error. Compounded by the slip-op-for-published pinpoint issue (CC-2): *Carloss* has an 818 F.3d 988 reporter cite.
- **Fix:** on the serial lane, confirm the majority pinpoint page in 818 F.3d for the "talismanic"/"objective officer" language and **strike the "(Gorsuch, J., dissenting)" parenthetical** from that Sources line (or move it to the separately-cited dissent material, if any is quoted).
- **needs_cl:** **Yes** — *United States v. Carloss*, 818 F.3d 988 (10th Cir. 2016), majority vs. dissent pinpoint attribution.

### B-M6 · The Warrant Requirement · geofence/computer-search circuit quotes (Recent developments) — live-verify
- **Dimension:** D3/D1 (frontier). Framing PASSES (no SCOTUS in recent-dev; pending SCOTUS threshold noted in the brief, not the section — N5-clean).
- **Locator:** Recent developments — *United States v. Smith* (5th Cir. 2024, geofence "modern-day general warrants"), *United States v. Chatrie* (4th Cir., panel + en banc), *United States v. Holcomb* (9th Cir. 2025, "dominion and control" clause).
- **Problem:** Three circuit developments carry specific holdings/quotes on a live, fast-moving split. (The *Smith* here is the **legitimate** geofence case — correctly distinct from the banned apocryphal "Holiday/McCall/Smith" trio; not a guardrail violation.)
- **Fix:** confirm each holding + the pending-SCOTUS geofence-argument status on the serial lane at the gate (drift risk — R9/§8.8).
- **needs_cl:** **Yes** — *Smith* (5th Cir.), *Chatrie* (4th Cir.), *Holcomb* (9th Cir.).

### B-M7 · Plain View Doctrine · large state/circuit frontier apparatus — live-verify
- **Dimension:** D3/D1. Framing PASSES (state cases labeled "Persuasive — state, illustrative" and paired with federal; Carpenter flagged "NOT plain-view authority").
- **Locator:** Recent developments Line B (digital frontier) — *Burgess*(10th), *Ganias*(2d), *Loera*(10th), *Morton*(5th), *Loines*(6th), *Tuggle*(7th), *Smith*(5th), *Chatrie*(4th); state *Volle*(Kan. 2025), *Mansor*(Or. 2018), *Hughes*(Mich.); plus *Tarantino*(N.C.)/*Herlth*(2026 PA Super) in the brief.
- **Problem:** Heavy quote/pinpoint density on state + circuit authority, incl. a **2026** case (*Herlth*, 2026 PA Super 114) and a **2025** case (*Volle*, 580 P.3d 1223). High drift/verification surface.
- **Fix:** batch-confirm identities, quotes, and pinpoints on the serial lane; spot-check the two 2025–2026 state cites hardest.
- **needs_cl:** **Yes** — the Line-B circuit/state set (esp. *Herlth* 2026, *Volle* 2025).

### B-M8 · Automobile Exception · in-circuit quotes — live-verify
- **Dimension:** D3/D1. Framing PASSES; *Anchondo* correctly framed "Pitfall, not authority."
- **Locator:** *Camou* (773 F.3d 932, 943, 9th Cir. — phone ≠ container); *Morley* (99 F.4th 1328, 1338, 11th Cir. 2024 — two-element restatement, used in the brief); *Gastiaburo* (16 F.3d 582, 587, 4th Cir. — 38-day gap "legally irrelevant").
- **Fix:** confirm quotes + pinpoints on the serial lane.
- **needs_cl:** **Yes** — *Camou*, *Morley*, *Gastiaburo*.

### B-M9 · Exigent Circumstances and Hot Pursuit · circuit quotes + a mixed reporter pinpoint
- **Dimension:** D3/D1/D7. Framing PASSES; *Santana* "limited by *Lange*" (N4) present and consistent; hot-vs-fresh line and *Newman* illustration are faithful.
- **Locator:** *Newman v. Underhill* (134 F.4th 1025, 9th Cir. 2025, quotes at "slip op. at 10, 12, 13" — see CC-2); *Meyer* (8th Cir. 2021). Also *Mitchell v. Wisconsin* cited "588 U.S. 840 (2019) (plurality), 139 S. Ct. 2525, 2539" — mixing U.S. and S. Ct. reporters in one pinpoint.
- **Fix:** confirm *Newman*/*Meyer* quotes; reconcile *Newman*'s pinpoint to 134 F.4th pagination; normalize the *Mitchell* pinpoint (prefer the U.S. reporter page when the slot exists, or footnote the parallel S. Ct. cite).
- **needs_cl:** **Yes** — *Newman v. Underhill* (9th Cir.), *United States v. Meyer* (8th Cir.), *Mitchell* pinpoint form.

### B-M10 · Border Searches · device-split circuit quotes — live-verify
- **Dimension:** D2/D3/D1. Framing PASSES — the split is annotated, circuits named, "no nationwide device rule" stated; *Brignoni-Ponce* ancestry-factor honestly caveated.
- **Locator:** *Cotterman* (709 F.3d 952, "slip op., at 17" — CC-2), *Cano* (934 F.3d 1002, "slip op., at 5" — CC-2), *Kolsuz* (890 F.3d 133, 146), *Aigbekaen* (943 F.3d 713, 721), *Touset* (890 F.3d 1227, Part III.A), *Alasaad* (988 F.3d 8, 21–22).
- **Fix:** confirm each quote; reconcile the *Cotterman*/*Cano* slip-op pinpoints to their published F.3d pagination.
- **needs_cl:** **Yes** — the device-split set above.

### B-M11 · Securing the Scene · *August* 4-part test quote + slip-op pinpoint
- **Dimension:** D3/D2/D1. Framing PASSES — *August* is honestly labeled a "doctrinal-extension flag (*Buie* outside arrest / into curtilage), not an opinion-recognized circuit split."
- **Locator:** *United States v. August* (136 F.4th 595, 5th Cir. 2025, quote at "slip op., at 5" — CC-2); *Conner* (127 F.3d 663, 666).
- **Fix:** confirm the 4-part test quote; reconcile *August*'s pinpoint to 136 F.4th pagination.
- **needs_cl:** **Yes** — *United States v. August* (5th Cir.), *United States v. Conner* (8th Cir.).

### CC-2 · Cross-cutting · slip-op pinpoints used for cases that carry a final published reporter cite
- **Dimension:** D7 (citation hygiene) + D1 (pinpoint verifiability). Does not fail SR-2; systemic across the cluster.
- **Affected (non-exhaustive):** *Graham v. Barnette* (5 F.4th 872 → "slip op. at 10"), *Carloss* (818 F.3d 988 → "slip op. at 10–11"), *French v. Merrill* (15 F.4th 116 → "slip op. at 39"), *Cotterman* (709 F.3d 952 → "slip op., at 17"), *Cano* (934 F.3d 1002 → "slip op., at 5"), *August* (136 F.4th 595 → "slip op., at 5"), *Newman* (134 F.4th 1025 → "slip op. at 10/12/13"). (SCOTUS slip-op pinpoints for genuinely un-paginated recent cases — *Case v. Montana* 2026, *Caniglia* 2021, *Lange* 2021, *King* 2011, *Collins* 2018 — are a separate, more defensible practice, though *Caniglia*/*Lange*/*King*/*Collins* now have U.S. pagination.)
- **Problem:** Where a case has a final F.3d/F.4th reporter page, the Bluebook pinpoint is the reporter page (e.g., `15 F.4th at 130`), not the slip-op page. Slip-op pinpoints on published opinions are (a) harder to verify against CL's `html_with_citations` and (b) will read as unfinished to an instructor.
- **Fix:** on the serial lane (which must read these opinions anyway for the quote confirmations above), capture the **reporter pinpoint page** and normalize each slip-op citation to it.
- **needs_cl:** **Yes** — the set above (folded into the per-page quote confirmations).

---

## LOW-severity findings

### CC-1 · Cross-cutting · dedicated `amendment:` frontmatter field absent on 6 of 13 pages
- **Dimension:** D10 (structure / template consistency). Does **not** fail SR-2 and does **not** fail LINT-3.
- **Missing the dedicated field:** Automobile Exception · Exigent Circumstances and Hot Pursuit · Search Incident to Arrest · Consent Searches · Knock and Talk · Special Needs and Administrative Searches. **Present on:** PC&RS, Warrant Requirement, Plain View, Emergency Aid, Community Caretaking, Border Searches, Securing the Scene.
- **Verification:** `scripts/lint/lint3_structure.py` reads `amendment` / `controlling_amendment` **if present, else parses the amendment from `jurisdiction:`/body**. Every affected page carries `jurisdiction: Federal (U.S. Const. amend. IV)`, so the fallback finds exactly one controlling amendment → LINT-3 does **not** flag them (roster: LINT-3 = 2 LOW corpus-wide, 0 med/high). The spec itself tolerates this ("pre-overhaul pages carry the amendment inside `jurisdiction:`, not a dedicated field").
- **Problem:** Purely a consistency wrinkle inside the **overhauled** set — 7 pages adopt the §8.1 dedicated field, 6 do not. Cosmetic; no display or gate impact.
- **Fix (optional, deterministic):** add `amendment: "U.S. Const. amend. IV"` to the 6 pages for template uniformity. Non-blocking.
- **needs_cl:** No.

### CC-1b · Special Needs and Administrative Searches · `title:` frontmatter field absent
- **Dimension:** D10. Does not fail SR-2.
- **Locator:** frontmatter carries `aliases`, `topic`, `type`, `jurisdiction`, `status`, `related` — but **no `title:`** (every other cluster-B page has one). Display is unaffected (Quartz derives the title from the H1 `# Special Needs and Administrative Searches`).
- **Fix:** add `title: "Special Needs and Administrative Searches"` for template uniformity. Non-blocking.
- **needs_cl:** No.

### Per-page LOW `needs_cl` routing flags (no severity beyond the CL lane)
- **SITA** — *Trupiano* (334 U.S. 699) / *Rabinowitz* good-law history (folded into B-H1's deletion, but the history statement may be spot-confirmed); *Davis*(4th)/*Perez*(1st)/*Braxton*(10th) recent-dev quotes.
- **Consent** — *Lewis*(6th Cir. 2023) / *Carlton Williams*(3d Cir. 2018) recent-dev quotes.
- **Knock and Talk** — *Walker*/*Lundin*/*French* quotes (folded into CC-2).
- **Special Needs** — *Payne*(9th)/*Oliveras*(2d) recent-dev quotes; *Frank v. Maryland* overruled-status + *Wyman v. James* good-law niche.
- **Automobile / Exigent** — CC-1 amendment field (above).

---

## Confirmations demanded by the review brief

### The exhaustive-treatment set is genuinely exhaustive (§6.6)
| Page | Verdict | Evidence of genuine depth |
|---|---|---|
| **Knock and Talk** | **Exhaustive ✓** | Leads with the field-decisive **area · purpose · time · manner** checklist; teaches each dimension separately (customary route + "small departure" *Walker*; purpose objective test + drug-dog/flashlight; **time** 4 a.m. *Lundin* vs 5 a.m. *Walker*; **manner** knock-wait-leave, repeated intrusion *French*); plus "No Trespassing" (*Carloss*), plain-view limits (*Collins*), stays-consensual (*Bostick*/*Drayton*), *Payton* threshold + *Caniglia* no-caretaking-bootstrap, *King* no-manufactured-exigency, and an explicit knock-and-**announce** distinction. **Circuit split ANNOTATED, not resolved**, circuits named (see below). |
| **Consent Searches** | **Exhaustive ✓** | Three prongs **bulleted on their own lines up front** (per §6.2); each prong deep (voluntariness floor *Bumper* + no-warning *Schneckloth/Drayton/Robinette* + custody *Watson*; authority *Matlock/Rodriguez* + third-party limits *Chapman/Stoner* + co-tenant *Randolph/Fernandez*; scope *Jimeno* + **destruction/*Osage*** + duration/withdrawal + digital forensic). Withdrawal corollary correctly flagged circuit-developed/Persuasive-tier, not SCOTUS. |
| **Community Caretaking** | **Exhaustive ✓** | Two labeled strands; *Garner* 3-part test up front; *Rideau*/*Graham* PC-of-dangerousness; *Caniglia* on the label as "category error." See split confirmation below. |
| **Exigent Circumstances and Hot Pursuit** | **Exhaustive ✓** | Three exigencies up front; hot-vs-fresh (**Bandiero** teaching line + *Newman* continuity); *Santana* **"limited by *Lange*"** (N4) with the field-application *why*; evidence-dissipation *Schmerber → McNeely → Mitchell* + *Birchfield* cross-wrinkle; **no-police-created-exigency** *King*; **gravity** *Welsh*; scope tethered + freeze *McArthur/Segura*. |
| **Curtilage** | *(not in cluster B — Dunn factors verified as folded up front only insofar as cross-referenced from Plain View/Knock and Talk; owned by cluster A)* | — |

### The caretaking split honors the spec (S6 · R8 / §6.4.A)
- **Two pages exist:** `Emergency Aid` + `Community Caretaking` (old title aliased on Community Caretaking: `aliases: [..., "Community Caretaking and Emergency Aid"]`). **✓**
- **Scope explicit — home-barred / vehicles / persons-in-public.** Community Caretaking states it up front: "**NON-HOME** doctrine with **two labeled strands** … The **home is barred**." Emergency Aid owns the home-entry lane. **✓**
- **Emergency Aid honors the split spec:**
  - **Brigham City "basis to believe" NOT "see it"** — a **dedicated paragraph** ("Read the standard exactly — 'basis to believe,' not 'see it'") + pitfall #1 + the Mermaid node label. Source-agnostic standard preserved; L8-faithful. **✓**
  - ***Case v. Montana* Key on Emergency Aid** — re-homed from Recent-dev to Key (N5), with the "no further gloss / neither RS nor PC" holding. **✓** *(quotes → needs_cl, B-M2.)*
  - ***Caniglia*** present as the controlling **home-entry LIMIT**; ***Mincey*** stays (no murder-scene exception); *Fisher* (no ironclad proof); *Ryburn* (imminent violence); *Tyler/Clifford* fire-scene dissipation. **✓**
- **Community Caretaking honors the split spec:**
  - ***Garner* (10th Cir.) 3-part test stated up front**, numbered/bulleted, with the independent-RS backstop. **✓**
  - ***Rideau* (5th Cir. en banc)** impaired-person-in-roadway + patdown-still-needs-RS. **✓**
  - ***Graham v. Barnette* (8th Cir.)** — label a **"category error"**; serious mental-health seizure needs **probable cause of dangerousness**. **✓** *(quotes/pinpoint → needs_cl, B-M3; slip-op pinpoint → CC-2.)*
  - **Vehicles strand** — *Cady* anchor + inventory cross-link *Opperman*/*Bertine* → Special Needs/SITA. **✓**
  - Cross-link **Seizure of the Person** (caretaking-justified seizures, placed by holding, not *Terry*). **✓**
- ***Caniglia* appears on BOTH pages** — Emergency Aid (home-entry limit) **and** Community Caretaking (Key, "Limit," home-bar + category-error caveat). **✓**
- **Recent developments N5-clean on both** — circuit/state only; every SCOTUS holding (incl. *Case v. Montana*, *Caniglia*) homed to Key. **✓**

### Emergency Aid / Community Caretaking D2/L8 framing (the split's danger points) — all honored
- *Brigham City* "basis to believe" not "see it": **honored** (Emergency Aid dedicated para + pitfall; Exigent also states "a **basis to believe** … not a requirement that officers **see** the injury").
- *Caniglia* on both pages: **honored**.
- *Case v. Montana* Key on Emergency Aid: **honored**.
- Community Caretaking scope explicit (home-barred / vehicles / persons-in-public): **honored**.
- *Garner* test up front: **honored**.

### Knock-and-talk split — ANNOTATED, not resolved (S6 · §9 open item)
- Explicit "⚖ **Circuit split (annotated, not resolved)**" in the brief and Recent developments; **circuits named** — **1st** (*French*) / **9th** (*Lundin*) say bare arrest/investigative purpose **can** break the license; **10th** (*Carloss*) / **11th** (*Walker*) treat ordinary knock-and-talks as undisturbed. No national rule stated; pitfall #6 warns against stating a back-door/bare-purpose rule as settled. **✓** *(one attribution nit on the Carloss pinpoint — B-M5.)*

### D10 / N5 structural sweep (all 13 pages)
- **No SCOTUS in any Recent-developments section** — verified page-by-page; every recent-dev entry is circuit/state with an expand/narrow/split/first-impression role label. **✓ (LINT-3 roster: 0 med/high.)**
- **Section order** (Brief → Key cases → Related across doctrines → Recent developments → Visual → Sources) holds on every page; nuances/pitfalls folded into the brief (no `## Nuances`/`## Common pitfalls` headings). **✓**
- **Single controlling amendment** — every page resolves to a single Fourth-Amendment controlling amendment (Andresen's 5th-Am. discussion on Warrant Requirement is cross-reference, not a second controlling amendment); the only wrinkle is the **dedicated-field inconsistency** (CC-1, LOW).

### D6 lexicon spot-check (not primary dimension, but scanned)
- No banned "persuasive, not binding" seen in cluster B; circuit cases name the circuit; 6-tier labels used ("Binding — SCOTUS", "Binding in-circuit — Nth Cir.", "Persuasive (outside circuit)", "Persuasive — state, illustrative", "Persuasive only — non-precedential" [*Trent* on Collective Knowledge, out of cluster], "Historical"). The corpus roster shows **2 HIGH LINT-4** findings somewhere — **not localized to cluster B by this review** (D6 is out of Reviewer B's assigned set; flagged for the D6 reviewer / LINT-4 lane). The legitimate geofence *United States v. Smith* (Warrant Requirement, Plain View, Border) is **not** the banned apocryphal trio — no guardrail violation.

---

## Bottom line for the adjudicator
- **SR-2: 13/13 PASS.** No page is escalated on the composite instructor-grade gate. The exhaustive-treatment pages are genuinely exhaustive on line-drawing; the caretaking split meets the spec in full (scope explicit, *Garner* up front, *Caniglia* on both, *Case v. Montana* Key on Emergency Aid, "basis to believe" ≠ "see it", knock-and-talk split annotated not resolved).
- **One HIGH editorial fix (deterministic):** delete the visible `*[FLAG — new history note]*` marker on Search Incident to Arrest.
- **One MEDIUM cleanliness + unresolved `needs_cl`:** the PC&RS *In re Winship* HTML gate comment — confirm on CL, then delete.
- **Route to the serial CL lane (`needs_cl`):** the circuit/state quote set per page (esp. **Osage**, the **Garner/Rideau/Graham** strand, **Case v. Montana** 2026, the geofence/device splits) **and** normalize the systemic **slip-op-pinpoint-for-published-reporter** pattern (CC-2) to reporter pinpoints while those opinions are being read anyway.
- **LOW/optional:** add the dedicated `amendment:` field to 6 pages and `title:` to Special Needs for template uniformity (degrades gracefully today; not a gate blocker).
