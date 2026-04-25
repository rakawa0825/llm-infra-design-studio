# Case 007 Report

## Summary

v0.8 adds contract failure and review-required fixtures for the LLM Contract Layer.

## Result

Status: passed

## Rejected Failure Cases

- `invalid_approved_by_human_output.json`
- `invalid_missing_source_references_output.json`
- `invalid_empty_human_approval_points_output.json`
- `invalid_assumption_promoted_to_fact_output.json`
- `invalid_design_update_marked_approved_output.json`
- `invalid_unresolved_item_closed_output.json`
- `approved_by_human` result status.
- Missing `source_references`.
- Empty `human_approval_points`.
- Assumption-like claim under confirmed facts.
- Approval-like artifact update status.
- Unresolved item marked `closed`.

## Accepted Review Cases

- `valid_review_required_output.json`
- `valid_needs_more_information_output.json`
- `review_required` output with source-backed facts and human approval points.
- `needs_more_information` output with information gaps and do-not-reflect-yet items.

## Remaining Gaps

- The validator is intentionally lightweight.
- More contract failure fixtures should be added before optional LLM integration.
