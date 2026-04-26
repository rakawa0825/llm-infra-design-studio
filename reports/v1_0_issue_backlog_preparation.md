# v1.0 Issue Backlog Preparation

## Executive Summary

This update prepares a local GitHub Issue backlog for the project after v1.0 private preview. It does not create GitHub Issues directly. The backlog is kept in Markdown so the next roadmap items can be reviewed before being converted into GitHub Issues.

## Files Added

- `docs/project_backlog.md`
- `docs/issue_drafts/001_resume_ready_project_summary.md`
- `docs/issue_drafts/002_source_registry_and_artifact_map.md`
- `docs/issue_drafts/003_design_baseline_registry.md`
- `docs/issue_drafts/004_rag_ready_source_metadata_model.md`
- `docs/issue_drafts/005_private_preview_checklist.md`
- `docs/issue_drafts/006_license_decision.md`
- `docs/issue_drafts/007_external_review_readiness.md`
- `docs/issue_drafts/008_v1_1_source_registry_scope.md`
- `.github/ISSUE_TEMPLATE/roadmap_task.md`
- `.github/ISSUE_TEMPLATE/public_release_check.md`
- `.github/ISSUE_TEMPLATE/validation_improvement.md`
- `.github/ISSUE_TEMPLATE/domain_model_improvement.md`
- `reports/v1_0_issue_backlog_preparation.md`

## Why Issue Backlog Is Needed Now

The repository has reached v1.0 private preview. Before adding more implementation, the next work should be organized into reviewable issues that preserve scope boundaries and avoid premature API, SaaS, or LLM integration.

## Immediate Recommended Issues

1. Prepare resume-ready project summary.
2. Add source registry and artifact map.
3. Create private preview checklist.
4. Decide license before public release.

## v1.1 Recommendation

The recommended v1.1 focus is Source Registry and Artifact Map. This should define how source evidence maps to review artifacts and proposed artifact updates before future RAG-ready, MCP-ready, or mock generation workflows.

## Public Release Blockers

- License decision.
- Final public-safe review.
- GitHub Pages alignment.
- Human approval before repository visibility change.
- Confirmation that examples remain synthetic.

## Validation Results

- `python3 scripts/run_sample_workflow.py --check-only`: passed
- `python3 scripts/validate_llm_contracts.py --include-negative`: passed
- `git diff --check`: passed
- working-file public-safe grep: no findings

## Public-Safety Result

The new backlog and issue drafts are public-safe. They do not include private project data or real customer information.

## Recommended Commit Message

```text
Add v1.0 issue backlog drafts
```

## Private Directory Confirmation

Private adjacent directories were not read.
