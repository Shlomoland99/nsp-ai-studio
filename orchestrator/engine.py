import logging
from .contracts import CreativeJob, ProviderAdapter, ProviderResult
from .exceptions import ConsentRequired
from .router import CapabilityRouter

log = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self, router: CapabilityRouter, adapters: dict[str, ProviderAdapter]) -> None:
        self.router, self.adapters = router, adapters
    async def run(self, job: CreativeJob) -> ProviderResult:
        if any(x in job.capabilities for x in ("face-consistency", "talking-avatar")) and not job.consent_granted:
            raise ConsentRequired("Explicit authorization is required for voice/face identity features.")
        provider_id = self.router.route(job)
        adapter = self.adapters.get(provider_id)
        if adapter is None:
            raise RuntimeError(f"Adapter is not configured: {provider_id}")
        log.info("dispatching creative job", extra={"provider": provider_id, "intent": job.intent})
        return await adapter.execute(job)
