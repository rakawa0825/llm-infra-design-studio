# Routing SD-WAN Impact Review Skill

## Purpose

Review routing and SD-WAN impact without creating vendor-specific configuration.

## When to Use

Use when evidence mentions underlay, overlay, preferred path, backup path, local internet breakout, cloud security steering, or failover behavior.

## Inputs

- Network baseline.
- Meeting notes.
- Synthetic vendor note.

## Process

1. Identify routing domain and affected site.
2. Compare normal and backup path assumptions.
3. Flag cloud security steering dependencies.
4. Preserve unresolved failover behavior.
5. Mark approval requirements.

## Outputs

- Routing impact analysis.
- Information gaps.
- Human approval points.

## Quality Checks

- No vendor configuration is generated.
- Failover assumptions remain unresolved until confirmed.
- Human approval remains required.

## Failure Modes

- Inventing route policy.
- Treating tentative traffic steering as approved.
- Missing backup path impact.

## Human Review Required

Routing, SD-WAN, and failover behavior require human approval before design updates.

## Example Inputs

- `samples/input/scenario_003_network_baseline.md`

## Example Outputs

- `samples/output/scenario_003_routing_impact_analysis.md`
