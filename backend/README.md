# Arogya AI — FastAPI Backend

## Entry point
`main.py` exports the FastAPI application. `api/index.py` imports it for Vercel's Python runtime.

## Local run
From the `backend` directory:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Vercel setup
Import this repository as a separate Vercel project and set its Root Directory to `backend`.

Set these Environment Variables in the backend Vercel project:

- `OLLAMA_BASE_URL`: externally reachable Ollama-compatible API base URL, for example a hosted endpoint base without `/api/chat`.
- `OLLAMA_API_KEY`: optional bearer token if the provider requires one.
- `OLLAMA_MODEL`: optional model name; defaults to `qwen3:0.6b`.
- `FRONTEND_ORIGINS`: comma-separated exact Vercel frontend origins, e.g. `https://your-frontend.vercel.app`.

The laptop-only `http://127.0.0.1:11434` endpoint is not used in production. Without `OLLAMA_BASE_URL`, the chat route responds with HTTP 503 and a configuration error.

## Test
- `GET /health`
- `POST /arogya/chatting` with JSON `{"message":"Describe your general health question"}`

This is a prototype API. It is not a diagnostic service and does not replace a qualified clinician.
