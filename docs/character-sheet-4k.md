# 4K character-sheet pipeline

The character-sheet builder creates a provider-neutral request for a 3x3,
identity-consistent reference sheet at **3840x2160 PNG**.

## API

Call POST /v1/character-sheets with:

~~~json
{
  "subject_name": "Rabbi Yigal Cohen",
  "reference_labels": ["front", "speaking", "profile"],
  "consent_granted": true
}
~~~

The endpoint validates the request, builds a ComfyUI-compatible job payload,
and routes it to the local ComfyUI provider. The actual render requires a
running ComfyUI instance and installed identity-preservation/upscaling models
(for example IP-Adapter or InstantID plus a tiled 4K upscaler). No credentials
are stored in the repository.

consent_granted is intentionally required for identity-based generation,
following the repository's face/voice authorization rule.
