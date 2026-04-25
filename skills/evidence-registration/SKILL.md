# Evidence Registration

## Purpose

Record and classify meeting evidence, official source excerpts, baseline references, and review inputs.

## When to Use

Use when new evidence enters the design lifecycle.

## Inputs

- Meeting evidence
- Official source excerpt
- Existing design baseline
- Source metadata

## Process

1. Assign or reference source IDs.
2. Classify evidence type.
3. Record source date, version, owner role, and downstream use.
4. Mark sample-safety status.

## Outputs

- Evidence registration notes
- Source manifest update candidate

## Quality Checks

- Evidence type is explicit.
- Source reference is preserved.
- Private content is not included.

## Failure Modes

- Treating evidence registration as source approval.
- Dropping source version or date.

## Human Review Required

Required for uncertain source origin and baseline use.

## Example Inputs

- `samples/input/sample_sse_network_alignment_meeting.md`
- `samples/input/sample_official_source_excerpt.md`
- `samples/input/sample_existing_design_baseline.md`

## Example Outputs

- `samples/output/sample_design_decision_packet.md`
