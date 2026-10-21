# Arogya AI — FastAPI Backend

## Entry point

`main.py` exports the FastAPI `app`. `api/index.py` imports it for Vercel's Python runtime.

## Local run

From the `backend` directory:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Vercel deployment

Import the repository and set the project's **Root Directory** to `backend`. Set `OLLAMA_BASE_URL` to the base URL of a publicly reachable Ollama-compatible API server (without the `/api/chat` suffix). Optionally set `OLLAMA_API_KEY` and `OLLAMA_MODEL`.

The default local endpoint `127.0.0.1:11434` is intentionally not assumed in production: it would point to the deployment runtime itself, not your laptop. Without `OLLAMA_BASE_URL`, `/arogya/chatting` returns HTTP 503 with a configuration message.

## Test

- `GET /health` (once configured in `main.py`)
- `POST /arogya/chatting` with JSON `{ "message": "Describe your general health question" }`

Medical responses are informational only and do not replace a qualified clinician.
