# YouTube VTT Analysis Instruction Template

## Variables

- VIDEO_TITLE:
- VIDEO_URL:
- VIDEO_ID:
- INPUT_VTT_FILE:
- PRIMARY_OUTPUT_LANGUAGE:
- TARGET_WORKFLOW:
- DOMAIN_CONTEXT:
- OUTPUT_DIR:

## Objective

Convert a YouTube or external video VTT file into structured study artifacts for learning, workflow pattern extraction, and readiness notes.

The goal is not to create a public transcript mirror, full translation, or redistributed version of the source content.

## Processing Requirements

1. Preserve the original VTT file.
2. Create a cleaned transcript with timestamps.
3. Create a plain transcript for internal processing.
4. Split the transcript into 10 to 15 minute segments.
5. Produce segment summaries.
6. Extract key concepts.
7. Extract tool and workflow usage patterns.
8. Map findings to `TARGET_WORKFLOW`.
9. Produce readiness notes.
10. Produce a final report and processing log.

## Output Directory Structure

Create this structure under `OUTPUT_DIR`:

```text
OUTPUT_DIR/
  00_original/
  10_cleaned/
  20_segments/
  30_summaries/
  40_concepts/
  50_workflow_mapping/
  60_readiness_notes/
  90_reports/
```

Copy the original VTT into:

```text
OUTPUT_DIR/00_original/
```

Do not modify the original VTT file.

## VTT Cleaning

Create:

```text
OUTPUT_DIR/10_cleaned/transcript_cleaned_with_timestamps.md
OUTPUT_DIR/10_cleaned/transcript_cleaned_plain.txt
```

Remove:

- `WEBVTT` header,
- timestamp cue formatting artifacts,
- duplicated subtitle fragments,
- inline timestamp tags such as `<00:00:01.000>`,
- caption styling tags,
- empty lines,
- repeated auto-caption residues where obvious.

Preserve:

- approximate timestamps,
- sentence order,
- speaker content,
- technical terms,
- uncertainty where the transcript appears unreliable.

Use this timestamped Markdown format:

```md
## 00:00:00 - 00:01:00

Transcript text...
```

The plain text file should not include timestamps.

## Segmenting

Split the transcript into approximately 10 to 15 minute segments.

Output one Markdown file per segment:

```text
OUTPUT_DIR/20_segments/segment_00_00-10.md
OUTPUT_DIR/20_segments/segment_01_10-20.md
```

Each segment file should include:

```md
# Segment NN: HH:MM:SS - HH:MM:SS

## Transcript

...

## Notes

- Important terms:
- Possible topic:
```

## Segment Summaries

Create:

```text
OUTPUT_DIR/30_summaries/segment_summaries.md
```

Summarize in `PRIMARY_OUTPUT_LANGUAGE`.

Use this format:

```md
# Segment Summaries

## Segment 00: 00:00 - 10:00

### Summary

...

### Key Points

- ...

### Operational Implications

- ...

### Connection to TARGET_WORKFLOW

- ...
```

Do not translate every sentence. Summarize accurately and practically.

## Key Concepts

Create:

```text
OUTPUT_DIR/40_concepts/key_concepts_glossary.md
```

Include concepts explicitly mentioned in the transcript and any workflow-critical inferred concepts. Label inferred concepts clearly.

Use this format:

```md
## Concept Name

### Source Basis

Explicit transcript fact or clearly marked inference.

### Meaning

...

### Practical Meaning

...

### Connection to TARGET_WORKFLOW

...
```

## Usage Patterns

Create:

```text
OUTPUT_DIR/40_concepts/usage_patterns.md
```

Use this format:

```md
# Usage Patterns

## Pattern 1: ...

### What the source says

...

### Practical meaning

...

### How to apply to local projects

...

### Risk / limitation

...
```

Focus on reusable workflow patterns, not entertainment value or promotional language.

## Workflow Mapping

Map source concepts to `TARGET_WORKFLOW`.

Create:

```text
OUTPUT_DIR/50_workflow_mapping/workflow_mapping.md
```

Use this table:

```md
# Workflow Mapping

| Source Concept | Meaning in Source | Target Workflow Equivalent | Example Use | Risk |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
```

Include a short proposed processing sequence if relevant.

## Readiness Notes

Create:

```text
OUTPUT_DIR/60_readiness_notes/readiness_notes.md
```

Separate:

- what the source says,
- what is inferred,
- what can be applied,
- what must not be overclaimed,
- how the learning artifact can support OpenAI readiness or portfolio preparation.

Do not claim official OpenAI endorsement unless explicitly sourced.

## Final Report

Create a concise final report in `PRIMARY_OUTPUT_LANGUAGE`.

Output:

```text
OUTPUT_DIR/90_reports/final_report.md
```

Required sections:

```md
# VIDEO_TITLE Analysis Report

## 1. Source Summary

## 2. Key Concepts

## 3. Practical Usage Patterns

## 4. Connection to TARGET_WORKFLOW

## 5. Human Review and Publication Boundary

## 6. Risks and Overclaim Boundaries

## 7. Recommended Next Steps
```

## Processing Log

Create:

```text
OUTPUT_DIR/90_reports/processing_log.md
```

The processing log should include:

- input filename,
- generated files,
- parsing issues,
- difficult or low-confidence sections,
- inferred concepts,
- recommended manual review points.

## Safety Rules

- Do not publish a full transcript.
- Do not include copyrighted long excerpts.
- Do not publish a full translation.
- Do not overclaim official endorsement.
- Keep generated analysis separate from source transcript.
- Mark assumptions clearly.
- Preserve timestamps for important claims where possible.
- Keep full source-derived material local unless rights allow redistribution.

## Acceptance Criteria

The task is complete when these files exist locally:

```text
OUTPUT_DIR/00_original/
OUTPUT_DIR/10_cleaned/transcript_cleaned_with_timestamps.md
OUTPUT_DIR/10_cleaned/transcript_cleaned_plain.txt
OUTPUT_DIR/20_segments/*.md
OUTPUT_DIR/30_summaries/segment_summaries.md
OUTPUT_DIR/40_concepts/key_concepts_glossary.md
OUTPUT_DIR/40_concepts/usage_patterns.md
OUTPUT_DIR/50_workflow_mapping/workflow_mapping.md
OUTPUT_DIR/60_readiness_notes/readiness_notes.md
OUTPUT_DIR/90_reports/final_report.md
OUTPUT_DIR/90_reports/processing_log.md
```

Before copying anything into a public repository, keep only repository-safe derivatives such as generic workflow docs, reusable templates, metadata, and short case notes.
