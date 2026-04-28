#!/usr/bin/env python3
"""Validate the lifecycle minimal synthetic sample."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SAMPLE_ROOT = ROOT / "samples" / "lifecycle_minimal"

REQUIRED_FILES = [
    "README.md",
    "input/customer_hearing_note.md",
    "input/meeting_transcript_excerpt.md",
    "input/existing_design_excerpt.md",
    "input/review_comments.yaml",
    "input/vendor_note.md",
    "intermediate/evidence_registry.yaml",
    "intermediate/requirement_candidates.yaml",
    "intermediate/unresolved_items.yaml",
    "intermediate/missing_inputs.yaml",
    "intermediate/design_issue_log.yaml",
    "output/requirement_definition_draft.md",
    "output/high_level_design_patch.md",
    "output/detailed_design_handoff.md",
    "output/review_response_draft.md",
    "output/human_approval_checklist.md",
]

EXPECTED_SOURCE_IDS = {f"SRC-{index:03d}" for index in range(1, 6)}
EXPECTED_REQUIREMENT_IDS = {f"REQ-CAND-{index:03d}" for index in range(1, 4)}
EXPECTED_UNRESOLVED_IDS = {f"UNRES-{index:03d}" for index in range(1, 4)}
EXPECTED_MISSING_IDS = {f"MISS-{index:03d}" for index in range(1, 4)}
EXPECTED_DESIGN_ISSUE_IDS = {f"DI-{index:03d}" for index in range(1, 5)}
EXPECTED_REVIEW_COMMENT_IDS = {f"RC-{index:03d}" for index in range(1, 5)}

ID_PATTERNS = {
    "source": re.compile(r"\bSRC-\d{3}\b"),
    "requirement": re.compile(r"\bREQ-CAND-\d{3}\b"),
    "unresolved": re.compile(r"\bUNRES-\d{3}\b"),
    "missing": re.compile(r"\bMISS-\d{3}\b"),
    "design_issue": re.compile(r"\bDI-\d{3}\b"),
    "review_comment": re.compile(r"\bRC-\d{3}\b"),
}

RISKY_PUBLIC_TERMS = [
    "ORI" + "X",
    "Soft" + "Bank",
    "Prisma",
    "Cisco",
    "192.168",
    "10.0",
    "172.16",
]
IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

APPROVAL_MARKERS = [
    "REVIEW_REQUIRED",
    "DRAFT",
    "not approved",
    "Final customer approval: No",
    "Production readiness: No",
    "Artifact reflection allowed: No",
]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read(path: Path, failures: list[str]) -> str:
    if not path.is_file():
        failures.append(f"missing required file: {rel(path)}")
        return ""
    return path.read_text(encoding="utf-8")


def load_files(failures: list[str]) -> dict[str, str]:
    texts: dict[str, str] = {}
    for item in REQUIRED_FILES:
        path = SAMPLE_ROOT / item
        texts[item] = read(path, failures)
    return texts


def all_sample_text(texts: dict[str, str]) -> str:
    return "\n".join(texts.values())


def ids_in(text: str, pattern_name: str) -> set[str]:
    return set(ID_PATTERNS[pattern_name].findall(text))


def check_expected_ids(
    label: str,
    expected: set[str],
    pattern_name: str,
    all_text: str,
    required_locations: list[tuple[str, str]],
    texts: dict[str, str],
    failures: list[str],
) -> None:
    found_all = ids_in(all_text, pattern_name)
    unexpected = sorted(found_all - expected)
    if unexpected:
        failures.append(f"unexpected {label} IDs found: {', '.join(unexpected)}")

    missing_global = sorted(expected - found_all)
    if missing_global:
        failures.append(f"expected {label} IDs not found in sample: {', '.join(missing_global)}")

    for file_key, purpose in required_locations:
        text = texts.get(file_key, "")
        found = ids_in(text, pattern_name)
        missing = sorted(expected - found)
        if missing:
            failures.append(
                f"{file_key} missing {label} IDs for {purpose}: {', '.join(missing)}"
            )


def check_design_issue_traceability(texts: dict[str, str], failures: list[str]) -> None:
    output_text = "\n".join(
        [
            texts.get("output/high_level_design_patch.md", ""),
            texts.get("output/review_response_draft.md", ""),
        ]
    )
    found = ids_in(output_text, "design_issue")
    if not found:
        failures.append(
            "no design issue IDs appear in high_level_design_patch.md or review_response_draft.md"
        )


def is_negative_line(line: str) -> bool:
    lower = line.lower()
    negative_markers = [
        " no",
        ": no",
        "not ",
        "does not",
        "do not",
        "must not",
        "without",
        "none",
    ]
    return any(marker in lower for marker in negative_markers)


def check_risky_approval_language(texts: dict[str, str], failures: list[str]) -> None:
    output_files = [key for key in texts if key.startswith("output/")]
    risky_patterns = [
        ("approved by default", re.compile(r"\bapproved by default\b", re.IGNORECASE)),
        ("final approved", re.compile(r"\bfinal approved\b", re.IGNORECASE)),
        ("production-ready", re.compile(r"\bproduction-ready\b", re.IGNORECASE)),
        ("production ready", re.compile(r"\bproduction ready\b", re.IGNORECASE)),
        (
            "autonomous design approval",
            re.compile(r"\bautonomous design approval\b", re.IGNORECASE),
        ),
        ("replaces engineers", re.compile(r"\breplaces engineers\b", re.IGNORECASE)),
    ]

    for file_key in output_files:
        for line_number, line in enumerate(texts[file_key].splitlines(), start=1):
            for label, pattern in risky_patterns:
                if not pattern.search(line):
                    continue
                if label in {"final approved", "production-ready", "production ready"} and is_negative_line(line):
                    continue
                failures.append(f"{file_key}:{line_number}: risky approval language: {line.strip()}")


def check_approval_boundaries(texts: dict[str, str], failures: list[str]) -> None:
    output_text = "\n".join(texts[key] for key in texts if key.startswith("output/"))
    for marker in APPROVAL_MARKERS:
        if marker not in output_text:
            failures.append(f"approval boundary marker missing from outputs: {marker}")
    check_risky_approval_language(texts, failures)


def check_detailed_design_boundary(texts: dict[str, str], failures: list[str]) -> None:
    handoff = texts.get("output/detailed_design_handoff.md", "")
    patch = texts.get("output/high_level_design_patch.md", "")

    if not handoff:
        failures.append("detailed design handoff output is empty or missing")
    if "detailed-design handoff" not in patch and "detailed design" not in patch.lower():
        failures.append("high_level_design_patch.md must reference detailed-design handoff")

    risky_parameter_phrases = [
        "final routing parameter",
        "final routing policy",
        "approved routing parameter",
        "approved failover behavior",
    ]
    lower_patch = patch.lower()
    for phrase in risky_parameter_phrases:
        if phrase in lower_patch:
            failures.append(f"high_level_design_patch.md includes final parameter language: {phrase}")

    boundary_text = f"{patch}\n{handoff}".lower()
    for token in ["routing", "failover", "monitoring"]:
        if token not in boundary_text:
            failures.append(f"detailed-design boundary missing topic: {token}")
    if "review_required" not in boundary_text and "detailed-design handoff" not in boundary_text:
        failures.append("routing/failover/monitoring boundary must remain review-required or handoff")


def check_public_safety(texts: dict[str, str], failures: list[str]) -> None:
    for file_key, text in texts.items():
        for term in RISKY_PUBLIC_TERMS:
            if term in text:
                failures.append(f"{file_key}: public-safety risky term found: {term}")
        for match in IPV4_RE.finditer(text):
            failures.append(f"{file_key}: IPv4-looking address found: {match.group(0)}")


def validate() -> list[str]:
    failures: list[str] = []
    texts = load_files(failures)
    combined = all_sample_text(texts)

    if failures:
        return failures

    check_expected_ids(
        "source",
        EXPECTED_SOURCE_IDS,
        "source",
        combined,
        [("intermediate/evidence_registry.yaml", "source registry coverage")],
        texts,
        failures,
    )
    check_expected_ids(
        "requirement candidate",
        EXPECTED_REQUIREMENT_IDS,
        "requirement",
        combined,
        [
            ("intermediate/requirement_candidates.yaml", "candidate registry coverage"),
            ("output/requirement_definition_draft.md", "requirement draft traceability"),
        ],
        texts,
        failures,
    )
    check_expected_ids(
        "unresolved item",
        EXPECTED_UNRESOLVED_IDS,
        "unresolved",
        combined,
        [
            ("intermediate/unresolved_items.yaml", "unresolved registry coverage"),
            ("output/detailed_design_handoff.md", "handoff traceability"),
            ("output/high_level_design_patch.md", "design patch traceability"),
        ],
        texts,
        failures,
    )
    check_expected_ids(
        "missing input",
        EXPECTED_MISSING_IDS,
        "missing",
        combined,
        [
            ("intermediate/missing_inputs.yaml", "missing input registry coverage"),
            ("output/requirement_definition_draft.md", "requirement draft traceability"),
        ],
        texts,
        failures,
    )
    check_expected_ids(
        "design issue",
        EXPECTED_DESIGN_ISSUE_IDS,
        "design_issue",
        combined,
        [("intermediate/design_issue_log.yaml", "design issue registry coverage")],
        texts,
        failures,
    )
    check_design_issue_traceability(texts, failures)
    check_expected_ids(
        "review comment",
        EXPECTED_REVIEW_COMMENT_IDS,
        "review_comment",
        combined,
        [
            ("input/review_comments.yaml", "review comment input coverage"),
            ("output/review_response_draft.md", "review response traceability"),
        ],
        texts,
        failures,
    )
    check_approval_boundaries(texts, failures)
    check_detailed_design_boundary(texts, failures)
    check_public_safety(texts, failures)

    return failures


def main() -> int:
    failures = validate()
    if failures:
        print("Lifecycle minimal validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Lifecycle minimal validation passed.")
    print()
    print("Checked:")
    print("- required files")
    print("- source IDs")
    print("- requirement candidate IDs")
    print("- unresolved item IDs")
    print("- missing input IDs")
    print("- design issue IDs")
    print("- review comment IDs")
    print("- approval boundary markers")
    print("- detailed-design handoff boundary")
    print("- public-safety terms")
    return 0


if __name__ == "__main__":
    sys.exit(main())
