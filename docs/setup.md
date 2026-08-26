# Setup

## Local development

Use Python 3.11 or newer, create a virtual environment, install the dev extra, and copy .env.example to .env. Configure only the integrations you intend to run.

Start ComfyUI separately, usually at http://127.0.0.1:8188, and set COMFYUI_BASE_URL if needed. The bridge sends API-compatible prompt payloads and reports health without requiring ComfyUI at import time.

Run pytest and ruff check .

## External tools

FFmpeg, Blender, DaVinci Resolve/Fusion, and OBS remain separately installed applications. Their adapters use executable paths, WebSocket URLs, or script APIs from environment variables. Cloud integrations use environment-provided API keys/tokens. Never paste credentials into YAML, source, tests, or workflow JSON.
