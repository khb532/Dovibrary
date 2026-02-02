# Dovibrary

개인 유틸리티 및 도구 모음 저장소.

## 프로젝트

### Python/Server
로컬 서버 프로젝트.

### Python/Mp3Convert
YouTube 영상을 MP3로 변환하는 도구.
- `yt-dlp` 기반
- FFmpeg 자동 설치 스크립트 포함 (`setup_ffmpeg.py`)

## 설치

각 프로젝트 폴더에서 venv 생성 후 의존성 설치:

```bash
cd Python/<프로젝트명>
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
