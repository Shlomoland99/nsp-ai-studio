from orchestrator.contracts import ProviderResult, CreativeJob
class OBSAdapter:
    provider_id = "obs"
    async def health(self) -> bool: return True
    async def execute(self, job: CreativeJob) -> ProviderResult: return ProviderResult(self.provider_id, "planned")
