# Scenario 003 Network Baseline

## Baseline ID

`BASE-NET-003`

## Current Assumptions

- Branch-A and Branch-B use SD-WAN connectivity for enterprise traffic.
- Primary-DC is the normal application location.
- DR-DC is available for recovery review but failover behavior is not finalized.
- Internet breakout currently does not define Cloud-Security-Service steering.
- Monitoring-System receives generic device alerts but does not define Cloud-Security-Service steering alerts.

## Unresolved Baseline Items

- Security inspection scope for branch internet traffic.
- Failover behavior between Primary-DC and DR-DC.
- Alert ownership for Cloud-Security-Service traffic steering.
- Communication matrix entries for Cloud-Security-Service.

## Approval Status

Status: `review_required`
