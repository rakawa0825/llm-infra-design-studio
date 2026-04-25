# Evidence-to-Decision Loop

## Goal

Convert meeting evidence, official source excerpts, and existing design baseline content into a design decision packet for human review.

## Inputs

- Meeting evidence
- Official source excerpt
- Existing design baseline
- Review comments
- Current issue register
- Current decision log

## Process

1. Register meeting evidence.
2. Register official source excerpt.
3. Register existing design baseline.
4. Extract source-backed facts.
5. Extract assumptions.
6. Reconcile with official source.
7. Compare against baseline.
8. Identify design impact.
9. Generate information gap request.
10. Generate design decision packet.
11. Generate design reflection request.
12. Route for human approval.

## Outputs

- Official source reconciliation
- Information gap request
- Design decision packet
- Design reflection request
- Approval checkpoint list

## Quality Gate

- Meeting statements are not automatically accepted.
- Official source excerpts are supporting evidence, not approval records.
- Baseline comparison is explicit.
- Reflection requests are not approved design updates.
- Human decision state is visible.

## Human Approval / Escalation

Escalate conflicts, insufficient evidence, design impact, baseline updates, risk acceptance, customer-facing implications, and artifact reflection requests.

## State Updates

- Add new gaps to `state/issues.md`.
- Add pending or approved decisions to `state/decisions.md`.
- Add baseline impact to `state/delta_log.md`.
- Add approval checkpoints to `state/approval_points.md`.

## Next Cycle

Approved changes become baseline input. Rejected, deferred, and needs-more-information items remain open for the next cycle.
