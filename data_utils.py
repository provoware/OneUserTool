import os

def genres_profile_path():
    """Return absolute path to genres_profile.json inside the Projekt directory."""
    return os.path.join(os.path.dirname(__file__), "Projekt", "genres_profile.json")
