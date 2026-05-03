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

It also performs limited relationship-aware checks:

- `REQ` items reference `SRC` evidence or are explicitly marked `source_mode: human_entered`,
- `RV` items target at least one `REQ` or `DS`,
- `PD` items address at least one `RV` and target at least one `DS`,
- `DR` items review at least one `PD`,
- `DL` items decide or reference at least one `DR`, `PD`, `RV`, or `REQ`,
- `HO` items link back to at least one `DL`, `RV`, or `REQ`,
- `VR` items list checked IDs through `validates` or `checked_ids`,
- `trace_map.md` contains the full trace chain,
- open, deferred, and pending items remain visible in `trace_map.md`.

The command reports `PASS` or `FAIL` clearly and exits nonzero when failures exist.

## Warning And Failure Behavior

Failures include:

- missing referenced IDs,
- invalid ID format,
- duplicate IDs,
- filename and metadata ID mismatch,
- missing required metadata,
- `public_safety` values other than `synthetic_only`,
- missing required minimal relationships,
- missing full trace chain in `trace_map.md`,
- open, deferred, or pending items missing from `trace_map.md`.

Warnings include:

- status values outside the current known set,
- missing non-critical trace map section headings.

Warnings do not produce a nonzero exit. Failures do.

## What It Does Not Check Yet

This first validator does not check:

- deep relationship semantics beyond the minimal checks listed above,
- whether unresolved items appear in every possible index,
- whether handoff items are complete,
- whether validation result records cover every required relationship,
- whether Markdown body language is sufficient for a design review,
- whether any item is approved for production use.

Those checks may be added later as separate validation design and implementation work.

This is intentionally a limited v0.2 prototype slice, not a general validation framework.

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
Warnings: 0
```

Failure output includes a failure list and exits nonzero.
