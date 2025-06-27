import json
import os


def profiles_path() -> str:
    """Return the path to the genres profile JSON file."""
    return os.path.join(os.path.dirname(__file__), "Projekt", "genres_profile.json")


def load_profiles() -> dict:
    """Load genre profiles or create a default file if necessary."""
    path = profiles_path()
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"Favoriten": []}, f)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f) or {"Favoriten": []}


def save_profiles(data: dict) -> None:
    """Persist genre profile data to disk."""
    with open(profiles_path(), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
