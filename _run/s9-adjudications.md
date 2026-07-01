# S9 Serial-CourtListener Adjudications (L4, concurrency-1) — 2026-06-30

Two-key discipline (L1): no legal statement asserted/changed without CL (or, where CL is
corrupted/unavailable for a post-cutoff item, primary/secondary **web L2**) evidence. Tier
re-probe: **NEW (≥20/min)** — ~9 opening calls, no OLD-5/min throttle. The only throttle hit was
the **citation-lookup batch endpoint** (`analyze_citations`), handled within-turn via
`resume_citation_analysis(wait=true)`. CL calls logged to `_overhaul/ledger/cl-calls.log`.

---

## 1. Chatrie-2026 (CRITICAL two-key) — **VERDICT: UPHELD (reframed)**
- **CL evidence:** `search(scotus, Chatrie/geofence)` returns ONLY cluster **10881683**; `read_document(10881683)` → the opinion text is ***Harmon v. ABC 2 News Station*** (E.D. Wis. 24-cv-600). **CL object 10881683 is CORRUPTED** — CL cannot two-key this case. (Matches the escalation's warning.)
- **Web L2 evidence (independent):** *Chatrie v. United States*, No. 25-112, **609 U.S. ___ (2026)**, decided **2026-06-29** — geofence/Location-History acquisition **IS** a Fourth Amendment search; geofence warrants **not** categorically unconstitutional; **vacated & remanded** PC/particularity. Confirmed across supremecourt.gov (slip op. 25-112), SCOTUSblog, Cornell LII, Justia, EPIC, IAPP, Wikipedia.
- **Action:** created `content/cases/Chatrie v. United States.md` (Binding — SCOTUS, slip-op sourced, CL-confirm pending); reframed geofence framing on **7 pages** (Two Definitions [anchor→Key], Third-Party Doctrine [Key], Exclusionary Rule, Standing, Fourth Amendment Framework, Warrant Requirement, Plain View) + Carpenter cross-link + Case Index row. Escalation file CLOSED with verdict. **0 residual** stale "pending/cert/undecided" geofence language corpus-wide. CL backfill ticket left open (never ingest 10881683).

## 2. Moore-Bush (en banc, pole-camera) — **VERDICT: Curtilage was WRONG → FIXED**
- **CL evidence:** `search_document(6348506)` (36 F.4th 320) — verbatim: *"Per curiam. The district court order granting … motions to suppress is **unanimously reversed** by the en banc court. We remand with instructions to **deny** the motions to suppress."* Six judges split **3-3** on whether it was a search; **all** agreed the ***Davis* good-faith exception** (reliance on then-binding circuit precedent *Bucci*) required reversal → **evidence ADMITTED**.
- **Adjudication:** *Two Definitions of Search* ("admitted … good-faith saved it either way") = **CORRECT/UPHELD**. *Curtilage* ("the tie affirmed suppression below") = **WRONG → corrected** to "unanimously reversed; evidence admitted; 3-3 only on the search question; Davis good-faith." (Fourth Amendment Framework already stated it correctly.)

## 3. Knight v. Jacobson URL — **DONE**
- **CL evidence:** `search(citation="300 F.3d 1272")` → cluster **778847**, *Arthur Knight v. Jacobson* (11th Cir. 2002), docket 01-15506.
- **Action:** added `https://www.courtlistener.com/opinion/778847/arthur-knight-v-jacobson-officer-badge-3359-individual/` to *Arrest in the Home* Sources (replaced "to be added at the serial-CL gate").

## 4. Good-law currency batch (SR-1) — **# checked: 453 unique cites · # changed: 0**
- **Method:** `analyze_citations` over all 456 corpus cites in 2 batches (226 + 227 = **453 unique citation strings**; ~3 non-extractable slip-op/old-English cites). **Batch 1: 226/226 verified. Batch 2: 227/227 verified.** **0 hallucinations** (the 188 "case name differs" WARNINGs are artifacts of the one-cite-per-line blob format — eyecite attaches each line's trailing token to the next cite; CL's canonical names all matched the intended cases).
- **NOT FOUND (all real cases; CL citation-index gaps for the specific reporter pincite, NOT corpus errors):** Heien v. North Carolina (574 U.S. 54 → CL indexes it as 135 S. Ct. 530, cluster 2760668, verified), **Riley v. California (573 U.S. 373)**, People v. Hughes (506 Mich. 512), State v. Mitcham (258 Ariz. 435), State v. Volle (580 P.3d 1223), United States v. Morton (46 F.4th 331). AMBIGUOUS (Patel/J.L./Samson/Saucier/NASA-FLRA/Newman) all resolved to the correct primary cluster.
- **Treatment audit:** 456 case pages → 438 good, 11 limited, 5 overruled, 2 abrogated. All 18 non-good are correctly-known historical treatments (Aguilar/Spinelli→Gates; Olmstead/Wolf/Gouled/Jones/Michigan v. Jackson→overruled; Belton/Thornton→Gant; etc.). **No case surfaced as newly negative-treated since generation.**

## 5. CL-URL identity SAMPLE (L3 meta-audit) — **# checked: 40 · pass rate: 40/40 (100%) · mismatches: 0**
- **Method:** random sample (seed 917) of 40 case pages; `search_document(opinion_id, " v. ")` across 4 batches of 10 → confirmed each stored `opinion_id` resolves AND its opinion text names the case (caption/self-cite/topic match). All 40 confirmed (e.g., Weeks, Ohio v. Robinette, Newman v. Underhill, Brady, Berghuis v. Thompkins, Wade, Buie, Garrity, Wesby, Touset, Cano, Fare v. Michael C.). The corpus's 456 stored opinion_ids are **clean**.
- **Note:** the *watch-list* probe (not the 456) surfaced a **second corrupted CL object** — see #6 (Zorn).

## 6. needs_cl recent/watch-list cases — **all REAL; 2 corrections made**
- **Confirmed real + correctly stated:** Glossip v. Oklahoma (604 U.S. 226, 2025, cluster 10339023/10776870 — Napue new trial), Barnes v. Felix (605 U.S. 73, 2025 — totality/no-time-limit), Case v. Montana (2026, cluster 10774335, Published), United States v. Trent (2026, cluster 10855903, **Unpublished** — page correctly says "non-precedential"), United States v. Hunt (2025, cluster 10661637, Published — abandonment device/data), United States v. Mendoza (2026, cluster 10771114, Published — hotel-checkout REP), Jimerson v. Lewis (116 F.4th 407, 5th Cir. 2024), Mayville (10th Cir. 2020), Small (4th Cir. 2019), Ziglar v. Abbasi (582 U.S. 120, 2017), In re Winship (397 U.S. 358 — proof-beyond-reasonable-doubt; used correctly on *Lego v. Twomey*/suspicion-ladder).
- **Correction A — Martin v. United States:** page cited **605 U.S. 371**; CL cluster 10776839 + web (Wikipedia/Justia/SCOTUS) all give **605 U.S. 395 (2025)** → **fixed 371→395** (2 occurrences, §1983 page).
- **Correction B — Zorn v. Linton (SECOND corrupted CL object):** CL cluster/opinion **10813527** ("Zorn v. Linton" in metadata) actually resolves to ***Strike 3 Holdings, LLC v. John Doe*** (D.D.C. BitTorrent copyright case) — **corrupted**, same pattern as Chatrie's 10881683. **Web L2 CONFIRMS** Zorn is real: SCOTUS **No. 25-297, 607 U.S. ___ (2026)**, decided 2026-03-23, **per curiam** summary reversal of a 2d Cir. QI denial (Vermont Capitol protest wristlock; Sotomayor, J., dissenting). The §1983 page's *statement* is correct; **fixed the Source line** — removed the corrupted CL URL, corrected 606→**607 U.S.**, added the slip-op link (25-297) and a "CL object 10813527 corrupted — do not ingest" warning.

## 7. CC-2 slip-op → reporter pinpoints — **KEEP slip-op for all 7 (no changes)**
- Graham v. Barnette, Carloss, French v. Merrill, Cotterman, Cano, August, Newman: every case page's Sources note already documents "CourtListener carries the **slip opinion**." Spot-checked **Cano** (opinion 4426344): text uses slip-opinion pagination ("UNITED STATES V. CANO / 4"), **no F.3d/F.4th reporter star-pagination**; corroborated by prior S6-CL log entries (Carloss, Newman = slip-only). Per the runbook, **KEEP slip-op** (do not fabricate a reporter page). No normalization performed.

---

## Corrupted CL objects discovered (do NOT ingest)
| CL opinion id | Indexed as | Actually resolves to |
|---|---|---|
| **10881683** | Chatrie v. United States (scotus, 25-112, 2026-06-29) | *Harmon v. ABC 2 News Station* (E.D. Wis. 24-cv-600) |
| **10813527** | Zorn v. Linton (2026-03-23) | *Strike 3 Holdings, LLC v. John Doe* (D.D.C., BitTorrent) |

Both real SCOTUS decisions were two-keyed via **web L2** (primary slip ops 25-112 and 25-297 exist on supremecourt.gov). CL backfill tickets left open for both.
