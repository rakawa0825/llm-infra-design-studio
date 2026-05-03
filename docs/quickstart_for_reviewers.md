# Quickstart for Reviewers

## What This Repository Demonstrates

This repository demonstrates an LLM-assisted Infrastructure Design Lifecycle Framework.

It shows how scattered infrastructure design evidence can be organized into text-based, source-backed, reviewable, traceable, human-approved design artifacts.

The v0.1 path focuses on:

- customer hearing and meeting evidence,
- requirement clarification,
- requirement definition draft,
- high-level design / basic design patch,
- detailed-design handoff,
- unresolved item preservation,
- human approval checklist,
- text-based artifact generation.

## What This Repository Is Not

- Not production-ready.
- Not autonomous infrastructure design.
- Not a replacement for qualified engineers.
- Not primarily a proposal-generation system.
- Not a Word / Excel / PowerPoint rendering tool.
- Not a config generator.
- Not a network diagram generator.
- Not a repository for real customer data.

## Recommended Reading Path

Use this path for a focused review:

1. [README](../README.md)
2. [Infrastructure Design Lifecycle Framework](architecture/infrastructure_design_lifecycle_framework.md)
3. [v0.1 Scope](roadmap/v0_1_scope.md)
4. [v0.1 Synthetic Case Design](cases/v0_1_synthetic_case_design.md)
5. [Lifecycle Minimal Sample](../samples/lifecycle_minimal/README.md)
6. [Requirement Definition Draft](../samples/lifecycle_minimal/output/requirement_definition_draft.md)
7. [High-Level Design Patch](../samples/lifecycle_minimal/output/high_level_design_patch.md)
8. [Detailed-Design Handoff](../samples/lifecycle_minimal/output/detailed_design_handoff.md)
9. [Human Approval Checklist](../samples/lifecycle_minimal/output/human_approval_checklist.md)
10. [Workspace Minimal Traceability Sample](../samples/workspace_minimal/README.md)
11. [Workspace Minimal Validation](validation/workspace_minimal_validation.md)
12. [Artifact Generation Contract](artifacts/artifact_generation_contract.md)
13. [Text Document Output Templates](artifacts/text_document_output_templates.md)

## Validation Commands

Run the reviewer-facing validation path:

```bash
python3 scripts/run_sample_workflow.py --check-only
python3 scripts/validate_lifecycle_minimal.py
python3 scripts/validate_artifact_generation_plan.py
python3 scripts/validate_workspace_minimal.py
python3 scripts/check_sensitive_identifiers.py
```

What each command checks:

- `scripts/run_sample_workflow.py --check-only`: repository structure, required assets, validation scripts, public-safe scan, and sample/eval presence.
- `scripts/validate_lifecycle_minimal.py`: lifecycle minimal sample files, ID consistency, approval-boundary markers, detailed-design handoff boundary, and public-safe terms.
- `scripts/validate_artifact_generation_plan.py`: artifact generation plan, template paths, output paths, source IDs, review states, allowed / forbidden claims, and plan-level public-safe terms.
- `scripts/validate_workspace_minimal.py`: v0.2 Markdown-only traceability sample IDs, metadata, basic references, unresolved item visibility, and human approval boundary markers.
- `scripts/check_sensitive_identifiers.py`: configured sensitive identifier patterns.

## v0.2 Traceability Slice Checklist

Use this path after the v0.1 lifecycle review:

1. Inspect [Workspace Minimal Traceability Sample](../samples/workspace_minimal/README.md).
2. Inspect [trace_map.md](../samples/workspace_minimal/trace_map.md).
3. Run `python3 scripts/validate_workspace_minimal.py`.
4. Run `python3 scripts/run_sample_workflow.py --check-only`.

This slice is synthetic, Markdown-only, and not production-ready. It shows how source evidence, requirements, design sections, review items, patch drafts, decisions, handoffs, validation records, and human approval boundaries can remain traceable.

## What Validation Proves

Validation proves that the current synthetic repository state satisfies local consistency rules:

- required sample files exist,
- IDs are consistent,
- source references are preserved,
- approval boundaries are visible,
- artifact generation plan paths are valid,
- public-safety checks pass.

## What Validation Does Not Prove

Validation does not prove:

- a real network design is correct,
- generated text is customer-approved,
- the workflow is production-ready,
- the repository replaces engineering review,
- Word / Excel / PowerPoint formatting exists.

## Suggested Reviewer Conclusion

Evaluate this repository as a workflow prototype for infrastructure design teams, not as a finished product.

The useful question is whether the framework preserves evidence, uncertainty, lifecycle phase, and human approval boundaries while preparing reviewable design artifacts.
