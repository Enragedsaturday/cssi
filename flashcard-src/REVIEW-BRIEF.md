# CSSI Flashcard Deck — adversarial REVIEW + FIX brief

You are an adversarial reviewer AND editor for ONE page's flashcard deck. You will read the deck,
the source page, and the staging manifest, find problems, and FIX them in place — then report.

## Read (only these)
1. This brief.
2. Your DECK json (a bare array of cards) — path in your task.
3. Your PAGE markdown — path in your task (the verified doctrine prose + Key cases + pitfalls).
4. Your MANIFEST `*.citations.json` if one exists — the verified ground truth for cites/holdings.

## Audit every card against these standards
- **Accuracy (highest priority):** every legal assertion must be traceable to the PAGE prose or the
  MANIFEST. Flag/fix anything fabricated, mischaracterized, or beyond the source. `cite` must match
  the manifest `bluebook` exactly; `source` must match the manifest `courtlistener_url` exactly.
  Wrong/invented reporters, pinpoints, holdings → fix or delete.
- **Guardrails:** English/colonial cases = non-binding history (must be labeled so, never the federal
  rule). NEVER assert Holiday, McCall, or Smith — delete any such card. Heller = 2A framing only.
  Mnemonics (C.R.E.W., Strive for Five, 3 Golden Rules) are maxims, not case law — no citation.
  State/circuit cases must be labeled non-binding/persuasive and paired with federal authority.
- **Atomicity:** one fact per card (a verbatim multi-part TEST may stay whole, but there should also
  be per-element cards). Split or trim non-atomic cards.
- **Active recall / unambiguous / context-anchored:** prompt names the case/doctrine; no yes/no
  prompts, no vague "Discuss…", no give-aways where the front contains the answer.
- **No duplicates / near-duplicates** within the deck.
- **Schema:** each card keeps `id, page, topic, type(qa|cloze|definition), front, back, tags[]` and
  optional `cite, source`. Keep `id` stable; only mint a new id (same slug prefix, new number) when
  you SPLIT a card. Do not collide ids.

## Output (do BOTH)
1. **Rewrite your DECK json file in place** with the corrected full array (valid JSON, bare array).
   Preserve all good cards unchanged. The deck should stay thorough — fix, don't gut it; only delete
   a card if it's unfixable (inaccurate/guardrail-violating/irredeemably duplicative).
2. **Return a concise report:** cards before → after count; list each material change (id: what & why);
   and an explicit "ACCURACY: clean" or the list of accuracy problems you fixed. If the deck was
   already solid, say so and make only minimal changes.

Be a tough reviewer but a conservative editor: never introduce new legal content not in the
page/manifest; when in doubt, delete rather than invent.
