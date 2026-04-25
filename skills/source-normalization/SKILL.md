# Source Normalization

## Purpose

Normalize fragmented wording into stable terminology without changing meaning.

## When to Use

Use before extracting requirements from multiple sources.

## Inputs

- Source manifest
- Raw notes
- Existing design excerpts

## Process

1. Identify component names and aliases.
2. Map aliases to canonical names.
3. Preserve source references.
4. Flag ambiguous terms.

## Outputs

- Normalized term map
- Ambiguity list

## Quality Checks

- Original meaning is preserved.
- Ambiguities remain visible.

## Failure Modes

- Silent meaning changes.
- False alias mapping.

## Human Review Required

Required for canonical names and ambiguous mappings.
