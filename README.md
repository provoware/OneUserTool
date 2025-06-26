# OneUserTool

A simple PyQt5 desktop application combining multiple small modules.

## Requirements

- Python 3.7 or newer
- Dependencies listed in `requirements.txt`

Install the dependencies in a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application

You can start the tool directly using Python:

```bash
python3 main.py
```

Alternatively run the helper script which restarts the app after crashes:

```bash
bash start_oneusertool.sh
```

## Data Directory

When running the tool it creates a `Projekt/` directory in the repository with
these subfolders/files:

```
Projekt/
├── Songtexte/          # gespeicherte Liedtexte
├── Notizen/            # eigene Notizen
└── genres_profile.json # Genre-Profile für mehrere Module
```

## Module Overview

- **Songtexte** – Editor zum Anlegen und Verwalten von Songtexten.
- **Genres** – Archiv für Genres inkl. Export-/Import-Optionen.
- **Zufallsgenerator** – wählt zufällige Genres aus einem Profil aus.
- **Notizen** – einfacher Texteditor zum Speichern von Notizen.

Tipps für Einsteiger: probieren Sie zunächst das Genre-Archiv aus und
experimentieren Sie mit eigenen Profilen. Nutzen Sie anschließend den
Zufallsgenerator, um Inspiration für neue Songtexte oder Notizen zu sammeln.
