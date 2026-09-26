# ADR-002 — OpenSearch for Vector Retrieval

## Status
Accepted for the reference architecture.

## Context
The RAG solution needs semantic retrieval, metadata filtering, operational observability and alignment with the AWS estate.

## Decision
Use **Amazon OpenSearch Service** as the reference vector-retrieval layer.

## Rationale
- Vector and text-search capabilities in one managed service.
- Familiar AWS IAM/network integration.
- Metadata filtering supports governed retrieval.
- Appropriate for teams already operating OpenSearch.

## Risks / alternatives
A purpose-built vector database may outperform or simplify some retrieval workloads. The choice should be revisited using measured recall, latency, cost and operational-complexity data.

## Delivery implication
The backlog must preserve a retrieval abstraction so changing vector stores does not require rewriting the entire application.
