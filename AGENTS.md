# Codex / Agent Instructions — NSP AI Studio

## Mission
Build NSP AI Studio as a modular AI creator operating system. A user should be able to describe a creative result in natural language and have the system route work through the best available local or cloud engines.

## Architecture rules
1. Do not vendor entire third-party applications into this repository.
2. Integrate external applications through API, MCP, CLI, WebSocket, scripting, SDK, watch-folder, or file exchange where supported.
3. Keep provider adapters isolated behind stable interfaces.
4. Core orchestration code must not depend on provider-specific payload shapes.
5. Never hard-code credentials.
6. Never commit `.env`, API keys, tokens, passwords, cookies, OAuth refresh tokens, or private certificates.
7. Voice/face cloning features must require authorization/consent semantics.
8. Prefer free/open/local implementations when quality is sufficient.
9. ComfyUI is the primary local generative-media engine.
10. FFmpeg is the canonical media-processing layer.
11. DaVinci Resolve/Fusion is the preferred professional finishing layer.
12. Blender is the preferred 3D/VFX engine.
13. OBS is the preferred live/recording engine.
14. CapCut is a mobile/rapid-edit endpoint, not the core backend.
15. New providers must be addable without changing the orchestrator core.

## Required integration targets
ComfyUI, Wan, FLUX, SDXL, InstantID, IP-Adapter, ControlNet, PuLID, XTTS-v2, F5-TTS, OpenVoice, MuseTalk, LivePortrait, Whisper, WhisperX, FFmpeg, DaVinci Resolve, Fusion, Blender, OBS, CapCut, Gemini, Kling, Higgsfield, Manus, Perplexity, Canva, Notion, Google Drive, Google Sheets, GitHub.

## Required pipelines
- ai-film
- cinematic-ad
- youtube-longform
- youtube-short
- instagram-reel
- tiktok
- thumbnail
- virtual-studio
- character-consistency
- talking-avatar
- podcast-cleanup
- short-film
- multi-platform-publish

## Engineering standards
Use Python 3.11+, typed public interfaces, explicit exceptions, structured logging, provider health checks, tests for registries and routing, and no silent fallbacks that change cost, privacy, or provider behavior.

## First build task
Scaffold the repository with:
- README.md
- .gitignore
- .env.example
- pyproject.toml
- docs/architecture.md
- docs/setup.md
- config/providers.yaml
- config/models.yaml
- config/pipelines.yaml
- orchestrator/
- integrations/
- services/
- workflows/
- scripts/
- tests/

Create a ComfyUI bridge, provider abstraction, capability router, model registry, pipeline registry, and starter tests. Do not commit any real credentials.
