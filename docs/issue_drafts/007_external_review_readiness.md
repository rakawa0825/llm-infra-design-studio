# Prepare External Review Readiness

## Summary

Prepare the repository for review by a hiring reviewer or technical reviewer.

## Why This Matters

The repository should communicate value quickly without requiring a reviewer to read every file.

## Scope

- 30-second README check.
- 3-minute scenario path.
- One-command validation.
- Pages alignment.
- Public-safe review.
- Known limitations.

## Out of Scope

- New feature development.
- Public release.
- Real customer examples.

## Acceptance Criteria

- Reviewer path is clear.
- README, private preview guide, and scenario index are aligned.
- Validation passes.
- Known limitations are visible.

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
```

## Labels

review-readiness, documentation, private-preview

## Priority

Medium
