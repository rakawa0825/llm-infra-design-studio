# Case 005: Workflow Scaffold Generator

## Goal

Verify that v0.6 can create a reusable evidence-to-decision scaffold without producing approved design content.

## Inputs

- `scripts/generate_workflow_scaffold.py`
- `generated/scenario_003/evidence-to-decision/`

## Checks

- The generator script exists.
- The evidence-to-decision scaffold exists.
- Generated files default to `draft`.
- Generated files require human approval.
- Generated files do not claim approved design status.
- Generated scaffold content remains public-safe.
- No private identifiers appear.

## Expected Result

The scaffold is valid when it creates placeholder artifacts for review and clearly keeps all design decisions under human approval.
