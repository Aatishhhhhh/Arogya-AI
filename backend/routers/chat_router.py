from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3:0.6b"
router = APIRouter()
class ChatRequest(BaseModel):
    message: str
@router.post("/arogya/chatting")
def get_response(userdata: ChatRequest):
    problem = userdata.message
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are the Arogya AI healthcare assistant. "
                    "Do not claim to diagnose medical conditions "
                    "or prescribe medication. Use reviewed health "
                    "records when they are supplied. If information "
                    "is insufficient, state that clearly. "
                    "Do not invent medical facts.",
                    "do not invent facts"
                ),
            },
            {
                "role": "user",
                "content": problem,
            },
        ],
        "think": False,
        "stream": False,
        "options": {
            "temperature": 0.2,
        },
    }
    response = httpx.post(
        URL,
        json=payload,
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()
    answer = data.get("message", {}).get("content", "").strip()
    if not answer:
        raise HTTPException(
            status_code=502,
            detail="The AI model returned an empty response.",
        )
    return {
        "reply": answer,
        "model": MODEL,
    }
    