from .contracts import CreativeJob
from .exceptions import RoutingError
from .registry import Registry

class CapabilityRouter:
    def __init__(self, registry: Registry) -> None:
        self.registry = registry
    def route(self, job: CreativeJob) -> str:
        for spec in self.registry.providers.values():
            if job.local_only and spec.kind != "local":
                continue
            if all(cap in spec.capabilities for cap in job.capabilities):
                return spec.id
        raise RoutingError(f"No provider satisfies capabilities: {job.capabilities}")
