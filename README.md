# OneUserTool

OneUserTool ist eine kleine Desktop-Anwendung auf Basis von PyQt5. Sie umfasst drei Module zur Verwaltung von Songtexten, zur Organisation von Genre-Profilen und zum Zufallsauswählen von Genres.

## Installation
1. Python 3.7 oder höher installieren.
2. Abhängigkeiten mittels `pip install -r requirements.txt` installieren.
3. Optional ein virtuelles Environment nutzen.

## Starten
```bash
python main.py
```
Oder das Skript `start_oneusertool.sh` verwenden, welches automatisch ein Log unter `logs/run.log` anlegt.

## Module
- **Songtexte** – Speichert Texte einzelner Songs als Dateien unter `Projekt/Songtexte`.
- **Genres** – Verwalten Sie Profillisten von Genres. Diese können exportiert, importiert und als Backup gesichert werden.
- **Zufallsgenerator** – Wählt eine zufällige Anzahl Genres aus einem Profil und kopiert sie in die Zwischenablage.

## Hinweise
Alle Daten werden im Unterordner `Projekt` gespeichert. Bei Fehlern finden Sie hilfreiche Informationen im Log-Verzeichnis.
