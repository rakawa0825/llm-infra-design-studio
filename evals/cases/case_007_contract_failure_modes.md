# Case 007: Contract Failure Modes

## Goal

Verify that contract failure fixtures are rejected and review-required fixtures are accepted before any future LLM integration.

## Fixtures

- `valid_review_required_output.json`
- `valid_needs_more_information_output.json`
- `invalid_approved_by_human_output.json`
- `invalid_missing_source_references_output.json`
- `invalid_empty_human_approval_points_output.json`
- `invalid_assumption_promoted_to_fact_output.json`
- `invalid_design_update_marked_approved_output.json`
- `invalid_unresolved_item_closed_output.json`

## Checks

- Invalid `approved_by_human` output is rejected.
- Missing source references are rejected.
- Empty human approval points are rejected.
- Assumption promoted to fact is rejected.
- Approval-like design update language is rejected.
- Unresolved item closure without human approval is rejected.
- `review_required` output is accepted but not treated as approved.
- `needs_more_information` output is accepted but remains incomplete.

## Expected Result

The validator passes only when expected-valid fixtures pass and expected-invalid fixtures are rejected.
