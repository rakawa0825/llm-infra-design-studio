# Scenario 002 Human Approval Checklist

| Approval ID | Item | Decision Scope | Approver Role | Decision Date | Decision Status | Rationale | Source Reference | Residual Risk | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NS-AP-001 | Branch-to-DR management traffic scope | Communication matrix baseline | Engineering lead | 2026-04-25 | needs_more_information | Customer confirmation required. | NS-SRC-001, NS-SRC-002 | Matrix may overstate allowed flows. | Linked to NS-GAP-001. |
| NS-AP-002 | DR failover alert ownership | Operations monitoring baseline | Operations lead | 2026-04-25 | review_required | Owner must be confirmed before baseline. | NS-SRC-001, NS-SRC-004 | Alert response may be ambiguous. | Linked to NS-GAP-002. |
| NS-AP-003 | Vendor retention and correlation behavior | Operations acceptance | Vendor owner | 2026-04-25 | vendor_confirmation_required | Configuration-dependent behavior. | NS-SRC-003 | Acceptance may change. | Linked to NS-GAP-003. |

## Approval Rules

- Pending or needs_more_information items are not approved.
- Risk acceptance requires explicit human approval.
- Design reflection requests are not baseline updates until approved.
