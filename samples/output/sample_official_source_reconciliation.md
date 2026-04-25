# Sample Official Source Reconciliation

| Source ID | Source Type | Source Date Or Version | Extracted Claim | Related Meeting Statement | Alignment Status | Conflict Or Gap | Required Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-007 | Synthetic official source excerpt | 2026-04-25 / v1.0 | Selected branch internet traffic can use supported traffic steering methods. | Branch internet traffic may go through Cloud-Security-Service. | partially_aligned | Meeting scope says branch internet traffic broadly; source says selected traffic. | Clarify inspection scope before baseline update. |
| SRC-007 | Synthetic official source excerpt | 2026-04-25 / v1.0 | Policy enforcement depends on configured inspection policy and tenant settings. | Inspection scope is still unclear. | aligned | No conflict; scope remains unresolved. | Create information gap request. |
| SRC-007 | Synthetic official source excerpt | 2026-04-25 / v1.0 | Failover depends on SD-WAN edge configuration and selected traffic steering design. | Failover behavior must be confirmed. | aligned | Confirmation still required. | Keep failover as open gap. |
| SRC-007 | Synthetic official source excerpt | 2026-04-25 / v1.0 | Logging and monitoring exports require operations confirmation. | Monitoring-System must show traffic steering availability. | partially_aligned | Event type and alert behavior are not defined. | Route to operations follow-up. |

## Human Review Required

- Do not treat partial alignment as approved design.
- Review scope, failover, and monitoring gaps before reflection request approval.
