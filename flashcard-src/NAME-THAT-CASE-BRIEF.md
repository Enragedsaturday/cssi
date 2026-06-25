# "Name That Case" deck — generation brief (read fully before writing)

You are ONE research-writer producing part of the **Name That Case** recognition flashcard deck for
the CSSI (Certified Search & Seizure Instructor) course — a federal, criminal-procedure deck used to
cram for a *Kahoot-style "name the case from the clue" game*. Your slice = ONE doctrine bucket
(named in your task). Accuracy is paramount: a wrong holding or a fabricated cite loses the game and
breaks trust. Another agent will adversarially review your output.

## The deck's job
The player sees a CLUE and must NAME THE CASE. So the **front is the clue, the back is the answer +
everything worth knowing about that case, bundled together** (the user explicitly wants the full
bundle on ONE card per case, facts kept together — do NOT split a case across multiple cards).

## Output
Write a **bare JSON array** of card objects to the EXACT path given in your task
(`flashcard-src/decks/<your-slug>.json`). Valid JSON only — no prose around it, no trailing commas.

### Card schema (every field except cite/source REQUIRED)
```jsonc
{
  "id": "<your-slug>-<case-short>-NN", // MUST start with your file slug; globally unique; sequential
  "page": "name-that-case",            // literal, same for every card in the deck
  "topic": "Name That Case",           // literal, same for every card — this drives the study filter
  "type": "qa",
  "front": "the CLUE → ends by asking for the case",
  "back":  "the full bundle (see below), markdown-lite",
  "tags":  ["name-that-case", "<doctrine-tag>", "<case-short>", "<concept tags>"],
  "cite":  "Bluebook cite with pinpoint where apt",   // verified
  "source":"https://www.courtlistener.com/opinion/..."// the case's CourtListener URL
}
```
`page` and `topic` are LITERAL constants above — do not change them (one topic = one study filter;
the doctrine lives in `tags`). Only the `id` prefix is yours (your file slug).

## FRONT — the clue (one per case, pick the MOST identifying angle)
Craft the front so the answer is **unambiguously THIS case** — include the signature distinguishing
fact, not a generic one that fits five cases. Lead with whichever clue most identifies the case:
- **Fact pattern** (default): a tight scenario in the case's signature facts, ending "— which case?"
  e.g. *"Officers arrest a man for a suspended license, handcuff him, lock him in the squad car, then
  search his passenger compartment. Which case?"*
- **Quote / doctrine name** when THAT is the case's signature: *"Which case gave us the 'reasonable
  expectation of privacy' test?"* / *"Origin of 'fruit of the poisonous tree'?"*
- **Holding / rule** when the rule is the famous part: *"Which case held police need a warrant to
  search the digital contents of a cell phone seized incident to arrest?"*
Keep fronts concise (1–3 sentences). Never reveal the case name in the front.

## BACK — the full bundle (markdown-lite, use \n and **bold**)
One back string, formatted so it reads as a mini-flashcard. Template:
```
**<Case Name> (<year>)**
Holding: <one crisp sentence — the rule it stands for>.
Signature: <the famous quote OR doctrine label, in quotes if verbatim>.
Why it matters: <what doctrine it anchors / how it changed the law> (1 line).
⚠ Don't confuse with <Other Case> — <the one deciding fact that separates them>.   ← only when apt
```
The ⚠ line is the confusable-pair discriminator folded onto the card (per user: one card per case).
Add it for cases with a notorious near-miss (see clusters in your task). Omit if none.
Keep each line tight; the whole back should be scannable in ~5 seconds.

## VERIFICATION protocol (non-negotiable — accuracy over coverage)
1. **Reuse verified vault data first.** For any case already in the CSSI vault, copy its cite + holding
   + CourtListener URL from the verified sources rather than re-deriving:
   - Doctrine pages: `/Users/johngalt/Library/Mobile Documents/com~apple~CloudDocs/Main/CSSI/*.md`
   - Verified manifests: `.../CSSI/_staging/*.citations.json` (fields: `case`, `bluebook`, `court`,
     `year`, `courtlistener_url`, `proposition`, `pinpoint`). These are GROUND TRUTH.
   - Existing decks for style: `flashcard-src/decks/*.json`.
2. **CourtListener-verify every case NOT in the vault** (Miranda, interrogation, eyewitness ID, and
   any case you add). Use the claude.ai **CourtListener MCP** — you may need `ToolSearch` with
   `select:mcp__claude_ai_CourtListener__search,mcp__claude_ai_CourtListener__read_document` (and
   `..._search_document`, `..._get_endpoint_item`) to load the schemas first. Confirm: (a) the case is
   REAL and the cite/reporter is correct, (b) the holding you state is actually the holding
   (`read_document`/`search_document`), (c) capture the canonical CourtListener opinion URL for
   `source`. Gotchas: cluster-id ≠ opinion-id; the CL account tier is ≥20/min, so pace calls and
   back off on 429s.
3. **Never invent** a cite, reporter, pinpoint, year, or quote. If you can't verify it, OMIT the card.
   A missing card beats a wrong one.

## GUARDRAILS (carried from the vault's rulebook — see also `_conventions.md`)
- English/colonial cases (Entick, Wilkes, Paxton's Case) = non-binding HISTORY; label as such, never
  as the federal rule. Do NOT assert the apocryphal "Holiday / McCall / Smith" trio.
- Mnemonics (C.R.E.W., Three Golden Rules, Strive for Five) are instructor maxims, NOT case law —
  don't attach a cite to them; generally don't make them "Name That Case" cards at all.
- State cases only as clearly-labeled non-binding illustrations tied to the federal anchor.
- **Circuit cases**: include only genuine issue-of-first-impression / important clarifiers; LABEL the
  court in the back ("(9th Cir.)") and note it's persuasive, not nationwide binding. The
  border-device forensic-search split is explicitly wanted (label the circuits).
- If a case's holding is genuinely contested or you're unsure, OMIT rather than guess.

## SCAN for gaps
Your task lists the core cases for your bucket. Also do a brief scan for **important** cases in your
doctrine that the list missed (landmark SCOTUS or a key, well-known progeny with a nameable
signature). Add them (verified). Skip low-yield restatements — a case earns a card only if it has a
distinctive fact/holding/quote an instructor would build a clue around.

## Sizing
Right-size to your bucket's real case count — typically **15–30 cards** (one per case). Quality over
count. Don't pad; don't split a case into multiple cards.

## Worked example (one card)
```json
{
  "id": "name-that-case-exceptions-search-gant-07",
  "page": "name-that-case",
  "topic": "Name That Case",
  "type": "qa",
  "front": "Police arrest a driver for a suspended license, handcuff him, secure him in the patrol car, then search the passenger compartment of his car. Which case?",
  "back": "**Arizona v. Gant (2009)**\nHolding: Police may search a vehicle incident to a recent occupant's arrest only if the arrestee is unsecured and within reaching distance of the compartment, OR it is reasonable to believe the vehicle contains evidence of the offense of arrest.\nSignature: narrowed the old bright-line vehicle search.\nWhy it matters: replaced the broad reading of New York v. Belton; the controlling rule for vehicle SIA.\n⚠ Don't confuse with **Belton** (old bright-line: search compartment incident to any occupant's arrest) or **Riley** (cell-phone data needs a warrant).",
  "tags": ["name-that-case", "search-incident-to-arrest", "automobile", "gant", "confusable"],
  "cite": "Arizona v. Gant, 556 U.S. 332 (2009)",
  "source": "https://www.courtlistener.com/opinion/145843/arizona-v-gant/"
}
```

Produce the JSON array now. Validate it parses.
