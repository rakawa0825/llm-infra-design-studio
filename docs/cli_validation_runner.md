# CLI Validation Runner

## Purpose

The CLI validation runner gives first-time reviewers a reproducible way to check the repository's Markdown-first workflow prototype.

It verifies that the repository structure, synthetic samples, eval cases, source registry artifacts, LLM contract fixtures, and public-safe boundaries are still coherent.

The runner supports the project goal: source-backed, reviewable, traceable, and human-approved infrastructure design workflow outputs.

## Why validation matters

LLM-assisted infrastructure design workflows can fail in subtle ways. A generated or drafted artifact may look polished while missing source references, hiding unresolved items, promoting assumptions into facts, or implying approval that humans have not granted.

Validation matters because it helps detect structural drift before review artifacts are trusted. It checks that:

- source-backed workflow assets exist,
- `review_required` and unresolved states remain visible,
- contract failure cases are rejected,
- sensitive identifiers are not present,
- sample outputs still match expected repository behavior,
- human approval boundaries remain explicit.

These checks make the repository more than a writing sample. They show evidence discipline, review-state handling, failure-mode coverage, and public-safe workflow hygiene.

## Validation commands

Recommended first command:

```bash
python3 scripts/run_sample_workflow.py --check-only
```

Deeper validation:

```bash
python3 scripts/validate_llm_contracts.py --include-negative
python3 scripts/validate_source_registry.py
python3 scripts/validate_lifecycle_minimal.py
python3 scripts/validate_artifact_generation_plan.py
python3 scripts/check_sensitive_identifiers.py
python3 scripts/validate_output_schema.py
python3 scripts/check_unresolved_assertions.py
python3 scripts/compare_expected_outputs.py
git diff --check
```

## What each check verifies

### `python3 scripts/run_sample_workflow.py --check-only`

Checks repository-level readiness: required files, required directories, sample outputs, eval cases, source registry assets, network domain assets, generator assets, LLM contract assets, validation scripts, and public-safe scan.

Why it matters: this is the one-command entry point for reviewers. It verifies that the repository is structurally coherent.

Failure examples:

- required sample output is missing,
- eval case is missing,
- validation script fails,
- public-safe scan finds a risky identifier.

### `python3 scripts/validate_llm_contracts.py --include-negative`

Checks LLM input/output contract samples and negative fixtures.

Why it matters: future LLM-assisted steps must not claim approval, omit human approval points, hide unresolved items, or promote assumptions into confirmed facts.

Failure examples:

- output status is `approved_by_human`,
- human approval points are empty,
- source references are missing,
- design update wording implies approval,
- unresolved item is closed without human approval.

### `python3 scripts/validate_source_registry.py`

Checks Source Registry and Artifact Map samples.

Why it matters: review artifacts need traceability from source evidence to impacted artifacts. This is the basis for future RAG/MCP-ready workflows without implementing RAG or MCP yet.

Failure examples:

- required headings are missing,
- source IDs are not represented in the artifact map,
- human approval boundary is absent,
- `approved_by_human` appears without a human-only note.

### `python3 scripts/validate_lifecycle_minimal.py`

Checks the lifecycle minimal synthetic sample.

Why it matters: the lifecycle sample demonstrates the v0.1 path from scattered evidence to requirement candidates, unresolved items, high-level design patch, detailed-design handoff, review response, and human approval checklist.

Failure examples:

- required lifecycle sample file is missing,
- source IDs or requirement IDs drift,
- unresolved items disappear from output artifacts,
- approval boundary markers are missing,
- detailed-design handoff is not preserved,
- public-safe terms or IPv4-looking addresses appear.

### `python3 scripts/validate_artifact_generation_plan.py`

Checks the lifecycle minimal artifact generation plan.

Why it matters: the plan connects intermediate lifecycle state to text-based document outputs through explicit template paths, output paths, source IDs, dependencies, approval gates, review states, allowed claims, forbidden claims, and validation checks.

Failure examples:

- artifact ID is missing,
- template path or output path does not exist,
- intermediate dependency is missing,
- source ID is not part of the lifecycle sample,
- review state is not `REVIEW_REQUIRED`,
- allowed or forbidden claims are empty.

### `python3 scripts/check_sensitive_identifiers.py`

Checks for risky or private identifiers in repository content.

Why it matters: all samples must remain synthetic and public-safe.

