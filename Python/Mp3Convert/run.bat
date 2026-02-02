@echo off
chcp 65001 > nul
cd /d "%~dp0"
title YouTube MP3 Downloader

echo ========================================================
echo       YouTube to MP3 Downloader
echo ========================================================
echo.

if not exist ".venv\Scripts\python.exe" goto ERR_VENV
if not exist "src\mp3_script.py" goto ERR_SCRIPT

:INPUT_URL
echo.
set "URL="
set /p "URL=YouTube URL (q=quit): "
if /i "%URL%"=="q" goto END
if "%URL%"=="" goto INPUT_URL

echo.
echo --------------------------------------------------------
".venv\Scripts\python.exe" src\mp3_script.py "%URL%"
echo --------------------------------------------------------
goto INPUT_URL

:ERR_VENV
echo [ERROR] .venv not found
pause
goto END

:ERR_SCRIPT
echo [ERROR] mp3_script.py not found
pause
goto END

:END
