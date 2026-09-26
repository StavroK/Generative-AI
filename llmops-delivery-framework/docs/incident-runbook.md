# AI Incident Runbook

## Example incident triggers
- Protected data exposed in a response
- Material authorization bypass
- Sustained unsupported-answer spike
- Model/provider outage
- Cost anomaly or runaway requests
- Harmful or policy-violating output in governed use case

## First response
1. Contain: disable affected route/tool/model if needed.
2. Preserve: retain correlation IDs, logs and configuration versions.
3. Assess: users/data/actions affected.
4. Communicate: incident owner and business owner.
5. Recover: rollback or apply approved mitigation.
6. Learn: post-incident review and control update.
