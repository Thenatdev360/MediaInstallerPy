import subprocess
import os
import platform

MEDIA_DIR = "media"
COOKIES_FILE = "cookies.txt"

os.makedirs(MEDIA_DIR, exist_ok=True)

browsers = ["edge", "chrome", "firefox"]

print("""
Media Installer Tool
--------------------
1 - Download MUSIC (mp3 + thumbnail + subtitles)
2 - Download VIDEO (best quality)
""")

option = input("Choose option: ")
url = input("Paste video URL: ")

BASE = [
    "yt-dlp",
    "--js-runtimes", "node",
    "--remote-components", "ejs:github"
]

def is_android():
    return "android" in platform.platform().lower()

def build_cmd(extra):
    cmd = BASE + extra

    if option == "1":
        os.makedirs(f"{MEDIA_DIR}/music", exist_ok=True)
        cmd += [
            "-x",
            "--audio-format", "mp3",
            "--embed-thumbnail",
            "--embed-metadata",
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang", "en,es", 
            "-o", f"{MEDIA_DIR}/music/%(title)s.%(ext)s",
            url
        ]

    else:
        os.makedirs(f"{MEDIA_DIR}/video", exist_ok=True)
        cmd += [
            "-f", "bestvideo*+bestaudio/best",
            "--merge-output-format", "mp4",
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang", "en,es", 
            "-o", f"{MEDIA_DIR}/video/%(title)s.%(ext)s",
            url
        ]

    return subprocess.run(cmd).returncode == 0

def run_with_cookies():
    if os.path.exists(COOKIES_FILE):
        print("Trying cookies.txt...")
        return build_cmd(["--cookies", COOKIES_FILE])
    return False

def run_with_browser(browser):
    print(f"Trying {browser}...")
    return build_cmd(["--cookies-from-browser", browser])

success = False

success = run_with_cookies()

if not success and not is_android():
    for b in browsers:
        if run_with_browser(b):
            success = True
            break

if success:
    print("\nDownloaded successfully.")
else:
    print("\nAll methods failed.")
