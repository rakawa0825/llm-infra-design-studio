# Scenario 002 Issue Register

| Issue ID | Issue | Category | Owner Role | Status | Impact | Next Action | Source Reference | Approval Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NS-ISS-001 | Branch-to-DR management traffic scope is unclear. | Customer confirmation | Customer owner | customer_confirmation_required | May change communication matrix. | Ask customer which management flows are in scope. | NS-SRC-001, NS-SRC-002 | Yes |
| NS-ISS-002 | DR failover alert ownership is not agreed. | Internal review | Operations lead | unresolved | May affect operations readiness and escalation model. | Confirm alert triage owner. | NS-SRC-001, NS-SRC-004 | Yes |
| NS-ISS-003 | Monitoring retention and event correlation behavior are not confirmed. | Vendor confirmation | Vendor owner | vendor_confirmation_required | May affect operations acceptance. | Request configuration details from vendor. | NS-SRC-003 | Yes |
| NS-ISS-004 | Alert severity mapping requires detailed design. | Detailed-design handoff | Detailed design owner | detailed_design_handoff | May affect alert routing and response. | Define severity mapping during detailed design. | NS-SRC-003, NS-SRC-004 | Yes |

## Human Approval Points

- Do not close NS-ISS-001 without customer confirmation.
- Do not mark NS-ISS-002 confirmed without human owner decision.
- Carry NS-ISS-004 into detailed-design handoff.
