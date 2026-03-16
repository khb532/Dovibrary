@echo off
chcp 65001 > nul
cd /d "%~dp0"
title Video Downloader

echo ========================================================
echo              Video Downloader
echo ========================================================
echo.

if not exist ".venv\Scripts\python.exe" goto ERR_VENV
if not exist "src\download.py" goto ERR_SCRIPT

:INPUT_URL
echo.
set "URL="
set /p "URL=Video URL (q=quit): "
if /i "%URL%"=="q" goto END
if "%URL%"=="" goto INPUT_URL

echo.
echo --------------------------------------------------------
".venv\Scripts\python.exe" src\download.py "%URL%"
echo --------------------------------------------------------
goto INPUT_URL

:ERR_VENV
echo [ERROR] .venv not found
pause
goto END

:ERR_SCRIPT
echo [ERROR] download.py not found
pause
goto END

:END
