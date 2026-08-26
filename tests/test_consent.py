import pytest
from orchestrator.contracts import CreativeJob
from orchestrator.engine import Orchestrator
from orchestrator.exceptions import ConsentRequired
from orchestrator.registry import Registry
from orchestrator.router import CapabilityRouter
def test_identity_features_require_consent():
    class Adapter:
        async def execute(self, job): return None
    engine = Orchestrator(CapabilityRouter(Registry()), {"comfyui": Adapter()})
    with pytest.raises(ConsentRequired):
        import asyncio; asyncio.run(engine.run(CreativeJob("avatar", ("talking-avatar",))))
