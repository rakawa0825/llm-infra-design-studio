# Network Domain Classification Skill

## Purpose

Classify source evidence into network design review domains.

## When to Use

Use when meeting evidence, source excerpts, or baseline notes may affect communication matrix, routing, security boundary, monitoring, or DR/failover artifacts.

## Inputs

- Source manifest.
- Meeting or review evidence.
- Existing design baseline.
- Domain model documents.

## Process

1. Identify explicit network design statements.
2. Classify each statement into one or more review domains.
3. Separate facts, assumptions, unresolved items, and handoff items.
4. Preserve source references.
5. Mark human approval points.

## Outputs

- Network domain review packet.
- Domain coverage table.
- Unresolved item list.

## Quality Checks

- Every classified item has a source reference.
- Assumptions remain assumptions.
- Unresolved items remain open.
- No final approval is created.

## Failure Modes

- Over-classifying generic statements.
- Treating tentative meeting statements as approved.
- Missing cross-domain impact.

## Human Review Required

Human review is required for production-impacting domain classification and artifact reflection.

## Example Inputs

- `samples/input/scenario_003_network_domain_meeting.md`
- `samples/input/scenario_003_network_baseline.md`

## Example Outputs

- `samples/output/scenario_003_network_domain_review_packet.md`
