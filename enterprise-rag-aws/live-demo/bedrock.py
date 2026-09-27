import os
import boto3


LANGUAGE_NAMES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "pt": "Portuguese",
}


def bedrock_answer(question: str, evidence: list[str], language: str = "en") -> str:
    region = os.environ.get("AWS_REGION", "us-west-2")
    model_id = os.environ.get("BEDROCK_MODEL_ID")
    if not model_id:
        raise RuntimeError("BEDROCK_MODEL_ID is not configured")

    client = boto3.client("bedrock-runtime", region_name=region)
    language_name = LANGUAGE_NAMES.get(language, "English")

    system = f"""You are a governed enterprise knowledge assistant.
Answer only from the evidence supplied by the application.
If the evidence is insufficient, say so clearly.
Do not invent policies, approvals, thresholds, dates, or owners.
Keep the response concise and decision-oriented.
Answer in {language_name}."""

    context = "\n\n---\n\n".join(evidence)
    prompt = f"""QUESTION:
{question}

APPROVED EVIDENCE:
{context}

Answer the question using only the approved evidence."""

    response = client.converse(
        modelId=model_id,
        system=[{"text": system}],
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig={
            "maxTokens": 500,
            "temperature": 0.1,
            "topP": 0.9,
        },
    )
    return response["output"]["message"]["content"][0]["text"]
