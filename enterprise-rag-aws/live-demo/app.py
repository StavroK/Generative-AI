from pathlib import Path
import os
import time

import streamlit as st

from bedrock import bedrock_answer
from retrieval import retrieve
from storage import (
    add_document,
    delete_document,
    init_db,
    list_documents,
    reset_documents,
    retrieval_documents,
    seed_from_markdown,
    update_document,
)

BASE = Path(__file__).parent
SEED_DOCS = BASE / "demo_docs"

init_db()
if not list_documents():
    seed_from_markdown(SEED_DOCS)

st.set_page_config(page_title="Northstar RAG Demo", layout="wide")

LANGUAGES = {
    "English": "en",
    "Español": "es",
    "Français": "fr",
    "Português": "pt",
}

T = {
    "en": {
        "title": "Northstar Enterprise Knowledge Assistant",
        "mode_demo": "Generation mode: Demo Mode (Bedrock-ready, no AWS inference required)",
        "mode_bedrock": "Generation mode: Amazon Bedrock",
        "caption": "Portfolio demo: governed evidence retrieval + cited answer generation + knowledge lifecycle management",
        "ask_tab": "Ask the Knowledge Base",
        "manage_tab": "Manage Knowledge Base",
        "suggested": "Suggested interview questions",
        "custom": "Or ask your own question",
        "placeholder": "Ask about governance, architecture, risk, evaluation, cost, or production readiness...",
        "answer": "Answer",
        "sources": "Sources",
        "why": "Why these sources were retrieved",
        "fallback": "I do not have enough approved evidence to answer that question.",
        "governance": "Governance",
        "g1": "Answers are generated only when approved evidence is retrieved.",
        "g2": "Low-confidence retrieval produces a safe fallback.",
        "g3": "Sources are shown with every answer.",
        "fictional": "All Northstar content and metrics are fictional demonstration data.",
        "admin": "Knowledge Base Administration",
        "admin_desc": "Demonstrate the full RAG knowledge lifecycle: add, modify, delete, then re-query the knowledge base.",
        "pass": "Admin passphrase",
        "disabled": "Knowledge Base editing is disabled until KB_ADMIN_PASSWORD is configured.",
        "enter": "Enter the admin passphrase to enable mutations.",
        "enabled": "Admin access enabled",
        "doc_count": "Knowledge documents",
        "add": "Add a document",
        "doc_lang": "Document language",
        "doc_title": "Document title / source name",
        "doc_content": "Document content",
        "add_btn": "Add to knowledge base",
        "required": "Title and content are required.",
        "added": "Document added. Ask a related question in the RAG tab to see it retrieved.",
        "modify": "Modify or delete existing content",
        "select": "Select document",
        "save": "Save changes",
        "saved": "Document updated. Retrieval now uses the new content.",
        "confirm_delete": "Confirm delete",
        "delete": "Delete document",
        "deleted": "Document deleted from the knowledge base.",
        "reset": "Reset demo content",
        "reset_desc": "Restores the original fictional Northstar source documents.",
        "reset_confirm": "I understand this replaces current demo content",
        "reset_btn": "Reset knowledge base",
        "reset_done": "Knowledge base reset to the original demo content.",
    },
    "es": {
        "title": "Asistente de Conocimiento Empresarial Northstar",
        "mode_demo": "Modo de generación: Demo (preparado para Bedrock, sin inferencia AWS)",
        "mode_bedrock": "Modo de generación: Amazon Bedrock",
        "caption": "Demo de portafolio: recuperación gobernada de evidencia + respuestas con fuentes + gestión del ciclo de conocimiento",
        "ask_tab": "Consultar la Base de Conocimiento",
        "manage_tab": "Administrar Base de Conocimiento",
        "suggested": "Preguntas sugeridas para la entrevista",
        "custom": "O haz tu propia pregunta",
        "placeholder": "Pregunta sobre gobierno, arquitectura, riesgo, evaluación, costo o preparación para producción...",
        "answer": "Respuesta",
        "sources": "Fuentes",
        "why": "Por qué se recuperaron estas fuentes",
        "fallback": "No tengo suficiente evidencia aprobada para responder esa pregunta.",
        "governance": "Gobierno",
        "g1": "Las respuestas se generan solo cuando se recupera evidencia aprobada.",
        "g2": "Una recuperación de baja confianza activa una respuesta segura.",
        "g3": "Las fuentes se muestran con cada respuesta.",
        "fictional": "Todo el contenido y métricas de Northstar son datos ficticios para demostración.",
        "admin": "Administración de la Base de Conocimiento",
        "admin_desc": "Demuestra el ciclo completo de RAG: agregar, modificar, eliminar y volver a consultar.",
        "pass": "Contraseña de administrador",
        "disabled": "La edición está deshabilitada hasta configurar KB_ADMIN_PASSWORD.",
        "enter": "Ingresa la contraseña de administrador para habilitar cambios.",
        "enabled": "Acceso de administrador habilitado",
        "doc_count": "Documentos de conocimiento",
        "add": "Agregar documento",
        "doc_lang": "Idioma del documento",
        "doc_title": "Título / nombre de fuente",
        "doc_content": "Contenido del documento",
        "add_btn": "Agregar a la base",
        "required": "Título y contenido son obligatorios.",
        "added": "Documento agregado. Haz una pregunta relacionada para comprobar la recuperación.",
        "modify": "Modificar o eliminar contenido existente",
        "select": "Seleccionar documento",
        "save": "Guardar cambios",
        "saved": "Documento actualizado. La recuperación ya usa el nuevo contenido.",
        "confirm_delete": "Confirmar eliminación",
        "delete": "Eliminar documento",
        "deleted": "Documento eliminado de la base de conocimiento.",
        "reset": "Restablecer contenido demo",
        "reset_desc": "Restaura los documentos ficticios originales de Northstar.",
        "reset_confirm": "Entiendo que esto reemplaza el contenido actual",
        "reset_btn": "Restablecer base",
        "reset_done": "Base de conocimiento restablecida.",
    },
    "fr": {
        "title": "Assistant de Connaissances d’Entreprise Northstar",
        "mode_demo": "Mode de génération : Démo (prêt pour Bedrock, sans inférence AWS)",
        "mode_bedrock": "Mode de génération : Amazon Bedrock",
        "caption": "Démo portfolio : récupération gouvernée des preuves + réponses sourcées + gestion du cycle de connaissances",
        "ask_tab": "Interroger la Base de Connaissances",
        "manage_tab": "Gérer la Base de Connaissances",
        "suggested": "Questions suggérées pour l’entretien",
        "custom": "Ou posez votre propre question",
        "placeholder": "Questionnez la gouvernance, l’architecture, le risque, l’évaluation, le coût ou la mise en production...",
        "answer": "Réponse",
        "sources": "Sources",
        "why": "Pourquoi ces sources ont été récupérées",
        "fallback": "Je ne dispose pas de suffisamment de preuves approuvées pour répondre.",
        "governance": "Gouvernance",
        "g1": "Les réponses sont générées uniquement lorsqu’une preuve approuvée est récupérée.",
        "g2": "Une récupération à faible confiance déclenche une réponse sûre.",
        "g3": "Les sources sont affichées avec chaque réponse.",
        "fictional": "Tout le contenu et les métriques Northstar sont fictifs et destinés à la démonstration.",
        "admin": "Administration de la Base de Connaissances",
        "admin_desc": "Démontrez le cycle RAG complet : ajouter, modifier, supprimer, puis interroger de nouveau.",
        "pass": "Mot de passe administrateur",
        "disabled": "L’édition est désactivée tant que KB_ADMIN_PASSWORD n’est pas configuré.",
        "enter": "Saisissez le mot de passe administrateur pour autoriser les modifications.",
        "enabled": "Accès administrateur activé",
        "doc_count": "Documents de connaissance",
        "add": "Ajouter un document",
        "doc_lang": "Langue du document",
        "doc_title": "Titre / nom de la source",
        "doc_content": "Contenu du document",
        "add_btn": "Ajouter à la base",
        "required": "Le titre et le contenu sont obligatoires.",
        "added": "Document ajouté. Posez une question associée pour tester la récupération.",
        "modify": "Modifier ou supprimer le contenu existant",
        "select": "Sélectionner un document",
        "save": "Enregistrer les modifications",
        "saved": "Document mis à jour. La récupération utilise maintenant le nouveau contenu.",
        "confirm_delete": "Confirmer la suppression",
        "delete": "Supprimer le document",
        "deleted": "Document supprimé de la base de connaissances.",
        "reset": "Réinitialiser le contenu de démo",
        "reset_desc": "Restaure les documents fictifs Northstar d’origine.",
        "reset_confirm": "Je comprends que cela remplace le contenu actuel",
        "reset_btn": "Réinitialiser la base",
        "reset_done": "Base de connaissances réinitialisée.",
    },
    "pt": {
        "title": "Assistente de Conhecimento Empresarial Northstar",
        "mode_demo": "Modo de geração: Demo (pronto para Bedrock, sem inferência AWS)",
        "mode_bedrock": "Modo de geração: Amazon Bedrock",
        "caption": "Demo de portfólio: recuperação governada de evidências + respostas com fontes + gestão do ciclo de conhecimento",
        "ask_tab": "Consultar a Base de Conhecimento",
        "manage_tab": "Gerenciar Base de Conhecimento",
        "suggested": "Perguntas sugeridas para a entrevista",
        "custom": "Ou faça sua própria pergunta",
        "placeholder": "Pergunte sobre governança, arquitetura, risco, avaliação, custo ou preparação para produção...",
        "answer": "Resposta",
        "sources": "Fontes",
        "why": "Por que estas fontes foram recuperadas",
        "fallback": "Não tenho evidências aprovadas suficientes para responder a essa pergunta.",
        "governance": "Governança",
        "g1": "As respostas são geradas somente quando evidências aprovadas são recuperadas.",
        "g2": "Recuperação de baixa confiança ativa uma resposta segura.",
        "g3": "As fontes são exibidas em cada resposta.",
        "fictional": "Todo o conteúdo e métricas Northstar são fictícios e destinados à demonstração.",
        "admin": "Administração da Base de Conhecimento",
        "admin_desc": "Demonstre o ciclo completo de RAG: adicionar, modificar, excluir e consultar novamente.",
        "pass": "Senha de administrador",
        "disabled": "A edição está desabilitada até KB_ADMIN_PASSWORD ser configurada.",
        "enter": "Digite a senha de administrador para habilitar alterações.",
        "enabled": "Acesso de administrador habilitado",
        "doc_count": "Documentos de conhecimento",
        "add": "Adicionar documento",
        "doc_lang": "Idioma do documento",
        "doc_title": "Título / nome da fonte",
        "doc_content": "Conteúdo do documento",
        "add_btn": "Adicionar à base",
        "required": "Título e conteúdo são obrigatórios.",
        "added": "Documento adicionado. Faça uma pergunta relacionada para testar a recuperação.",
        "modify": "Modificar ou excluir conteúdo existente",
        "select": "Selecionar documento",
        "save": "Salvar alterações",
        "saved": "Documento atualizado. A recuperação já usa o novo conteúdo.",
        "confirm_delete": "Confirmar exclusão",
        "delete": "Excluir documento",
        "deleted": "Documento excluído da base de conhecimento.",
        "reset": "Restaurar conteúdo demo",
        "reset_desc": "Restaura os documentos fictícios Northstar originais.",
        "reset_confirm": "Entendo que isso substitui o conteúdo atual",
        "reset_btn": "Restaurar base",
        "reset_done": "Base de conhecimento restaurada.",
    },
}

