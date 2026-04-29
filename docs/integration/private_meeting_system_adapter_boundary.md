# Private Meeting System Adapter Boundary

## Purpose

This document defines the boundary between private operational meeting systems and the public-safe LLM Infra Design Studio framework.

The goal is to describe how a private meeting-minutes or transcript runner can inform the public framework at an abstract workflow, schema, and validation level without copying private implementation, private data, or operational artifacts into this repository.

## Positioning

Private meeting systems may implement:

- evidence intake,
- source routing,
- evidence normalization,
- candidate extraction,
- resolution,
- validation,
- private output adapters.

The public framework defines reusable concepts, schemas, synthetic samples, and validation patterns.

Private operational artifacts must not be copied into the public repository. The public repository should model reusable abstractions only.

## Allowed Public-Safe Abstractions

The following concepts may be modeled publicly when expressed generically and with synthetic examples only:

- evidence intake,
- source manifest,
- source registry,
- source role,
- source priority,
- current / previous classification,
- source strength,
- baseline strength,
- fallback primary,
- candidate extraction,
- resolved items,
- final artifact stage,
- coverage gap report,
- structured notes coverage,
- metadata validation,
- human approval states,
- output adapter boundary.

## Private-Only Materials

The following must remain private and must not be copied into this repository:

- real customer data,
- real project names,
- transcripts,
- meeting minutes,
- generated private outputs,
- participant masters,
- customer-specific kits,
- private prompts,
- private governance files,
- runtime paths,
- hostnames,
- sensitive filenames,
- private PDFs, images, or OCR outputs.

If a private file name or path contains a real customer, project, site, host, or organization identifier, it must not be quoted in public documentation.

## Recommended Integration Model

Use this integration model:

```text
Private operational runner
-> private operational artifacts
-> private sanitized lessons
-> public-safe schema / workflow / validation patterns
-> synthetic examples only
```

The private runner remains separate. The public framework may learn from the private runner's operational model, but only through sanitized concepts and synthetic examples.

## Mapping Model

| Private operational concept | Public-safe equivalent | Public action |
| --- | --- | --- |
| upload intake | evidence intake | document as concept |
| source routing | source type classification | extract adapter spec |
| source manifest | source registry / manifest | extend schema |
| source role | source role taxonomy | extend schema |
| source priority | source priority / authority model | extend schema |
| current / previous split | freshness / baseline status | add validation concept |
| source strength | evidence strength | add validation concept |
| baseline strength | baseline confidence | add validation concept |
| fallback primary | fallback source policy | document as concept |
| candidate extraction | candidate stage | stage contract |
| resolution | evidence-to-decision loop | stage contract |
| final stage separation | artifact approval boundary | stage contract |
| coverage gap report | validation gate | add validator concept |
| structured notes coverage | coverage validation concept | add validator concept |
| metadata validation | source metadata validation | add validator concept |
| final private outputs | artifact adapter boundary | keep private / synthetic only |

## Public Release Impact

Public release should be evaluated after this boundary is documented and reflected in the roadmap.

This document does not mean a private runner is included in the public repository. It means the public framework can describe how private operational systems may connect through sanitized schema, workflow, validation, and synthetic sample patterns.

Public portfolio visibility can proceed only after final human review confirms that:

- the private runner is not represented as included,
- private artifacts are not copied,
- integration claims remain abstract,
- synthetic examples are used for public demonstration.

## Non-Goals

This document does not add:

- private implementation import,
- private data import,
- runtime integration,
- real transcript processing in the public repository,
- production deployment,
- private output adapters,
- private prompt migration,
- private file or hostname documentation.

