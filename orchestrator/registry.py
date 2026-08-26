from dataclasses import dataclass
from pathlib import Path
import yaml

@dataclass(frozen=True)
class ProviderSpec:
    id: str
    kind: str
    adapter: str
    capabilities: tuple[str, ...]
    env: tuple[str, ...]

@dataclass(frozen=True)
class ModelSpec:
    id: str
    provider: str
    capability: str
    aliases: tuple[str, ...]

class Registry:
    def __init__(self, config_dir: str | Path = "config") -> None:
        root = Path(config_dir)
        providers = yaml.safe_load((root / "providers.yaml").read_text())["providers"]
        models = yaml.safe_load((root / "models.yaml").read_text())["models"]
        self.providers = {p["id"]: ProviderSpec(p["id"], p["kind"], p["adapter"], tuple(p["capabilities"]), tuple(p.get("env", []))) for p in providers}
        self.models = {m["id"]: ModelSpec(m["id"], m["provider"], m["capability"], tuple(m.get("aliases", []))) for m in models}