QUESTIONS = {
    "en": [
        "What is required before an AI solution can move to production?",
        "When does an AI agent require human approval?",
        "How is the Northstar AI portfolio governed?",
        "Why did the team choose Bedrock instead of SageMaker for the RAG MVP?",
        "What AI quality metrics are reviewed before release?",
        "How does the program control AI cost and usage?",
        "What happens during an AI incident?",
        "What should happen when authorization is ambiguous?",
    ],
    "es": [
        "¿Qué se requiere antes de que una solución de IA pase a producción?",
        "¿Cuándo requiere aprobación humana un agente de IA?",
        "¿Cómo se gobierna el portafolio de IA Northstar?",
        "¿Por qué se eligió Bedrock en lugar de SageMaker para el MVP de RAG?",
        "¿Qué métricas de calidad de IA se revisan antes de liberar?",
        "¿Cómo controla el programa el costo y uso de IA?",
        "¿Qué sucede durante un incidente de IA?",
        "¿Qué debe ocurrir cuando la autorización es ambigua?",
    ],
    "fr": [
        "Qu’est-ce qui est requis avant qu’une solution d’IA passe en production ?",
        "Quand un agent d’IA nécessite-t-il une approbation humaine ?",
        "Comment le portefeuille IA Northstar est-il gouverné ?",
        "Pourquoi l’équipe a-t-elle choisi Bedrock plutôt que SageMaker pour le MVP RAG ?",
        "Quelles métriques de qualité IA sont examinées avant la mise en production ?",
        "Comment le programme contrôle-t-il les coûts et l’utilisation de l’IA ?",
        "Que se passe-t-il lors d’un incident IA ?",
        "Que doit-il se passer lorsque l’autorisation est ambiguë ?",
    ],
    "pt": [
        "O que é necessário antes de uma solução de IA entrar em produção?",
        "Quando um agente de IA exige aprovação humana?",
        "Como o portfólio de IA Northstar é governado?",
        "Por que a equipe escolheu Bedrock em vez de SageMaker para o MVP de RAG?",
        "Quais métricas de qualidade de IA são revisadas antes da liberação?",
        "Como o programa controla custo e uso de IA?",
        "O que acontece durante um incidente de IA?",
        "O que deve acontecer quando a autorização é ambígua?",
    ],
}

