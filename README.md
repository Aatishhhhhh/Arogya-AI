# Arogya AI

Arogya AI is a healthcare frontend and FastAPI prototype.

## Repository layout
- `frontend/`: static HTML/CSS/JavaScript web app
- `backend/`: FastAPI endpoint and Ollama-compatible inference adapter

## Frontend deployment
Create a Vercel project from this repository, set Root Directory to `frontend`, and deploy with the `Other` framework preset.

## Backend deployment
Create a second Vercel project from the same repository, set Root Directory to `backend`, and set the environment variables described in `backend/README.md`.

## Important prototype limitations
Google sign-in is a demo flow. Profile/family data uses browser localStorage, report uploads are browser-local previews, doctor cards use sample data, and the AI backend currently accepts text only. Do not enter real medical records until authentication, server-side authorization, encryption, secure object storage, and appropriate clinical/security review are implemented.
