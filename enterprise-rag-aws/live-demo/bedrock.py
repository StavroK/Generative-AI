import os
import boto3


SYSTEM = """You are a governed enterprise knowledge assistant.
Answer only from the evidence supplied by the application.
If the evidence is insufficient, say so clearly.
Do not invent policies, approvals, thresholds, dates, or owners.
Keep the response concise and decision-oriented."""


def bedrock_answer(question: str, evidence: list[str]) -> str:
    region = os.environ.get("AWS_REGION", "us-east-1")
    model_id = os.environ.get("BEDROCK_MODEL_ID")
    if not model_id:
        raise RuntimeError("BEDROCK_MODEL_ID is not configured")

    client = boto3.client("bedrock-runtime", region_name=region)

    context = "\n\n---\n\n".join(evidence)
    prompt = f"""QUESTION:
{question}

APPROVED EVIDENCE:
{context}

Answer the question using only the approved evidence."""

    response = client.converse(
        modelId=model_id,
        system=[{"text": SYSTEM}],
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig={
            "maxTokens": 500,
            "temperature": 0.1,
            "topP": 0.9,
        },
    )
    return response["output"]["message"]["content"][0]["text"]
