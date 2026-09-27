# Conhecimento Empresarial Northstar — Português

## Preparação para produção
Antes de uma solução de IA entrar em produção, o responsável de negócio deve aprovar o uso previsto; os limites de avaliação devem ser atingidos; controles de acesso e classificação de dados devem ser revisados; monitoramento, gestão de incidentes e procedimentos de rollback devem estar ativos; não pode existir um achado de segurança bloqueante; e premissas de custo e alertas de uso devem estar documentados.

## Controles para agentes de IA
Ações de pesquisa somente leitura podem ser automatizadas para usuários autorizados. Ações que criam compromissos, enviam comunicações externas, alteram dados mestres ou executam transações financeiras exigem autorização explícita e podem exigir aprovação humana. Se a autorização for ambígua, o agente deve parar e não inferir permissão. Toda ação de alto impacto deve gerar uma trilha auditável.

## Governança do portfólio
O portfólio Northstar tem revisão semanal por workstream, revisão quinzenal de dependências e comitê executivo mensal. Os projetos reportam escopo, confiança em marcos, previsão de orçamento, dependências, itens RAID e métricas de IA. Amarelo significa atenção gerencial mas recuperação possível. Vermelho significa provável necessidade de intervenção executiva, replanejamento ou mudança de escopo.

## Decisões de arquitetura
Para o MVP de RAG, Northstar escolheu Amazon Bedrock para acesso gerenciado a modelos fundacionais e Amazon OpenSearch Service como camada vetorial de referência. Bedrock favorece velocidade e menor esforço operacional. SageMaker permanece para treinamento personalizado, hosting especializado, maior controle de MLOps ou customização do modelo. Recuperação e geração são desacopladas para manter decisões reversíveis.

## Avaliação de IA
Antes da liberação, uma solução GenAI é avaliada com um conjunto de testes versionado. A revisão inclui taxa de respostas fundamentadas, precisão de citações, taxa de respostas não suportadas, latência, sucesso da tarefa, testes adversariais e custo por solicitação. Para o piloto RAG, a meta é pelo menos 95% de respostas fundamentadas, pelo menos 95% de precisão de citações e no máximo 3% de respostas não suportadas.

## Governança de custos
Northstar trata custo de IA como métrica de entrega. Cada projeto acompanha consumo, custo por 1.000 solicitações, custo por tarefa de negócio e variação contra previsão. Alertas são configurados antes da produção. Se o custo ultrapassa o limite aprovado, podem ser usados otimização de prompts, ajuste de recuperação, troca de modelo, cache, controles de tráfego ou mudança de escopo.

## Resposta a incidentes
Um incidente de IA pode incluir exposição de dados protegidos, bypass de autorização, conteúdo prejudicial, aumento de respostas não suportadas, consumo excessivo de tokens ou falha do provedor. A sequência é conter, preservar evidências, avaliar impacto, comunicar, recuperar e realizar revisão pós-incidente com melhoria mensurável dos controles.
