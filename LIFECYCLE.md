# Lifecycle

The full lifecycle is:

```text
Initial structuring
-> review
-> semantic delta detection
-> merge decision
-> detailed design handoff
-> implementation
-> migration
-> operation
-> change management
-> incident analysis
-> next refresh cycle
```

## Initial Structuring

Sources are collected, registered, normalized, and transformed into traceable draft artifacts.

## Lifecycle To Workflow Mapping

`SERVICE_BLUEPRINT.md` describes the recurring service loop. The files in `workflows/` are the executable Markdown process steps. This mapping keeps the broader lifecycle aligned with the workflow IDs.

| Lifecycle Stage | Workflow ID | Workflow File | Human Approval Required |
| --- | --- | --- | --- |
| Initial structuring | 00 | `workflows/00_intake.md` | Yes, for uncertain source origin or sample-safety concerns |
| Initial structuring | 01 | `workflows/01_source_manifest.md` | Yes, for source ownership or confidentiality uncertainty |
| Initial structuring | 02 | `workflows/02_normalization.md` | Yes, for canonical naming choices affecting external wording |
| Initial structuring | 03 | `workflows/03_requirement_extraction.md` | Yes, before requirements become a baseline |
| Review | 04 | `workflows/04_design_logic_review.md` | Yes, for architecture, security, operations, and migration-impact decisions |
| Review | 05 | `workflows/05_verification.md` | Yes, before publication or release readiness claims |
| Semantic delta detection | 06 | `workflows/06_delta_impact_analysis.md` | Yes, for merge, reject, or defer decisions |
| Merge decision | 07 | `workflows/07_artifact_update.md` | Yes, for customer-facing text and detailed-design handoff items |
| Detailed design handoff | 08 | `workflows/08_human_approval.md` | Yes, all final decisions remain human-owned |
| Implementation to refresh | Next cycle | Reuse `workflows/00_intake.md` through `workflows/08_human_approval.md` | Yes, when new evidence changes scope, risk, or baseline decisions |

## Review

Engineers review facts, assumptions, contradictions, unresolved issues, and proposed handoff items.

## Semantic Delta Detection

New inputs are compared with previous approved artifacts to identify changed meaning, not just changed text.

## Merge Decision

Humans decide whether a delta should update the design baseline, remain unresolved, or be rejected.

## Detailed Design Handoff

Approved high-level requirements are handed to detailed design owners with open questions clearly marked.

## Implementation To Refresh

Implementation, migration, operation, change management, and incident analysis generate new evidence for the next refresh cycle.
