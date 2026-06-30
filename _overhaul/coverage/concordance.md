# Concordance — SR-5 Discordances (Thread-N live ingest vs Thread-P prior)

> **S5 closeout, 2026-06-30 · branch `overhaul/build`.** Per R12/SR-5: where the blind live ingest (reading the actual opinion text on CourtListener) **diverged** from the frozen prior conclusion / queue-homing hint in `thread-P.md`, the divergence is logged here — **what diverged · which conclusion stands · evidence** — so no prior verified conclusion is silently overwritten and every change is auditable. Source: `_overhaul/ledger/cl-calls.log` per-case entries + the authored `content/cases/` pages. Every divergence below was resolved **home-by-holding (N1)** or **treatment-by-opinion (N4)** — i.e. the *live reading of the opinion* controls, with the prior conclusion preserved as the recorded alternative.

All affected cases **have pages** and are in the Case Index; none was dropped.

## A. Holding / ratio divergences (prior characterization vs live opinion)

| Case | What diverged | Which stands | Evidence |
|---|---|---|---|
| **State v. Mitcham** (258 Ariz. 435 (2024)) | Prior catalog characterized the exclusionary-rule exception as **independent-source**; live reading shows the Arizona Supreme Court distinguished the two exceptions and actually applied **inevitable discovery**. | **Live: inevitable discovery.** Page recites the independent-source *definition* (¶34) but the holding rests on inevitable discovery. | "would have **inevitably** obtained Mitcham's DNA profile from an independent, untainted source despite the warrantless search…" — 258 Ariz. 435, ¶37. Home = [[The Exclusionary Rule]]; related [[Nix v. Williams]] (inevitable discovery) + [[Murray v. United States]] (independent-source roots). |
| **United States v. Anchondo** (156 F.3d 1043 (10th Cir. 1998)) | Queue **mischaracterized** it as an automobile-exception case. Live holding is **search incident to arrest** (search preceding a near-contemporaneous arrest). | **Live: SITA.** | "the cocaine on the defendant's person was the result of a lawful **search incident to arrest**" *1046. Page note records the common miscite. Home re-homed to [[Automobile Exception]] *Related* with the SITA holding stated. |
| **United States v. Braxton** (61 F.4th 830 (10th Cir. 2023)) | Queue homed it on SITA as if SITA-affirmed; live ratio is **inevitable-discovery rejected** (SITA invalidity conceded by the government). | **Live: inevitable discovery did not save the search.** Homed on [[Search Incident to Arrest]] via the concession. | "the government concedes…not justified by the warrant exception for searches incident to arrest" slip op. 7; "inevitable-discovery exception…does not apply, and the gun…must be suppressed" slip op. 17. |
| **United States v. Morton** (46 F.4th 331 (5th Cir. 2022) (en banc)) | Prior hint pointed at the digital general-warrant / particularity ratio; live en-banc disposition **resolved on the good-faith exception** (the particularity discussion is concurrence/dicta). | **Live: good-faith resolution** (the squarely-decided ground). Homed [[Plain View Doctrine]] (digital-search particularity) with the good-faith resolution flagged. | Page note: "En banc; resolved on the good-faith exception." |

## B. Home re-homes (N1 — home-by-holding overrides queue homing hint)

| Case | Queue home hint | Live home (stands) | Evidence / reason |
|---|---|---|---|
| **Gerstein v. Pugh** (420 U.S. 103) | [[Seizure of the Person]] **+ [[Arrest in the Home]]** | [[Seizure of the Person]] **Anchor (sole)** — Arrest-in-the-Home **pruned** | Holding is the post-arrest prompt-PC hearing; it has no arrest-in-home basis. "judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest" *114. |
| **Winston v. Lee** (470 U.S. 753) | [[The Warrant Requirement]] **+ [[Search Incident to Arrest]]** | [[The Warrant Requirement]] **Limiting (sole)** — SITA **pruned** | Separately-warranted compelled-surgery bodily search, **not** incident to arrest. "compelled surgical intrusion…may be unreasonable even if likely to produce evidence" *759. |
| **United States v. Ramirez** (523 U.S. 65) | [[The Warrant Requirement]] **+ [[Knock and Talk]]** | [[The Warrant Requirement]] **Progeny (sole)** — Knock-and-Talk **pruned** | This is knock-and-**announce** warrant execution, not consensual knock-and-talk. Homed with Sabbath/Wilson/Richards/Banks. |
| **United States v. Van Leeuwen** (397 U.S. 249) | [[Special Needs and Administrative Searches]] | [[Terry Stops and Reasonable Suspicion]] **+ [[Two Definitions of Search]]** — Special-Needs **pruned** | Individualized-RS brief seizure of mail pending a warrant, **not** a suspicionless special-needs regime; re-homed parallel to its pair *Place*. |
| **Taylor v. Alabama** (457 U.S. 687) | [[The Exclusionary Rule]] **+ [[Due-Process Voluntariness of Confessions]]** | [[The Exclusionary Rule]] Key—Progeny **+ [[Seizure of the Person]]** — Voluntariness **dropped**, re-homed to Seizure | Holding is 4A fruits/attenuation; confession conceded 5A-**voluntary** yet suppressed — it teaches *voluntariness ≠ attenuation*. Re-homed with Dunaway/Kaupp/Brown. |
| **Cardwell v. Lewis** (417 U.S. 583) | [[Automobile Exception]] **+ [[Curtilage]]** | [[Automobile Exception]] **+ [[Two Definitions of Search]]** — Curtilage **overridden** | Ratio is reduced-vehicle-REP / no-search-of-exterior, not curtilage. |
| **Lewis v. United States (1966)** (385 U.S. 206) | [[Consent Searches]] (first) | [[Two Definitions of Search]] **primary** + Consent secondary | Home-by-holding: search-threshold / misplaced-trust ratio leads. |
| **Virginia v. Moore** (553 U.S. 164) | [[Search Incident to Arrest]] (lead) | **[[Seizure of the Person]]** lead (SITA + Exclusionary kept) | Central holding = arrest-reasonableness; led with Seizure per N1. |
| **United States v. Harris (1968)** (390 U.S. 234) | [[Plain View Doctrine]] *Related* (queue: "during a lawful inventory") | [[Plain View Doctrine]] **Key—Progeny** (role upgraded); inventory question **reserved** → reframed protective-measure + plain view | Court expressly reserved the inventory-regulation question; queue one-liner imprecise. |

