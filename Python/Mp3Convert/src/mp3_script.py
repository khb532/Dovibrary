import sys
import yt_dlp
import os

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '?%').strip()
        speed = d.get('_speed_str', '?').strip()
        print(f"\r다운로드 중... {percent} ({speed})    ", end='', flush=True)
    elif d['status'] == 'finished':
        print("\n다운로드 완료. MP3 변환 중... (잠시 대기)")

def download_mp3(url):
    # 프로젝트 루트 디렉토리 기준 (src의 상위 폴더)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mp3_dir = os.path.join(base_dir, 'mp3')
    temp_dir = os.path.join(base_dir, 'temp')

    # 폴더가 혹시 없으면 생성 (안전장치)
    os.makedirs(mp3_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        # 경로 설정: home은 최종 저장소, temp는 임시 작업소
        'paths': {
            'home': mp3_dir,
            'temp': temp_dir
        },
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '256',
        }],
        # 파일명 템플릿 (경로는 paths가 처리하므로 파일명만 지정)
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        # FFmpeg가 같은 폴더에 있을 경우를 위해 경로 지정 (선택사항이나 안전하게 추가)
        'ffmpeg_location': os.path.join(base_dir, 'bin'),
        'progress_hooks': [progress_hook]
    }

    print(f"저장 위치: {mp3_dir}")
    print(f"다운로드 시작: {url}")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("변환 완료!")
    except Exception as e:
        print(f"\n오류 발생: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python mp3_script.py \"유튜브_URL\"")
    else:
        url = sys.argv[1]
        download_mp3(url)