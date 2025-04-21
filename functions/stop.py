from tkinter import messagebox
import subprocess

def stop_all():
    global stop_flag
    stop_flag = True
    messagebox.showinfo("STOP", "Bot został zatrzymany (jeśli wspiera flagę stopu).")

def stop_adb():
    subprocess.Popen(["x-terminal-emulator", "-e", "adb kill-server"])
    messagebox.showinfo("ADB", "ADB zostało wyłączone.")
