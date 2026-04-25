# Source Normalization

## Purpose

Normalize fragmented wording into stable terminology without changing meaning.

## When to Use

Use before extracting requirements from multiple sources.

## Inputs

- Source manifest
- Raw notes
- Existing design excerpts

## Example Inputs

- `samples/output/sample_source_manifest.md`
- `samples/input/sample_meeting_transcript.md`
- `samples/input/sample_existing_design_excerpt.md`

## Process

1. Identify component names and aliases.
2. Map aliases to canonical names.
3. Preserve source references.
4. Flag ambiguous terms.

## Outputs

- Normalized term map
- Ambiguity list

## Example Outputs

- `templates/requirements_table_template.md`
- `samples/output/sample_unresolved_issues.md`

## Quality Checks

- Original meaning is preserved.
- Ambiguities remain visible.

## Failure Modes

- Silent meaning changes.
- False alias mapping.

## Human Review Required

Required for canonical names and ambiguous mappings.
