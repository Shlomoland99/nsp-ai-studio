"""Character-sheet request builder with identity and consent safeguards."""
from dataclasses import dataclass

MAX_REFERENCES = 5
FOUR_K_WIDTH = 3840
FOUR_K_HEIGHT = 2160


@dataclass(frozen=True)
class CharacterSheetSpec:
    subject_name: str
    reference_labels: tuple[str, ...]
    width: int = FOUR_K_WIDTH
    height: int = FOUR_K_HEIGHT
    panels: int = 9
    consent_granted: bool = False

    def __post_init__(self) -> None:
        if not self.subject_name.strip():
            raise ValueError("subject_name must not be empty")
        if not self.reference_labels or len(self.reference_labels) > MAX_REFERENCES:
            raise ValueError(f"reference_labels must contain 1-{MAX_REFERENCES} items")
        if self.width != FOUR_K_WIDTH or self.height != FOUR_K_HEIGHT:
            raise ValueError("character-sheet output is fixed at 3840x2160 (4K landscape)")
        if self.panels != 9:
            raise ValueError("character-sheet layout must contain exactly 9 panels")
        if not self.consent_granted:
            raise ValueError("consent_granted must be true for identity-based generation")


def build_character_sheet_prompt(spec: CharacterSheetSpec) -> str:
    """Return a provider-neutral prompt for an identity-consistent 3x3 sheet."""
    refs = ", ".join(f"@Image{i}" for i in range(1, len(spec.reference_labels) + 1))
    return f"""Create a professional photorealistic character reference sheet for {spec.subject_name}.
Use {refs} as identity reference images. Preserve the same face, skin tone, body proportions,
facial hair, hairstyle, wardrobe, and distinctive features in every panel.

Layout: a clean 3x3 grid with nine panels on a neutral studio background:
1. front neutral portrait; 2. warm smile; 3. speaking with gentle emphasis;
4. left profile; 5. right three-quarter view; 6. seated with a relevant prop;
7. full-body standing; 8. open welcoming gesture; 9. palms-together gesture.

Use soft cinematic lighting, realistic skin texture, natural hair detail, accurate hands,
consistent scale, and sharp production-reference quality. No text, captions, logos,
watermarks, extra people, distorted hands, duplicate faces, or identity drift.
Output exactly {spec.width}x{spec.height} pixels."""


def build_character_sheet_payload(spec: CharacterSheetSpec) -> dict[str, object]:
    """Build the payload consumed by the provider-neutral job router."""
    return {
        "asset_type": "character-sheet",
        "format": "png",
        "width": spec.width,
        "height": spec.height,
        "panels": spec.panels,
        "reference_labels": list(spec.reference_labels),
        "prompt": build_character_sheet_prompt(spec),
    }
