import sys
import argparse
from pathlib import Path
from PIL import Image

ICO_SIZE = (256, 256)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMP_DIR = PROJECT_ROOT / "temp"
ICO_DIR = PROJECT_ROOT / "ico"


def ensure_dirs() -> None:
    TEMP_DIR.mkdir(exist_ok=True)
    ICO_DIR.mkdir(exist_ok=True)


def convert(input_path: Path) -> Path:
    ensure_dirs()

    temp_path = TEMP_DIR / (input_path.stem + "_resized.png")
    output_path = ICO_DIR / (input_path.stem + ".ico")

    with Image.open(input_path) as img:
        img = img.convert("RGBA")
        resized = img.resize(ICO_SIZE, Image.LANCZOS)
        resized.save(temp_path, format="PNG")

    with Image.open(temp_path) as img:
        img.save(output_path, format="ICO", sizes=[ICO_SIZE])

    temp_path.unlink(missing_ok=True)

    print(f"완료: {output_path}")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="PNG → ICO 변환기 (256x256 고정)")
    parser.add_argument("input", nargs="?", help="변환할 PNG 파일 경로")
    args = parser.parse_args()

    if not args.input:
        parser.print_help()
        sys.exit(0)

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"오류: 파일을 찾을 수 없습니다 — {input_path}")
        sys.exit(1)
    if input_path.suffix.lower() != ".png":
        print(f"오류: PNG 파일이 아닙니다 — {input_path}")
        sys.exit(1)

    convert(input_path)


if __name__ == "__main__":
    main()
