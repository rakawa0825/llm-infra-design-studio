# Requirement Extraction

## Goal

Extract source-backed requirements and classify uncertainty.

## Input

- Source manifest
- Normalized terms
- Communication requirements

## Process

1. Extract candidate requirements.
2. Attach source IDs.
3. Classify status as confirmed fact, assumption, unresolved, or handoff.
4. Identify confirmation owner.

## Output

- Requirements table

## Quality Gate

No requirement is accepted without a source ID.

## Human Approval / Escalation

Escalate contradictions and unowned requirements.
