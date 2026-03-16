import sys
import yt_dlp
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "downloads"
FFMPEG_DIR = BASE_DIR / "bin"

load_dotenv(BASE_DIR / ".env")
COOKIE_FILE = os.getenv("COOKIE_FILE")

COOKIE_ERRORS = (
    "login",
    "sign in",
    "authentication",
    "cookie",
    "403",
    "private",
    "unavailable",
)


def download(url: str):
    OUTPUT_DIR.mkdir(exist_ok=True)

    ydl_opts = {
        "outtmpl": str(OUTPUT_DIR / "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "ffmpeg_location": str(FFMPEG_DIR),
    }

    if COOKIE_FILE and Path(COOKIE_FILE).exists():
        ydl_opts["cookiefile"] = COOKIE_FILE

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        msg = str(e).lower()
        if any(keyword in msg for keyword in COOKIE_ERRORS):
            print()
            print("이 콘텐츠는 로그인이 필요할 수 있습니다.")
            print("브라우저에서 쿠키를 내보낸 후 .env의 COOKIE_FILE 경로를 확인해주세요.")
        raise


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python download.py <URL>")
        sys.exit(1)

    download(sys.argv[1])
