# YouTube Transcript to Study Artifact Workflow

## Purpose

This workflow converts YouTube subtitle or VTT materials into structured internal study artifacts without committing full transcripts, full translations, or copyrighted source material to the repository.

The goal is to preserve reusable process knowledge:

- how to extract and clean subtitle inputs,
- how to segment long-form learning material,
- how to summarize and extract concepts,
- how to map lessons into the Field-to-Artifact Pipeline,
- how to keep human review and redistribution boundaries explicit.

日本語メモ: 動画そのものの全文翻訳ではなく、学習・業務転用のための構造化メモを作るための手順である。

## When to Use

Use this workflow when a video, talk, course, or webinar contains material that may inform infrastructure design operations, LLM-assisted workflows, agentic tooling, or portfolio-ready process design.

Do not use this workflow to create a public mirror of a transcript or a full public translation.

## Inputs

Typical inputs:

- YouTube URL or video ID,
- downloaded `.vtt` subtitle file,
- optional audio file for manual review,
- target workflow or domain context,
- output directory for local-only processing,
- intended output language,
- human review criteria.

Each input should be treated as source material. If the source is not redistributable, keep it outside the public repository.

## Tools

Suggested tools:

- `yt-dlp` for subtitle and optional audio extraction,
- Codex for cleaning, segmentation, summarization, concept extraction, and workflow mapping,
- Markdown for reviewable outputs,
- `git diff --check` before committing reusable docs or templates.

## Basic yt-dlp Commands

List available subtitles:

```bash
yt-dlp --list-subs "VIDEO_URL"
```

Download English subtitles without the video:

```bash
yt-dlp --skip-download --write-auto-subs --sub-lang en --sub-format vtt "VIDEO_URL"
```

Download manually provided subtitles when available:

```bash
yt-dlp --skip-download --write-subs --sub-lang en --sub-format vtt "VIDEO_URL"
```

## Subtitle Extraction Flow

1. Create a local working directory outside the public repository.
2. Download the `.vtt` file with `yt-dlp`.
3. Preserve the original `.vtt` unchanged.
4. Clean subtitle artifacts such as `WEBVTT`, inline timestamp tags, duplicate auto-caption fragments, and empty lines.
5. Produce a local timestamped transcript and a local plain transcript.
6. Segment the transcript into reviewable time blocks, commonly 10 to 15 minutes.
7. Use the segmented material only as internal source context for summaries and workflow extraction.

## Optional Audio Extraction Flow

Audio may be useful when auto-caption quality is low or proper nouns are uncertain.

```bash
yt-dlp -x --audio-format mp3 "VIDEO_URL"
```

Use audio only for manual verification. Do not commit audio files to the repository.

## Codex Processing Flow

Recommended Codex stages:

1. Copy the original VTT into a local-only `00_original/` folder.
2. Generate cleaned transcript files in a local-only `10_cleaned/` folder.
3. Generate 10 to 15 minute segment files in a local-only `20_segments/` folder.
4. Create segment summaries, preferably concise and practical rather than sentence-by-sentence translation.
5. Extract key concepts and define how each concept is used in the source.
6. Extract reusable usage patterns.
7. Map the concepts to the target workflow.
8. Create readiness or application notes when relevant.
9. Create a processing log that records parsing issues, difficult sections, and recommended manual review points.

## Human Review Gate

Human review is required before any source-derived claim is reused externally.

Reviewers should check:

- whether the claim is explicitly present in the source,
- whether the claim is an inference,
- whether the timestamp is available,
- whether the summary overstates the source,
- whether source material can be redistributed,
- whether the output is safe for a public repository.

Mark uncertain or inferred items as `review_required` or `inference`.

## Output Artifact Types

Local-only artifacts may include:

- original VTT copy,
- cleaned timestamped transcript,
- cleaned plain transcript,
- segmented transcript files,
- Japanese or English segment summaries,
- key concept glossary,
- usage pattern notes,
- workflow mapping tables,
- application or readiness notes,
- processing logs.

Repository-safe artifacts may include:

- generic workflow documentation,
- reusable Codex instruction templates,
- short case README files,
- source-safe lessons learned,
- public-safe process diagrams or tables.

Do not commit full transcript files, full translated transcripts, downloaded audio, or source-derived long excerpts.

## Copyright and Redistribution Cautions

This workflow is designed for internal study and process extraction. It is not a license to republish copyrighted subtitle text.

Public repository rules:

- Do not commit full transcripts.
- Do not commit full translations.
- Do not include long source excerpts.
- Keep examples short and transformative.
- Preserve source title and URL for attribution when appropriate.
- Separate what the source says from what the workflow infers.

## Relationship to Field-to-Artifact Pipeline

This workflow is a lightweight example of the Field-to-Artifact Pipeline.

```text
Raw source material
-> Source intake
-> Cleaning and segmentation
-> Concept extraction
-> Workflow mapping
-> Human review gate
-> Repository-safe reusable artifact
```

The same pattern applies to infrastructure inputs such as field notes, photos, screenshots, meeting transcripts, vendor answers, and existing design documents.

## Relationship to LLM-Assisted Infrastructure Design Lifecycle Framework

The workflow supports the lifecycle framework by showing how unstructured source material becomes reviewable and traceable process knowledge.

Infrastructure design equivalents:

- VTT source file -> meeting transcript or field note source,
- cleaned transcript -> normalized evidence text,
- segment summary -> source context card,
- concept glossary -> domain vocabulary extraction,
- workflow mapping -> artifact map candidate,
- processing log -> review and audit trail,
- human review gate -> approval boundary before external reuse.

The workflow does not approve design decisions. It prepares structured learning artifacts that humans can evaluate, adapt, or reject.
