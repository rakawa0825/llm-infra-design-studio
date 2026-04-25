# Requirements Extraction

## Purpose

Extract source-backed requirements and separate facts, assumptions, and unresolved items.

## When to Use

Use after source normalization.

## Inputs

- Source manifest
- Normalized source notes
- Communication requirements

## Example Inputs

- `samples/output/sample_source_manifest.md`
- `samples/input/sample_meeting_transcript.md`
- `samples/input/sample_communication_requirements.csv`

## Process

1. Extract candidate requirements.
2. Attach source IDs.
3. Classify each item as fact, assumption, unresolved, or handoff.
4. Mark confirmation owner.

## Outputs

- Requirements table
- Confirmation items

## Example Outputs

- `samples/output/sample_requirements_table.md`
- `samples/output/sample_unresolved_issues.md`

## Quality Checks

- No requirement lacks a source.
- Assumptions are not marked as confirmed.

## Failure Modes

- Invented requirements.
- Missing contradiction flags.

## Human Review Required

Required before requirements become baseline.
