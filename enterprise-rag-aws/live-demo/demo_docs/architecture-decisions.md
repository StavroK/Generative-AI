# Architecture Decision Summary

For the initial Northstar RAG MVP, the team selected Amazon Bedrock for managed foundation-model access and Amazon OpenSearch Service as the reference vector retrieval layer.

Bedrock was selected because the MVP prioritized rapid delivery, managed model access, and lower infrastructure-management overhead.

SageMaker remains an alternative for workloads that require custom model training, specialized hosting, deeper MLOps control, or model-level customization.

The architecture deliberately separates retrieval from generation so the vector store or model provider can be changed without redesigning the entire application.

Architecture decisions are treated as reversible when business requirements, latency, cost, quality, or security evidence changes.
