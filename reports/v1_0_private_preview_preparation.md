# v1.0 Private Preview Preparation

## Summary

v1.0 private preview preparation focuses the repository on reviewer entrypoints rather than new product features. The README is shortened, private preview guidance is added, and the scenario index gives reviewers a direct path through the strongest synthetic examples.

Goal:

```text
A reviewer can understand the project in 30 seconds, inspect one network-domain scenario in 3 minutes, and run validation in one command.
```

## Files Changed

- `README.md`
- `ROADMAP.md`
- `docs/private_preview_guide.md`
- `docs/scenario_index.md`
- `reports/v1_0_private_preview_preparation.md`

## README Changes

- Removed inline v0.2 through v0.9 version-history sections.
- Kept project overview, quick start, core workflow, human governance, network domains, validation, and public-safe boundaries.
- Added reviewer entrypoints.
- Pointed detailed version history to `ROADMAP.md`.

## Reviewer Entrypoints

- `README.md`
- `docs/private_preview_guide.md`
- `docs/scenario_index.md`
- `docs/network_design_domain_model.md`
- `samples/output/scenario_003_network_domain_review_packet.md`
- `scripts/run_sample_workflow.py`

## Remaining Public-Release Blockers

- License decision.
- GitHub Pages update.
- Final human approval before public visibility change.
- Optional README polish after GitHub rendering review.

## Validation Results

- `python3 scripts/run_sample_workflow.py --check-only`: passed
- `python3 scripts/validate_llm_contracts.py --include-negative`: passed
- `git diff --check`: passed
- working-file public-safe grep: no findings

## Recommended Commit Message

```text
Prepare v1.0 private preview
```
