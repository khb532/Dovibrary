# Video Downloader

URL을 입력하면 영상을 자동 다운로드. yt-dlp 기반.

## 사용법

```
init.bat   # 최초 1회 - 환경 설치 및 쿠키 경로 설정
run.bat    # 실행
```

다운로드된 파일은 `downloads/`에 저장.

## 쿠키

로그인이 필요한 사이트는 브라우저에서 쿠키를 내보낸 후 `.env`에 경로 지정.

```
COOKIE_FILE=your/path/to/cookies.txt
```
