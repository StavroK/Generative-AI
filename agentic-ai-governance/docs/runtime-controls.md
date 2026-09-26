# Runtime Controls

## Control sequence
1. Authenticate caller.
2. Resolve user entitlements.
3. Validate tool against allowlist.
4. Validate arguments against schema.
5. Evaluate transaction risk.
6. Require approval if threshold/policy demands it.
7. Execute with scoped identity.
8. Record immutable audit events.
9. Observe outcome and exceptions.

## Example runtime budgets
- Maximum agent steps per request: 12
- Maximum external write actions: 1 approved action
- Maximum unresolved tool failures before termination: 2
- Mandatory stop on authorization ambiguity

These values are illustrative and would be tuned per enterprise risk appetite.
