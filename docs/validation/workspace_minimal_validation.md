# Workspace Minimal Validation

## Purpose

Workspace minimal validation checks the Markdown-only `samples/workspace_minimal` synthetic traceability sample.

It is a small deterministic validator for the first public-safe v0.2 sample shape. It does not call an LLM, run a private connector, generate artifacts, or approve design language.

## Command

```bash
python3 scripts/validate_workspace_minimal.py
```

## What The Validator Checks

The validator scans Markdown files under `samples/workspace_minimal` and detects files that contain a YAML metadata block with an `id` field.

For ID-bearing files, it checks:

- valid ID prefixes: `SRC`, `REQ`, `DS`, `RV`, `PD`, `DR`, `DL`, `HO`, `VR`,
- ID format using the `PREFIX-001` style,
- filename stem matches metadata `id`,
- IDs are unique across the workspace,
- required metadata fields exist:
  - `id`,
  - `type`,
  - `status`,
  - `human_approval`,
  - `public_safety`,
- `public_safety` is `synthetic_only`,
- referenced IDs exist for obvious relationship fields:
  - `derived_from`,
  - `targets`,
  - `related`,
  - `addresses`,
  - `reviews`,
  - `decides`,
  - `created_by`,
  - `creates_handoff`,
  - `validates`,
  - `checked_ids`.

The command reports `PASS` or `FAIL` clearly and exits nonzero when failures exist.

## What It Does Not Check Yet

This first validator does not check:

- relationship meaning or lifecycle correctness beyond confirming that referenced IDs exist,
- whether unresolved items appear in every expected index,
- whether handoff items are complete,
- whether validation result records cover every required relationship,
- whether Markdown body language is sufficient for a design review,
- whether any item is approved for production use.

Those checks may be added later as separate validation design and implementation work.

## Human Approval Boundary

This validator supports human review by catching simple ID and metadata consistency problems.

It does not replace human approval.

Humans still own:

- final design decisions,
- unresolved item closure,
- risk acceptance,
- customer-facing language,
- production-impacting interpretation,
- publication and external sharing.

Passing this validator means the synthetic sample is structurally consistent for its current limited checks. It does not prove real infrastructure design correctness or production readiness.

## Expected Output

Successful output looks like:

```text
Workspace minimal validation: PASS
Workspace: samples/workspace_minimal
Markdown files checked: 11
ID-bearing files checked: 9
IDs found: 9
```

Failure output includes a failure list and exits nonzero.
