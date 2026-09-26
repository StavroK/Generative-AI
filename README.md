# Senior AI Technical Project Manager Portfolio

[![AWS](https://img.shields.io/badge/AWS-Bedrock%20%7C%20SageMaker%20%7C%20Lambda%20%7C%20S3-orange)](./enterprise-rag-aws/)
[![GenAI](https://img.shields.io/badge/GenAI-RAG%20%7C%20Agents%20%7C%20LLMOps-blue)](./llmops-delivery-framework/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Governance%20%7C%20RAID%20%7C%20Exec%20Reporting-green)](./ai-portfolio-governance/)
[![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit%20%2B%20Plotly-red)](./ai-program-risk-dashboard/)

## Executive summary

This portfolio demonstrates how I would lead a multi-project enterprise AI program from **business case and architecture through Agile execution, production readiness, risk governance, and executive reporting**.

The portfolio is organized around the fictional **Northstar Enterprise AI Transformation Program** so that every artifact fits into one coherent delivery story.

## Portfolio at a glance

| Area | What it proves | Open |
|---|---|---|
| Enterprise RAG on AWS | GenAI + AWS architecture, backlog, security, IaC, release governance | [View](./enterprise-rag-aws/) |
| AI Portfolio Governance | Multi-project health, budget, dependencies, RAID, steering decisions | [View](./ai-portfolio-governance/) |
| Agentic AI Governance | Human approval, tool authorization, runtime policy boundaries | [View](./agentic-ai-governance/) |
| LLMOps Delivery Framework | AI-specific lifecycle gates, observability, incidents, release criteria | [View](./llmops-delivery-framework/) |
| AI Program Risk Dashboard | Executive visualization of delivery and AI KPIs | [View](./ai-program-risk-dashboard/) |
| AI TPM Playbook | Reusable charters, readiness reviews, Scrum cadence and governance templates | [View](./ai-project-manager-playbook/) |

## Northstar program architecture

```mermaid
flowchart TD
    EX[Executive Steering Committee] --> PMO[AI Portfolio Governance]
    PMO --> RAG[Customer Support RAG]
    PMO --> LEGAL[Contract Intelligence]
    PMO --> AGENT[Sales AI Agent]
    PMO --> ML1[Predictive Maintenance]
    PMO --> ML2[Fraud Detection]

    RAG --> AWS[Shared AWS AI Platform]
    LEGAL --> AWS
    AGENT --> AWS
    ML1 --> AWS
    ML2 --> AWS

    AWS --> BEDROCK[Amazon Bedrock]
    AWS --> SM[Amazon SageMaker]
    AWS --> S3[Amazon S3]
    AWS --> OS[Amazon OpenSearch]
    AWS --> LAMBDA[AWS Lambda]

    PMO --> LLMOPS[LLMOps / MLOps Gates]
    PMO --> DASH[Executive Risk Dashboard]
```

## What I want an interviewer to see

- I can manage **multiple concurrent AI initiatives**, not only one prototype.
- I understand enough architecture to challenge assumptions and sequence work credibly.
- I treat **AI evaluation, security, cost, and operations** as delivery gates—not afterthoughts.
- I can convert technical progress into **decision-oriented executive reporting**.
- I know how to govern AI agents with authorization boundaries and human approval.
- I use Agile ceremonies to improve flow and evidence, not to create meeting overhead.

## Suggested interview walkthrough

1. Start with [AI Portfolio Governance](./ai-portfolio-governance/) to show portfolio-level leadership.
2. Open [Enterprise RAG on AWS](./enterprise-rag-aws/) for architecture, backlog and production-readiness depth.
3. Show [Agentic AI Governance](./agentic-ai-governance/) for modern GenAI risk controls.
4. Open [LLMOps Delivery Framework](./llmops-delivery-framework/) to explain how AI delivery differs from normal software delivery.
5. Finish with the [AI Program Risk Dashboard](./ai-program-risk-dashboard/) and [Role Match](./docs/ROLE_MATCH.md).

## Repository map

```text
Generative-AI/
├── enterprise-rag-aws/
├── ai-portfolio-governance/
├── agentic-ai-governance/
├── llmops-delivery-framework/
├── ai-program-risk-dashboard/
├── ai-project-manager-playbook/
└── docs/
    └── ROLE_MATCH.md
```

## Scope note

All business names, budgets, metrics and scenarios in the Northstar program are fictional and created for portfolio demonstration. Reference architectures and controls are intended to show technical-delivery fluency and governance judgment; they do not claim production deployment of every illustrated component.
