# Review-to-Patch Minimal Example

## What this sample demonstrates

This sample shows how fragmented infrastructure review evidence can become a source-backed, reviewable design patch package.

The scenario is synthetic. It uses Atlas Retail, Branch-A, and Cloud-Security-Service as fictional identifiers. It does not include real customer names, real project names, real people, real diagrams, real IP addresses, or private documents.

## Scenario

Atlas Retail is reviewing a proposed branch-to-cloud security service traffic flow. The review includes:

- a proposed Branch-A to Cloud-Security-Service flow,
- unresolved inspection scope,
- a vendor lifecycle note that must not become a design constraint without approval,
- a QoS/routing detail that must remain `review_required`,
- a detailed design handoff item for implementation-level routing validation.

## Input files

- `input/source_registry.yaml`: synthetic source records.
- `input/review_comments.yaml`: fragmented review comments.
- `input/source_context_cards.yaml`: allowed and disallowed uses for each source.

## Output files

- `output/decomposed_review_items.yaml`: review comments decomposed into facts, assumptions, unresolved items, proposed changes, and handoff items.
- `output/artifact_map.yaml`: source and review item mapping to impacted artifacts.
- `output/design_patch_package.yaml`: one source-backed patch package that remains approval-gated.
- `output/human_approval_checklist.md`: human review checklist for the patch package.

## How review states are used

- `source_backed`: supported by a listed synthetic source.
- `draft`: structured but not ready for approval.
- `review_required`: requires human review before artifact reflection.
- `detailed_design_handoff`: must be handled by detailed design or implementation owners.
- `unresolved`: remains open and must not be closed automatically.

## What remains human-owned

Humans must decide:

- whether inspection scope is confirmed,
- whether QoS/routing behavior is acceptable,
- whether a vendor lifecycle note belongs in design constraints or operational notes,
- whether the communication matrix should be updated,
- whether the patch can be reflected into any approved artifact.

## Why this is not an approved design

The output package is a review artifact. It is not an approved design update, production configuration, or final architecture decision. The patch remains `review_required` and `do_not_reflect_yet: true` until a human approves it.
