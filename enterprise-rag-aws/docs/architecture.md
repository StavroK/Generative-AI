# Architecture Overview

## Components
- **Amazon S3** — governed source-document storage.
- **AWS Lambda** — serverless orchestration and API logic.
- **Amazon Bedrock** — foundation-model inference and embeddings reference capability.
- **Amazon OpenSearch Service** — vector retrieval layer.
- **Amazon API Gateway** — managed API entry point.
- **Amazon CloudWatch** — logs, metrics and alarms.
- **AWS IAM** — least-privilege identities and roles.
- **AWS KMS** — encryption keys for protected data.

## Logical request path
1. User submits a question.
2. API authenticates and authorizes the request.
3. Retrieval service queries the vector index.
4. Relevant passages and metadata are assembled.
5. Bedrock generates a grounded response using retrieved context.
6. Response returns citations and confidence/evaluation metadata.
7. Telemetry is emitted for latency, token usage, failures and quality sampling.

## Key design principles
- Retrieval before generation.
- Source traceability by default.
- Least privilege.
- No secrets in code.
- Model/provider abstraction where practical.
- Evaluation gates before production promotion.
