# NSP AI Studio

NSP AI Studio is a deployable API and orchestration service for routing creative requests to local and cloud providers.

## Scope

This repository focuses on the web/API service, provider adapters, ComfyUI connectivity, configuration, and deployment. Payments, mobile applications, and media-publishing pipelines are intentionally out of scope.

## Quick start

    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install -e '.[dev]'
    cp .env.example .env
    uvicorn backend.app.main:app --reload --port 8000

Health check:

    curl http://localhost:8000/health

Submit an API job:

    curl -X POST http://localhost:8000/v1/jobs -H 'Content-Type: application/json' -d '{"intent":"poster","capabilities":["text-to-image"],"local_only":true}'

Run tests with pytest. Use Docker Compose for local deployment.

## Integrations

ComfyUI, FFmpeg, Blender, OBS, Gemini, Canva, Notion, Google Drive, Google Sheets, and GitHub are represented through isolated adapters. Configure credentials only through environment variables or your deployment secret manager.