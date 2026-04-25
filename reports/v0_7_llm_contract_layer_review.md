# v0.7 LLM Contract Layer Review

## Executive Summary

v0.7 adds an LLM-ready input and output contract layer for future workflow execution. The implementation defines JSON schemas, JSON templates, synthetic sample packages, state documentation, and a local validator while preserving the boundary that LLM-assisted output cannot approve design decisions.

## Files Added

- `docs/llm_contract_layer.md`
- `docs/llm_state_model.md`
- `schemas/llm_input_contract.schema.json`
- `schemas/llm_output_contract.schema.json`
- `templates/llm_input_package_template.json`
- `templates/llm_output_package_template.json`
- `samples/input/sample_llm_input_package.json`
- `samples/output/sample_llm_output_package.json`
- `scripts/validate_llm_contracts.py`
- `evals/cases/case_006_llm_contract_layer.md`
- `evals/expected/case_006_expected.md`
- `evals/reports/case_006_report.md`
- `reports/v0_7_llm_contract_layer_review.md`

## Files Updated

- `README.md`
- `scripts/run_sample_workflow.py`
- `scripts/compare_expected_outputs.py`
- `scripts/validate_output_schema.py`
- `scripts/check_sensitive_identifiers.py`
- `reports/latest_cli_validation_run.md`

## What v0.7 Demonstrates

- The repository can define a future LLM input package without sending real data.
- The output package separates facts, assumptions, unresolved items, gaps, impacts, proposed updates, human approval points, and do-not-reflect-yet items.
- The validator catches missing required fields, missing safety constraints, missing approval points, and invalid final approval status in LLM output.
- The validation runner now includes the contract validator.

## What It Does Not Demonstrate

- It does not call an LLM.
- It does not call external APIs.
- It does not generate final design documents.
- It does not approve or update artifacts.

## Contract Validation Results

- `python3 scripts/validate_llm_contracts.py`: passed
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

- More failure-mode cases should be added before any optional LLM integration.
- Contract validation remains intentionally lightweight and does not replace full JSON Schema validation.
- Future workflow execution needs clear input selection and redaction rules.

## Recommended Commit Message

```text
Add LLM-ready input output contract
```

## Private Directory Confirmation

Private adjacent directories were not read.
