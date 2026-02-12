#!/bin/bash

echo "MediaInstaller Setup"

if ! command -v python3 &> /dev/null
then
    echo "Installing Python..."
    sudo apt install python3 -y || brew install python
fi

mkdir -p media

if ! command -v yt-dlp &> /dev/null
then
    sudo apt install yt-dlp ffmpeg -y || brew install yt-dlp ffmpeg
fi

echo "DONE"