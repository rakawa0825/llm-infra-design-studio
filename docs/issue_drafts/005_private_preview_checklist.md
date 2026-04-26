# Create Private Preview Checklist

## Summary

Create a checklist before sharing the private repository with reviewers.

## Why This Matters

The repository should remain controlled and public-safe during private preview. A checklist reduces accidental exposure or overclaiming.

## Scope

- README reviewed.
- Private preview guide reviewed.
- Scenario index reviewed.
- Validation runner passed.
- No private identifiers.
- GitHub Pages copy aligned.
- Repository remains private unless approved.

## Out of Scope

- Public release.
- Repository visibility changes.
- New features.

## Acceptance Criteria

- Checklist exists and is easy to run manually.
- Validation commands are included.
- Human approval before public release is explicit.

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
python3 scripts/validate_llm_contracts.py --include-negative
```

## Labels

private-preview, release-readiness, checklist

## Priority

High
