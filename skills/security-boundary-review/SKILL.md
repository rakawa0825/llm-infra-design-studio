# Security Boundary Review Skill

## Purpose

Review security and SSE boundary impact using generic Cloud-Security-Service terminology.

## When to Use

Use when evidence mentions inspection scope, enforcement boundary, traffic steering, excluded traffic, or responsibility ownership.

## Inputs

- Meeting notes.
- Synthetic vendor note.
- Baseline security assumptions.

## Process

1. Identify traffic scope and inspection scope.
2. Identify enforcement and steering boundaries.
3. Flag exclusions and ownership gaps.
4. Separate customer and vendor confirmation needs.
5. Mark human approval points.

## Outputs

- Security boundary review.
- Confirmation items.
- Do-not-reflect-yet items.

## Quality Checks

- No real vendor policy names are used.
- Inspection scope remains unresolved when evidence is insufficient.
- Approval boundary is explicit.

## Failure Modes

- Treating generic vendor notes as approval.
- Expanding inspection scope without source evidence.
- Ignoring excluded traffic.

## Human Review Required

Inspection scope and responsibility boundary changes require human approval.

## Example Inputs

- `samples/input/scenario_003_synthetic_vendor_note.md`

## Example Outputs

- `samples/output/scenario_003_security_boundary_review.md`
