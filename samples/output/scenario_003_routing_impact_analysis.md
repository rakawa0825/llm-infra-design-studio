# Scenario 003 Routing Impact Analysis

| route_domain | affected_site | normal_path | backup_path | traffic_steering_assumption | dependency | risk | required_confirmation | approval_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| branch_internet | Branch-A | SD-WAN-Edge-01 to Cloud-Security-Service | SD-WAN-Edge-02 under DR review | selected traffic may steer to Cloud-Security-Service | policy and routing configuration | backup path behavior is unresolved | network and architecture review | review_required |
| branch_internet | Branch-B | SD-WAN-Edge-01 to Cloud-Security-Service | SD-WAN-Edge-02 under DR review | selected traffic may steer to Cloud-Security-Service | policy and routing configuration | no approved failover behavior | human approval | review_required |

## Human Approval Points

- Routing / SD-WAN impact must be approved before artifact reflection.
- No route policy or vendor configuration is generated.
