import tkinter as tk
from tkinter import messagebox
from updater import check_update_and_download
from config import CURRENT_VERSION

def run_update():
    result = check_update_and_download(CURRENT_VERSION)
    if result:
        messagebox.showinfo("Update", "App updated! Restarting...")
    else:
        messagebox.showinfo("Update", "Already latest version ✅")

app = tk.Tk()
app.title("Auto Update App")
app.geometry("300x200")

label = tk.Label(app, text=f"Version: {CURRENT_VERSION}", font=("Arial", 12))
label.pack(pady=20)

btn_update = tk.Button(app, text="Check for Update", command=run_update)
btn_update.pack(pady=10)

btn_exit = tk.Button(app, text="Exit", command=app.quit)
btn_exit.pack(pady=10)

app.mainloop()