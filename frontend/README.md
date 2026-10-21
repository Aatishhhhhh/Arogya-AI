# Arogya AI — Web Frontend Prototype

Static HTML/CSS/JavaScript prototype for the Arogya AI frontend.

## Local preview

Open `index.html` in a modern browser. No build step is required.

## Deploy on Vercel

1. Push this folder to the `Arogya-AI` GitHub repository.
2. In Vercel, choose **Add New → Project** and import the GitHub repository.
3. Select **Other** as the Framework Preset.
4. Keep the project root as `./`. Leave the build command empty; there is no build step.
5. Deploy.

## Prototype limitations

- Google sign-in is a demo flow, not real OAuth.
- Health form data is stored in browser localStorage, not a secure medical database.
- Selected medical-report images are previewed in the current browser session only; files are not uploaded to a backend.
- AI chat and doctor filters are frontend prototypes. They are not yet connected to a deployed API or live doctor/booking service.
