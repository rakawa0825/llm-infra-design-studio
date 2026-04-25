# Design Decision Packet Generation

## Purpose

Prepare structured design decision packets for human review.

## When to Use

Use after source reconciliation, baseline comparison, and information gap identification.

## Inputs

- Official source reconciliation
- Baseline comparison notes
- Information gap requests
- Design impact analysis

## Process

1. Summarize sources and confirmed facts.
2. List assumptions and gaps.
3. Summarize baseline comparison.
4. Draft proposed artifact updates.
5. Mark human decisions required and do-not-reflect items.

## Outputs

- Design decision packet

## Quality Checks

- Decision status is not approved by default.
- Human approval requirements are explicit.
- Gaps and assumptions remain visible.

## Failure Modes

- Producing final-looking decisions.
- Omitting do-not-reflect items.

## Human Review Required

Always required before design reflection.

## Example Inputs

- `samples/output/sample_official_source_reconciliation.md`
- `samples/output/sample_information_gap_request.md`

## Example Outputs

- `samples/output/sample_design_decision_packet.md`
