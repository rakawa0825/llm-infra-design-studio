# <artifact_title>

This template is for a high-level design / basic design document patch.

## Patch status

- lifecycle_phase: "<high_level_design>"
- patch_status: "DRAFT"
- approval_status: "REVIEW_REQUIRED"
- production_readiness: "NO"

## Target artifact

- artifact_id: "<artifact_id>"
- artifact_name: "<artifact_name>"

## Target section

- section_id: "<affected_section>"
- section_title: "<section_title>"

## Current gap

Describe the current design gap, stale baseline, missing requirement, or unresolved review point.

## Proposed draft text

```text
<proposed_text>
```

This text is a draft. It must not include final routing parameters, production-ready claims, or final customer approval language.

## Source references

- `<source_id>`: `<source_summary>`

## Unresolved dependencies

- `<unresolved_item_id>`: `<unresolved_dependency>`
- `<missing_input_id>`: `<missing_input_dependency>`

## Detailed-design handoff markers

- `DETAILED_DESIGN_HANDOFF`: `<handoff_item_summary>`

Items marked `DETAILED_DESIGN_HANDOFF` must not be written as high-level design decisions.

## Human approval requirement

- approval_required: true
- approver_role: "<owner_role>"
- approval_status: "REVIEW_REQUIRED"

This patch remains a review artifact until human approval is recorded.
