#!/usr/bin/env python3
"""Validate LLM contract templates and samples with standard library checks."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "schemas/llm_input_contract.schema.json",
    "schemas/llm_output_contract.schema.json",
    "templates/llm_input_package_template.json",
    "templates/llm_output_package_template.json",
    "samples/input/sample_llm_input_package.json",
    "samples/output/sample_llm_output_package.json",
]

INPUT_REQUIRED_FIELDS = [
    "contract_version",
    "package_id",
    "workflow",
    "scenario_id",
    "source_bundle",
    "existing_baseline",
    "task_request",
    "constraints",
    "human_approval_policy",
]

OUTPUT_REQUIRED_FIELDS = [
    "contract_version",
    "package_id",
    "workflow",
    "scenario_id",
    "result_status",
    "confirmed_facts",
    "assumptions",
    "unresolved_items",
    "information_gaps",
    "design_impacts",
    "proposed_artifact_updates",
    "human_approval_points",
    "do_not_reflect_yet",
    "failure_metadata",
]

WORKFLOWS = {"meeting-to-design", "evidence-to-decision"}
ALLOWED_OUTPUT_STATUSES = {"draft", "review_required", "needs_more_information", "rejected", "failed"}
REQUIRED_CONSTRAINTS = [
    "do_not_invent_requirements",
    "do_not_mark_as_approved",
    "preserve_uncertainty",
    "require_source_references",
]
REQUIRED_APPROVAL_POLICY = [
    "approval_required_for_design_decisions",
    "approval_required_for_risk_acceptance",
    "approval_required_for_artifact_updates",
]
REQUIRED_SOURCE_FIELDS = [
    "source_id",
    "source_type",
    "source_summary",
    "source_text",
    "source_status",
]
RISKY_MARKERS = [
    "ORI" + "X",
    "Soft" + "Bank",
    "HC" + "NET",
    "Palo " + "Alto",
    "poporonbook" + ".local",
]
LOCAL_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.local\b")


def load_json(relative_path: str, failures: list[str]) -> Any:
    path = ROOT / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        failures.append(f"{relative_path}: invalid JSON: {exc}")
    except FileNotFoundError:
        failures.append(f"{relative_path}: missing file")
    return None


def missing_fields(data: dict[str, Any], required: list[str]) -> list[str]:
    return [field for field in required if field not in data]


def validate_input_package(data: Any, label: str, failures: list[str]) -> None:
    if not isinstance(data, dict):
        failures.append(f"{label}: expected object")
        return
    for field in missing_fields(data, INPUT_REQUIRED_FIELDS):
        failures.append(f"{label}: missing field: {field}")
    if data.get("workflow") not in WORKFLOWS:
        failures.append(f"{label}: unsupported workflow: {data.get('workflow')}")

    source_bundle = data.get("source_bundle")
    if not isinstance(source_bundle, list) or not source_bundle:
        failures.append(f"{label}: source_bundle must be a non-empty list")
    else:
        for index, source in enumerate(source_bundle):
            if not isinstance(source, dict):
                failures.append(f"{label}: source_bundle[{index}] must be an object")
                continue
            for field in missing_fields(source, REQUIRED_SOURCE_FIELDS):
                failures.append(f"{label}: source_bundle[{index}] missing field: {field}")

    constraints = data.get("constraints", {})
    if not isinstance(constraints, dict):
        failures.append(f"{label}: constraints must be an object")
    else:
        for field in REQUIRED_CONSTRAINTS:
            if constraints.get(field) is not True:
                failures.append(f"{label}: constraint must be true: {field}")

    approval_policy = data.get("human_approval_policy", {})
    if not isinstance(approval_policy, dict):
        failures.append(f"{label}: human_approval_policy must be an object")
    else:
        for field in REQUIRED_APPROVAL_POLICY:
            if approval_policy.get(field) is not True:
                failures.append(f"{label}: approval policy must be true: {field}")


def validate_output_package(data: Any, label: str, failures: list[str]) -> None:
    if not isinstance(data, dict):
        failures.append(f"{label}: expected object")
        return
    for field in missing_fields(data, OUTPUT_REQUIRED_FIELDS):
        failures.append(f"{label}: missing field: {field}")

    result_status = data.get("result_status")
    if result_status not in ALLOWED_OUTPUT_STATUSES:
        failures.append(f"{label}: unsupported result_status: {result_status}")
    if result_status == "approved_by_human":
        failures.append(f"{label}: LLM output must not set approved_by_human")

    for field in ["human_approval_points", "do_not_reflect_yet"]:
        value = data.get(field)
        if not isinstance(value, list) or not value:
            failures.append(f"{label}: {field} must be a non-empty list")


def scan_json_samples(failures: list[str]) -> None:
    for relative_path in [
        "templates/llm_input_package_template.json",
        "templates/llm_output_package_template.json",
        "samples/input/sample_llm_input_package.json",
        "samples/output/sample_llm_output_package.json",
    ]:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8", errors="replace")
        for marker in RISKY_MARKERS:
            if marker in text:
                failures.append(f"{relative_path}: risky marker found")
        if LOCAL_EMAIL_RE.search(text):
            failures.append(f"{relative_path}: local email pattern found")


def main() -> int:
    failures: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            failures.append(f"missing file: {relative_path}")

    load_json("schemas/llm_input_contract.schema.json", failures)
    load_json("schemas/llm_output_contract.schema.json", failures)
    input_template = load_json("templates/llm_input_package_template.json", failures)
    output_template = load_json("templates/llm_output_package_template.json", failures)
    input_sample = load_json("samples/input/sample_llm_input_package.json", failures)
    output_sample = load_json("samples/output/sample_llm_output_package.json", failures)

    for label, data in [
        ("input template", input_template),
        ("input sample", input_sample),
    ]:
        if data is not None:
            validate_input_package(data, label, failures)

    for label, data in [
        ("output template", output_template),
        ("output sample", output_sample),
    ]:
        if data is not None:
            validate_output_package(data, label, failures)

    scan_json_samples(failures)

    if failures:
        print("LLM contract validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("LLM contract validation passed.")
    print("- schema files found")
    print("- templates parsed")
    print("- samples parsed")
    print("- constraints enforce uncertainty and approval boundaries")
    print("- output requires human approval and do-not-reflect-yet items")
    return 0


if __name__ == "__main__":
    sys.exit(main())
