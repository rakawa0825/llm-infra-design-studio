# Scenario 002 Requirements Table

| Requirement ID | Requirement | Status | Source ID | Confidence | Confirmation Owner | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| NS-REQ-001 | Primary-DC availability alerting should remain visible to Monitoring-System. | confirmed | NS-SRC-001, NS-SRC-004 | High | Operations lead | Supported by meeting and operations requirements. |
| NS-REQ-002 | DR-DC failover alerting may be required during resilience events. | assumption | NS-SRC-001, NS-SRC-004 | Medium | Operations lead | Ownership and alert behavior are not confirmed. |
| NS-REQ-003 | Branch-to-DR management traffic may need communication matrix entries. | customer_confirmation_required | NS-SRC-001, NS-SRC-002, NS-SRC-004 | Medium | Customer owner | Scope is not approved. |
| NS-REQ-004 | Monitoring event retention period requires vendor confirmation. | vendor_confirmation_required | NS-SRC-003, NS-SRC-004 | High | Vendor owner | Depends on selected configuration. |
| NS-REQ-005 | Alert severity mapping is a detailed-design handoff item. | detailed_design_handoff | NS-SRC-003, NS-SRC-004 | Medium | Detailed design owner | Define before operations acceptance. |

## Human Approval Points

- Do not add Branch-to-DR management traffic to baseline until customer confirms scope.
- Do not accept DR failover monitoring ownership until human review.
- Do not treat vendor answer as operations acceptance.
