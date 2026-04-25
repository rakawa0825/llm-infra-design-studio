# Sample Design Review Meeting Transcript

## Context

This is a synthetic ExampleCorp design review meeting. It contains no real project data.

## Meeting Purpose

Review branch migration requirements, communication matrix impact, monitoring readiness, and approval needs before detailed design.

## Transcript

**ExampleCorp Project Lead:** Branch-A remains in the standard SD-WAN migration path. Branch-B may need a temporary exception for local internet breakout during the first migration window, but this is not approved yet.

**ExampleCorp Network Reviewer:** If Branch-B keeps local breakout temporarily, the communication matrix may need a separate row for branch-to-cloud inspection behavior. We should not update the baseline until the customer confirms the exception.

**ExampleCorp Operations Reviewer:** Monitoring-System should receive tunnel availability events for SD-WAN-Edge-01 and SD-WAN-Edge-02. Exact alert thresholds are a detailed-design handoff item.

**Cloud-Security-Service Vendor Owner:** The service can export logs, but retention period and export format depend on the selected tenant configuration. We need a vendor confirmation item before operations acceptance.

**Engineering Lead:** Tentatively, we will draft an update proposal that separates Branch-B exception handling, monitoring thresholds, and log retention. This proposal requires human approval before any artifact becomes baseline.

## Candidate Facts

- Branch-A remains in the standard migration path.
- Monitoring-System needs tunnel availability events.
- Log retention and export format require vendor confirmation.

## Assumptions

- Branch-B may need temporary local breakout during migration.

## Items That Must Not Be Treated As Approved

- Branch-B temporary local breakout exception.
- Communication matrix baseline update for Branch-B exception behavior.
- Operations acceptance based on unconfirmed log retention.
