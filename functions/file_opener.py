from pathlib import Path
import requests

def load_phrases():
    github_url = "https://raw.githubusercontent.com/Kontariox/RewardsBot/refs/heads/main/phrases.txt"

    PHRASES_DIR = Path.home() / ".config" / "MicrosoftRewardsBot"
    PHRASES_DIR.mkdir(parents=True, exist_ok=True)
    PHRASES_FILE = PHRASES_DIR / "phrases.txt"

    if not PHRASES_FILE.exists():
        print("Plik nie istnieje, pobieram z GitHub...")

        response = requests.get(github_url)

        # Sprawdzamy, czy pobranie pliku zakończyło się sukcesem
        if response.status_code == 200:
            with open(PHRASES_FILE, "w", encoding="utf-8") as plik:
                plik.write(response.text)
            print("Plik został pobrany i zapisany.")
        else:
            print("Błąd podczas pobierania pliku z GitHub. Status:", response.status_code)
            return []

    with open(PHRASES_FILE, "r", encoding="utf-8") as plik:
        frazy = [linia.strip() for linia in plik if linia.strip() != ""]
    return frazy