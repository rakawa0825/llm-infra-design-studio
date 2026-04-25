# Design Update Planning

## Purpose

Draft artifact update proposals from source-backed design deltas.

## When to Use

Use after design delta analysis and before human approval.

## Inputs

- Delta report
- Requirements table
- Issue register
- Decision log
- Templates

## Process

1. Identify affected artifacts.
2. Summarize source-backed change rationale.
3. Separate proposed updates from accepted design.
4. Mark human approval requirements and residual risk.

## Outputs

- Design update proposal
- Approval checklist updates
- Detailed-design handoff items

## Quality Checks

- Every proposed update has a source reference.
- Proposal status is explicit.
- Unresolved items remain visible.

## Failure Modes

- Treating proposals as approved design.
- Hiding scope impact as editorial cleanup.
- Dropping unresolved issues from the proposal.

## Human Review Required

Required before artifact updates become baseline.

## Example Inputs

- `samples/output/sample_issue_register.md`
- `samples/output/sample_decision_log.md`
- `templates/design_update_proposal_template.md`

## Example Outputs

- `samples/output/sample_design_update_proposal.md`
- `samples/output/sample_human_approval_checklist.md`
