from orchestrator.contracts import ProviderResult, CreativeJob
class GenericCloudAdapter:
    def __init__(self, provider_id: str = "cloud") -> None: self.provider_id = provider_id
    async def health(self) -> bool: return True
    async def execute(self, job: CreativeJob) -> ProviderResult: return ProviderResult(self.provider_id, "planned")
