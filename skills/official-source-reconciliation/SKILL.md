# Official Source Reconciliation

## Purpose

Compare meeting statements with provided official source excerpts.

## When to Use

Use before design impact analysis when an official source excerpt is available.

## Inputs

- Meeting evidence
- Official source excerpt
- Source manifest

## Process

1. Extract claims from the official source excerpt.
2. Match meeting statements to source claims.
3. Classify alignment status.
4. Identify conflicts, gaps, and required actions.

## Outputs

- Official source reconciliation table

## Quality Checks

- Alignment status is explicit.
- Missing evidence remains marked.
- Official source does not become approval by itself.

## Failure Modes

- Overstating source applicability.
- Treating partial alignment as confirmed design.

## Human Review Required

Required for conflicts, gaps, and design impact interpretation.

## Example Inputs

- `samples/input/sample_sse_network_alignment_meeting.md`
- `samples/input/sample_official_source_excerpt.md`

## Example Outputs

- `samples/output/sample_official_source_reconciliation.md`
