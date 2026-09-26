# Live Bedrock RAG Demo

A small, deployable portfolio demo that combines:

- **Amazon Bedrock Converse API** for generation
- local evidence retrieval over curated Markdown documents
- explicit citations
- safe fallback when retrieval confidence is too low
- configurable AWS region and Bedrock model ID

This keeps the public demo inexpensive and simple while preserving the enterprise architecture story in the parent project.

## Run locally

```bash
cd enterprise-rag-aws/live-demo
pip install -r requirements.txt
export AWS_REGION=us-east-1
export BEDROCK_MODEL_ID=<model-or-inference-profile-id>
# authenticate with normal AWS SDK credentials OR:
export AWS_BEARER_TOKEN_BEDROCK=<bedrock-api-key>
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

Main file:

`enterprise-rag-aws/live-demo/app.py`

Add these secrets/environment values in the deployment platform:

- `AWS_REGION`
- `BEDROCK_MODEL_ID`
- Bedrock authentication, preferably through a deployment-specific credential mechanism

Do **not** commit AWS credentials or API keys to GitHub.

## What the demo proves

The application separates:

1. retrieval;
2. evidence thresholding;
3. prompt construction;
4. Bedrock generation;
5. citation return;
6. latency/error telemetry.

The enterprise reference architecture in the parent folder replaces local retrieval with S3/OpenSearch or an approved Bedrock Knowledge Base pattern.
