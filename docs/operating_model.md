# Operating Model

## Purpose

LLM Infra Design Studio treats enterprise infrastructure design as a recurring, evidence-driven lifecycle. The goal is to turn meetings, hearings, review comments, and vendor answers into traceable design artifacts without replacing human engineering judgment.

## Operating Roles

| Role | Responsibility |
| --- | --- |
| PM / PL | Tracks scope, timeline, issue ownership, responsibility boundaries, and follow-up status. |
| Infrastructure Architect | Reviews end-to-end architecture consistency and dependency alignment. |
| Domain Lead | Reviews network, security, operations, or monitoring implications within a specific domain. |
| Reviewer | Challenges evidence, assumptions, contradictions, and readiness for approval. |
| Human Approver | Owns scope commitments, risk acceptance, design decisions, and handoff decisions. |

## Recurring Cycle

1. Collect meeting or hearing inputs.
2. Register sources and preserve traceability.
3. Extract requirements, issues, decisions, and confirmation items.
4. Analyze design deltas against the current understanding.
5. Draft artifact update proposals.
6. Route human approval points.
7. Store decisions and unresolved items for the next cycle.

## Meeting-to-Design Flow

Meetings are the entry point, not the product. A meeting transcript becomes useful only after it is transformed into requirements, issue records, decision records, design deltas, update proposals, and approval checkpoints.

## Issue and Decision Handling

Issues, tentative decisions, and confirmed decisions must remain separate.

| Item Type | Handling |
| --- | --- |
| Issue | Track owner, impact, next action, and confirmation need. |
| Tentative decision | Record as pending until human approval is captured. |
| Confirmed decision | Store with source reference, approver role, decision date, and rationale. |
| Unresolved item | Preserve across cycles until clarified or explicitly closed by a human decision. |

## Artifact Update Model

Design artifacts are updated through proposals. A proposal may identify affected requirements, communication matrices, monitoring notes, unresolved issue lists, or handoff items, but it is not approved design until the required human decision is recorded.

## Human Governance

Humans remain accountable for design direction, scope commitments, risk acceptance, customer-facing language, unresolved item closure, detailed-design handoff, and production-impacting decisions.

## What v0.2 Demonstrates

- Meeting intake as source evidence.
- Requirement, issue, decision, and confirmation extraction.
- Design delta analysis from meeting outcomes.
- Artifact update proposals with visible approval status.
- Preservation of unresolved items across the cycle.

## What v0.2 Does Not Do

- It does not create a meeting-minutes product.
- It does not approve design changes.
- It does not create production network configuration.
- It does not integrate with a SaaS UI, ticketing system, or live project repository.
