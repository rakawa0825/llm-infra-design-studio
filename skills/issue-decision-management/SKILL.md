# Issue Decision Management

## Purpose

Separate issues, tentative decisions, confirmed decisions, and unresolved items.

## When to Use

Use after meeting intake, requirement extraction, or delta analysis.

## Inputs

- Meeting intake record
- Requirements table
- Review comments
- Delta report

## Process

1. Extract issues with owner, impact, next action, and source reference.
2. Extract decision statements and classify status.
3. Keep tentative decisions separate from confirmed decisions.
4. Carry unresolved items forward until human closure.

## Outputs

- Issue register
- Decision log
- Pending decision list

## Quality Checks

- Issues and decisions are not mixed.
- Every item has a source reference.
- Pending items are not treated as accepted.

## Failure Modes

- Closing unresolved issues without approval.
- Treating meeting agreement as baseline approval.
- Missing confirmation owner.

## Human Review Required

Required for issue closure, decision confirmation, and baseline updates.

## Example Inputs

- `samples/input/sample_design_review_meeting_transcript.md`
- `samples/output/sample_delta_report.md`

## Example Outputs

- `samples/output/sample_issue_register.md`
- `samples/output/sample_decision_log.md`
