# Scenario 002 Existing Design Baseline

## Baseline Metadata

| Baseline ID | Scenario | Status | Date | Notes |
| --- | --- | --- | --- | --- |
| BASE-002 | Northstar Manufacturing | review_required | 2026-04-25 | Synthetic baseline for data center resilience and monitoring review |

## Current Resilience Assumption

Primary-DC is the normal operations target. DR-DC is available for continuity scenarios, but monitoring behavior during failover is not fully defined.

## Current Communication Matrix Assumption

The communication matrix includes branch-to-Primary-DC application reachability. Branch-to-DR management traffic is not approved as a baseline communication flow.

## Current Monitoring Assumption

Monitoring-System receives basic availability events. Alert correlation, retention, and triage ownership remain unresolved.

## Baseline Open Items

- Confirm management traffic scope during DR failover.
- Confirm alert ownership during Primary-DC to DR-DC transition.
- Confirm monitoring retention and event correlation behavior.
