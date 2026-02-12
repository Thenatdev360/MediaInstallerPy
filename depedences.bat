@echo off
title MediaInstaller - Installing dependencies
echo ===============================
echo   MediaInstaller Installer
echo ===============================

REM ================= PYTHON =================

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Python...
    curl -L https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe -o python.exe
    start /wait python.exe /quiet InstallAllUsers=1 PrependPath=1
    del python.exe
) else (
    echo Python already installed
)

REM ================= NODE =================

where node >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Node.js...
    curl -L https://nodejs.org/dist/v22.11.0/node-v22.11.0-x64.msi -o node.msi
    start /wait node.msi /quiet
    del node.msi
) else (
    echo Node already installed
)

REM ================= YT-DLP =================

if not exist yt-dlp.exe (
    echo Downloading yt-dlp...
    curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe -o yt-dlp.exe
) else (
    echo yt-dlp already exists
)

REM ================= MEDIA FOLDER =================

if not exist media mkdir media

echo.
echo ===============================
echo DONE. Restart terminal.
pause
