# Human Approval Check

## Purpose

Ensure required approval points are explicit before decisions move forward.

## When to Use

Use before artifact update, detailed design handoff, or publication.

## Inputs

- Approval checklist
- Delta report
- Requirements table

## Example Inputs

- `samples/output/sample_human_approval_checklist.md`
- `samples/output/sample_delta_report.md`
- `samples/output/sample_requirements_table.md`

## Process

1. List required approvals.
2. Confirm approver role and decision status.
3. Separate approved, rejected, pending, and escalated items.
4. Record residual risk.

## Outputs

- Human approval checklist

## Example Outputs

- `samples/output/sample_human_approval_checklist.md`
- `templates/publication_checklist_template.md`

## Quality Checks

- No pending approval is treated as accepted.
- Risk acceptance is explicit.

## Failure Modes

- Closing unresolved issues without named approval.

## Human Review Required

Always required.
