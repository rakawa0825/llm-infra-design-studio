# Scenario 003 DR Failover Review

| dr_item_id | normal_state | failover_trigger | failover_path | restoration_path | monitoring_impact | communication_matrix_impact | security_boundary_impact | approval_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DR-003-001 | Primary-DC active | unresolved DR trigger | DR-DC path under review | unresolved | Monitoring-System alerting requires review | Cloud-Security-Service rows may need DR notes | inspection behavior during DR is unresolved | human_approval_required |
| DR-003-002 | Branch internet via reviewed steering path | Cloud-Security-Service path failure | SD-WAN-Edge-02 backup path under review | unresolved | alert owner unresolved | backup communication path needs review | excluded traffic behavior unresolved | needs_more_information |

## Human Approval Points

- DR failover behavior is not approved.
- Restoration behavior requires architecture and operations review.
