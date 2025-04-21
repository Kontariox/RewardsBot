import pyautogui
import time
import threading
from tkinter import ttk, messagebox
import tkinter as tk

def get_coords(x_entry, y_entry):
    def capture():
        time.sleep(5)
        x, y = pyautogui.position()
        x_entry.delete(0, tk.END)
        x_entry.insert(0, str(x))
        y_entry.delete(0, tk.END)
        y_entry.insert(0, str(y))
        messagebox.showinfo("Gotowe", f"Zapisano X={x}, Y={y}")
    threading.Thread(target=capture).start()
    messagebox.showinfo("Uwaga", "Masz 5 sekund na najechanie myszką w miejsce kliknięcia")