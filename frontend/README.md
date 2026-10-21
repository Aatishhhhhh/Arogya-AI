# Arogya AI — Web Frontend

Static HTML/CSS/JavaScript frontend for Arogya AI.

## Deploy

Import this repository into Vercel and set the **Root Directory** to `frontend`. Use the `Other` framework preset and leave the build command empty.

The AI chat calls `https://arogya-ai-backend-sandy.vercel.app/arogya/chatting` by default. To override it before deploying, edit `API_BASE_URL` near the top of the JavaScript in `index.html`.

## Prototype limitations

- Google sign-in is a demo flow, not real OAuth.
- Profile/family details are stored in browser localStorage, not protected clinical storage.
- Medical image uploads are preview-only; the current backend accepts text only.
- Doctor directory uses sample listings and does not book appointments.
