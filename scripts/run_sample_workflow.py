#!/usr/bin/env python3
"""Run lightweight repository validation for the sample workflow."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TOP_LEVEL_FILES = [
    "README.md",
    "AGENTS.md",
    "SERVICE_BLUEPRINT.md",
    "LIFECYCLE.md",
    "HUMAN_GOVERNANCE.md",
]

REQUIRED_DIRECTORIES = [
    "docs",
    "workflows",
    "agents",
    "skills",
    "templates",
    "samples/input",
    "samples/output",
    "evals/cases",
    "evals/expected",
    "evals/fixtures/llm_contract",
    "evals/reports",
    "scripts",
    "reports",
    "schemas",
]

REQUIRED_SAMPLE_OUTPUTS = [
    "sample_source_manifest.md",
    "sample_requirements_table.md",
    "sample_delta_report.md",
    "sample_human_approval_checklist.md",
    "sample_issue_register.md",
    "sample_decision_log.md",
    "sample_stakeholder_questions.md",
    "sample_design_update_proposal.md",
    "sample_official_source_reconciliation.md",
    "sample_information_gap_request.md",
    "sample_design_decision_packet.md",
    "sample_design_reflection_request.md",
    "scenario_002_source_manifest.md",
    "scenario_002_requirements_table.md",
    "scenario_002_issue_register.md",
    "scenario_002_decision_log.md",
    "scenario_002_delta_report.md",
    "scenario_002_design_decision_packet.md",
    "scenario_002_information_gap_request.md",
    "scenario_002_design_reflection_request.md",
    "scenario_002_human_approval_checklist.md",
    "scenario_003_network_domain_review_packet.md",
    "scenario_003_routing_impact_analysis.md",
    "scenario_003_security_boundary_review.md",
    "scenario_003_monitoring_logging_review.md",
    "scenario_003_dr_failover_review.md",
    "sample_source_registry.md",
    "sample_artifact_map.md",
]

REQUIRED_EVAL_CASES = [
    "case_001_basic_delta.md",
    "case_002_meeting_to_design_update.md",
    "case_003_evidence_to_decision_loop.md",
    "case_004_second_synthetic_scenario.md",
    "case_005_workflow_scaffold_generator.md",
    "case_006_llm_contract_layer.md",
    "case_007_contract_failure_modes.md",
    "case_008_network_domain_pack.md",
    "case_009_source_registry_artifact_map.md",
]

REQUIRED_SOURCE_REGISTRY_ASSETS = [
    "docs/source_registry_model.md",
    "docs/artifact_map_model.md",
    "templates/source_registry_template.md",
    "templates/artifact_map_template.md",
    "scripts/validate_source_registry.py",
]

REQUIRED_NETWORK_DOMAIN_ASSETS = [
    "docs/network_design_domain_model.md",
    "docs/communication_matrix_model.md",
    "docs/routing_sdwan_impact_model.md",
    "docs/security_sse_boundary_model.md",
    "docs/monitoring_logging_requirement_model.md",
    "docs/dr_failover_review_model.md",
    "templates/network_domain_review_packet_template.md",
    "templates/routing_impact_analysis_template.md",
    "templates/security_boundary_review_template.md",
    "templates/monitoring_logging_requirement_template.md",
    "templates/dr_failover_review_template.md",
    "skills/network-domain-classification/SKILL.md",
    "skills/communication-matrix-review/SKILL.md",
    "skills/routing-sdwan-impact-review/SKILL.md",
    "skills/security-boundary-review/SKILL.md",
    "skills/monitoring-logging-review/SKILL.md",
    "skills/dr-failover-review/SKILL.md",
    "agents/network-domain-review-lead.md",
    "workflows/11_network_domain_review.md",
    "samples/input/scenario_003_network_domain_meeting.md",
    "samples/input/scenario_003_network_baseline.md",
    "samples/input/scenario_003_network_requirements.csv",
    "samples/input/scenario_003_synthetic_vendor_note.md",
]

REQUIRED_GENERATOR_ASSETS = [
    "scripts/generate_workflow_scaffold.py",
    "docs/workflow_scaffold_generator.md",
    "generated/scenario_003/evidence-to-decision/README.md",
    "generated/scenario_003/evidence-to-decision/design_decision_packet.md",
    "generated/scenario_003/evidence-to-decision/design_reflection_request.md",
    "generated/scenario_003/evidence-to-decision/information_gap_request.md",
]

REQUIRED_LLM_CONTRACT_ASSETS = [
    "docs/llm_contract_layer.md",
    "docs/llm_state_model.md",
    "schemas/llm_input_contract.schema.json",
    "schemas/llm_output_contract.schema.json",
    "templates/llm_input_package_template.json",
    "templates/llm_output_package_template.json",
    "samples/input/sample_llm_input_package.json",
    "samples/output/sample_llm_output_package.json",
    "scripts/validate_llm_contracts.py",
    "docs/contract_failure_modes.md",
    "docs/review_required_policy.md",
    "evals/fixtures/llm_contract/valid_review_required_output.json",
    "evals/fixtures/llm_contract/valid_needs_more_information_output.json",
    "evals/fixtures/llm_contract/invalid_approved_by_human_output.json",
    "evals/fixtures/llm_contract/invalid_missing_source_references_output.json",
    "evals/fixtures/llm_contract/invalid_empty_human_approval_points_output.json",
    "evals/fixtures/llm_contract/invalid_assumption_promoted_to_fact_output.json",
    "evals/fixtures/llm_contract/invalid_design_update_marked_approved_output.json",
    "evals/fixtures/llm_contract/invalid_unresolved_item_closed_output.json",
]

VALIDATION_SCRIPTS = [
    "scripts/check_sensitive_identifiers.py",
    "scripts/validate_output_schema.py",
    "scripts/check_unresolved_assertions.py",
    "scripts/compare_expected_outputs.py",
    "scripts/validate_llm_contracts.py --include-negative",
    "scripts/validate_source_registry.py",
]

TEXT_SUFFIXES = {".md", ".csv", ".py", ".txt", ".json", ".gitignore", ".yml", ".yaml", ".html", ".css"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", "tmp", "work", "private"}
RISKY_TERMS = [
    "ORI" + "X",
    "Soft" + "Bank",
    "HC" + "NET",
    "Palo " + "Alto",
    "poporonbook" + ".local",
]
LOCAL_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.local\b")


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: list[str]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def status_text(passed: bool) -> str:
    return "passed" if passed else "failed"


def check_paths(name: str, paths: list[Path], expect_dir: bool = False) -> CheckResult:
    missing: list[str] = []
    for path in paths:
        if expect_dir:
            if not path.is_dir():
                missing.append(rel(path))
        elif not path.is_file():
            missing.append(rel(path))
    return CheckResult(name=name, passed=not missing, details=missing)


def run_validation_script(script: str) -> CheckResult:
    parts = script.split()
    command = [sys.executable, str(ROOT / parts[0]), *parts[1:]]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    details = []
    if completed.stdout.strip():
        details.extend(completed.stdout.strip().splitlines())
    if completed.stderr.strip():
        details.extend(completed.stderr.strip().splitlines())
    return CheckResult(
        name=script,
        passed=completed.returncode == 0,
        details=details or [f"exit code {completed.returncode}"],
    )


def iter_public_safe_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in relative_parts):
            continue
        if path.suffix in TEXT_SUFFIXES or path.name == ".gitignore":
            files.append(path)
    return files


def public_safe_scan() -> CheckResult:
    findings: list[str] = []
    for path in iter_public_safe_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for term in RISKY_TERMS:
            if term in text:
                findings.append(f"{rel(path)}: risky marker found")
        for match in LOCAL_EMAIL_RE.finditer(text):
            findings.append(f"{rel(path)}: local email pattern found: {match.group(0)}")
    return CheckResult(name="Public-safe scan", passed=not findings, details=findings)


def build_results() -> list[CheckResult]:
    results = [
        check_paths("Required files", [ROOT / path for path in REQUIRED_TOP_LEVEL_FILES]),
        check_paths("Required directories", [ROOT / path for path in REQUIRED_DIRECTORIES], expect_dir=True),
        check_paths("Sample outputs", [ROOT / "samples" / "output" / path for path in REQUIRED_SAMPLE_OUTPUTS]),
        check_paths("Eval cases", [ROOT / "evals" / "cases" / path for path in REQUIRED_EVAL_CASES]),
        check_paths("Source registry assets", [ROOT / path for path in REQUIRED_SOURCE_REGISTRY_ASSETS]),
        check_paths("Network domain assets", [ROOT / path for path in REQUIRED_NETWORK_DOMAIN_ASSETS]),
        check_paths("Generator assets", [ROOT / path for path in REQUIRED_GENERATOR_ASSETS]),
        check_paths("LLM contract assets", [ROOT / path for path in REQUIRED_LLM_CONTRACT_ASSETS]),
    ]
    results.extend(run_validation_script(script) for script in VALIDATION_SCRIPTS)
    results.append(public_safe_scan())
    return results


def print_summary(results: list[CheckResult]) -> None:
    grouped_validations = [result for result in results if result.name in VALIDATION_SCRIPTS]
    validation_passed = all(result.passed for result in grouped_validations)
    script_details = [
        f"{result.name}: {status_text(result.passed)}"
        for result in grouped_validations
    ]
    by_name = {result.name: result for result in results}
    overall = all(result.passed for result in results)

    print("LLM Infra Design Studio - CLI Validation Runner")
    print(f"Repository root: {ROOT}")
    print(f"Required files: {status_text(by_name['Required files'].passed)}")
    print(f"Required directories: {status_text(by_name['Required directories'].passed)}")
    print(f"Sample outputs: {status_text(by_name['Sample outputs'].passed)}")
    print(f"Eval cases: {status_text(by_name['Eval cases'].passed)}")
    print(f"Source registry assets: {status_text(by_name['Source registry assets'].passed)}")
    print(f"Network domain assets: {status_text(by_name['Network domain assets'].passed)}")
    print(f"Generator assets: {status_text(by_name['Generator assets'].passed)}")
    print(f"LLM contract assets: {status_text(by_name['LLM contract assets'].passed)}")
    print(f"Validation scripts: {status_text(validation_passed)}")
    for detail in script_details:
        print(f"  - {detail}")
    print(f"Public-safe scan: {status_text(by_name['Public-safe scan'].passed)}")
    print(f"Overall result: {status_text(overall)}")


def report_lines(results: list[CheckResult]) -> list[str]:
    overall = all(result.passed for result in results)
    lines = [
        "# CLI Validation Run",
        "",
        f"- timestamp: {datetime.now(timezone.utc).isoformat()}",
        "- repository_root: `.`",
        f"- overall_status: {status_text(overall)}",
        "",
        "## Checked Files",
        "",
    ]
    for path in REQUIRED_TOP_LEVEL_FILES:
        lines.append(f"- `{path}`")
    lines.extend(["", "## Checked Directories", ""])
    for path in REQUIRED_DIRECTORIES:
        lines.append(f"- `{path}`")
    lines.extend(["", "## Sample Outputs", ""])
    for path in REQUIRED_SAMPLE_OUTPUTS:
        lines.append(f"- `samples/output/{path}`")
    lines.extend(["", "## Eval Cases", ""])
    for path in REQUIRED_EVAL_CASES:
        lines.append(f"- `evals/cases/{path}`")
    lines.extend(["", "## Source Registry Assets", ""])
    for path in REQUIRED_SOURCE_REGISTRY_ASSETS:
        lines.append(f"- `{path}`")
    lines.extend(["", "## Network Domain Assets", ""])
    for path in REQUIRED_NETWORK_DOMAIN_ASSETS:
        lines.append(f"- `{path}`")
    lines.extend(["", "## Generator Assets", ""])
    for path in REQUIRED_GENERATOR_ASSETS:
        lines.append(f"- `{path}`")
    lines.extend(["", "## LLM Contract Assets", ""])
    for path in REQUIRED_LLM_CONTRACT_ASSETS:
        lines.append(f"- `{path}`")

    lines.extend(["", "## Validation Command Results", ""])
    for result in results:
        lines.append(f"### {result.name}")
        lines.append("")
        lines.append(f"Status: {status_text(result.passed)}")
        if result.details:
            lines.append("")
            for detail in result.details:
                lines.append(f"- {detail}")
        lines.append("")

    public_safe = next(result for result in results if result.name == "Public-safe scan")
    lines.extend([
        "## Public-Safe Scan Result",
        "",
        f"Status: {status_text(public_safe.passed)}",
        "",
        "## Next Recommended Action",
        "",
    ])
    if overall:
        lines.append("Review the generated report and commit only if the workflow state is intended.")
    else:
        lines.append("Fix failed checks before committing or publishing changes.")
    return lines


def write_report(path: Path, results: list[CheckResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(report_lines(results)) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate sample workflow assets.")
    parser.add_argument("--check-only", action="store_true", help="Run checks without writing a report.")
    parser.add_argument("--write-report", action="store_true", help="Write a Markdown validation report.")
    parser.add_argument("--report-path", help="Markdown report path. Implies --write-report.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not (ROOT / "README.md").is_file() or not (ROOT / "scripts").is_dir():
        print(f"Repository root check failed: {ROOT}", file=sys.stderr)
        return 1

    results = build_results()
    print_summary(results)

    should_write = args.write_report or bool(args.report_path)
    if should_write and not args.check_only:
        report_path = ROOT / (args.report_path or "reports/latest_cli_validation_run.md")
        write_report(report_path, results)
        print(f"Report written: {report_path}")

    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
