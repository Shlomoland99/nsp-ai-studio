from orchestrator.exceptions import ConsentRequired
def require_consent(granted: bool, feature: str) -> None:
    if not granted: raise ConsentRequired(f"Consent is required for {feature}.")
