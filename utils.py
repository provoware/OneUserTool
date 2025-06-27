import os
import json


def data_path():
    """Return path to the genre profile JSON and ensure directory exists."""
    path = os.path.join(os.path.dirname(__file__), "Projekt", "genres_profile.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def load_profiles():
    """Load genre profiles with graceful fallback for corrupted files."""
    path = data_path()
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"Favoriten": []}, f)
        return {"Favoriten": []}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        data = {"Favoriten": []}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)
    return data or {"Favoriten": []}


def save_profiles(data):
    """Persist genre profiles to disk."""
    with open(data_path(), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
