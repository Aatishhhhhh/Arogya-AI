import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.chat_router import router as chat_r

app = FastAPI(
    title="Arogya AI API",
    version="0.1.0",
    description="Prototype API for Arogya AI.",
)

# Exact deployed frontend domains should be supplied through the
# FRONTEND_ORIGINS environment variable, comma-separated.
# Local origins below are for development only.
configured_origins = os.getenv("FRONTEND_ORIGINS", "")
origins = [
    origin.strip().rstrip("/")
    for origin in configured_origins.split(",")
    if origin.strip()
]
origins.extend([
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://arogya-ai-backend-sandy.vercel.app",
])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.get("/")
async def root():
    return {"service": "arogya-ai-backend", "status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok", "service": "arogya-ai-backend"}


app.include_router(chat_r)
