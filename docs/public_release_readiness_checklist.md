# Public Release Readiness Checklist

## Purpose

Use this checklist before making the repository public.

The checklist verifies positioning clarity, public-safe content, synthetic data usage, first-time reviewer path, validation path, known limitations, and overclaiming risk.

This checklist does not publish the repository. It supports a human Go / No-Go decision before any public release.

## Repository Positioning

- [ ] The repository describes itself as an LLM-assisted Infrastructure Design Lifecycle Framework.
- [ ] It does not present itself as a production-ready tool.
- [ ] It does not claim autonomous infrastructure design.
- [ ] It does not claim to replace engineers.
- [ ] It treats document generation as required, but text-based and review-oriented in v0.1.
- [ ] It positions Word / Excel / PowerPoint rendering as future adapter work.
- [ ] It positions proposal generation as optional / future, not the core focus.
- [ ] It positions meeting minutes as one input source, not the final product.
- [ ] It positions Review-to-Patch as one downstream workflow, not the whole system.

## Public-Safe Content

- [ ] No real customer names.
- [ ] No real project names.
- [ ] No real vendor names or product names.
- [ ] No real IP addresses or hostnames.
- [ ] No real meeting transcripts.
- [ ] No private design excerpts.
- [ ] No internal organization names.
- [ ] No confidential diagrams.
- [ ] Synthetic examples are clearly marked as fictional.

## Reviewer Path

- [ ] README explains the core focus.
- [ ] `docs/quickstart_for_reviewers.md` exists.
- [ ] `docs/INDEX.md` links to the main documents.
- [ ] The lifecycle minimal sample is easy to find.
- [ ] Validation commands are easy to find.
- [ ] Known limitations are visible.

## Validation Readiness

Run:

```bash
python3 scripts/run_sample_workflow.py --check-only
python3 scripts/validate_lifecycle_minimal.py
python3 scripts/validate_artifact_generation_plan.py
python3 scripts/check_sensitive_identifiers.py
git diff --check
```

Checklist:

- [ ] All validation commands pass.
- [ ] Validation failure messages are readable.
- [ ] Validation does not require external services.
- [ ] Validation does not require LLM API keys.
- [ ] Validation does not prove real network correctness.
- [ ] Validation does not approve design language.

## Go / No-Go Decision

GO if:

- the reviewer path is clear,
- validations pass,
- known limitations are explicit,
- no sensitive information is found,
- v0.1 scope is not overstated.

NO-GO if:

- sensitive information is found,
- README overclaims production readiness,
- validation path is unclear,
- examples look like real customer data,
- document generation is implied to be final-approved output.

