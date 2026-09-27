# AI Evaluation Standard

Before release, each GenAI solution must be evaluated against a versioned test set.

The minimum review includes:

- grounded answer rate;
- citation precision;
- unsupported answer rate;
- latency;
- task success;
- prompt-injection or adversarial test results;
- cost per request or cost per business transaction.

For the Northstar RAG pilot, the target grounded answer rate is at least 95 percent, citation precision is at least 95 percent, and unsupported answer rate is no more than 3 percent.

A model or prompt change cannot be promoted solely because subjective responses "look better." It must be evaluated against the same or an approved successor benchmark.
