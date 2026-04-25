#!/usr/bin/env python3
"""Validate LLM contract templates, samples, and failure fixtures."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "evals" / "fixtures" / "llm_contract"

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
SOURCE_BACKED_OUTPUT_LISTS = [
    "confirmed_facts",
    "assumptions",
    "unresolved_items",
    "information_gaps",
    "design_impacts",
    "proposed_artifact_updates",
    "human_approval_points",
    "do_not_reflect_yet",
]
APPROVED_LANGUAGE = {
    "approved",
    "approved_for_update",
    "ready_for_production",
    "final_design",
}
UNCERTAIN_LANGUAGE = {
    "assume",
    "assumption",
    "may",
    "might",
    "uncertain",
    "tentative",
    "appears",
}
CLOSED_LANGUAGE = {"closed", "resolved", "complete", "completed"}
RISKY_MARKERS = [
    "ORI" + "X",
    "Soft" + "Bank",
    "HC" + "NET",
    "Palo " + "Alto",
    "poporonbook" + ".local",
]
LOCAL_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.local\b")


@dataclass(frozen=True)
class FixtureExpectation:
    filename: str
    should_pass: bool
    label: str


FIXTURE_EXPECTATIONS = [
    FixtureExpectation("valid_review_required_output.json", True, "Review-required fixture"),
    FixtureExpectation("valid_needs_more_information_output.json", True, "Needs-more-information fixture"),
    FixtureExpectation("invalid_approved_by_human_output.json", False, "Invalid approved_by_human fixture"),
    FixtureExpectation("invalid_missing_source_references_output.json", False, "Invalid missing source references fixture"),
    FixtureExpectation("invalid_empty_human_approval_points_output.json", False, "Invalid empty human approval points fixture"),
    FixtureExpectation("invalid_assumption_promoted_to_fact_output.json", False, "Invalid assumption promoted to fact fixture"),
    FixtureExpectation("invalid_design_update_marked_approved_output.json", False, "Invalid design update marked approved fixture"),
    FixtureExpectation("invalid_unresolved_item_closed_output.json", False, "Invalid unresolved item closed fixture"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate LLM contract assets.")
    parser.add_argument("--include-negative", action="store_true", help="Validate expected pass/fail fixture behavior.")
    return parser.parse_args()


def load_json(relative_path: str | Path, failures: list[str]) -> Any:
    path = Path(relative_path)
    if not path.is_absolute():
        path = ROOT / path
    label = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        failures.append(f"{label}: invalid JSON: {exc}")
    except FileNotFoundError:
        failures.append(f"{label}: missing file")
    return None


def missing_fields(data: dict[str, Any], required: list[str]) -> list[str]:
    return [field for field in required if field not in data]


def normalize_words(value: Any) -> str:
    if isinstance(value, str):
        return value.lower()
    if isinstance(value, dict):
        return " ".join(normalize_words(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(normalize_words(item) for item in value)
    return str(value).lower()


def contains_term(text: str, term: str) -> bool:
    return re.search(rf"\b{re.escape(term)}\b", text) is not None


def source_refs_present(item: dict[str, Any]) -> bool:
    refs = item.get("source_references")
    return isinstance(refs, list) and bool(refs) and all(isinstance(ref, str) and ref for ref in refs)


def validate_input_package(data: Any, label: str) -> list[str]:
    failures: list[str] = []
    if not isinstance(data, dict):
        return [f"{label}: expected object"]
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
    return failures


def validate_output_package(data: Any, label: str) -> list[str]:
    failures: list[str] = []
    if not isinstance(data, dict):
        return [f"{label}: expected object"]
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

    for field in SOURCE_BACKED_OUTPUT_LISTS:
        value = data.get(field)
        if not isinstance(value, list):
            continue
        for index, item in enumerate(value):
            if isinstance(item, dict) and not source_refs_present(item):
                failures.append(f"{label}: {field}[{index}] missing source_references")

    for index, fact in enumerate(data.get("confirmed_facts", [])):
        if not isinstance(fact, dict):
            continue
        fact_text = normalize_words(fact)
        if fact.get("status") == "assumption" or any(contains_term(fact_text, word) for word in UNCERTAIN_LANGUAGE):
            failures.append(f"{label}: confirmed_facts[{index}] appears to contain an assumption")

    for index, update in enumerate(data.get("proposed_artifact_updates", [])):
        if not isinstance(update, dict):
            continue
        update_text = normalize_words(update)
        if any(contains_term(update_text, word) for word in APPROVED_LANGUAGE):
            failures.append(f"{label}: proposed_artifact_updates[{index}] contains approval-like language")

    for index, item in enumerate(data.get("unresolved_items", [])):
        if not isinstance(item, dict):
            continue
        item_text = normalize_words(item)
        if any(contains_term(item_text, word) for word in CLOSED_LANGUAGE):
            failures.append(f"{label}: unresolved_items[{index}] appears closed without human approval")
    return failures


def scan_json_paths(paths: list[str | Path]) -> list[str]:
    failures: list[str] = []
    for relative_path in paths:
        path = Path(relative_path)
        if not path.is_absolute():
            path = ROOT / path
        label = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        for marker in RISKY_MARKERS:
            if marker in text:
                failures.append(f"{label}: risky marker found")
        if LOCAL_EMAIL_RE.search(text):
            failures.append(f"{label}: local email pattern found")
    return failures


def validate_positive_assets() -> list[str]:
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
            failures.extend(validate_input_package(data, label))

    for label, data in [
        ("output template", output_template),
        ("output sample", output_sample),
    ]:
        if data is not None:
            failures.extend(validate_output_package(data, label))

    failures.extend(
        scan_json_paths(
            [
                "templates/llm_input_package_template.json",
                "templates/llm_output_package_template.json",
                "samples/input/sample_llm_input_package.json",
                "samples/output/sample_llm_output_package.json",
            ]
        )
    )
    return failures


def validate_fixture(expectation: FixtureExpectation) -> tuple[bool, list[str]]:
    fixture_path = FIXTURE_DIR / expectation.filename
    failures: list[str] = []
    data = load_json(fixture_path, failures)
    if data is not None:
        failures.extend(validate_output_package(data, expectation.label))
        failures.extend(scan_json_paths([fixture_path]))
    actual_passed = not failures
    expected_behavior_met = actual_passed is expectation.should_pass
    return expected_behavior_met, failures


def validate_negative_mode() -> list[str]:
    failures: list[str] = []
    if not FIXTURE_DIR.is_dir():
        return [f"missing fixture directory: {FIXTURE_DIR.relative_to(ROOT)}"]

    print("LLM Contract Validation")
    positive_failures = validate_positive_assets()
    if positive_failures:
        print("Positive sample: failed")
        failures.extend(positive_failures)
    else:
        print("Positive sample: passed")

    for expectation in FIXTURE_EXPECTATIONS:
        behavior_ok, fixture_failures = validate_fixture(expectation)
        if expectation.should_pass:
            status = "passed" if behavior_ok else "failed"
            print(f"{expectation.label}: {status}")
        else:
            status = "rejected as expected" if behavior_ok else "accepted unexpectedly"
            print(f"{expectation.label}: {status}")
        if not behavior_ok:
            failures.append(f"{expectation.label}: unexpected validation result")
            failures.extend(fixture_failures)

    if failures:
        print("Overall result: failed")
    else:
        print("Overall result: passed")
    return failures


def main() -> int:
    args = parse_args()

    if args.include_negative:
        failures = validate_negative_mode()
        if failures:
            for failure in failures:
                print(f"- {failure}")
            return 1
        return 0

    failures = validate_positive_assets()
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
