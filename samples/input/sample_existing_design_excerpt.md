# Sample Existing Design Excerpt

## Context

This synthetic excerpt represents a simplified current-state design summary.

## Current State

ExampleCorp currently connects Branch-A and Branch-B to Primary-DC using legacy WAN connectivity. DR-DC is available for continuity scenarios. Monitoring-System receives basic reachability events from data center components.

## Target Direction

The draft target direction introduces SD-WAN-Edge-01 and SD-WAN-Edge-02 for branch connectivity and uses Cloud-Security-Service for internet-bound traffic inspection.

## Addressing

Documentation-only networks are used in samples:

- Branch sample range: `192.0.2.0/24`
- Data center sample range: `198.51.100.0/24`
- Cloud service sample range: `203.0.113.0/24`
