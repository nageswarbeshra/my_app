import requests
import os
import sys
from utils.downloader import download_file

VERSION_URL = "https://github.com/nageswarbeshra/my_app/blob/main/version.json"

def check_update_and_download(current_version):
    try:
        data = requests.get(VERSION_URL).json()
        latest_version = data["version"]

        if latest_version != current_version:
            download_file(data["url"], "new_app.exe")
            replace_and_restart()
            return True
    except Exception as e:
        print("Update failed:", e)

    return False


def replace_and_restart():
    current_exe = sys.argv[0]

    with open("update.bat", "w") as f:
        f.write(f"""
@echo off
timeout /t 2 >nul
del "{current_exe}"
rename new_app.exe "{os.path.basename(current_exe)}"
start "" "{current_exe}"
""")

    os.system("update.bat")
    sys.exit()