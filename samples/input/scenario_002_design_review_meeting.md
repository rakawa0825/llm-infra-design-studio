# Scenario 002 Design Review Meeting

## Context

This is a synthetic Northstar Manufacturing design review meeting. It contains no real project data.

Northstar Manufacturing is reviewing data center resilience and operations monitoring changes for branch connectivity, Primary-DC, and DR-DC.

## Meeting Notes

**Northstar Project Lead:** The team wants clearer visibility during DR failover. We need to know whether branch-to-DR management traffic should be added to the communication matrix.

**Northstar Operations Lead:** Monitoring-System should alert when Primary-DC monitoring becomes unavailable and DR-DC monitoring takes over, but ownership for alert triage is not agreed yet.

**Northstar Network Reviewer:** SD-WAN branches can reach DR-DC, but management traffic classification is ambiguous. We should not mark all management flows as approved until the customer confirms which operations flows are in scope.

**Northstar Resilience Reviewer:** Tentatively, DR failover alerting should be included in the next design update proposal. This is not approval to change the baseline.

**Monitoring Vendor Owner:** The monitoring platform can receive availability and syslog-style events. Retention and alert correlation behavior depend on the service configuration selected during detailed design.

## Candidate Facts

- Primary-DC and DR-DC are part of the resilience review.
- Monitoring-System should support visibility during DR failover.
- Vendor behavior depends on selected monitoring configuration.

## Assumptions

- Branch-to-DR management traffic may need communication matrix entries.
- DR failover alert ownership may belong to operations, but this is not confirmed.

## Items That Must Not Be Treated As Approved

- Adding all management traffic to the communication matrix.
- Treating operations alert ownership as confirmed.
- Treating DR failover alerting as an approved baseline update.
