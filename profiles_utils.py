"""Utility functions for genre profile management."""
import os, json

def data_path():
    """Return path to the genres profile JSON file."""
    return os.path.join(os.path.dirname(__file__), "Projekt", "genres_profile.json")


def load_profiles():
    """Load profile data from disk, creating the file if necessary."""
    path = data_path()
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"Favoriten": []}, f)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f) or {"Favoriten": []}
