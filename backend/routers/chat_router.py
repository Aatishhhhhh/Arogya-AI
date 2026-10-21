import os

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

# Configure this in Vercel Project Settings > Environment Variables.
# It must be an externally reachable Ollama-compatible API endpoint,
# not http://127.0.0.1:11434 from your laptop.
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "").rstrip("/")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "")
MODEL = os.getenv("OLLAMA_MODEL", "qwen3:0.6b")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)


@router.post("/arogya/chatting")
async def get_response(userdata: ChatRequest):
    if not OLLAMA_BASE_URL:
        raise HTTPException(
            status_code=503,
            detail=(
                "AI inference is not configured. Set OLLAMA_BASE_URL "
                "to a publicly reachable Ollama-compatible API endpoint."
            ),
        )

    problem = userdata.message.strip()
    if not problem:
        raise HTTPException(status_code=422, detail="Message cannot be empty.")

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are the Arogya AI healthcare assistant. "
                    "Provide general health information, not a diagnosis. "
                    "Do not prescribe medication or recommend treatment as a substitute "
                    "for a licensed clinician. State uncertainty when information is "
                    "insufficient, never invent medical facts, and advise urgent care "
                    "for potentially life-threatening symptoms."
                ),
            },
            {"role": "user", "content": problem},
        ],
        "think": False,
        "stream": False,
        "options": {"temperature": 0.2},
    }

    headers = {}
    if OLLAMA_API_KEY:
        headers["Authorization"] = f"Bearer {OLLAMA_API_KEY}"

    try:
        async with httpx.AsyncClient(timeout=90.0) as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/chat",
                json=payload,
                headers=headers,
            )
            response.raise_for_status()
            data = response.json()
    except httpx.TimeoutException as exc:
        raise HTTPException(
            status_code=504,
            detail="The AI inference service timed out.",
        ) from exc
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"The AI inference service returned HTTP {exc.response.status_code}.",
        ) from exc
    except (httpx.HTTPError, ValueError) as exc:
        raise HTTPException(
            status_code=502,
            detail="Could not communicate with the AI inference service.",
        ) from exc

    answer = data.get("message", {}).get("content", "")
    if not isinstance(answer, str) or not answer.strip():
        raise HTTPException(
            status_code=502,
            detail="The AI model returned an empty response.",
        )

    return {"reply": answer.strip(), "model": MODEL}
