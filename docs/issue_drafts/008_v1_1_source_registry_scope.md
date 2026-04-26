# Define v1.1 Source Registry Scope

## Summary

Define the exact implementation scope for v1.1 Source Registry and Artifact Map.

## Why This Matters

The next implementation should be tightly scoped. Source registry and artifact map are the most useful next step before mock generation or LLM integration.

## Scope

- Files to create.
- Files to update.
- Scripts to add.
- Eval case.
- Validation commands.
- Commit message candidate.

## Out of Scope

- RAG implementation.
- LLM API integration.
- SaaS UI.
- Production network design automation.

## Acceptance Criteria

- v1.1 implementation plan is concrete.
- Scope is small enough for one commit.
- Validation commands are listed.
- Human approval boundary remains explicit.

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
git diff --check
```

## Labels

v1.1, planning, source-registry, artifact-map

## Priority

High
