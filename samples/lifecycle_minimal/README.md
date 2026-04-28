# Lifecycle Minimal Sample

## Purpose

This synthetic public-safe sample demonstrates the v0.1 lifecycle from scattered infrastructure design evidence to text-based review artifacts.

It shows how customer hearing evidence, meeting context, review comments, an existing design excerpt, and a vendor-style note can become:

- evidence registry entries,
- requirement candidates,
- unresolved items,
- missing inputs,
- a design issue log,
- a requirement definition draft,
- a high-level design / basic design patch,
- a detailed-design handoff,
- a review response draft,
- a human approval checklist.

This sample is not production-ready. It does not automate final design approval. All document outputs are text-based review artifacts.

## Input files

- `input/customer_hearing_note.md`
- `input/meeting_transcript_excerpt.md`
- `input/existing_design_excerpt.md`
- `input/review_comments.yaml`
- `input/vendor_note.md`

## Intermediate files

- `intermediate/evidence_registry.yaml`
- `intermediate/requirement_candidates.yaml`
- `intermediate/unresolved_items.yaml`
- `intermediate/missing_inputs.yaml`
- `intermediate/design_issue_log.yaml`

## Output files

- `output/requirement_definition_draft.md`
- `output/high_level_design_patch.md`
- `output/detailed_design_handoff.md`
- `output/review_response_draft.md`
- `output/human_approval_checklist.md`

## Expected review path

1. Read `input/customer_hearing_note.md`.
2. Read `input/review_comments.yaml`.
3. Inspect `intermediate/evidence_registry.yaml`.
4. Inspect `intermediate/requirement_candidates.yaml`.
5. Inspect `intermediate/unresolved_items.yaml`.
6. Inspect `output/requirement_definition_draft.md`.
7. Inspect `output/high_level_design_patch.md`.
8. Inspect `output/detailed_design_handoff.md`.
9. Inspect `output/human_approval_checklist.md`.

## What the sample demonstrates

- Scattered evidence can be normalized into a registry.
- Customer intent can become requirement candidates without becoming final approved requirements.
- Unresolved inspection, exception traffic, routing policy, and monitoring questions remain visible.
- Detailed-design handoff items are separated from high-level design language.
- Human approval is required before artifact reflection.

## What the sample does not prove

- It does not prove production readiness.
- It does not prove correctness for a real customer network.
- It does not approve final design language.
- It does not generate configuration, diagrams, Word documents, Excel workbooks, or PowerPoint decks.
- It does not replace qualified engineering review.
