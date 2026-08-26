from orchestrator.contracts import ProviderResult, CreativeJob
class BlenderAdapter:
    provider_id = "blender"
    async def health(self) -> bool: return True
    async def execute(self, job: CreativeJob) -> ProviderResult: return ProviderResult(self.provider_id, "planned")
