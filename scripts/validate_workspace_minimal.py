#!/usr/bin/env python3
"""Validate the Markdown-only workspace_minimal synthetic sample."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SAMPLE_ROOT = ROOT / "samples" / "workspace_minimal"

VALID_PREFIXES = {"SRC", "REQ", "DS", "RV", "PD", "DR", "DL", "HO", "VR"}
REQUIRED_METADATA_FIELDS = {"id", "type", "status", "human_approval", "public_safety"}
RELATIONSHIP_FIELDS = {
    "derived_from",
    "targets",
    "related",
    "addresses",
    "reviews",
    "decides",
    "created_by",
    "creates_handoff",
    "validates",
    "checked_ids",
}
ID_RE = re.compile(r"^(SRC|REQ|DS|RV|PD|DR|DL|HO|VR)-([0-9]{3})$")
YAML_BLOCK_RE = re.compile(r"```yaml\n(.*?)\n```", re.DOTALL)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_metadata_block(text: str) -> dict[str, object]:
    match = YAML_BLOCK_RE.search(text)
    if not match:
        return {}

    metadata: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip("\"'")
            if value:
                metadata[key] = value
                current_key = None
            else:
                metadata[key] = []
                current_key = key
            continue

        if current_key and stripped.startswith("- "):
            value = stripped[2:].strip().strip("\"'")
            existing = metadata.get(current_key)
            if isinstance(existing, list):
                existing.append(value)

    return metadata


def iter_markdown_files() -> list[Path]:
    if not SAMPLE_ROOT.is_dir():
        return []
    return sorted(SAMPLE_ROOT.rglob("*.md"))


def is_id_bearing(metadata: dict[str, object]) -> bool:
    return bool(metadata.get("id"))


def scalar(metadata: dict[str, object], key: str) -> str:
    value = metadata.get(key)
    return value if isinstance(value, str) else ""


def values(metadata: dict[str, object], key: str) -> list[str]:
    value = metadata.get(key)
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def validate_id_format(item_id: str, file_path: Path, failures: list[str]) -> None:
    match = ID_RE.match(item_id)
    if not match:
        prefix = item_id.split("-", 1)[0] if "-" in item_id else item_id
        if prefix and prefix not in VALID_PREFIXES:
            failures.append(f"{rel(file_path)}: unknown ID prefix: {item_id}")
        else:
            failures.append(f"{rel(file_path)}: malformed ID: {item_id}")
        return

    if match.group(2) == "000":
        failures.append(f"{rel(file_path)}: ID numeric suffix must start at 001: {item_id}")


def validate_metadata(file_path: Path, metadata: dict[str, object], failures: list[str]) -> None:
    item_id = scalar(metadata, "id")

    missing = sorted(field for field in REQUIRED_METADATA_FIELDS if not metadata.get(field))
    if missing:
        failures.append(f"{rel(file_path)}: missing required metadata fields: {', '.join(missing)}")

    if item_id:
        validate_id_format(item_id, file_path, failures)

    if file_path.stem != item_id:
        failures.append(
            f"{rel(file_path)}: filename stem does not match metadata id: "
            f"{file_path.stem} != {item_id or '<missing>'}"
        )

    public_safety = scalar(metadata, "public_safety")
    if public_safety and public_safety != "synthetic_only":
        failures.append(
            f"{rel(file_path)}: public_safety must be synthetic_only, found: {public_safety}"
        )


def validate_relationships(
    file_path: Path,
    metadata: dict[str, object],
    known_ids: set[str],
    failures: list[str],
) -> None:
    item_id = scalar(metadata, "id") or rel(file_path)
    for field in sorted(RELATIONSHIP_FIELDS):
        for referenced_id in values(metadata, field):
            if not ID_RE.match(referenced_id):
                failures.append(
                    f"{rel(file_path)}: relationship field {field} has malformed ID "
                    f"{referenced_id} on {item_id}"
                )
                continue
            if referenced_id not in known_ids:
                failures.append(
                    f"{rel(file_path)}: relationship field {field} references missing ID "
                    f"{referenced_id} on {item_id}"
                )


def main() -> int:
    failures: list[str] = []
    markdown_files = iter_markdown_files()

    if not SAMPLE_ROOT.is_dir():
        failures.append(f"missing sample directory: {rel(SAMPLE_ROOT)}")
    if not markdown_files:
        failures.append(f"no Markdown files found under {rel(SAMPLE_ROOT)}")

    id_to_files: dict[str, list[Path]] = {}
    id_bearing_files: list[Path] = []
    metadata_by_file: dict[Path, dict[str, object]] = {}

    for file_path in markdown_files:
        text = read_text(file_path)
        metadata = parse_metadata_block(text)
        if not is_id_bearing(metadata):
            continue

        id_bearing_files.append(file_path)
        item_id = scalar(metadata, "id")
        id_to_files.setdefault(item_id, []).append(file_path)
        metadata_by_file[file_path] = metadata
        validate_metadata(file_path, metadata, failures)

    for item_id, files in sorted(id_to_files.items()):
        if item_id and len(files) > 1:
            locations = ", ".join(rel(path) for path in files)
            failures.append(f"duplicate ID {item_id}: {locations}")

    known_ids = {item_id for item_id in id_to_files if ID_RE.match(item_id)}
    for file_path, metadata in sorted(metadata_by_file.items()):
        validate_relationships(file_path, metadata, known_ids, failures)

    if failures:
        print("Workspace minimal validation: FAIL")
        print(f"Workspace: {rel(SAMPLE_ROOT)}")
        print(f"Markdown files checked: {len(markdown_files)}")
        print(f"ID-bearing files checked: {len(id_bearing_files)}")
        print("Failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Workspace minimal validation: PASS")
    print(f"Workspace: {rel(SAMPLE_ROOT)}")
    print(f"Markdown files checked: {len(markdown_files)}")
    print(f"ID-bearing files checked: {len(id_bearing_files)}")
    print(f"IDs found: {len(id_to_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
