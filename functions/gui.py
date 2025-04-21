from functions.config import *
from functions.start import *
from functions.stop import *
from functions.coords import *
import functions.emergency as emergency

def create_gui():
    def exit_program():
        print("Zamykanie programu…")
        root.quit()
        root.destroy()

    root = tk.Tk()
    root.title("Bot GUI")

    config = load_config()

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # --- Desktop Tab ---
    frame_desktop = ttk.Frame(notebook)
    notebook.add(frame_desktop, text='Desktop')

    ttk.Label(frame_desktop, text="X:").grid(row=0, column=0)
    entry_x_desktop = ttk.Entry(frame_desktop)
    entry_x_desktop.grid(row=0, column=1)
    entry_x_desktop.insert(0, config.get("desktop", {}).get("x", ""))

    ttk.Label(frame_desktop, text="Y:").grid(row=1, column=0)
    entry_y_desktop = ttk.Entry(frame_desktop)
    entry_y_desktop.grid(row=1, column=1)
    entry_y_desktop.insert(0, config.get("desktop", {}).get("y", ""))

    ttk.Label(frame_desktop, text="Liczba wyszukiwań:").grid(row=2, column=0)
    entry_count_desktop = ttk.Entry(frame_desktop)
    entry_count_desktop.grid(row=2, column=1)
    entry_count_desktop.insert(0, config.get("desktop", {}).get("count", ""))

    btn_coords_desktop = ttk.Button(frame_desktop, text="Pobierz koordynaty",
                                    command=lambda: get_coords(entry_x_desktop, entry_y_desktop))
    btn_coords_desktop.grid(row=3, column=0, columnspan=2, pady=2)

    btn_start_desktop = ttk.Button(frame_desktop, text="Start Desktop", command=lambda: start_desktop(entry_x_desktop, entry_y_desktop, entry_count_desktop, status_desktop))
    btn_start_desktop.grid(row=4, column=0, columnspan=2, pady=4)

    # --- Mobile Tab ---
    frame_mobile = ttk.Frame(notebook)
    notebook.add(frame_mobile, text='Mobile')

    ttk.Label(frame_mobile, text="X:").grid(row=0, column=0)
    entry_x_mobile = ttk.Entry(frame_mobile)
    entry_x_mobile.grid(row=0, column=1)
    entry_x_mobile.insert(0, config.get("mobile", {}).get("x", ""))

    ttk.Label(frame_mobile, text="Y:").grid(row=1, column=0)
    entry_y_mobile = ttk.Entry(frame_mobile)
    entry_y_mobile.grid(row=1, column=1)
    entry_y_mobile.insert(0, config.get("mobile", {}).get("y", ""))

    ttk.Label(frame_mobile, text="Liczba wyszukiwań:").grid(row=2, column=0)
    entry_count_mobile = ttk.Entry(frame_mobile)
    entry_count_mobile.grid(row=2, column=1)
    entry_count_mobile.insert(0, config.get("mobile", {}).get("count", ""))

    ttk.Label(frame_mobile, text="Port:").grid(row=3, column=0)
    entry_port = ttk.Entry(frame_mobile)
    entry_port.grid(row=3, column=1)
    entry_port.insert(0, config.get("mobile", {}).get("port", ""))

    btn_coords_mobile = ttk.Button(frame_mobile, text="Pobierz koordynaty",
                                   command=lambda: get_coords(entry_x_mobile, entry_y_mobile))
    btn_coords_mobile.grid(row=4, column=0, columnspan=2, pady=2)

    btn_start_mobile = ttk.Button(frame_mobile, text="Start Mobile", command=lambda: start_mobile(entry_x_mobile, entry_y_mobile, entry_count_mobile, entry_port, status_mobile))
    btn_start_mobile.grid(row=5, column=0, columnspan=2, pady=4)

    # --- ADB Tab ---
    frame_adb = ttk.Frame(notebook)
    notebook.add(frame_adb, text='ADB')

    btn_adb = ttk.Button(frame_adb, text="Wyłącz ADB", command=stop_adb)
    btn_adb.pack(pady=10)

    # --- Bottom Panel ---
    frame_bottom = ttk.Frame(root)
    frame_bottom.pack(pady=10)

    btn_save = ttk.Button(frame_bottom, text="📂 Zapisz konfigurację", command=lambda: save_config_data(entry_x_desktop.get(), entry_y_desktop.get(), entry_count_desktop.get(), entry_x_mobile.get(), entry_y_mobile.get(), entry_count_mobile.get(), entry_port.get()))
    btn_save.grid(row=0, column=0, padx=10)

    btn_stop = ttk.Button(frame_bottom, text="🚩 STOP", command=stop_all)
    btn_stop.grid(row=0, column=1, padx=10)

    status_desktop = tk.StringVar()
    status_desktop.set("Status: oczekiwanie...")
    ttk.Label(frame_desktop, textvariable=status_desktop).grid(row=5, column=0, columnspan=2)

    status_mobile = tk.StringVar()
    status_mobile.set("Status: oczekiwanie...")
    ttk.Label(frame_mobile, textvariable=status_mobile).grid(row=6, column=0, columnspan=2)

    emergency.start_hotkey_listener(exit_program)

    root.mainloop()



