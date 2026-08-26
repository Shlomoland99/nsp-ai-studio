from orchestrator.registry import Registry
def test_registry_loads_required_models():
    registry = Registry()
    assert {"flux", "sdxl", "wan", "whisper"} <= set(registry.models)
def test_registry_has_comfyui():
    assert Registry().providers["comfyui"].kind == "local"
