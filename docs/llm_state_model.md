# LLM State Model

## Purpose

This state model defines the allowed states for future LLM-assisted workflow execution.

## Allowed States

| State | Meaning | Owner |
| --- | --- | --- |
| `draft` | Work is incomplete or newly initialized. | System or human |
| `review_required` | Output is ready for human review but not approved. | System or human |
| `needs_more_information` | Source evidence is insufficient. | System or human |
| `rejected` | A human reviewer rejected the output or proposal. | Human |
| `approved_by_human` | A human approver explicitly approved the item. | Human only |
| `failed` | Contract validation or processing failed. | System |

## Approval Rules

- `approved_by_human` can only be set by a human.
- LLM-generated outputs must not set final approval.
- `review_required` is the normal state for design decision packets.
- `needs_more_information` is used when source evidence is insufficient.
- `failed` is used for contract validation or processing failures.

## Boundary

The state model supports future automation without transferring design approval authority to an LLM-assisted step.
