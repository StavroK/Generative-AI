# Connaissances d’Entreprise Northstar — Français

## Préparation à la production
Avant le passage en production d’une solution IA, le responsable métier doit approuver l’usage prévu; les seuils d’évaluation doivent être atteints; les contrôles d’accès et la classification des données doivent être vérifiés; la supervision, la gestion des incidents et les procédures de retour arrière doivent être actives; aucun problème de sécurité bloquant ne doit rester ouvert; et les hypothèses de coût ainsi que les alertes d’usage doivent être documentées.

## Contrôles des agents IA
Les actions de recherche en lecture seule peuvent être automatisées pour les utilisateurs autorisés. Les actions qui créent un engagement, envoient des communications externes, modifient des données de référence ou exécutent des transactions financières exigent une autorisation explicite et peuvent nécessiter une approbation humaine. Si l’autorisation est ambiguë, l’agent doit s’arrêter et ne pas déduire une permission. Toute action à fort impact doit produire une trace auditable.

## Gouvernance du portefeuille
Le portefeuille Northstar est revu chaque semaine au niveau des workstreams, toutes les deux semaines pour les dépendances et chaque mois en comité exécutif. Les projets rapportent le périmètre, la confiance dans les jalons, le budget prévisionnel, les dépendances, les éléments RAID et les métriques IA. Jaune signifie attention managériale mais récupération possible. Rouge signifie qu’une intervention exécutive, une replanification ou un changement de périmètre est probablement nécessaire.

## Décisions d’architecture
Pour le MVP RAG, Northstar a choisi Amazon Bedrock pour l’accès géré aux modèles de fondation et Amazon OpenSearch Service comme couche vectorielle de référence. Bedrock favorise la rapidité de livraison et réduit la charge d’exploitation. SageMaker est conservé pour l’entraînement personnalisé, l’hébergement spécialisé, un contrôle MLOps plus poussé ou la personnalisation du modèle. La récupération et la génération sont découplées pour conserver des décisions réversibles.

## Évaluation IA
Avant mise en production, une solution GenAI est évaluée sur un jeu de tests versionné. La revue couvre le taux de réponses fondées, la précision des citations, le taux de réponses non supportées, la latence, la réussite des tâches, les tests adversariaux et le coût par requête. Pour le pilote RAG, la cible est au moins 95% de réponses fondées, au moins 95% de précision de citation et au plus 3% de réponses non supportées.

## Gouvernance des coûts
Northstar traite le coût IA comme une métrique de livraison. Chaque projet suit consommation, coût par 1 000 requêtes, coût par tâche métier et variance par rapport au budget. Les alertes sont configurées avant production. En cas de dépassement, les leviers comprennent optimisation des prompts, réglage de la récupération, changement de modèle, cache, contrôle du trafic ou modification du périmètre.

## Réponse aux incidents
Un incident IA peut inclure une fuite de données protégées, un contournement d’autorisation, un contenu nuisible, une hausse des réponses non fondées, une consommation excessive de tokens ou une panne du fournisseur. La séquence est contenir, préserver les preuves, évaluer l’impact, communiquer, rétablir et conduire une revue post-incident avec amélioration mesurable des contrôles.
