@echo off
chcp 65001 > nul
cd /d "%~dp0"
title Video Downloader - 초기화

echo ========================================================
echo         Video Downloader - 초기화
echo ========================================================
echo.

:: 가상환경 생성
if exist ".venv\Scripts\python.exe" (
    echo [OK] 가상환경이 이미 존재합니다.
) else (
    echo [1/4] 가상환경 생성 중...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] 가상환경 생성 실패. Python이 설치되어 있는지 확인하세요.
        pause
        exit /b 1
    )
    echo [OK] 가상환경 생성 완료.
)

:: 의존성 설치
echo.
echo [2/4] 패키지 설치 중...
".venv\Scripts\pip.exe" install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] 패키지 설치 실패.
    pause
    exit /b 1
)
echo [OK] 패키지 설치 완료.

:: ffmpeg 설치
echo.
if exist "bin\ffmpeg.exe" (
    echo [3/4] ffmpeg가 이미 존재합니다.
) else (
    echo [3/4] ffmpeg 다운로드 중...
    ".venv\Scripts\python.exe" src\setup_ffmpeg.py
    if errorlevel 1 (
        echo [ERROR] ffmpeg 설치 실패.
        pause
        exit /b 1
    )
)

:: .env 생성
echo.
if exist ".env" (
    echo [4/4] .env 파일이 이미 존재합니다.
) else (
    echo [4/4] 쿠키 파일 설정
    echo   로그인이 필요한 사이트의 쿠키 파일 경로를 입력하세요.
    echo   (없으면 엔터로 건너뜀)
    echo.
    set "COOKIE_PATH="
    set /p "COOKIE_PATH=쿠키 파일 경로: "

    if "%COOKIE_PATH%"=="" (
        echo COOKIE_FILE=> .env
        echo [OK] .env 생성 완료. (쿠키 없음)
    ) else (
        echo COOKIE_FILE=%COOKIE_PATH%> .env
        echo [OK] .env 생성 완료.
    )
)

echo.
echo ========================================================
echo           초기화 완료! run.bat으로 실행하세요.
echo ========================================================
pause
