import pytest

from services.character_sheet import (
    FOUR_K_HEIGHT,
    FOUR_K_WIDTH,
    CharacterSheetSpec,
    build_character_sheet_payload,
)


def valid_spec() -> CharacterSheetSpec:
    return CharacterSheetSpec(
        subject_name="Rabbi Yigal Cohen",
        reference_labels=("front", "profile", "speaking"),
        consent_granted=True,
    )


def test_payload_is_4k_and_9_panel():
    payload = build_character_sheet_payload(valid_spec())
    assert payload["width"] == FOUR_K_WIDTH == 3840
    assert payload["height"] == FOUR_K_HEIGHT == 2160
    assert payload["panels"] == 9


def test_prompt_uses_all_reference_slots():
    prompt = build_character_sheet_payload(valid_spec())["prompt"]
    assert "@Image1" in prompt and "@Image3" in prompt


def test_consent_is_required():
    with pytest.raises(ValueError, match="consent_granted"):
        CharacterSheetSpec(
            subject_name="Rabbi Yigal Cohen",
            reference_labels=("front",),
        )


def test_no_more_than_five_references():
    with pytest.raises(ValueError, match="1-5"):
        CharacterSheetSpec(
            subject_name="Rabbi Yigal Cohen",
            reference_labels=("1", "2", "3", "4", "5", "6"),
            consent_granted=True,
        )
