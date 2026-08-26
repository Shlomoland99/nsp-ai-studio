import asyncio
from integrations.comfyui.bridge import ComfyUIAdapter
async def main() -> None:
    adapter = ComfyUIAdapter()
    print({"comfyui": await adapter.health()})
if __name__ == "__main__": asyncio.run(main())
