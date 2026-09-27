# AI Cost Governance Standard

Northstar manages AI cost as a delivery metric rather than waiting for a monthly cloud bill.

Each project reports:

- forecast monthly AI usage;
- token or inference consumption;
- cost per 1,000 requests where applicable;
- cost per successful business task;
- variance against forecast.

Usage alerts are configured before production launch.

Teams must explicitly set output token limits for model calls and avoid sending unnecessary context.

When cost exceeds the approved threshold, the response may include prompt optimization, retrieval tuning, model substitution, caching, traffic controls, or business-scope changes.

FinOps participates in portfolio reviews for material AI workloads.
