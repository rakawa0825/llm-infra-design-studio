#!/usr/bin/env python3
"""Validate required headings and simple table columns in sample outputs."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "sample_source_manifest.md": ["# Sample Source Manifest", "## Notes"],
    "sample_requirements_table.md": [
        "# Sample Requirements Table",
        "## Customer Confirmation Items",
        "## Vendor Confirmation Items",
        "## Detailed-Design Handoff Items",
        "## Human Approval Points",
    ],
    "sample_unresolved_issues.md": ["# Sample Unresolved Issues", "## Human Approval Points"],
    "sample_delta_report.md": ["# Sample Delta Report", "## Assumptions", "## Human Approval Points"],
    "sample_human_approval_checklist.md": ["# Sample Human Approval Checklist", "## Approval Rules"],
    "sample_issue_register.md": ["# Sample Issue Register", "## Human Approval Points"],
    "sample_decision_log.md": ["# Sample Decision Log", "## Decision Rules"],
    "sample_stakeholder_questions.md": ["# Sample Stakeholder Questions", "## Human Review Required"],
    "sample_design_update_proposal.md": [
        "# Sample Design Update Proposal",
        "## Proposal Summary",
        "## Source Evidence",
        "## Proposed Artifact Updates",
        "## Human Approval Points",
    ],
    "sample_official_source_reconciliation.md": [
        "# Sample Official Source Reconciliation",
        "## Human Review Required",
    ],
    "sample_information_gap_request.md": [
        "# Sample Information Gap Request",
        "## Status Allowed Values",
    ],
    "sample_design_decision_packet.md": [
        "# Sample Design Decision Packet",
        "## Metadata",
        "## Confirmed Facts",
        "## Assumptions",
        "## Human Decisions Required",
        "## Do Not Reflect Yet",
    ],
    "sample_design_reflection_request.md": [
        "# Sample Design Reflection Request",
        "## Human Approval Points",
        "## Reflection Status Allowed Values",
    ],
    "scenario_002_source_manifest.md": ["# Scenario 002 Source Manifest", "## Notes"],
    "scenario_002_requirements_table.md": ["# Scenario 002 Requirements Table", "## Human Approval Points"],
    "scenario_002_issue_register.md": ["# Scenario 002 Issue Register", "## Human Approval Points"],
    "scenario_002_decision_log.md": ["# Scenario 002 Decision Log", "## Decision Rules"],
    "scenario_002_delta_report.md": ["# Scenario 002 Delta Report", "## Assumptions", "## Human Approval Points"],
    "scenario_002_design_decision_packet.md": [
        "# Scenario 002 Design Decision Packet",
        "## Metadata",
        "## Confirmed Facts",
        "## Assumptions",
        "## Human Decisions Required",
        "## Do Not Reflect Yet",
    ],
    "scenario_002_information_gap_request.md": [
        "# Scenario 002 Information Gap Request",
        "## Status Allowed Values",
    ],
    "scenario_002_design_reflection_request.md": [
        "# Scenario 002 Design Reflection Request",
        "## Human Approval Points",
        "## Reflection Status Allowed Values",
    ],
    "scenario_002_human_approval_checklist.md": [
        "# Scenario 002 Human Approval Checklist",
        "## Approval Rules",
    ],
    "scenario_003_network_domain_review_packet.md": [
        "# Scenario 003 Network Domain Review Packet",
        "## Domain Coverage",
        "## Communication Matrix Impact",
        "## Routing / SD-WAN Impact",
        "## Security / SSE Boundary Impact",
        "## Monitoring / Logging Impact",
        "## DR / Failover Impact",
        "## Human Approval Points",
        "## Do Not Reflect Yet",
    ],
    "scenario_003_routing_impact_analysis.md": [
        "# Scenario 003 Routing Impact Analysis",
        "## Human Approval Points",
    ],
    "scenario_003_security_boundary_review.md": [
        "# Scenario 003 Security Boundary Review",
        "## Human Approval Points",
    ],
    "scenario_003_monitoring_logging_review.md": [
        "# Scenario 003 Monitoring Logging Review",
        "## Human Approval Points",
    ],
    "scenario_003_dr_failover_review.md": [
        "# Scenario 003 DR Failover Review",
        "## Human Approval Points",
    ],
    "sample_source_registry.md": [
        "# Sample Source Registry",
        "## Source Registry",
        "## Source Type Taxonomy",
        "## Source Status Taxonomy",
        "## Authority Levels",
        "## Human Approval Boundary",
    ],
    "sample_artifact_map.md": [
        "# Sample Artifact Map",
        "## Artifact Map",
        "## Source-To-Artifact Traceability",
        "## Human Approval Points",
        "## Do Not Reflect Yet",
    ],
}

REQUIRED_TABLE_COLUMNS = {
    "sample_source_manifest.md": [
        "Source ID",
        "Title",
        "Type",
        "Owner",
        "Date",
        "Summary",
        "Sample-Safety Status",
        "Downstream Use",
    ],
    "sample_requirements_table.md": [
        "Requirement ID",
        "Requirement",
        "Status",
        "Source ID",
        "Confidence",
        "Confirmation Owner",
        "Notes",
    ],
    "sample_unresolved_issues.md": [
        "Issue ID",
        "Issue",
        "Category",
        "Owner",
        "Source ID",
        "Impact",
        "Next Action",
        "Approval Needed",
    ],
    "sample_delta_report.md": [
        "Delta ID",
        "New Source",
        "Previous Understanding",
        "New Information",
        "Impacted Artifact",
        "Impact",
        "Recommendation",
        "Human Decision",
    ],
    "sample_human_approval_checklist.md": [
        "Approval ID",
        "Item",
        "Approval Type",
        "Required Approver",
        "Status",
        "Residual Risk",
        "Notes",
    ],
    "sample_issue_register.md": [
        "Issue ID",
        "Issue",
        "Category",
        "Owner Role",
        "Status",
        "Impact",
        "Next Action",
        "Source Reference",
        "Approval Required",
    ],
    "sample_decision_log.md": [
        "Decision ID",
        "Decision Statement",
        "Decision Status",
        "Decision Scope",
        "Owner Role",
        "Approver Role",
        "Decision Date",
        "Source Reference",
        "Rationale",
        "Follow-Up",
    ],
    "sample_stakeholder_questions.md": [
        "Question ID",
        "Target Stakeholder",
        "Question",
        "Reason",
        "Design Impact",
        "Status",
        "Source Reference",
        "Needed Before",
    ],
    "sample_design_update_proposal.md": [
        "Proposal ID",
        "Impacted Artifact",
        "Proposed Update",
        "Status",
        "Source Reference",
        "Human Approval Required",
    ],
    "sample_official_source_reconciliation.md": [
        "Source ID",
        "Source Type",
        "Source Date Or Version",
        "Extracted Claim",
        "Related Meeting Statement",
        "Alignment Status",
        "Conflict Or Gap",
        "Required Action",
    ],
    "sample_information_gap_request.md": [
        "Gap ID",
        "Gap Type",
        "Related Source",
        "Affected Artifact",
        "Question",
        "Owner Role",
        "Required Before",
        "Status",
    ],
    "sample_design_decision_packet.md": [
        "Decision ID",
        "Decision",
        "Decision Status",
        "Approver Role",
    ],
    "sample_design_reflection_request.md": [
        "Request ID",
        "Target Artifact",
        "Target Section",
        "Proposed Change",
        "Evidence",
        "Assumptions",
        "Approval Required",
        "Reflection Status",
    ],
    "scenario_002_source_manifest.md": [
        "Source ID",
        "Title",
        "Type",
        "Owner",
        "Date",
        "Summary",
        "Sample-Safety Status",
        "Downstream Use",
    ],
    "scenario_002_requirements_table.md": [
        "Requirement ID",
        "Requirement",
        "Status",
        "Source ID",
        "Confidence",
        "Confirmation Owner",
        "Notes",
    ],
    "scenario_002_issue_register.md": [
        "Issue ID",
        "Issue",
        "Category",
        "Owner Role",
        "Status",
        "Impact",
        "Next Action",
        "Source Reference",
        "Approval Required",
    ],
    "scenario_002_decision_log.md": [
        "Decision ID",
        "Decision Statement",
        "Decision Status",
        "Decision Scope",
        "Owner Role",
        "Approver Role",
        "Decision Date",
        "Source Reference",
        "Rationale",
        "Follow-Up",
    ],
    "scenario_002_delta_report.md": [
        "Delta ID",
        "New Source",
        "Previous Understanding",
        "New Information",
        "Impacted Artifact",
        "Impact",
        "Recommendation",
        "Human Decision",
    ],
    "scenario_002_design_decision_packet.md": [
        "Decision ID",
        "Decision",
        "Decision Status",
        "Approver Role",
    ],
    "scenario_002_information_gap_request.md": [
        "Gap ID",
        "Gap Type",
        "Related Source",
        "Affected Artifact",
        "Question",
        "Owner Role",
        "Required Before",
        "Status",
    ],
    "scenario_002_design_reflection_request.md": [
        "Request ID",
        "Target Artifact",
        "Target Section",
        "Proposed Change",
        "Evidence",
        "Assumptions",
        "Approval Required",
        "Reflection Status",
    ],
    "scenario_002_human_approval_checklist.md": [
        "Approval ID",
        "Item",
        "Decision Scope",
        "Approver Role",
        "Decision Date",
        "Decision Status",
        "Rationale",
        "Source Reference",
        "Residual Risk",
        "Notes",
    ],
    "scenario_003_network_domain_review_packet.md": [
        "Domain",
        "Coverage Status",
        "Source Reference",
        "Notes",
    ],
    "scenario_003_routing_impact_analysis.md": [
        "route_domain",
        "affected_site",
        "normal_path",
        "backup_path",
        "traffic_steering_assumption",
        "dependency",
        "risk",
        "required_confirmation",
        "approval_status",
    ],
    "scenario_003_security_boundary_review.md": [
        "boundary_id",
        "traffic_scope",
        "inspection_scope",
        "enforcement_point",
        "excluded_traffic",
        "responsibility_owner",
        "confirmation_required",
        "approval_status",
    ],
    "scenario_003_monitoring_logging_review.md": [
        "monitoring_item_id",
        "monitored_component",
        "event_or_metric",
        "log_source",
        "alert_owner",
        "threshold_status",
        "retention_status",
        "detailed_design_handoff",
        "approval_status",
    ],
    "scenario_003_dr_failover_review.md": [
        "dr_item_id",
        "normal_state",
        "failover_trigger",
        "failover_path",
        "restoration_path",
        "monitoring_impact",
        "communication_matrix_impact",
        "security_boundary_impact",
        "approval_status",
    ],
    "sample_source_registry.md": [
        "Source ID",
        "Source Type",
        "Source Title",
        "Source Summary",
        "Source Status",
        "Authority Level",
        "Owner Role",
        "Source Date Or Version",
        "Related Workflow",
        "Related Artifacts",
        "Privacy Classification",
        "Freshness Status",
        "Unresolved Items",
        "Human Review Required",
        "Notes",
    ],
    "sample_artifact_map.md": [
        "Artifact ID",
        "Artifact Type",
        "Artifact Title",
        "Artifact Status",
        "Related Sources",
        "Impacted Sections",
        "Proposed Updates",
        "Unresolved Dependencies",
        "Approval Required",
        "Approver Role",
        "Next Action",
        "Do Not Reflect Yet",
    ],
}

REQUIRED_CSV_COLUMNS = {
    "sample_communication_matrix.csv": [
        "source_zone",
        "source_component",
        "destination_zone",
        "destination_component",
        "protocol",
        "port",
        "direction",
        "status",
        "source_id",
        "notes",
    ],
    "samples/input/scenario_003_network_requirements.csv": [
        "requirement_id",
        "domain",
        "requirement",
        "status",
        "source_reference",
        "confirmation_owner",
        "notes",
    ],
}

REQUIRED_JSON_OBJECTS = {
    "samples/input/sample_llm_input_package.json": [
        "contract_version",
        "package_id",
        "workflow",
        "scenario_id",
        "source_bundle",
        "constraints",
        "human_approval_policy",
    ],
    "samples/output/sample_llm_output_package.json": [
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
    ],
}

GENERATED_REQUIRED = {
    "generated/scenario_003/evidence-to-decision/README.md": [
        "# Evidence-To-Decision Scaffold",
        "## Metadata",
        "## Scaffold Warning",
        "## Status Constraints",
    ],
    "generated/scenario_003/evidence-to-decision/source_manifest.md": [
        "# Source Manifest",
        "## Metadata",
        "## Source Inventory",
        "## Missing Sources",
    ],
    "generated/scenario_003/evidence-to-decision/official_source_reconciliation.md": [
        "# Official Source Reconciliation",
        "## Metadata",
        "## Source Claims",
        "## Required Actions",
    ],
    "generated/scenario_003/evidence-to-decision/information_gap_request.md": [
        "# Information Gap Request",
        "## Metadata",
        "## Gap Table",
        "## Status Allowed Values",
    ],
    "generated/scenario_003/evidence-to-decision/design_decision_packet.md": [
        "# Design Decision Packet",
        "## Metadata",
        "## Confirmed Facts",
        "## Human Decisions Required",
        "## Do Not Reflect Yet",
    ],
    "generated/scenario_003/evidence-to-decision/design_reflection_request.md": [
        "# Design Reflection Request",
        "## Metadata",
        "## Target Artifacts",
        "## Approval Required",
    ],
    "generated/scenario_003/evidence-to-decision/human_approval_checklist.md": [
        "# Human Approval Checklist",
        "## Metadata",
        "## Approval Items",
        "## Decision Status",
    ],
}

GENERATED_REQUIRED_COLUMNS = [
    "Item ID",
    "Status",
    "Source References",
    "Human Approval Required",
    "Notes",
]


def markdown_table_headers(text: str) -> list[list[str]]:
    headers: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if cells and not all(set(cell) <= {"-", " "} for cell in cells):
                headers.append(cells)
    return headers


def missing_columns(actual: list[str], required: list[str]) -> list[str]:
    return [column for column in required if column not in actual]


def has_required_columns(headers: list[list[str]], required: list[str]) -> bool:
    return any(not missing_columns(header, required) for header in headers)


def main() -> int:
    output_dir = ROOT / "samples" / "output"
    failures: list[str] = []

    for filename, headings in REQUIRED.items():
        path = output_dir / filename
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                failures.append(f"{path.relative_to(ROOT)} missing heading: {heading}")

        required_columns = REQUIRED_TABLE_COLUMNS.get(filename, [])
        if required_columns:
            headers = markdown_table_headers(text)
            if not has_required_columns(headers, required_columns):
                for column in required_columns:
                    failures.append(f"{path.relative_to(ROOT)} missing table column: {column}")

    for filename, required_columns in REQUIRED_CSV_COLUMNS.items():
        path = ROOT / filename if "/" in filename else output_dir / filename
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            header = next(reader, [])
        for column in missing_columns(header, required_columns):
            failures.append(f"{path.relative_to(ROOT)} missing CSV column: {column}")

    for relative_path, required_fields in REQUIRED_JSON_OBJECTS.items():
        path = ROOT / relative_path
        if not path.exists():
            failures.append(f"missing file: {relative_path}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{relative_path} invalid JSON: {exc}")
            continue
        if not isinstance(data, dict):
            failures.append(f"{relative_path} must contain a JSON object")
            continue
        for field in required_fields:
            if field not in data:
                failures.append(f"{relative_path} missing JSON field: {field}")

    for relative_path, headings in GENERATED_REQUIRED.items():
        path = ROOT / relative_path
        if not path.exists():
            failures.append(f"missing file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                failures.append(f"{relative_path} missing heading: {heading}")
        if "status: `draft`" not in text:
            failures.append(f"{relative_path} missing draft status")
        if "human_approval_required: `true`" not in text:
            failures.append(f"{relative_path} missing human approval metadata")
        headers = markdown_table_headers(text)
        if not has_required_columns(headers, GENERATED_REQUIRED_COLUMNS):
            for column in GENERATED_REQUIRED_COLUMNS:
                failures.append(f"{relative_path} missing table column: {column}")

    if failures:
        print("Output schema validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Output schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
