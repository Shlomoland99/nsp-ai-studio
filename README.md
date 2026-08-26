# NSP AI Studio

NSP AI Studio is a modular AI creator operating system. It accepts intent, resolves capabilities, selects an approved provider, and executes media pipelines through stable provider-neutral interfaces.

## Principles

- ComfyUI is the primary local generative-media engine.
- FFmpeg is the canonical media-processing layer.
- DaVinci Resolve/Fusion, Blender, and OBS are professional endpoints.
- Providers are adapters; orchestration never depends on provider payload shapes.
- Credentials are loaded from environment variables and are never committed.
- Voice and face cloning require explicit authorization metadata.

## Quick start

    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install -e '.[dev]'
    cp .env.example .env
    pytest

Run a routing example:

    python -m orchestrator.cli --capability text-to-image --local-only

See docs/setup.md and docs/architecture.md.

## Required integrations

ComfyUI, Wan, FLUX, SDXL, InstantID, IP-Adapter, ControlNet, PuLID, XTTS-v2, F5-TTS, OpenVoice, MuseTalk, LivePortrait, Whisper, WhisperX, FFmpeg, DaVinci Resolve, Fusion, Blender, OBS, CapCut, Gemini, Kling, Higgsfield, Manus, Perplexity, Canva, Notion, Google Drive, Google Sheets, and GitHub are represented in the provider catalog. Install or configure each external system separately.
