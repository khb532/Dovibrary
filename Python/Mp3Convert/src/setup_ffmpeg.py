import os
import zipfile
import urllib.request
import shutil

def setup_ffmpeg():
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    zip_path = "ffmpeg.zip"
    extract_folder = "ffmpeg_temp"

    print(f"FFmpeg 다운로드 중... ({url})")
    # User-Agent 설정 (일부 서버 차단 방지)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    
    try:
        urllib.request.urlretrieve(url, zip_path)
        print("다운로드 완료. 압축 해제 중...")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        
        # 압축 풀린 폴더 찾기 (이름이 버전에 따라 다를 수 있음)
        extracted_dirs = [d for d in os.listdir(extract_folder) if os.path.isdir(os.path.join(extract_folder, d))]
        if not extracted_dirs:
            print("압축 해제 폴더를 찾을 수 없습니다.")
            return

        base_dir = os.path.join(extract_folder, extracted_dirs[0])
        bin_dir = os.path.join(base_dir, 'bin')

        # exe 파일 이동
        for filename in ['ffmpeg.exe', 'ffprobe.exe']:
            src = os.path.join(bin_dir, filename)
            dst = os.path.join(os.getcwd(), filename)
            if os.path.exists(src):
                shutil.move(src, dst)
                print(f"{filename} 설치 완료")
            else:
                print(f"{filename}을 찾을 수 없습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        # 정리
        print("임시 파일 정리 중...")
        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(extract_folder):
            shutil.rmtree(extract_folder)
        print("설정 완료!")

if __name__ == "__main__":
    setup_ffmpeg()
