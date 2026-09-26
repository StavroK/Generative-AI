# Agile Backlog

## EPIC 1 — Document Ingestion
**Outcome:** Authorized enterprise documents are transformed into searchable chunks with metadata.

### US-101 — Upload and ingest documents
As a knowledge manager, I want approved documents ingested from S3 so that employees can query current enterprise knowledge.

**Acceptance Criteria**
- PDF and text content supported for MVP.
- Document ID, owner, classification and effective date retained.
- Failed ingestion is logged and retryable.
- Unauthorized source locations are rejected.

### US-102 — Chunk and embed content
- Configurable chunk size and overlap.
- Embeddings stored with source metadata.
- Duplicate documents identified.

## EPIC 2 — Retrieval
### US-201 — Retrieve relevant passages
- Top-k retrieval configurable.
- Metadata filters supported.
- Retrieval latency instrumented.

## EPIC 3 — Generation
### US-301 — Generate grounded response
- Model only answers from supplied context for governed use case.
- Sources returned with answer.
- Fallback used when evidence is insufficient.

## EPIC 4 — Security
### US-401 — Enforce user access filters
- Retrieval results respect user/document authorization.
- Access-control tests included in CI or release validation.

## EPIC 5 — Evaluation
### US-501 — Run golden-set evaluation
- Versioned question/answer dataset.
- Groundedness, citation precision, latency and unsupported-answer rate reported.

## EPIC 6 — Production Operations
### US-601 — Monitor service health
- Error rate, P95 latency, token use and request volume visible.
- Alerts route to named support path.