language_label = st.selectbox("Language / Idioma / Langue / Idioma", list(LANGUAGES.keys()))
lang = LANGUAGES[language_label]
tx = T[lang]

mode = os.environ.get("GENERATION_MODE", "demo").lower()
is_bedrock = mode == "bedrock"
admin_password = os.environ.get("KB_ADMIN_PASSWORD", "")

st.title(tx["title"])
if is_bedrock:
    st.success(tx["mode_bedrock"])
else:
    st.warning(tx["mode_demo"])
st.caption(tx["caption"])

ask_tab, manage_tab = st.tabs([tx["ask_tab"], tx["manage_tab"]])

with ask_tab:
    with st.sidebar:
        st.subheader(tx["governance"])
        st.write(tx["g1"])
        st.write(tx["g2"])
        st.write(tx["g3"])
        st.caption(tx["fictional"])

    st.subheader(tx["suggested"])
    cols = st.columns(2)
    selected_question = None
    for idx, q in enumerate(QUESTIONS[lang]):
        if cols[idx % 2].button(q, use_container_width=True, key=f"q_{lang}_{idx}"):
            selected_question = q

    question = st.text_input(
        tx["custom"],
        value=selected_question or "",
        placeholder=tx["placeholder"],
        key=f"question_{lang}",
    )

    def demo_answer(question: str, evidence: list[str], language: str) -> str:
        joined = " ".join(evidence)
        sentences = [s.strip() for s in joined.replace("\n", " ").split(".") if s.strip()]
        selected = sentences[:5]
        prefixes = {
            "en": "Based on the approved evidence: ",
            "es": "Con base en la evidencia aprobada: ",
            "fr": "Selon les preuves approuvées : ",
            "pt": "Com base nas evidências aprovadas: ",
        }
        return prefixes[language] + ". ".join(selected) + "."

    if question:
        start = time.perf_counter()
        chunks = retrieve(question, retrieval_documents(lang), top_k=3)
        min_score = 0.18
        accepted = [c for c in chunks if c.score >= min_score]

        if not accepted:
            st.warning(tx["fallback"])
            st.caption(f"{time.perf_counter() - start:.2f}s")
        else:
            evidence = [c.text for c in accepted]
            answer = bedrock_answer(question, evidence, lang) if is_bedrock else demo_answer(question, evidence, lang)
            st.subheader(tx["answer"])
            st.write(answer)
            st.subheader(tx["sources"])
            for c in accepted:
                st.write(f"- {c.source} ({c.score:.2f})")
            with st.expander(tx["why"]):
                for c in accepted:
                    st.write(f"**{c.source}** — {c.score:.2f}")
                    st.write(c.text[:700] + ("..." if len(c.text) > 700 else ""))

