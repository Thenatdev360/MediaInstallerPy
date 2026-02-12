import subprocess
import os

MEDIA_DIR = "media"
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

def run_with_browser(browser):
    print(f"Trying {browser} cookies...")
    cmd = BASE + ["--cookies-from-browser", browser]

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
            "-f", "bv*+ba/b",
            "--merge-output-format", "mp4",
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang", "en,es",
            "-o", f"{MEDIA_DIR}/video/%(title)s.%(ext)s",
            url
        ]

    return subprocess.run(cmd).returncode == 0

success = False

for b in browsers:
    if run_with_browser(b):
        success = True
        break

if not success:
    print("\n Sorry all browsers failed.")
else:
    print("\n Downloaded successfully.")