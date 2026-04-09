@echo off
timeout /t 2 >nul
del "app_gui.exe"
rename new_app.exe "app_gui.exe"
start "" "app_gui.exe"