# Google-first product map

## Google APIs

Gemini Pro/Flash, Nano Banana image models, Veo video models, Gemini TTS,
and Gemini Live are represented as API-capable providers. They need a
user-owned `GEMINI_API_KEY`; this repository contains no credentials.

Availability, quotas, model names, and pricing depend on the Google account
and the selected model. A free tier, when offered, is limited and is not
unlimited production access.

## Google Labs

Flow, Mixboard, Opal, and Stitch are represented as launch surfaces. The
repository does not use unofficial scraping, browser automation, or invented
endpoints. If Google publishes an official API for a specific operation, its
adapter can be added without changing the orchestration contract.

## Tidio

Tidio is not a Google product. It is listed separately as a third-party
customer-support integration and requires its own Tidio account and key.

Copy `.env.example` to `.env` for local setup. Never commit the resulting
`.env` file or any secret.
