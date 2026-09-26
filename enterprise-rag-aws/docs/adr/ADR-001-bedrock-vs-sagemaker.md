# ADR-001 — Bedrock vs. SageMaker

## Status
Accepted for the RAG reference architecture.

## Context
The initial use case needs managed access to foundation models, rapid experimentation and minimal model-serving infrastructure.

## Decision
Use **Amazon Bedrock** for the initial RAG production path. Keep **Amazon SageMaker** as the preferred path for workloads requiring custom training, specialized hosting, model-level tuning or ML pipelines.

## Why
- Faster time to managed foundation-model access.
- Reduced infrastructure-management burden for the GenAI MVP.
- Good fit with the surrounding AWS security and observability stack.
- Preserves SageMaker for cases where the team needs deeper model lifecycle control.

## Tradeoffs
- Bedrock reduces operational overhead but can constrain some model-level customization.
- SageMaker provides more control but increases platform and MLOps complexity.

## TPM implication
Treat this as a reversible architecture decision. Revisit if evaluation, latency, cost, portability or customization requirements materially change.