with manage_tab:
    st.subheader(tx["admin"])
    st.write(tx["admin_desc"])
    password = st.text_input(tx["pass"], type="password", key=f"admin_{lang}")
    authorized = bool(admin_password) and password == admin_password

    if not admin_password:
        st.info(tx["disabled"])
    elif not authorized:
        st.info(tx["enter"])
    else:
        st.success(tx["enabled"])
        docs = list_documents()
        st.metric(tx["doc_count"], len(docs))

        with st.expander(tx["add"], expanded=True):
            doc_lang_label = st.selectbox(tx["doc_lang"], list(LANGUAGES.keys()), key="new_doc_lang")
            doc_lang = LANGUAGES[doc_lang_label]
            new_title = st.text_input(tx["doc_title"], key="new_title")
            new_content = st.text_area(tx["doc_content"], height=180, key="new_content")
            if st.button(tx["add_btn"], type="primary"):
                if not new_title.strip() or not new_content.strip():
                    st.error(tx["required"])
                else:
                    add_document(new_title, new_content, doc_lang)
                    st.success(tx["added"])
                    st.rerun()

        st.divider()
        st.subheader(tx["modify"])
        docs = list_documents()
        if docs:
            labels = {f'{d["language"].upper()} | {d["title"]} — {d["updated_at"]}': d for d in docs}
            selected_label = st.selectbox(tx["select"], list(labels.keys()))
            selected = labels[selected_label]
            edit_lang_label = st.selectbox(tx["doc_lang"], list(LANGUAGES.keys()), index=list(LANGUAGES.values()).index(selected["language"]), key=f"lang_{selected['id']}")
            edit_lang = LANGUAGES[edit_lang_label]
            edit_title = st.text_input(tx["doc_title"], value=selected["title"], key=f"title_{selected['id']}")
            edit_content = st.text_area(tx["doc_content"], value=selected["content"], height=260, key=f"content_{selected['id']}")

            c1, c2 = st.columns(2)
            if c1.button(tx["save"], type="primary"):
                update_document(selected["id"], edit_title, edit_content, edit_lang)
                st.success(tx["saved"])
                st.rerun()

            confirm_delete = c2.checkbox(tx["confirm_delete"], key=f"confirm_{selected['id']}")
            if c2.button(tx["delete"], disabled=not confirm_delete):
                delete_document(selected["id"])
                st.success(tx["deleted"])
                st.rerun()

        st.divider()
        st.subheader(tx["reset"])
        st.caption(tx["reset_desc"])
        reset_confirm = st.checkbox(tx["reset_confirm"])
        if st.button(tx["reset_btn"], disabled=not reset_confirm):
            reset_documents(SEED_DOCS)
            st.success(tx["reset_done"])
            st.rerun()
