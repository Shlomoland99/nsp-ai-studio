"""Google Gemini-family adapter boundary.

This adapter intentionally does not invent credentials or provider endpoints.
Wire the official Google GenAI SDK in deployment, using GEMINI_API_KEY.
"""

from dataclasses import dataclass
from os import getenv
from typing import Any


@dataclass
class GoogleAIAdapter:
    provider_id: str = "gemini-pro"

    def configured(self) -> bool:
        return bool(getenv("GEMINI_API_KEY"))

    def connection_status(self) -> dict[str, Any]:
        return {
            "provider": self.provider_id,
            "configured": self.configured(),
            "credential_env": "GEMINI_API_KEY",
            "note": "Model names and quota depend on the Google account and API access.",
        }

    def build_request(self, prompt: str, model: str | None = None) -> dict[str, Any]:
        if not self.configured():
            raise RuntimeError("GEMINI_API_KEY is not configured")
        return {"model": model or self.provider_id, "contents": prompt}
