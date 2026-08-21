@echo off
setlocal enabledelayedexpansion
title Katt-Converter
cd /d "%~dp0"

echo ====================================================
echo               Katt-Converter Setup
echo ====================================================

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python was not found in PATH.
    echo Please install Python 3.8+ and ensure "Add Python to PATH" is checked.
    pause
    exit /b 1
)

if not exist ".venv" (
    echo [*] Creating virtual environment...
    python -m venv .venv
)

call .venv\Scripts\activate.bat

echo [*] Checking Python dependencies...
python -m pip install --upgrade pip >nul 2>nul
pip install -r requirements.txt >nul 2>nul

where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    if not exist "ffmpeg.exe" (
        echo [!] FFmpeg not found. Attempting automatic download...
        powershell -Command "$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip' -OutFile 'ffmpeg.zip'"
        if exist "ffmpeg.zip" (
            echo [*] Extracting FFmpeg...
            powershell -Command "Expand-Archive -Path 'ffmpeg.zip' -DestinationPath 'temp_ffmpeg' -Force"
            for /r "temp_ffmpeg" %%i in (ffmpeg.exe ffprobe.exe) do move "%%i" "%~dp0" >nul 2>nul
            rmdir /s /q "temp_ffmpeg" >nul 2>nul
            del /f /q "ffmpeg.zip" >nul 2>nul
        )
    )
)

where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    if not exist "ffmpeg.exe" (
        echo [ERROR] Could not automatically download FFmpeg.
        echo Please place ffmpeg.exe and ffprobe.exe in this folder manually.
        pause
        exit /b 1
    )
)

echo [*] Launching Katt-Converter...
cls
python main.py
pause