# Résumé des Décisions d’Architecture

Pour le MVP RAG Northstar, l’équipe a choisi Amazon Bedrock pour l’accès géré aux modèles de fondation et Amazon OpenSearch Service comme couche de recherche vectorielle de référence.

Bedrock a été choisi pour accélérer la livraison, réduire la gestion d’infrastructure et offrir un accès géré aux modèles.

SageMaker reste une alternative lorsqu’un entraînement personnalisé, un hébergement spécialisé, un contrôle MLOps plus poussé ou une personnalisation du modèle sont nécessaires.

La récupération et la génération sont séparées afin de rendre les décisions d’architecture réversibles.
