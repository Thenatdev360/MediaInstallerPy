@echo off
title MediaInstaller Dependencies
cd /d %~dp0

echo ==========================
echo MediaInstaller Setup
echo ==========================

REM ---------------------------
REM PYTHON
REM ---------------------------

python --version >nul 2>&1

if errorlevel 1 (
    echo Python not found. Installing...

    curl -L -o python.exe https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe

    python.exe /quiet InstallAllUsers=1 PrependPath=1

    del python.exe

    echo Python installed.
) else (
    echo Python already installed.
)

REM ---------------------------
REM MEDIA FOLDER
REM ---------------------------

if not exist media mkdir media

REM ---------------------------
REM yt-dlp
REM ---------------------------

if not exist yt-dlp.exe (
    echo Downloading yt-dlp...
    curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
)

REM ---------------------------
REM ffmpeg
REM ---------------------------

if not exist ffmpeg (
    echo Downloading ffmpeg...

    mkdir ffmpeg
    cd ffmpeg

    curl -L -o ffmpeg.zip https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
    tar -xf ffmpeg.zip

    cd ..
)

REM ---------------------------
REM PATH
REM ---------------------------

setx PATH "%cd%;%cd%\ffmpeg\ffmpeg-*-essentials_build\bin;%PATH%"

echo.
echo ==========================
echo DONE. Restart terminal.
echo ==========================
pause