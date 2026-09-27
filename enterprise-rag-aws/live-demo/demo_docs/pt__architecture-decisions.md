# Resumo de Decisões de Arquitetura

Para o MVP de RAG Northstar, a equipe escolheu Amazon Bedrock para acesso gerenciado a modelos fundacionais e Amazon OpenSearch Service como camada de recuperação vetorial de referência.

Bedrock foi escolhido por priorizar entrega rápida, acesso gerenciado a modelos e menor esforço operacional de infraestrutura.

SageMaker continua como alternativa quando são necessários treinamento personalizado, hosting especializado, maior controle de MLOps ou customização do modelo.

A arquitetura separa recuperação e geração para tornar as decisões reversíveis.
