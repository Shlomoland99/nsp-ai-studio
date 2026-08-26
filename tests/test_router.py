import pytest
from orchestrator.contracts import CreativeJob
from orchestrator.exceptions import RoutingError
from orchestrator.registry import Registry
from orchestrator.router import CapabilityRouter
def test_local_routing():
    provider = CapabilityRouter(Registry()).route(CreativeJob("x", ("text-to-image",), local_only=True))
    assert provider == "comfyui"
def test_unknown_capability_fails():
    with pytest.raises(RoutingError):
        CapabilityRouter(Registry()).route(CreativeJob("x", ("does-not-exist",)))
