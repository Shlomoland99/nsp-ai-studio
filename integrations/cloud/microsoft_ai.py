"""Microsoft AI integration boundary.

Supports Azure AI Speech and Microsoft Foundry/Phi configuration without
storing credentials or pretending that research-only models are hosted APIs.
"""

from dataclasses import dataclass
from os import getenv
from typing import Any


@dataclass
class MicrosoftAIAdapter:
    provider_id: str = "microsoft-foundry"

    def configured(self) -> bool:
        return bool(getenv("AZURE_AI_API_KEY") or getenv("AZURE_SPEECH_KEY"))

    def connection_status(self) -> dict[str, Any]:
        return {
            "provider": self.provider_id,
            "configured": self.configured(),
            "credential_env": ["AZURE_AI_API_KEY", "AZURE_SPEECH_KEY"],
            "note": "Use the official Azure SDK/API for the selected deployment.",
        }

    def build_request(self, prompt: str, model: str | None = None) -> dict[str, Any]:
        if not self.configured():
            raise RuntimeError("Microsoft/Azure credentials are not configured")
        return {"model": model or self.provider_id, "input": prompt}
