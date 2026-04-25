# Sample Requirements Table

| Requirement ID | Requirement | Status | Source ID | Confidence | Confirmation Owner | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | Branch-A and Branch-B are in scope for SD-WAN migration. | Confirmed fact | SRC-001 | High | Engineering | Scope is synthetic. |
| REQ-002 | Primary-DC and DR-DC reachability should be maintained during migration. | Confirmed fact | SRC-001, SRC-002 | High | Engineering | Detailed routing design is out of scope for v0.1. |
| REQ-003 | Branch internet-bound traffic should use Cloud-Security-Service. | Assumption | SRC-001, SRC-004 | Medium | Customer | Policy behavior requires confirmation. |
| REQ-004 | Branch-B local breakout behavior during migration is unresolved. | Unresolved | SRC-001, SRC-003 | High | Customer | Must not be marked approved until confirmed. |
| REQ-005 | Monitoring-System should receive tunnel status and availability events. | Handoff | SRC-001, SRC-003, SRC-005 | Medium | Detailed design owner | Exact thresholds are deferred. |
| REQ-006 | Cloud-Security-Service log retention period requires vendor confirmation. | Unresolved | SRC-004 | High | Vendor | Needed before operations acceptance. |

## Customer Confirmation Items

- Confirm Branch-B local breakout behavior during migration.
- Confirm desired security inspection behavior for branch internet access.

## Vendor Confirmation Items

- Confirm Cloud-Security-Service log retention period.
- Confirm export format for Monitoring-System.

## Detailed-Design Handoff Items

- Define SD-WAN monitoring thresholds.
- Define log export format and integration method.
- Define routing and failover behavior for Primary-DC and DR-DC reachability.

## Human Approval Points

- Approve requirement baseline.
- Approve unresolved issue handling before detailed design handoff.
