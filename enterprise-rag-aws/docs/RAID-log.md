# RAID Log

| ID | Type | Description | Probability | Impact | Owner | Mitigation / Action | Status |
|---|---|---|---|---|---|---|---|
| R-001 | Risk | Retrieval quality below groundedness target | M | H | AI Lead | Tune chunking, metadata and reranking; expand eval set | Open |
| R-002 | Risk | Sensitive documents indexed outside intended audience | L | H | Security Lead | ACL-aware ingestion; access testing; IAM review | Open |
| R-003 | Risk | P95 latency exceeds target | M | M | Platform Lead | Profile retrieval/model latency; caching; model alternatives | Open |
| R-004 | Risk | Token consumption exceeds budget | M | M | TPM/FinOps | Cost dashboard; prompt/context limits; usage alerts | Open |
| A-001 | Assumption | Source documents have usable metadata | — | M | Product Owner | Validate sample during discovery | Open |
| I-001 | Issue | Policy taxonomy inconsistent across repositories | — | M | Knowledge Owner | Normalize metadata before bulk ingestion | Open |
| D-001 | Dependency | Security approval for production IAM roles | — | H | Security Lead | Review in Week 8, not at launch | Tracking |
