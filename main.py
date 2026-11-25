import os
from pathlib import Path

GLYPH = "🕷️"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(GLYPH, encoding="utf-8")


if __name__ == "__main__":
    main()
