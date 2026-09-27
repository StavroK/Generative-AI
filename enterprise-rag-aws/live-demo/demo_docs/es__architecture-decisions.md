# Resumen de Decisiones de Arquitectura

Para el MVP de RAG de Northstar, el equipo seleccionó Amazon Bedrock para acceso administrado a modelos fundacionales y Amazon OpenSearch Service como capa de recuperación vectorial de referencia.

Bedrock fue seleccionado porque el MVP priorizó entrega rápida, acceso administrado a modelos y menor carga de gestión de infraestructura.

SageMaker permanece como alternativa cuando se requiere entrenamiento personalizado, hosting especializado, mayor control de MLOps o personalización a nivel de modelo.

La arquitectura separa recuperación y generación para permitir cambios de vector store o proveedor de modelo sin rediseñar toda la solución.
