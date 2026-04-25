# CLI Validation Run

- timestamp: 2026-04-25T12:30:26.736658+00:00
- repository_root: `.`
- overall_status: passed

## Checked Files

- `README.md`
- `AGENTS.md`
- `SERVICE_BLUEPRINT.md`
- `LIFECYCLE.md`
- `HUMAN_GOVERNANCE.md`

## Checked Directories

- `docs`
- `workflows`
- `agents`
- `skills`
- `templates`
- `samples/input`
- `samples/output`
- `evals/cases`
- `evals/expected`
- `evals/reports`
- `scripts`
- `reports`
- `schemas`

## Sample Outputs

- `samples/output/sample_source_manifest.md`
- `samples/output/sample_requirements_table.md`
- `samples/output/sample_delta_report.md`
- `samples/output/sample_human_approval_checklist.md`
- `samples/output/sample_issue_register.md`
- `samples/output/sample_decision_log.md`
- `samples/output/sample_stakeholder_questions.md`
- `samples/output/sample_design_update_proposal.md`
- `samples/output/sample_official_source_reconciliation.md`
- `samples/output/sample_information_gap_request.md`
- `samples/output/sample_design_decision_packet.md`
- `samples/output/sample_design_reflection_request.md`
- `samples/output/scenario_002_source_manifest.md`
- `samples/output/scenario_002_requirements_table.md`
- `samples/output/scenario_002_issue_register.md`
- `samples/output/scenario_002_decision_log.md`
- `samples/output/scenario_002_delta_report.md`
- `samples/output/scenario_002_design_decision_packet.md`
- `samples/output/scenario_002_information_gap_request.md`
- `samples/output/scenario_002_design_reflection_request.md`
- `samples/output/scenario_002_human_approval_checklist.md`

## Eval Cases

- `evals/cases/case_001_basic_delta.md`
- `evals/cases/case_002_meeting_to_design_update.md`
- `evals/cases/case_003_evidence_to_decision_loop.md`
- `evals/cases/case_004_second_synthetic_scenario.md`
- `evals/cases/case_005_workflow_scaffold_generator.md`
- `evals/cases/case_006_llm_contract_layer.md`

## Generator Assets

- `scripts/generate_workflow_scaffold.py`
- `docs/workflow_scaffold_generator.md`
- `generated/scenario_003/evidence-to-decision/README.md`
- `generated/scenario_003/evidence-to-decision/design_decision_packet.md`
- `generated/scenario_003/evidence-to-decision/design_reflection_request.md`
- `generated/scenario_003/evidence-to-decision/information_gap_request.md`

## LLM Contract Assets

- `docs/llm_contract_layer.md`
- `docs/llm_state_model.md`
- `schemas/llm_input_contract.schema.json`
- `schemas/llm_output_contract.schema.json`
- `templates/llm_input_package_template.json`
- `templates/llm_output_package_template.json`
- `samples/input/sample_llm_input_package.json`
- `samples/output/sample_llm_output_package.json`
- `scripts/validate_llm_contracts.py`

## Validation Command Results

### Required files

Status: passed

### Required directories

Status: passed

### Sample outputs

Status: passed

### Eval cases

Status: passed

### Generator assets

Status: passed

### LLM contract assets

Status: passed

### scripts/check_sensitive_identifiers.py

Status: passed

- Sensitive identifier scan passed.

### scripts/validate_output_schema.py

Status: passed

- Output schema validation passed.

### scripts/check_unresolved_assertions.py

Status: passed

- Unresolved assertion check passed.

### scripts/compare_expected_outputs.py

Status: passed

- Expected output comparison passed.

### scripts/validate_llm_contracts.py

Status: passed

- LLM contract validation passed.
- - schema files found
- - templates parsed
- - samples parsed
- - constraints enforce uncertainty and approval boundaries
- - output requires human approval and do-not-reflect-yet items

### Public-safe scan

Status: passed

## Public-Safe Scan Result

Status: passed

## Next Recommended Action

Review the generated report and commit only if the workflow state is intended.
