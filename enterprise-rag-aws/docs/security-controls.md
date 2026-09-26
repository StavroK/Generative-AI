# Security Controls

| Control Area | Control |
|---|---|
| Identity | IAM least privilege; separated service roles |
| Data | S3 encryption with KMS; TLS in transit |
| Secrets | Secrets Manager / environment reference; never commit secrets |
| Authorization | Document-level access filters propagated to retrieval |
| Logging | Request IDs, failures, model usage; redact sensitive prompt content where required |
| Prompt Security | Injection test cases; system-prompt protections; tool boundary enforcement |
| Network | Private connectivity/VPC endpoints where architecture requires |
| Monitoring | CloudWatch alarms for failures, latency and anomalous usage |
| Audit | Configuration and release evidence retained |
