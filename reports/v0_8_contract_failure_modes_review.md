# v0.8 Contract Failure Modes Review

## Executive Summary

v0.8 hardens the LLM Contract Layer by adding review-required fixtures, needs-more-information fixtures, intentionally invalid fixtures, and validator logic that distinguishes expected pass and expected fail outcomes.

## Files Added

- `docs/contract_failure_modes.md`
- `docs/review_required_policy.md`
- `evals/fixtures/llm_contract/valid_review_required_output.json`
- `evals/fixtures/llm_contract/valid_needs_more_information_output.json`
- `evals/fixtures/llm_contract/invalid_approved_by_human_output.json`
- `evals/fixtures/llm_contract/invalid_missing_source_references_output.json`
- `evals/fixtures/llm_contract/invalid_empty_human_approval_points_output.json`
- `evals/fixtures/llm_contract/invalid_assumption_promoted_to_fact_output.json`
- `evals/fixtures/llm_contract/invalid_design_update_marked_approved_output.json`
- `evals/fixtures/llm_contract/invalid_unresolved_item_closed_output.json`
- `evals/cases/case_007_contract_failure_modes.md`
- `evals/expected/case_007_expected.md`
- `evals/reports/case_007_report.md`
- `reports/v0_8_contract_failure_modes_review.md`

## Files Updated

- `README.md`
- `scripts/validate_llm_contracts.py`
- `scripts/run_sample_workflow.py`
- `scripts/compare_expected_outputs.py`
- `reports/latest_cli_validation_run.md`

## What v0.8 Demonstrates

- The contract validator can accept safe `review_required` output.
- The contract validator can accept safe `needs_more_information` output.
- The contract validator rejects generated final approval.
- The contract validator rejects missing source references.
- The contract validator rejects empty human approval points.
- The contract validator rejects approval-like artifact update language.
- The contract validator rejects unresolved item closure without human approval.

## What It Does Not Demonstrate

- It does not call an LLM.
- It does not call external APIs.
- It does not generate design documents.
- It does not approve any artifact.

## Failure Cases Covered

- `invalid_approved_by_human_output.json`
- `invalid_missing_source_references_output.json`
- `invalid_empty_human_approval_points_output.json`
- `invalid_assumption_promoted_to_fact_output.json`
- `invalid_design_update_marked_approved_output.json`
- `invalid_unresolved_item_closed_output.json`

## Review-Required Cases Covered

- `valid_review_required_output.json`
- `valid_needs_more_information_output.json`

## Validation Results

- `python3 scripts/validate_llm_contracts.py`: passed
- `python3 scripts/validate_llm_contracts.py --include-negative`: passed
- `python3 scripts/run_sample_workflow.py`: passed
- `python3 scripts/run_sample_workflow.py --check-only`: passed
- `python3 scripts/run_sample_workflow.py --write-report`: passed
- `python3 scripts/check_sensitive_identifiers.py`: passed
- `python3 scripts/validate_output_schema.py`: passed
- `python3 scripts/check_unresolved_assertions.py`: passed
- `python3 scripts/compare_expected_outputs.py`: passed
- `git diff --check`: passed

## Public-Safety Result

Working-file public-safe scan excluding repository metadata returned no findings.

## Remaining Gaps

- Fixture coverage is still intentionally small.
- Future offline mock generation should reuse these failure checks.
- Additional source-traceability edge cases should be added before optional LLM integration.

## Recommended Commit Message

```text
Add contract failure and review-required cases
```

## Private Directory Confirmation

Private adjacent directories were not read.
