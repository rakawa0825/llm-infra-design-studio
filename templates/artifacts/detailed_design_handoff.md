# <artifact_title>

## Handoff status

- lifecycle_phase: "<detailed_design_handoff>"
- handoff_status: "DRAFT"
- approval_status: "REVIEW_REQUIRED"

## Purpose

Describe the items that must be handled in detailed design rather than finalized in high-level design.

Handoff items are not high-level design decisions.

## Handoff items

### `<unresolved_item_id>` `<handoff_item_title>`

- owner_role: "<owner_role>"
- source_references:
  - "<source_id>"
- required_decision: "<required_decision>"
- approval_required: true
- approval_status: "REVIEW_REQUIRED"

## Parameter or policy questions

- `<question_id>`: `<parameter_or_policy_question>`

## Source references

| Source ID | Source role | Notes |
| --- | --- | --- |
| `<source_id>` | `<source_role>` | `<notes>` |

## Approval requirement

Detailed-design handoff must be reviewed by the responsible human owner before closure.

## Return condition to upstream artifact

Return the item to the upstream artifact only when:

- the required decision is approved,
- source references are updated,
- unresolved items are closed by a human owner,
- artifact reflection is approved.
