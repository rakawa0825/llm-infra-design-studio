# DR Failover Review Skill

## Purpose

Review DR and failover behavior impact.

## When to Use

Use when evidence mentions normal state, failover trigger, failover path, restoration path, monitoring during failover, communication matrix impact, or security inspection impact.

## Inputs

- Network baseline.
- Meeting notes.
- Domain review packet.

## Process

1. Identify normal state and failover trigger assumptions.
2. Classify failover and restoration path impact.
3. Check monitoring and security inspection during failover.
4. Preserve unresolved DR behavior.
5. Mark operational approval requirements.

## Outputs

- DR/failover review.
- Unresolved failover items.
- Human approval points.

## Quality Checks

- No DR procedure is finalized.
- Restoration behavior remains review-required.
- Operational approval is visible.

## Failure Modes

- Treating tentative failover behavior as approved.
- Missing monitoring impact during DR.
- Missing security inspection impact.

## Human Review Required

DR and failover behavior require human approval before design reflection.

## Example Inputs

- `samples/input/scenario_003_network_domain_meeting.md`

## Example Outputs

- `samples/output/scenario_003_dr_failover_review.md`
