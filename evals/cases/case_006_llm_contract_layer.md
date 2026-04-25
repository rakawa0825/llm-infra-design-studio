# Case 006: LLM Contract Layer

## Goal

Verify that v0.7 defines a future LLM-assisted input and output contract without calling an LLM or allowing generated output to become an approved design decision.

## Inputs

- `schemas/llm_input_contract.schema.json`
- `schemas/llm_output_contract.schema.json`
- `templates/llm_input_package_template.json`
- `templates/llm_output_package_template.json`
- `samples/input/sample_llm_input_package.json`
- `samples/output/sample_llm_output_package.json`
- `scripts/validate_llm_contracts.py`

## Checks

- LLM input contract exists.
- LLM output contract exists.
- Sample input and output parse as JSON.
- Output requires human approval.
- Output does not claim approved design status.
- Uncertainty is preserved.
- Source traceability is required.
- No private identifiers appear.

## Expected Result

The contract layer is valid when future LLM-assisted output remains review-required, source-backed, uncertainty-preserving, and blocked from final approval.
