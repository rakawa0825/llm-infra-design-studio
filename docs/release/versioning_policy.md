# Versioning Policy

## Purpose

This document defines version language for LLM Infra Design Studio.

The goal is to keep functional scope, repository release status, product maturity, public visibility, and OSS/license status separate. A repository can be ready for public portfolio visibility without being production-ready or license-ready for broad reuse.

## Version Dimensions

### Functional Scope Version

Functional scope describes what the workflow prototype currently demonstrates.

Example:

```text
v0.1 Lifecycle Prototype
```

### Repository Release Status

Repository release status describes whether the repository is ready to be reviewed or made visible.

Example:

```text
Public Release Candidate
```

### Product Maturity

Product maturity describes whether the repository is a production product.

Current status:

```text
Not production-ready
```

### Public Visibility

Public visibility describes whether the repository has actually been made public.

Public visibility is a repository setting and must be changed only by explicit human action.

### OSS / License Status

OSS/license status describes whether reuse, redistribution, or forking terms are defined.

Public visibility does not automatically mean the repository is licensed for open-source reuse.

See [License Policy](license_policy.md) for the current no-license stance.

## Current Status

```text
Functional scope: v0.1 Lifecycle Prototype
Repository release status: Public Release Candidate
Suggested release label: v0.1.0-rc.1
Production status: Not production-ready
Public visibility: pending human action
OSS/license status: pending license decision if reuse/fork is intended
```

## Naming Rules

- Do not use `v1.0` until the workflow is stable across multiple synthetic scenarios.
- Do not use production-ready language.
- Do not treat public visibility as production readiness.
- Do not treat public visibility as an OSS license decision.
- Do not call future adapters current capabilities.
- Do not imply autonomous infrastructure design.
- Do not imply that the repository replaces engineers.

## Future Version Direction

```text
v0.1.0:
Public preview of lifecycle prototype

v0.2.0:
Customer hearing to requirement definition expansion

v0.3.0:
Requirement definition to basic design document generation expansion

v0.4.0:
Detailed-design handoff and parameter candidate expansion

v0.5.0:
Replay validation for time-sliced project evidence

v0.6.0:
Test / rollout / operations handover artifact expansion

v0.7.0:
Format adapter experiments for Word / Excel / PowerPoint

v0.8.0:
Diagram / config generation research prototypes

v1.0.0:
Only when documentation, lifecycle samples, validation, contribution policy, and license are stable enough for broader reuse
```
