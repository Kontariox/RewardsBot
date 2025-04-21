import threading
import subprocess
from tkinter import messagebox
from functions.bot import *

def start_desktop(entry_x_desktop, entry_y_desktop, entry_count_desktop, status_desktop):
    global stop_flag
    stop_flag = False

    def run():
        try:
            x = int(entry_x_desktop.get())
            y = int(entry_y_desktop.get())
            count = int(entry_count_desktop.get())

            def update_status(i, total):
                status_desktop.set(f"Wyszukiwanie {i} z {total}")

            bot(count, x, y, stop_check=lambda: stop_flag, status_callback=update_status)
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    threading.Thread(target=run).start()


def start_mobile(entry_x_mobile, entry_y_mobile, entry_count_mobile, entry_port, status_mobile):
    global stop_flag
    stop_flag = False

    def run():
        try:
            x = int(entry_x_mobile.get())
            y = int(entry_y_mobile.get())
            count = int(entry_count_mobile.get())
            port = entry_port.get()
            ip = f"192.168.0.51:{port}"

            # === ADB Connect ===
            adb_connect = subprocess.run(
                ["adb", "connect", ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            output = adb_connect.stdout.lower() + adb_connect.stderr.lower()

            if "failed" in output or "unable" in output or "no such" in output or "refused" in output:
                messagebox.showerror("ADB Błąd", f"Nie udało się połączyć z {ip}:\n\n{output.strip()}")
                return

            # === SCRCPY ===
            subprocess.Popen([
                "x-terminal-emulator", "-e",
                f"scrcpy -s {ip} -b 8M --max-fps=60 --capture-orientation=0"
            ])

            messagebox.showinfo("Info", "Masz 8 sekund na uruchomienie przeglądarki")
            time.sleep(8)

            def update_status(i, total):
                status_mobile.set(f"Wyszukiwanie {i} z {total}")

            bot_mobile(count, x, y, stop_check=lambda: stop_flag, status_callback=update_status)

            subprocess.run(["adb", "kill-server"])

        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    threading.Thread(target=run).start()