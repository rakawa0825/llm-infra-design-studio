# Meeting-to-Design Update

## Goal

Connect meeting and hearing inputs to requirement updates, issue and decision logs, design deltas, artifact update proposals, and human approval checkpoints.

## Inputs

- Meeting transcript
- Source manifest
- Current requirements table
- Current communication matrix
- Current unresolved issues
- Current decision state

## Process

1. Run meeting intake and confirm source safety.
2. Update the source manifest with the meeting source ID.
3. Extract requirements, issues, decisions, and confirmation items.
4. Separate tentative decisions from confirmed decisions.
5. Classify customer, vendor, internal review, and detailed-design questions.
6. Analyze design deltas against previous understanding.
7. Draft artifact update proposal.
8. Route human approval checklist items.
9. Store open issues, decisions, deltas, and approval points for the next cycle.

## Outputs

- Meeting intake record
- Issue register
- Decision log
- Stakeholder questions
- Delta report
- Design update proposal
- Human approval checklist updates

## Quality Gate

- No meeting statement is accepted as baseline without source reference and human approval status.
- Issues and decisions remain separate.
- Unresolved items are carried forward.
- Artifact update proposals are marked as proposals.

## Human Approval / Escalation

Escalate scope changes, risk acceptance, customer-facing language, issue closure, baseline updates, and detailed-design handoff decisions.

## State Updates

- Update `state/issues.md` for open issues.
- Update `state/decisions.md` for confirmed or pending decisions.
- Update `state/delta_log.md` for design deltas.
- Update `state/approval_points.md` for approval checkpoints.

## Next Cycle

Open issues, pending decisions, and unresolved confirmation items become source inputs for the next review cycle.
