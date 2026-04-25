# v0.3 Evidence-to-Decision Loop Review

## Executive Summary

v0.3 adds an Evidence-to-Decision Loop on top of the v0.2 meeting-to-design slice. The new loop combines meeting evidence, a synthetic official source excerpt, and an existing design baseline into a decision packet for human review. It prepares information gap requests and design reflection requests without approving or applying design updates.

The implementation preserves the repository's core boundary: LLMs structure evidence and draft review artifacts, while humans approve decisions, risk, baseline reflection, and unresolved item closure.

## Files Added

| Area | Files |
| --- | --- |
| Docs | `docs/evidence_to_decision_loop.md`, `docs/daily_design_operation_model.md` |
| Workflow | `workflows/10_evidence_to_decision_loop.md` |
| Templates | `templates/design_decision_packet_template.md`, `templates/information_gap_request_template.md`, `templates/official_source_reconciliation_template.md`, `templates/design_reflection_request_template.md` |
| Skills | `skills/evidence-registration/SKILL.md`, `skills/official-source-reconciliation/SKILL.md`, `skills/design-baseline-comparison/SKILL.md`, `skills/design-decision-packet-generation/SKILL.md`, `skills/information-gap-request/SKILL.md` |
| Agent | `agents/evidence-reconciliation-lead.md` |
| Inputs | `samples/input/sample_sse_network_alignment_meeting.md`, `samples/input/sample_official_source_excerpt.md`, `samples/input/sample_existing_design_baseline.md` |
| Outputs | `samples/output/sample_official_source_reconciliation.md`, `samples/output/sample_information_gap_request.md`, `samples/output/sample_design_decision_packet.md`, `samples/output/sample_design_reflection_request.md` |
| Evals | `evals/cases/case_003_evidence_to_decision_loop.md`, `evals/expected/case_003_expected.md`, `evals/reports/case_003_report.md` |

## Files Updated

| File | Update |
| --- | --- |
| `README.md` | Added v0.3 direction section. |
| agent boundary files | Clarified evidence reconciliation, verification, governance, lifecycle, facilitation, issue/decision, and artifact-generation boundaries. |
| `scripts/validate_output_schema.py` | Added v0.3 sample output heading and column checks. |
| `scripts/compare_expected_outputs.py` | Added case 003 token checks. |

## What v0.3 Demonstrates

- Meeting statements are reconciled with source excerpts instead of accepted directly.
- Official source excerpts support evidence but do not approve a design.
- Existing design baseline assumptions remain visible.
- Information gaps become targeted requests.
- Design decision packets separate facts, assumptions, gaps, impacts, and approvals.
- Design reflection requests remain approval-gated.

## Remaining Gaps

| Gap | Recommendation |
| --- | --- |
| Status values are checked only lightly. | Add strict status validation in a future CLI or schema module. |
| Baseline comparison is still sample-driven. | Add baseline state files or a CLI workflow in v0.4. |
| No automated artifact reflection exists. | Keep this out of scope until approval handling is stronger. |

## Validation Results

| Command | Result |
| --- | --- |
| `python3 scripts/check_sensitive_identifiers.py` | Passed |
| `python3 scripts/validate_output_schema.py` | Passed |
| `python3 scripts/check_unresolved_assertions.py` | Passed |
| `python3 scripts/compare_expected_outputs.py` | Passed |
| `git diff --check` | Passed |

## Public-Safety Check

Working-file public-safe grep returned no hits for restricted markers or local email patterns. Private project directories were not read.

## Recommended Commit Message

```text
Add evidence-to-decision loop
```

## Directory Handling

Only repository-local public-safe files were used. Private directories named in the working instructions were not read.
