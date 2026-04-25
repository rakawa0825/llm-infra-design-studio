# Sample Human Approval Checklist

| Approval ID | Item | Approval Type | Required Approver | Status | Residual Risk | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| AP-001 | Requirement baseline for ExampleCorp synthetic scenario | Design baseline | Engineering lead | Pending | Assumptions may remain open. | Required before treating requirements as baseline. |
| AP-002 | Branch-B migration exception handling | Customer confirmation | Customer owner | Pending | Traffic steering design may change. | Linked to ISS-001 and DELTA-001. |
| AP-003 | Cloud-Security-Service logging retention | Vendor confirmation | Vendor owner | Pending | Operations acceptance may change. | Linked to ISS-002. |
| AP-004 | Detailed design handoff | Handoff approval | Engineering lead | Pending | Handoff may include unresolved items. | Must list unresolved items explicitly. |
| AP-005 | Production impact decisions | Production approval | Change authority | Pending | Not in scope for v0.1 sample. | No production change is authorized by this repository. |

## Approval Rules

- Pending means not approved.
- Risk acceptance requires explicit human approval.
- Customer-facing statements require human review.
