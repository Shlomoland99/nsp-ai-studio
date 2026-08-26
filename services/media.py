from pathlib import Path
def ensure_output_dir(path: str | Path = "outputs") -> Path:
    target = Path(path); target.mkdir(parents=True, exist_ok=True); return target
