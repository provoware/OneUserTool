# OneUserTool

OneUserTool ist eine kleine PyQt-Anwendung zum Verwalten von Songtexten und Genres. Das Projekt besteht aus mehreren Modulen, die über eine Sidebar ausgewählt werden können.

## Installation

1. Stelle sicher, dass Python 3.7 oder höher installiert ist.
2. Erstelle eine virtuelle Umgebung und installiere die Abhängigkeiten:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Starte die Anwendung mit:
   ```bash
   python main.py
   ```

## Module

- **Songtext-Modul** – speichert und verwaltet Songtexte.
- **Genre-Archiv** – verwaltet unterschiedliche Genre-Profile.
- **Zufallsgenerator** – wählt zufällig Genres aus einem Profil aus.

## Hinweise für Anwender

- Mit `start_oneusertool.sh` kann die Anwendung in einer Endlosschleife gestartet werden, um Abstürze abzufangen.
- Die Daten werden im Ordner `Projekt/` im Repository gespeichert. Ein Backup kann direkt aus dem Genre-Modul heraus erstellt werden.