## C. Treatment / good-law divergences (N4 — current vitality corrected at ingest)

| Case | Prior | Live treatment (stands) | Evidence |
|---|---|---|---|
| **Spinelli v. United States** (393 U.S. 410) | listed as live two-prong authority | **Abrogated → Historical** (two-prong replaced by *Gates* totality) | abrogated by [[Illinois v. Gates]]; homed Historical. |
| **Wolf v. Colorado** (338 U.S. 25) | — | **Overruled on remedy by *Mapp*** (incorporation half survived) → Historical / foil | "Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search" *33; overruled-on-remedy by [[Mapp v. Ohio]]. |
| **United States v. Chadwick** (433 U.S. 1) | — | **Limited by *Acevedo*** (Chadwick-Sanders container distinction collapsed for cars) | treatment=limited; by [[California v. Acevedo]]. |
| **Escobedo v. Illinois** (378 U.S. 478) | — | **Limited** (result intact; rationale recast as 5A by *Miranda*, confined by *Kirby*/*Moran*) | treatment=limited; Key—Historical home. |
| **Mathis v. United States (1968)** (391 U.S. 1) | — | **Limited by *Howes v. Fields*** (incarceration alone ≠ automatic Miranda custody; totality) | treatment=limited. |
| **Yarborough v. Alvarado** (541 U.S. 652) | — | **Qualified for juveniles by *J.D.B.*** (age part of custody when known) — good law, flagged | N4/SR-5 flag in note. |
| **Townsend v. Sain** (372 U.S. 293) | — | Voluntariness holding **good law**; separate **federal-habeas hearing holding abrogated** by *Keeney* + AEDPA §2254(e)(2) | home-by-holding (voluntariness); habeas half flagged. |
| **United States v. Agurs** (427 U.S. 97) | — | **Three-situation materiality test superseded** by single "reasonable probability" of *Bagley*; disclosure duty survives | treatment=limited; by [[United States v. Bagley]]. |
| **Byars v. United States** (273 U.S. 28) | — | good (not overruled); **silver-platter framework superseded** by *Elkins*/*Mapp* → noted | treatment good + history note. |
| **United States v. Harris (1971)** (403 U.S. 573) | — | good (penal-interest factor survives under *Gates* totality); **Aguilar-Spinelli framework superseded** | treatment good + history note. |

## D. Identity / caption fixes (SR-5)

| Case | Fix | Evidence |
|---|---|---|
| **Florida v. Meyers** (466 U.S. 380) | Queue typo "Florida v. **Myers**" → filed correct official caption **"Florida v. Meyers"** + alias "Florida v. Myers" | CL/official caption "FLORIDA v. MEYERS, AKA WEYERS". |
| **Brower v. County of Inyo** (489 U.S. 593) | Filed under official caption "Brower v. County of Inyo" + alias "Brower v. Inyo County" (queue form) | CL caption. |
| **Henry v. United States (1959)** / **Harris v. United States (1968)** / **United States v. Harris (1971)** / **Mathis v. United States (1968)** / **Lewis v. United States (1966)** | Year-suffix disambiguation (R5 reversed-pair / same-stem collisions) + bare aliases | per-case filenames + aliases recorded. |

---

> **Concordance result:** all SR-5 divergences are resolved **home-by-holding / treatment-by-opinion** with the prior conclusion preserved as the recorded alternative. **No prior verified conclusion is silently absent or silently overwritten** (cross-check: `prior-reconciliation.md` — 0 regressions across 346 Thread-P cases).
