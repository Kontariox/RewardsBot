import pyautogui
import time
import random
from functions.file_opener import load_phrases

frazy = load_phrases()

def bot(wyszukiwania, x, y, stop_check=lambda: False, status_callback=lambda i, total: None):
    print("Masz 5 sekund żeby ustawić przeglądarkę z otwartą wyszukiwarką...")
    time.sleep(5)

    for i in range(wyszukiwania):
        if stop_check():
            print("Zatrzymano bota desktop.")
            break
        status_callback(i + 1, wyszukiwania)
        pyautogui.click(x, y)
        time.sleep(1)

        pyautogui.click(x, y)
        time.sleep(0.2)

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(0.2)

        fraza = random.choice(frazy)
        pyautogui.write(fraza, interval=0.05)
        pyautogui.press('enter')

        print(f"Wyszukiwanie {i + 1}/30: {fraza}")

        time.sleep(2.5)

        ile_scrolli = random.randint(2, 5)
        for _ in range(ile_scrolli):
            pyautogui.scroll(-3)
            time.sleep(random.uniform(0.5, 1.2))
        pyautogui.scroll(15)
        time.sleep(random.uniform(2.5, 5))

def bot_mobile(wyszukiwania, x, y, stop_check=lambda: False, status_callback=lambda i, total: None):
    print("Masz 5 sekund żeby ustawić przeglądarkę z otwartą wyszukiwarką...")
    time.sleep(5)

    for i in range(wyszukiwania):
        if stop_check():
            print("Zatrzymano bota mobile.")
            break
        status_callback(i + 1, wyszukiwania)
        pyautogui.click(x, y)
        time.sleep(1)

        pyautogui.click(x, y)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.2)
        pyautogui.press('backspace')
        time.sleep(0.2)

        fraza = random.choice(frazy)
        pyautogui.write(fraza, interval=0.05)
        pyautogui.press('enter')

        print(f"Wyszukiwanie {i + 1}/30: {fraza}")

        time.sleep(2.5)
        y2 =  y+200
        pyautogui.move(0, y2)

        ile_scrolli = random.randint(2, 5)
        for _ in range(ile_scrolli):
            pyautogui.scroll(-3)  # -500 = w dół, zmień na -1000 jeśli chcesz więcej
            time.sleep(random.uniform(0.5, 1.2))  # losowa pauza między scrollami
        pyautogui.scroll(15)

        time.sleep(random.uniform(2.5, 5))