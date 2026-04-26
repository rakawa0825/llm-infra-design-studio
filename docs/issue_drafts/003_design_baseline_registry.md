# Add Design Baseline Registry

## Summary

Define how the current design baseline is represented before deltas or proposed updates are applied.

## Why This Matters

Evidence-to-decision workflows need a clear baseline to compare against. Without a baseline registry, deltas and artifact update proposals are harder to validate.

## Scope

- Baseline ID.
- Artifact reference.
- Baseline status.
- Last reviewed date.
- Unresolved assumptions.
- Approval state.
- Link to source registry.

## Out of Scope

- Production baseline import.
- Real network diagram parsing.
- Automatic approval of baseline changes.

## Acceptance Criteria

- Baseline registry template exists.
- Synthetic sample baseline registry exists.
- Baseline entries link to source registry IDs.
- Unresolved assumptions remain visible.

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
```

## Labels

v1.1, baseline, traceability

## Priority

Medium
