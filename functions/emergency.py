from pynput.keyboard import Listener, Key
import threading

pressed_keys = set()
exit_callback = None  # zostanie ustawione z main.py

def on_press(key):
    try:
        if key == Key.ctrl_l or key == Key.ctrl_r:
            pressed_keys.add('ctrl')
        elif key.char == 'q':
            if 'ctrl' in pressed_keys and exit_callback:
                print("Ctrl+Q wykryto – wywołuję exit_callback.")
                exit_callback()
    except AttributeError:
        pass

def on_release(key):
    if key == Key.ctrl_l or key == Key.ctrl_r:
        pressed_keys.discard('ctrl')

def start_hotkey_listener(callback):
    global exit_callback
    exit_callback = callback

    thread = threading.Thread(
        target=lambda: Listener(on_press=on_press, on_release=on_release).run(),
        daemon=True
    )
    thread.start()