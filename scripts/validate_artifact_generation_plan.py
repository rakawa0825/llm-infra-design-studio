#!/usr/bin/env python3
"""Validate the lifecycle minimal artifact generation plan."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "samples" / "lifecycle_minimal" / "artifact_generation_plan.yaml"
CONTRACT_TEMPLATE = ROOT / "templates" / "contracts" / "artifact_generation_plan.yaml"

VALID_SOURCE_IDS = {f"SRC-{index:03d}" for index in range(1, 6)}
EXPECTED_ARTIFACT_IDS = {
    "ART-REQ-001",
    "ART-HLD-001",
    "ART-DDH-001",
    "ART-RR-001",
    "ART-HAC-001",
}
EXPECTED_ARTIFACT_TYPES = {
    "requirement_definition_draft",
    "high_level_design_patch",
    "detailed_design_handoff",
    "review_response_draft",
    "human_approval_checklist",
}
REQUIRED_FIELDS = {
    "artifact_id",
    "artifact_type",
    "lifecycle_phase",
    "template_path",
    "output_path",
    "input_sources",
    "intermediate_dependencies",
    "approval_gate",
    "review_state",
    "allowed_claims",
    "forbidden_claims",
    "validation_checks",
}

ARTIFACT_SPECIFIC = {
    "ART-REQ-001": {
        "artifact_type": "requirement_definition_draft",
        "template_path": "templates/artifacts/requirement_definition_draft.md",
        "output_path": "samples/lifecycle_minimal/output/requirement_definition_draft.md",
        "dependencies": {
            "samples/lifecycle_minimal/intermediate/requirement_candidates.yaml",
            "samples/lifecycle_minimal/intermediate/unresolved_items.yaml",
            "samples/lifecycle_minimal/intermediate/missing_inputs.yaml",
        },
    },
    "ART-HLD-001": {
        "artifact_type": "high_level_design_patch",
        "template_path": "templates/artifacts/high_level_design_patch.md",
        "output_path": "samples/lifecycle_minimal/output/high_level_design_patch.md",
        "dependencies": {
            "samples/lifecycle_minimal/intermediate/design_issue_log.yaml",
            "samples/lifecycle_minimal/input/existing_design_excerpt.md",
            "samples/lifecycle_minimal/input/review_comments.yaml",
        },
    },
    "ART-DDH-001": {
        "artifact_type": "detailed_design_handoff",
        "template_path": "templates/artifacts/detailed_design_handoff.md",
        "output_path": "samples/lifecycle_minimal/output/detailed_design_handoff.md",
        "dependencies": {
            "samples/lifecycle_minimal/intermediate/unresolved_items.yaml",
            "samples/lifecycle_minimal/input/vendor_note.md",
        },
    },
    "ART-RR-001": {
        "artifact_type": "review_response_draft",
        "template_path": "templates/artifacts/review_response_draft.md",
        "output_path": "samples/lifecycle_minimal/output/review_response_draft.md",
        "dependencies": {
            "samples/lifecycle_minimal/input/review_comments.yaml",
            "samples/lifecycle_minimal/intermediate/design_issue_log.yaml",
        },
    },
    "ART-HAC-001": {
        "artifact_type": "human_approval_checklist",
        "template_path": "templates/artifacts/human_approval_checklist.md",
        "output_path": "samples/lifecycle_minimal/output/human_approval_checklist.md",
        "dependencies": {
            "samples/lifecycle_minimal/intermediate/unresolved_items.yaml",
            "samples/lifecycle_minimal/intermediate/missing_inputs.yaml",
            "samples/lifecycle_minimal/output/requirement_definition_draft.md",
            "samples/lifecycle_minimal/output/high_level_design_patch.md",
            "samples/lifecycle_minimal/output/detailed_design_handoff.md",
            "samples/lifecycle_minimal/output/review_response_draft.md",
        },
    },
}

RISKY_PUBLIC_TERMS = [
    "ORI" + "X",
    "Soft" + "Bank",
    "REAL_VENDOR_NAME_PLACEHOLDER",
    "REAL_PRODUCT_NAME_PLACEHOLDER",
    "PRIVATE_ORGANIZATION_NAME_PLACEHOLDER",
    "192.168",
    "10.0",
    "172.16",
]
IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
SRC_RE = re.compile(r"\bSRC-\d{3}\b")


def unquote(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def parse_plan(path: Path, failures: list[str]) -> list[dict[str, object]]:
    if not path.is_file():
        failures.append(f"missing plan file: {rel(path)}")
        return []

    artifacts: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list_key: str | None = None

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith("  - artifact_id:"):
            if current is not None:
                artifacts.append(current)
            current = {"artifact_id": unquote(raw_line.split(":", 1)[1])}
            current_list_key = None
            continue

        if current is None:
            continue

        if raw_line.startswith("    ") and not raw_line.startswith("      "):
            key_value = raw_line.strip()
            if ":" not in key_value:
                failures.append(f"{rel(path)}:{line_number}: invalid mapping line")
                continue
            key, value = key_value.split(":", 1)
            value = value.strip()
            if value:
                current[key] = unquote(value)
                current_list_key = None
            else:
                current[key] = []
                current_list_key = key
            continue

        if raw_line.startswith("      - "):
            if current_list_key is None:
                failures.append(f"{rel(path)}:{line_number}: list item without parent key")
                continue
            value = unquote(raw_line.strip()[2:].strip())
            current[current_list_key].append(value)  # type: ignore[index,union-attr]
            continue

    if current is not None:
        artifacts.append(current)

    if not artifacts:
        failures.append(f"{rel(path)}: no artifact entries found")

    return artifacts


def as_list(entry: dict[str, object], key: str) -> list[str]:
    value = entry.get(key)
    if isinstance(value, list):
        return [str(item) for item in value]
    return []


def as_str(entry: dict[str, object], key: str) -> str:
    value = entry.get(key)
    return value if isinstance(value, str) else ""


def check_required_files(failures: list[str]) -> None:
    for path in [PLAN, CONTRACT_TEMPLATE]:
        if not path.is_file():
            failures.append(f"missing required file: {rel(path)}")


def check_path(path_value: str, expected_prefix: str, label: str, failures: list[str]) -> None:
    if not path_value.startswith(expected_prefix):
        failures.append(f"{label} must be under {expected_prefix}: {path_value}")
        return
    path = ROOT / path_value
    if not path.is_file():
        failures.append(f"{label} does not exist: {path_value}")


def check_public_safety(failures: list[str]) -> None:
    for path in [PLAN, CONTRACT_TEMPLATE]:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for term in RISKY_PUBLIC_TERMS:
            if term in text:
                failures.append(f"{rel(path)}: public-safety risky term found: {term}")
        for match in IPV4_RE.finditer(text):
            failures.append(f"{rel(path)}: IPv4-looking address found: {match.group(0)}")


def check_plan(artifacts: list[dict[str, object]], failures: list[str]) -> None:
    ids = {as_str(entry, "artifact_id") for entry in artifacts}
    types = {as_str(entry, "artifact_type") for entry in artifacts}

    missing_ids = sorted(EXPECTED_ARTIFACT_IDS - ids)
    extra_ids = sorted(ids - EXPECTED_ARTIFACT_IDS)
    if missing_ids:
        failures.append(f"missing expected artifact IDs: {', '.join(missing_ids)}")
    if extra_ids:
        failures.append(f"unexpected artifact IDs: {', '.join(extra_ids)}")

    missing_types = sorted(EXPECTED_ARTIFACT_TYPES - types)
    if missing_types:
        failures.append(f"missing expected artifact types: {', '.join(missing_types)}")

    plan_text = PLAN.read_text(encoding="utf-8") if PLAN.is_file() else ""
    unexpected_sources = sorted(set(SRC_RE.findall(plan_text)) - VALID_SOURCE_IDS)
    if unexpected_sources:
        failures.append(f"unexpected source IDs in plan: {', '.join(unexpected_sources)}")

    for entry in artifacts:
        artifact_id = as_str(entry, "artifact_id")
        missing_fields = sorted(field for field in REQUIRED_FIELDS if field not in entry)
        if missing_fields:
            failures.append(f"{artifact_id}: missing required fields: {', '.join(missing_fields)}")
            continue

        template_path = as_str(entry, "template_path")
        output_path = as_str(entry, "output_path")
        dependencies = as_list(entry, "intermediate_dependencies")
        input_sources = as_list(entry, "input_sources")

        check_path(template_path, "templates/artifacts/", f"{artifact_id} template_path", failures)
        check_path(output_path, "samples/lifecycle_minimal/output/", f"{artifact_id} output_path", failures)

        for dependency in dependencies:
            if "/" in dependency or dependency.endswith((".yaml", ".md")):
                if not (ROOT / dependency).is_file():
                    failures.append(f"{artifact_id} dependency does not exist: {dependency}")

        invalid_sources = sorted(set(input_sources) - VALID_SOURCE_IDS)
        if invalid_sources:
            failures.append(f"{artifact_id}: invalid input_sources: {', '.join(invalid_sources)}")

        if as_str(entry, "review_state") != "REVIEW_REQUIRED":
            failures.append(f"{artifact_id}: review_state must be REVIEW_REQUIRED")

        if any(token in as_str(entry, "review_state").upper() for token in ["APPROVED", "FINAL", "PRODUCTION_READY"]):
            failures.append(f"{artifact_id}: risky review_state value: {as_str(entry, 'review_state')}")

        for list_key in ["allowed_claims", "forbidden_claims", "validation_checks"]:
            if not as_list(entry, list_key):
                failures.append(f"{artifact_id}: {list_key} must not be empty")

        spec = ARTIFACT_SPECIFIC.get(artifact_id)
        if not spec:
            continue
        for key in ["artifact_type", "template_path", "output_path"]:
            expected = spec[key]
            actual = as_str(entry, key)
            if actual != expected:
                failures.append(f"{artifact_id}: {key} expected {expected}, found {actual}")

        missing_deps = sorted(spec["dependencies"] - set(dependencies))
        if missing_deps:
            failures.append(f"{artifact_id}: missing required dependencies: {', '.join(missing_deps)}")


def main() -> int:
    failures: list[str] = []
    check_required_files(failures)
    artifacts = parse_plan(PLAN, failures)
    if artifacts:
        check_plan(artifacts, failures)
    check_public_safety(failures)

    if failures:
        print("Artifact generation plan validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Artifact generation plan validation passed.")
    print()
    print("Checked:")
    print("- required plan files")
    print("- expected artifact IDs")
    print("- required fields")
    print("- template paths")
    print("- output paths")
    print("- intermediate dependencies")
    print("- source IDs")
    print("- review states")
    print("- allowed / forbidden claims")
    print("- artifact-specific mappings")
    print("- public-safety terms")
    return 0


if __name__ == "__main__":
    sys.exit(main())
