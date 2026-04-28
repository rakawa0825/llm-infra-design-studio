# <artifact_title>

## Review response status

- lifecycle_phase: "<review_response>"
- response_status: "DRAFT"
- approval_status: "REVIEW_REQUIRED"
- comments_closed_by_default: false

## Review comment mapping

| Review comment ID | Affected artifact | Affected section | Status |
| --- | --- | --- | --- |
| `<review_comment_id>` | `<artifact>` | `<affected_section>` | `REVIEW_REQUIRED` |

## Draft response

### `<review_comment_id>`

- draft_response: "<draft_response>"
- status: "REVIEW_REQUIRED"

## Related source IDs

- `<source_id>`

## Related requirement / issue IDs

- `<requirement_id>`
- `<design_issue_id>`
- `<unresolved_item_id>`

## Next action

`<next_action>`

## Closure allowed

No comment is closed by default.

Closure requires:

- source sufficiency review,
- unresolved item review,
- human approval,
- artifact reflection decision when applicable.

## Approval requirement

- approval_required: true
- approver_role: "<owner_role>"
- approval_status: "REVIEW_REQUIRED"
