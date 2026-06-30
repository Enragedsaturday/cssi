# CSSI — Information Architecture Spec (full build-out)

*Authored Phase 2. Adjudicated against DECISIONS.md. Status tags: **STABLE** = existing verified page, no change; **EDIT** = existing page, targeted additive edit; **NEW** = author this run.*

## Rename map — EMPTY (deliberate)
All 25 existing page slugs are **kept stable** to preserve flashcard ids + FSRS study progress (DECISIONS D-3/D-6). "Promote standing out of Exclusionary Rule" is a content split (new page + pointer), not a rename. New pages are purely additive. → `renames: {}` in ledger. This collapses the Phase 6 wikilink-rewrite to "add links to new pages" only.

## Buckets → pages (MOC order)

### 1. Foundations & history
- Common Law Origins — **STABLE**

### 2. Legal system, research & reference
- The Federal Court System — **STABLE**
- Legal Research and Case Citations — **STABLE**
- Common Legal Terms — **STABLE**
- **Case Index** — **NEW** (generated Phase 6: every verified case → cite · 1-line holding · good-law flag · CL link · home page[s])

### 3. The Fourth Amendment — framework & analysis
- Fourth Amendment Framework — **STABLE**
- Fourth Amendment Analysis Checklist — **STABLE**
- Two Definitions of Search — **STABLE**
- CREW — **STABLE**
- **Probable Cause and Reasonable Suspicion** — **NEW** (the standards-of-proof page the framework points to but never fully states)

### 4. Protected areas & threshold
- Curtilage — **STABLE**
- Abandonment — **STABLE**

### 5. Seizures of persons & force
- Seizure of the Person — **STABLE** (Hodari D. already here — today's "show of authority" note = dedupe, no re-add)
- Terry Stops and Reasonable Suspicion — **STABLE**
- Use of Force — **STABLE**
- **Collective Knowledge and the Fellow-Officer Rule** — **NEW** (vertical + horizontal; Whiteley, Hensley)

### 6. Recognized exceptions to the warrant requirement
- Arrest in the Home — **STABLE** (cross-links to Securing the Scene + Knock and Talk)
- Community Caretaking and Emergency Aid — **STABLE**
- Consent Searches — **STABLE**
- Plain View Doctrine — **STABLE**
- Automobile Exception — **STABLE**
- Search Incident to Arrest — **STABLE**
- Traffic Stops — **STABLE**
- **Knock and Talk** — **NEW** (implied license; Jardines, Kentucky v. King, French v. Merrill 1st Cir.)
- **Special Needs and Administrative Searches** — **NEW** (checkpoints, schools, probation/parole, admin/inventory)
- **Border Searches** — **NEW** (routine vs non-routine; the device forensic-search circuit split)
- **Securing the Scene: Detention, Protective Sweeps and Freezes** — **NEW** (Summers, Muehler, McArthur, Buie, Bailey, Payton enter-and-exclude, SACO/Conner-as-constructive-entry)

### 7. The warrant requirement
- **The Warrant Requirement** — **NEW** (PC for warrants, particularity, neutral & detached magistrate, Franks, knock-and-announce, anticipatory, staleness)

### 8. Remedies, standing & accountability
- The Exclusionary Rule — **EDIT** (keep the suppression spine + good-faith/attenuation/etc.; replace the in-page "standing (Rakas)" treatment with a 1-line pointer to the new Standing page)
- **Standing to Challenge a Search** — **NEW** (REP-based standing; Rakas, Rawlings, Carter, Olson, Byrd, Jones-2018; possession: actual vs constructive, joint, willful blindness)
- Section 1983 Liability and Qualified Immunity — **STABLE**
- Brady and Giglio — **STABLE**

### 9. Confessions & identifications (5A/6A — suppression of statements & IDs)
- **Due-Process Voluntariness of Confessions** — **NEW** (Brown, Ashcraft, Spano, Connelly — the pre-Miranda line)
- **Miranda and Custodial Interrogation** — **NEW** (Miranda; custody = Berkemer/Howes/JDB; interrogation = Innis; Quarles public-safety)
- **Miranda: Waiver and Invocation** — **NEW** (Edwards, Mosley, Davis, Berghuis v. Thompkins, Shatzer, Patane/Elstad fruits)
- **Sixth Amendment Right to Counsel** — **NEW** (Massiah, Brewer v. Williams, Kirby, Montejo, Patterson; offense-specific)
- **Eyewitness Identification** — **NEW** (Wade/Gilbert, Stovall, Neil v. Biggers, Manson v. Brathwaite, Perry v. NH)

### 10. Substantive defenses (adjacent — labeled non-suppression)
- **Entrapment** — **NEW** (Sorrells, Sherman, Jacobson, Russell, Mathews; subjective federal test — predisposition)

### 11. Instructor maxims & practical habits
- Three Golden Rules — **STABLE**
- Instructor Development — **EDIT** (append mark #4 "predict questions and confusions / anticipate student confusion")
- CREW — **STABLE**

## Totals
40 pages: **25 STABLE · 2 EDIT (instructor-development, exclusionary-rule) · 13 NEW doctrine + 1 NEW generated (Case Index) = 14 NEW.**
Authoring workload this run = 13 new doctrine pages + 2 edits + 1 generated index.

## Design rules
- Every doctrine page follows the `_conventions.md` template (Rule · Key cases · Nuances & limits · Common pitfalls · Visual[if multi-factor] · Flashcards · Sources). ½–1 page, digestible.
- Federal/state never blurred; SCOTUS binding, circuits persuasive (splits flagged), state illustrative+paired.
- Mermaid required where a multi-factor/branching test exists (Buie 2-prong; Miranda custody+interrogation gate; border routine/non-routine; standing decision tree; warrant validity flow).
- Dense, meaningful cross-links; every case links its CL opinion.
