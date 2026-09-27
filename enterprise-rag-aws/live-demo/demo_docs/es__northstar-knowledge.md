# Conocimiento Empresarial Northstar — Español

## Preparación para producción
Antes de que una solución de IA entre a producción, el responsable del negocio debe aprobar el uso previsto; deben cumplirse los umbrales de evaluación; deben revisarse los controles de acceso y la clasificación de datos; deben estar activos el monitoreo, la gestión de incidentes y los procedimientos de reversión; no debe existir un hallazgo de seguridad bloqueante; y deben documentarse los supuestos de costo y alertas de uso.

## Controles para agentes de IA
Las acciones de solo lectura pueden automatizarse para usuarios autorizados. Las acciones que crean compromisos, envían comunicaciones externas, modifican datos maestros o ejecutan transacciones financieras requieren autorización explícita y pueden requerir aprobación humana. Si la autorización es ambigua, el agente debe detenerse y no inferir permiso. Toda acción de alto impacto debe dejar evidencia auditable.

## Gobierno del portafolio
El portafolio Northstar tiene revisión semanal por frente de trabajo, revisión quincenal de dependencias y comité ejecutivo mensual. Los proyectos reportan alcance, confianza en hitos, pronóstico presupuestal, dependencias, RAID y métricas de calidad u operación de IA. Amarillo significa atención de gestión pero recuperación viable. Rojo significa que probablemente se requiere intervención ejecutiva, replaneación o cambio de alcance.

## Decisiones de arquitectura
Para el MVP de RAG, Northstar seleccionó Amazon Bedrock para acceso administrado a modelos fundacionales y Amazon OpenSearch Service como capa vectorial de referencia. Bedrock favorece velocidad de entrega y menor carga operativa. SageMaker se reserva para necesidades de entrenamiento personalizado, hosting especializado, mayor control de MLOps o personalización del modelo. Recuperación y generación están desacopladas para mantener decisiones reversibles.

## Evaluación de IA
Antes de liberar una solución GenAI se usa un conjunto de pruebas versionado. La revisión mínima incluye tasa de respuestas fundamentadas, precisión de citas, respuestas no respaldadas, latencia, éxito de tarea, pruebas adversariales y costo por solicitud. Para el piloto RAG, la meta es al menos 95% de respuestas fundamentadas, al menos 95% de precisión de citas y máximo 3% de respuestas no respaldadas.

## Gobierno de costos
Northstar administra el costo de IA como métrica de entrega. Cada proyecto reporta consumo, costo por 1,000 solicitudes, costo por tarea y variación contra pronóstico. Las alertas de uso se configuran antes de producción. Si el costo supera el umbral aprobado, pueden aplicarse optimización de prompts, ajuste de recuperación, cambio de modelo, caching, controles de tráfico o cambio de alcance.

## Respuesta a incidentes
Un incidente de IA puede incluir exposición de datos protegidos, bypass de autorización, contenido dañino, aumento de respuestas no respaldadas, consumo descontrolado de tokens o caída del proveedor. La secuencia es contener, preservar evidencia, evaluar impacto, comunicar, recuperar y realizar una revisión posterior con una mejora de control medible.
