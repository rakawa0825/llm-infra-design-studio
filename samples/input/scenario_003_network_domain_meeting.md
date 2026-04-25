# Scenario 003 Network Domain Meeting

## Scenario

Atlas Retail is reviewing Cloud-Security-Service traffic steering for branch internet traffic while checking DR failover and monitoring requirements.

## Participants

- Architecture reviewer
- Network domain lead
- Security reviewer
- Operations reviewer

## Meeting Excerpt

Branch-A and Branch-B may steer selected internet traffic through Cloud-Security-Service after SD-WAN policy review. The team said SD-WAN-Edge-01 could prefer Cloud-Security-Service during normal operation, while SD-WAN-Edge-02 may be used during DR conditions.

The inspection scope is not confirmed. Retail point-of-sale traffic may need exclusion, but this requires customer confirmation and security review.

The communication matrix may need rows for Branch-A and Branch-B toward Cloud-Security-Service, but ports and protocols are still pending detailed design.

Monitoring-System should receive alerts when Cloud-Security-Service steering fails, but alert ownership and severity are unresolved.

During DR, Primary-DC traffic may fail over to DR-DC while branch internet traffic continues through Cloud-Security-Service. This is a tentative statement and must not be treated as approved design.

## Human Approval Boundary

No routing, security inspection, monitoring ownership, or DR behavior is approved by this meeting excerpt.
