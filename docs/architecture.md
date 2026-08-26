# Architecture

The system is organized into five layers:

1. Orchestrator — stable request, capability, provider, and pipeline contracts; routing and execution policy.
2. Integrations — adapters for local/cloud tools. Each adapter owns transport and provider-specific payload mapping.
3. Services — cross-cutting media and safety services such as FFmpeg and consent validation.
4. Workflows — named pipeline definitions and ComfyUI workflow assets.
5. Configuration — declarative provider, model, and pipeline registries.

A request becomes a CreativeJob, is checked for required capabilities and consent, routed using registry metadata, and dispatched to an adapter. The core sees only ProviderAdapter, CapabilityRequirement, and ProviderResult.

No adapter may silently change provider, privacy, cost, or execution mode. Health checks are explicit and failures are raised as typed exceptions.
