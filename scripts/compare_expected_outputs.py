#!/usr/bin/env python3
"""Minimal placeholder comparison for v0.1 eval expectations."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    cases = [
        {
            "expected": ROOT / "evals" / "expected" / "case_001_expected.md",
            "outputs": [
                ROOT / "samples" / "output" / "sample_delta_report.md",
                ROOT / "samples" / "output" / "sample_unresolved_issues.md",
            ],
            "tokens": ["Branch-B", "Unresolved", "Customer", "Pending"],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_002_expected.md",
            "outputs": [
                ROOT / "samples" / "output" / "sample_issue_register.md",
                ROOT / "samples" / "output" / "sample_decision_log.md",
                ROOT / "samples" / "output" / "sample_stakeholder_questions.md",
                ROOT / "samples" / "output" / "sample_design_update_proposal.md",
            ],
            "tokens": [
                "Branch-B",
                "customer_confirmation_required",
                "vendor_confirmation_required",
                "detailed_design_handoff",
                "human_approval_required",
            ],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_003_expected.md",
            "outputs": [
                ROOT / "samples" / "output" / "sample_official_source_reconciliation.md",
                ROOT / "samples" / "output" / "sample_information_gap_request.md",
                ROOT / "samples" / "output" / "sample_design_decision_packet.md",
                ROOT / "samples" / "output" / "sample_design_reflection_request.md",
            ],
            "tokens": [
                "partially_aligned",
                "BASE-001",
                "customer_confirmation",
                "detailed-design handoff",
                "review_required",
                "needs_more_information",
            ],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_004_expected.md",
            "outputs": [
                ROOT / "samples" / "output" / "scenario_002_source_manifest.md",
                ROOT / "samples" / "output" / "scenario_002_requirements_table.md",
                ROOT / "samples" / "output" / "scenario_002_issue_register.md",
                ROOT / "samples" / "output" / "scenario_002_decision_log.md",
                ROOT / "samples" / "output" / "scenario_002_delta_report.md",
                ROOT / "samples" / "output" / "scenario_002_design_decision_packet.md",
                ROOT / "samples" / "output" / "scenario_002_information_gap_request.md",
                ROOT / "samples" / "output" / "scenario_002_design_reflection_request.md",
                ROOT / "samples" / "output" / "scenario_002_human_approval_checklist.md",
            ],
            "tokens": [
                "Northstar Manufacturing",
                "internal_review",
                "vendor_confirmation_required",
                "customer_confirmation_required",
                "Communication matrix",
                "Approval Required",
                "not approved",
            ],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_005_expected.md",
            "outputs": [
                ROOT / "generated" / "scenario_003" / "evidence-to-decision" / "README.md",
                ROOT / "generated" / "scenario_003" / "evidence-to-decision" / "source_manifest.md",
                ROOT / "generated" / "scenario_003" / "evidence-to-decision" / "official_source_reconciliation.md",
                ROOT / "generated" / "scenario_003" / "evidence-to-decision" / "information_gap_request.md",
                ROOT / "generated" / "scenario_003" / "evidence-to-decision" / "design_decision_packet.md",
                ROOT / "generated" / "scenario_003" / "evidence-to-decision" / "design_reflection_request.md",
                ROOT / "generated" / "scenario_003" / "evidence-to-decision" / "human_approval_checklist.md",
            ],
            "tokens": [
                "scenario_003",
                "evidence-to-decision",
                "draft",
                "human_approval_required",
                "This scaffold is not an approved design update.",
                "Human review and approval are required",
                "Do not mark generated scaffold content as `approved`.",
            ],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_006_expected.md",
            "outputs": [
                ROOT / "docs" / "llm_contract_layer.md",
                ROOT / "docs" / "llm_state_model.md",
                ROOT / "templates" / "llm_input_package_template.json",
                ROOT / "templates" / "llm_output_package_template.json",
                ROOT / "samples" / "input" / "sample_llm_input_package.json",
                ROOT / "samples" / "output" / "sample_llm_output_package.json",
            ],
            "tokens": [
                "contract_version",
                "evidence-to-decision",
                "do_not_invent_requirements",
                "do_not_mark_as_approved",
                "preserve_uncertainty",
                "require_source_references",
                "review_required",
                "human_approval_points",
                "do_not_reflect_yet",
                "needs_more_information",
            ],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_007_expected.md",
            "outputs": [
                ROOT / "evals" / "fixtures" / "llm_contract" / "valid_review_required_output.json",
                ROOT / "evals" / "fixtures" / "llm_contract" / "valid_needs_more_information_output.json",
                ROOT / "evals" / "fixtures" / "llm_contract" / "invalid_approved_by_human_output.json",
                ROOT / "evals" / "fixtures" / "llm_contract" / "invalid_missing_source_references_output.json",
                ROOT / "evals" / "fixtures" / "llm_contract" / "invalid_empty_human_approval_points_output.json",
                ROOT / "evals" / "fixtures" / "llm_contract" / "invalid_assumption_promoted_to_fact_output.json",
                ROOT / "evals" / "fixtures" / "llm_contract" / "invalid_design_update_marked_approved_output.json",
                ROOT / "evals" / "fixtures" / "llm_contract" / "invalid_unresolved_item_closed_output.json",
                ROOT / "evals" / "reports" / "case_007_report.md",
            ],
            "tokens": [
                "valid_review_required_output.json",
                "valid_needs_more_information_output.json",
                "invalid_approved_by_human_output.json",
                "invalid_missing_source_references_output.json",
                "invalid_empty_human_approval_points_output.json",
                "invalid_assumption_promoted_to_fact_output.json",
                "invalid_design_update_marked_approved_output.json",
                "invalid_unresolved_item_closed_output.json",
                "approved_by_human",
                "source_references",
                "human_approval_points",
                "approved_for_update",
                "closed",
                "needs_more_information",
            ],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_008_expected.md",
            "outputs": [
                ROOT / "docs" / "network_design_domain_model.md",
                ROOT / "docs" / "communication_matrix_model.md",
                ROOT / "docs" / "routing_sdwan_impact_model.md",
                ROOT / "docs" / "security_sse_boundary_model.md",
                ROOT / "docs" / "monitoring_logging_requirement_model.md",
                ROOT / "docs" / "dr_failover_review_model.md",
                ROOT / "samples" / "input" / "scenario_003_network_domain_meeting.md",
                ROOT / "samples" / "output" / "scenario_003_network_domain_review_packet.md",
                ROOT / "samples" / "output" / "scenario_003_routing_impact_analysis.md",
                ROOT / "samples" / "output" / "scenario_003_security_boundary_review.md",
                ROOT / "samples" / "output" / "scenario_003_monitoring_logging_review.md",
                ROOT / "samples" / "output" / "scenario_003_dr_failover_review.md",
            ],
            "tokens": [
                "Atlas Retail",
                "Communication Matrix",
                "Routing / SD-WAN",
                "Security / SSE",
                "Monitoring / Logging",
                "DR / Failover",
                "Cloud-Security-Service",
                "SD-WAN-Edge-01",
                "Monitoring-System",
                "human_approval_required",
                "review_required",
                "needs_more_information",
                "Do Not Reflect Yet",
            ],
        },
    ]

    failures: list[str] = []
    for case in cases:
        expected = case["expected"]
        output_paths = case["outputs"]
        for path in [expected, *output_paths]:
            if not path.exists():
                failures.append(f"missing file: {path.relative_to(ROOT)}")
        if failures:
            continue
        expected_text = expected.read_text(encoding="utf-8")
        combined = "\n".join(path.read_text(encoding="utf-8") for path in output_paths)
        for token in case["tokens"]:
            if token in expected_text and token not in combined:
                failures.append(f"expected token not found in sample outputs: {token}")

    if failures:
        print("Expected output comparison failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Expected output comparison passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
