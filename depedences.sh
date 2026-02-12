#!/bin/bash

echo "MediaInstaller Dependencies"

# PYTHON
if ! command -v python3 &> /dev/null; then
    sudo apt install python3 -y || brew install python
fi

# NODE
if ! command -v node &> /dev/null; then
    sudo apt install nodejs npm -y || brew install node
fi

# yt-dlp
if [ ! -f yt-dlp ]; then
    curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o yt-dlp
    chmod +x yt-dlp
fi

mkdir -p media

echo "DONE"
