# AI Incident Response

An AI incident includes any event where an AI system causes or risks material business, security, compliance, financial, or customer impact.

Examples include:

- protected data appearing in a response;
- authorization bypass;
- harmful or policy-violating output;
- sustained hallucination or unsupported-answer spikes;
- runaway token consumption;
- model-provider outage affecting a critical workflow.

The response sequence is:

1. contain the affected route, model, tool, or feature;
2. preserve logs, correlation IDs, prompt/model/retrieval versions, and evidence;
3. assess affected users, data, and actions;
4. notify the technical and business owners;
5. recover through rollback, model switch, configuration change, or feature disablement;
6. complete a post-incident review and update controls.

The objective is not only recovery. The incident must produce a measurable control improvement.
