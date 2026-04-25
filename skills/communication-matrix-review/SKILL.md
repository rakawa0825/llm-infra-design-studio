# Communication Matrix Review Skill

## Purpose

Review evidence for communication matrix impact.

## When to Use

Use when source/destination zones, components, protocols, ports, inspection, or logging requirements may change.

## Inputs

- Meeting notes.
- Requirements CSV.
- Existing communication assumptions.

## Process

1. Identify source and destination components.
2. Classify communication as confirmed, assumed, proposed, unresolved, or handoff.
3. Check inspection and logging dependencies.
4. Preserve source references.
5. Flag approval requirements.

## Outputs

- Communication matrix impact section.
- Unresolved communication items.
- Human approval points.

## Quality Checks

- No traffic rule is approved by the skill.
- All rows include source references.
- Proposed traffic remains proposed.

## Failure Modes

- Inventing ports or protocols.
- Treating a proposed communication as confirmed.
- Omitting logging or security dependencies.

## Human Review Required

Communication matrix changes require human approval before design reflection.

## Example Inputs

- `samples/input/scenario_003_network_requirements.csv`

## Example Outputs

- `samples/output/scenario_003_network_domain_review_packet.md`
