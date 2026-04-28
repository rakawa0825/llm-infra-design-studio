# Vendor Note

## Source

- Source ID: `SRC-005`
- Source type: vendor-style technical behavior note
- Scenario: branch network traffic handling
- Status: technical reference only

## Note

A cloud security service can inspect selected traffic classes when traffic is steered through the service according to the customer design.

Exception traffic may require explicit routing policy or policy handling. The behavior of exception traffic should be validated before it is reflected into design artifacts.

Failover behavior depends on the selected design and configuration. Monitoring and management traffic should be validated separately because it may have different operational requirements from user internet-bound traffic.

## Approval boundary

This note explains generic technical behavior. It does not equal customer approval, does not define final project scope, and does not approve design language.
