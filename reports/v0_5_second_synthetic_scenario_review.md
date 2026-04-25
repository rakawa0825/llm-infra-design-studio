# v0.5 Second Synthetic Scenario Review

## Executive Summary

v0.5 adds a second synthetic scenario to demonstrate that the workflow is not overfitted to the original ExampleCorp branch-connectivity sample. The new Northstar Manufacturing scenario focuses on data center resilience, operations monitoring, DR failover alerting, communication matrix impact, and ownership ambiguity.

The addition remains public-safe and does not introduce generation, APIs, UI, or SaaS features. It strengthens the sample and eval coverage used by the CLI validation runner.

## Files Added

| Area | Files |
| --- | --- |
| Inputs | `samples/input/scenario_002_design_review_meeting.md`, `samples/input/scenario_002_existing_design_baseline.md`, `samples/input/scenario_002_vendor_answer.md`, `samples/input/scenario_002_operations_requirements.csv` |
| Outputs | `samples/output/scenario_002_source_manifest.md`, `samples/output/scenario_002_requirements_table.md`, `samples/output/scenario_002_issue_register.md`, `samples/output/scenario_002_decision_log.md`, `samples/output/scenario_002_delta_report.md`, `samples/output/scenario_002_design_decision_packet.md`, `samples/output/scenario_002_information_gap_request.md`, `samples/output/scenario_002_design_reflection_request.md`, `samples/output/scenario_002_human_approval_checklist.md` |
| Evals | `evals/cases/case_004_second_synthetic_scenario.md`, `evals/expected/case_004_expected.md`, `evals/reports/case_004_report.md` |

## Files Updated

| File | Update |
| --- | --- |
| `README.md` | Added v0.5 direction section. |
| `docs/cli_validation_runner.md` | Noted scenario 002 coverage. |
| `scripts/run_sample_workflow.py` | Added scenario 002 output checks and case 004 eval check. |
| `scripts/compare_expected_outputs.py` | Added case 004 expected-token check. |
| `scripts/validate_output_schema.py` | Added heading and table-column checks for scenario 002 outputs. |

## What v0.5 Demonstrates

- The workflow can handle a second synthetic scenario with a different operational shape.
- Monitoring and DR resilience concerns can be represented without becoming a monitoring tool.
- Communication matrix impact can be identified without approving changes.
- Ownership ambiguity remains unresolved until human confirmation.
- Vendor answers are evidence, not approval.

## What It Does Not Demonstrate

- It does not generate outputs from inputs.
- It does not call an LLM.
- It does not validate real infrastructure.
- It does not approve operations readiness or communication matrix updates.

## Validation Results

| Command | Result |
| --- | --- |
| `python3 scripts/run_sample_workflow.py` | Passed |
| `python3 scripts/run_sample_workflow.py --check-only` | Passed |
| `python3 scripts/run_sample_workflow.py --write-report` | Passed |
| `python3 scripts/check_sensitive_identifiers.py` | Passed |
| `python3 scripts/validate_output_schema.py` | Passed |
| `python3 scripts/check_unresolved_assertions.py` | Passed |
| `python3 scripts/compare_expected_outputs.py` | Passed |
| `git diff --check` | Passed |

## Public-Safety Result

Working-file public-safe grep returned no hits for restricted markers or local email patterns.

## Remaining Gaps

| Gap | Recommendation |
| --- | --- |
| Scenario outputs are manually authored. | Add a minimal workflow generator in a future version. |
| Schema checks are still lightweight. | Add stricter status-value checks later. |
| Scenario index is implicit. | Consider a scenario catalog if more cases are added. |

## Recommended Commit Message

```text
Add second synthetic evaluation scenario
```

## Directory Handling

Only repository-local public-safe files were used. Private directories named in the working instructions were not read.
