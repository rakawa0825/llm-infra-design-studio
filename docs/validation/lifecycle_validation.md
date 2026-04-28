# Lifecycle Validation

## Purpose

Lifecycle validation checks that the v0.1 lifecycle minimal sample and its artifact generation plan remain internally consistent, public-safe, and approval-gated.

It helps reviewers validate the newer lifecycle framework path without reading every file manually.

## Commands

```bash
python3 scripts/validate_lifecycle_minimal.py
python3 scripts/validate_artifact_generation_plan.py
```

## What `validate_lifecycle_minimal.py` checks

- required lifecycle sample files,
- source IDs,
- requirement candidate IDs,
- unresolved item IDs,
- missing input IDs,
- design issue IDs,
- review comment IDs,
- approval boundary markers,
- detailed-design handoff boundary,
- public-safety terms.

## What `validate_artifact_generation_plan.py` checks

- artifact generation plan file,
- contract template file,
- artifact IDs,
- required fields,
- template paths,
- output paths,
- intermediate dependencies,
- source IDs,
- review states,
- allowed and forbidden claims,
- artifact-specific mappings,
- public-safety terms.

## What validation does not prove

This validation does not prove real network design correctness.

It does not approve design language.

It does not prove production readiness.

It does not replace engineering review.

## Relationship to the artifact generation contract

The lifecycle minimal sample shows one concrete synthetic case.

The artifact generation contract explains how intermediate lifecycle state maps into text-based review artifacts.

The validators check that these files remain aligned. They do not generate artifacts, render documents, call an LLM, or approve outputs.
