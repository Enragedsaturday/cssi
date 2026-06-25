# CSSI Flashcard Deck — generation brief (read this fully)

You are ONE writer producing the spaced-repetition flashcard deck for ONE page of the CSSI
(Certified Search & Seizure Instructor) wiki — a federal, criminal-suppression Fourth Amendment
course. Your output is a NEW, separate dataset (JSON), not an edit to any note. Another agent will
adversarially review it. Accuracy and spaced-repetition best practices are paramount.

## Inputs (read ONLY these — keep context thin)
- This brief.
- Your assigned PAGE markdown file (path given in your task) — the verified doctrine prose,
  including its Key cases table, Nuances, Common pitfalls, and existing weak `## Flashcards`.
- Your assigned STAGING MANIFEST `*.citations.json` if one exists (verified per-case data:
  `case`, `bluebook`, `court`, `year`, `courtlistener_url`, `proposition`, `pinpoint`, `weight`,
  plus `corrections` and `non_case_items`). This is your GROUND TRUTH for cites/holdings.

## Output
Write a BARE JSON ARRAY of card objects to the exact path given in your task
(`.../flashcards/decks/<slug>.json`). No prose around it — valid JSON only.

### Card object schema (every field except cite/source is REQUIRED)
```jsonc
{
  "id": "<page-slug>-<short-kebab>-NN",   // GLOBALLY UNIQUE. MUST start with your page slug.
  "page": "<page-slug>",                  // your page's new slug (given in task)
  "topic": "<Topic Display Name>",        // given in task; drives the site's topic filter
  "type": "qa" | "cloze" | "definition",  // qa=question/answer; cloze=fill-in; definition=term→meaning
  "front": "prompt — unambiguous, context-anchored (name the case/doctrine)",
  "back":  "answer — atomic, one fact",
  "tags":  ["lowercase-kebab", "..."],    // page slug + case short name + concept tags
  "cite":  "Bluebook cite",               // OPTIONAL: include for case-specific cards
  "source":"https://www.courtlistener.com/opinion/..."  // OPTIONAL: the case's CL url from manifest
}
```

## Spaced-repetition best practices (ENFORCE — reviewer will check)
- **Atomic.** One fact per card (minimum-information principle). Split multi-part holdings into
  separate cards, EXCEPT a verbatim multi-part legal TEST may be one card if the test is a unit
  (e.g. Dunn's 4 factors quoted as the recognized 4-factor test) — but also add per-factor cards.
- **Active recall, unambiguous, context-anchored.** Always name the case/doctrine in the prompt.
  No "What did the Court hold?" without saying which case. No yes/no prompts, no vague "Discuss…".
- **Mixed card types per case** (aim to cover, where the material supports it):
  - case → holding (one line)
  - case → rule/test, quoting any multi-part test/standard VERBATIM as the page/manifest states it
  - key facts → case (recognize the case from its facts)
  - holding/proposition → case (reverse)
  - significance ("why it matters" / what doctrine it anchors)
  - common pitfall (from the page's Common pitfalls — what officers/instructors get wrong)
- **Distinction cards** where the page sets up a contrast. Examples by page:
  Hodari D. vs Torres; trespass vs privacy; abandonment vs consent/bailment; curtilage vs open
  fields; Garner as an application of Graham; show-of-authority+submission vs physical force.
- **Doctrine / "why" cards.** A few cards on the page's core rule, the analytical sequence, and the
  reason the doctrine exists — not just per-case facts.
- Prefer a verified short **direct quote** when one crisply states the rule (use the manifest's
  `proposition`/`pinpoint` or a quote already in the page body). Put the pinpoint in `cite`.
- Avoid duplicates and near-duplicates. Each card earns its place.

## Accuracy guardrails (NON-NEGOTIABLE)
- **Bounded by the verified page + manifest.** Every legal assertion must be traceable to the page
  prose or the staging manifest. Do NOT introduce cases, holdings, or quotes not present there.
- Use the manifest `bluebook` strings for `cite` and `courtlistener_url` for `source` — copy them
  exactly; do not reformat or invent reporters/pages.
- **English/colonial cases stay non-binding history** (Paxton's Case, Wilkes, Entick, etc.) — label
  them as historical/non-binding, never as the federal rule. **Never assert Holiday, McCall, or
  Smith** (unverifiable — they are intentionally absent; do not create cards about them).
- State cases only as clearly-labeled non-binding illustrations paired with the controlling federal
  authority (mirror how the page does it). Heller is a SECOND Amendment case — only the "codify a
  pre-existing right" framing, labeled as 2A, if the page uses it.
- Mnemonics (C.R.E.W., Strive for Five, the 3 Golden Rules) are instructor maxims, NOT case law —
  present them plainly; do not citation-attach them.
- If something on the page is genuinely ambiguous, OMIT it rather than guess. Do NOT call
  CourtListener — the manifest already holds verified data; flag any doubt in a trailing `_notes`
  key is NOT allowed (array must be pure cards). Just omit doubtful cards.

## Sizing (right-size to page density; "extensive" but no padding)
- Rich doctrine pages (5–7 cases): roughly **20–40 cards**.
- Smaller doctrine pages (2–3 cases): roughly **12–22 cards**.
- Practical/mnemonic pages with no cases (CREW, the checklist): roughly **8–16 cards** covering the
  mnemonic letters, the analytical steps, the "why", and common misapplications.
- Quality over count. If you can't make a card atomic + accurate + non-duplicative, drop it.

## id discipline
- Every `id` MUST begin with your page slug and be unique within your deck (e.g.
  `curtilage-dunn-4factors-01`, `curtilage-open-fields-vs-curtilage-02`). The orchestrator relies on
  slug-prefixing to keep ids unique across all decks.
- Number sequentially; keep ids stable and descriptive.

Produce the JSON array now. Validate it parses (balanced brackets, quoted keys, no trailing commas).
