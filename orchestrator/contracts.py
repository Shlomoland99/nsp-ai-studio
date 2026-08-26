from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol

@dataclass(frozen=True)
class CreativeJob:
    intent: str
    capabilities: tuple[str, ...]
    payload: Mapping[str, Any] = field(default_factory=dict)
    local_only: bool = False
    consent_granted: bool = False

@dataclass(frozen=True)
class ProviderResult:
    provider_id: str
    status: str
    data: Mapping[str, Any] = field(default_factory=dict)

class ProviderAdapter(Protocol):
    provider_id: str
    async def health(self) -> bool: ...
    async def execute(self, job: CreativeJob) -> ProviderResult: ...