Failure examples:

- private customer or project identifier appears,
- private local email appears,
- sensitive organization name appears,
- non-public reference leaks into samples.

### `python3 scripts/validate_output_schema.py`

Checks expected headings, columns, and sample output structure.

Why it matters: workflow outputs should remain reviewable and consistent enough for humans to inspect.

Failure examples:

- required table column is missing,
- required output heading is missing,
- scenario output no longer follows the expected artifact structure.

### `python3 scripts/check_unresolved_assertions.py`

Checks that unresolved or review-required statements are not silently treated as complete.

Why it matters: uncertainty must remain visible. Infrastructure design review should not convert open questions into final-looking decisions.

Failure examples:

- unresolved item appears resolved without approval context,
- review-required item lacks human approval handling,
- assumptions are worded like confirmed facts.

### `python3 scripts/compare_expected_outputs.py`

Checks eval cases against expected tokens and behavior.

Why it matters: evals catch drift in the repository's intended examples and failure-mode coverage.

Failure examples:

- expected case token is missing,
- new scenario output no longer demonstrates required approval boundary,
- failure-mode report no longer includes the expected rejection behavior.

### `git diff --check`

Checks whitespace and patch formatting issues.

Why it matters: documentation and sample files should be clean enough for review and commit.

Failure examples:

- trailing whitespace,
- conflict markers,
- malformed patch whitespace.

## Recommended first-time reviewer flow

1. Read [README](../README.md) for the project purpose and boundaries.
2. Open [Review-to-Patch Minimal Example](../samples/review_to_patch_minimal/README.md) to inspect one small source-to-patch path.
3. Run:

   ```bash
   python3 scripts/run_sample_workflow.py --check-only
   ```

4. For deeper validation, run:

   ```bash
   python3 scripts/validate_llm_contracts.py --include-negative
   python3 scripts/validate_source_registry.py
   python3 scripts/validate_lifecycle_minimal.py
   python3 scripts/validate_artifact_generation_plan.py
   python3 scripts/check_sensitive_identifiers.py
   python3 scripts/validate_output_schema.py
   python3 scripts/check_unresolved_assertions.py
   python3 scripts/compare_expected_outputs.py
   ```

Passing checks means the current synthetic samples, contracts, fixtures, and expected outputs satisfy local repository validation rules.

It does not prove production readiness or correctness for a real-world network environment.

## Expected success output

The primary runner should end with:

```text
LLM Infra Design Studio - CLI Validation Runner
Required files: passed
Required directories: passed
Sample outputs: passed
Eval cases: passed
Source registry assets: passed
Network domain assets: passed
Generator assets: passed
LLM contract assets: passed
Validation scripts: passed
Public-safe scan: passed
Overall result: passed
```

The exact list may expand as repository validation grows.

## Failure categories

Validation failures usually fall into these categories:

- missing required file or directory,
- missing sample or eval artifact,
- schema or heading mismatch,
- missing source reference,
- lifecycle sample ID drift,
- artifact generation plan path drift,
- unresolved item handled incorrectly,
- human approval boundary missing,
- contract fixture accepted when it should be rejected,
- public-safe scan failure,
- expected-output drift,
- patch formatting issue.

When a check fails, the correct response is to inspect the source file, preserve uncertainty, and route ambiguous content to `review_required` rather than making final-looking design claims.

## What validation does not prove

Validation does not prove:

- production readiness,
- design correctness for a real customer network,
- approval by a qualified engineer,
- security certification,
- deployment safety,
- correctness of unsupported assumptions,
- readiness to use with real customer data.

Validation checks repository structure and workflow discipline. It is not a substitute for professional engineering review.

## Relationship to human approval

Validation can detect structural failures, missing source references, unresolved assertions, schema mismatches, sensitive identifiers, and expected-output drift.

Only humans can approve:

- final design decisions,
- risk acceptance,
- production-impacting changes,
- unresolved issue closure,
- customer-facing wording,
- detailed design handoff,
- artifact reflection.

The validation runner supports the human approval boundary. It does not replace it.

## Future improvements

Potential improvements:

- add validation for the Review-to-Patch minimal example files,
- add richer source freshness checks,
- add scenario-level report summaries,
- add machine-readable validation output,
- add offline mock generation after contract rules are stable,
- keep any future LLM integration behind the same contract and approval checks.
