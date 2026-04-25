# Monitoring Logging Review Skill

## Purpose

Review monitoring, logging, alert ownership, and operations handoff requirements.

## When to Use

Use when evidence mentions monitored components, event types, log sources, alert triggers, severity, retention, forwarding, thresholds, or owner roles.

## Inputs

- Network requirements CSV.
- Meeting notes.
- Baseline monitoring assumptions.

## Process

1. Identify monitored components.
2. Classify event or metric requirements.
3. Flag owner and threshold gaps.
4. Preserve retention and forwarding assumptions.
5. Mark detailed-design handoff items.

## Outputs

- Monitoring/logging review.
- Operations handoff items.
- Human approval points.

## Quality Checks

- Ownership gaps remain unresolved.
- Thresholds are not invented.
- Handoff items are explicit.

## Failure Modes

- Inventing alert thresholds.
- Closing ownership gaps without confirmation.
- Missing operations impact.

## Human Review Required

Monitoring ownership, thresholds, retention, and operations handoff require human review.

## Example Inputs

- `samples/input/scenario_003_network_requirements.csv`

## Example Outputs

- `samples/output/scenario_003_monitoring_logging_review.md`
