import json
from tkinter import messagebox
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "MicrosoftRewardsBot"
CONFIG_DIR.mkdir(parents=True, exist_ok=True)

CONFIG_FILE = CONFIG_DIR / "config.json"


def save_config_data(entry_x_desktop, entry_y_desktop, entry_count_desktop ,entry_x_mobile, entry_y_mobile, entry_count_mobile, entry_port):
    config_data = {
        "desktop": {
            "x": entry_x_desktop,
            "y": entry_y_desktop,
            "count": entry_count_desktop
        },
        "mobile": {
            "x": entry_x_mobile,
            "y": entry_y_mobile,
            "count": entry_count_mobile,
            "port": entry_port
        }
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f)
    messagebox.showinfo("Zapisano", "Konfiguracja została zapisana.")

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return {}