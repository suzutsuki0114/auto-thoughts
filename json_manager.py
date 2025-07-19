import json
from pathlib import Path

DATA_FILE = Path("data/informations.json")

class JsonManager:
    def __init__(self):
        self.load()

    def load(self):
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.informations = json.load(f)
        else:
            self.informations = {}

    def save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.informations, f, ensure_ascii=False, indent=4)

    def write(self, browser_path, email, class_id, number, name):
        self.informations = {
            "browser_path": browser_path,
            "email": email,
            "class_id": class_id,
            "number": number,
            "name": name,
        }
        self.save()

    def get_all(self):
        return self.informations

