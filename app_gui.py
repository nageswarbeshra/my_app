import tkinter as tk
from tkinter import messagebox
import requests
import os
import sys

CURRENT_VERSION = "1.0.0"

# 🔗 Change this to your GitHub raw version.json
VERSION_URL = "https://github.com/nageswarbeshra/my_app/blob/main/version.json"


def check_update():
    try:
        res = requests.get(VERSION_URL)
        data = res.json()

        latest_version = data["version"]

        if latest_version != CURRENT_VERSION:
            answer = messagebox.askyesno(
                "Update Available",
                f"New version {latest_version} available.\nDo you want to update?"
            )

            if answer:
                download_update(data["url"])
        else:
            messagebox.showinfo("No Update", "You are using latest version ✅")

    except Exception as e:
        messagebox.showerror("Error", f"Update check failed:\n{e}")


def download_update(url):
    try:
        messagebox.showinfo("Downloading", "Downloading update...")

        r = requests.get(url)
        with open("new_app.exe", "wb") as f:
            f.write(r.content)

        replace_and_restart()

    except Exception as e:
        messagebox.showerror("Error", f"Download failed:\n{e}")


def replace_and_restart():
    current_exe = sys.argv[0]

    # Create updater batch file
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


# 🔹 GUI
app = tk.Tk()
app.title("My Auto Update App")
app.geometry("300x200")

label = tk.Label(app, text=f"Version: {CURRENT_VERSION}", font=("Arial", 12))
label.pack(pady=20)

btn_update = tk.Button(app, text="Check for Update", command=check_update)
btn_update.pack(pady=10)

btn_exit = tk.Button(app, text="Exit", command=app.quit)
btn_exit.pack(pady=10)

app.mainloop()