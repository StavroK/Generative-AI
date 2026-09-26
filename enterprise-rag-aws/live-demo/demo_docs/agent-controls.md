# AI Agent Action Policy

Northstar AI agents follow a risk-based action policy.

Read-only search actions may be automated when the user is authorized.

Actions that create commitments, send external communications, change master data, or execute financial transactions require explicit authorization and may require human approval.

If authorization is ambiguous, the agent must stop rather than infer permission.

All high-impact tool actions must produce an auditable event containing the user, tool, action, decision, and outcome.
