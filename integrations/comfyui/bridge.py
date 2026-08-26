import httpx
from orchestrator.contracts import CreativeJob, ProviderResult
from orchestrator.exceptions import ProviderUnavailable

class ComfyUIAdapter:
    provider_id = "comfyui"
    def __init__(self, base_url: str = "http://127.0.0.1:8188", timeout: float = 120) -> None:
        self.base_url, self.timeout = base_url.rstrip("/"), timeout
    async def health(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/system_stats")
                return response.is_success
        except httpx.HTTPError:
            return False
    async def execute(self, job: CreativeJob) -> ProviderResult:
        workflow = job.payload.get("workflow")
        if not isinstance(workflow, dict):
            raise ValueError("ComfyUI jobs require payload['workflow'] as a mapping.")
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(f"{self.base_url}/prompt", json={"prompt": workflow})
                response.raise_for_status()
        except httpx.HTTPError as exc:
            raise ProviderUnavailable("ComfyUI prompt submission failed") from exc
        return ProviderResult(self.provider_id, "submitted", response.json())
