from orchestrator.contracts import CreativeJob, ProviderResult
class FFmpegAdapter:
    provider_id = "ffmpeg"
    async def health(self) -> bool: return True
    async def execute(self, job: CreativeJob) -> ProviderResult:
        return ProviderResult(self.provider_id, "planned", {"note": "Use services.media for validated FFmpeg commands."})
