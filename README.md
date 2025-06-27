# OneUserTool

OneUserTool ist eine kleine PyQt-Anwendung zum Verwalten von Songtexten und Genres. Das Projekt besteht aus mehreren Modulen, die über eine Sidebar ausgewählt werden können. Ab Version 0.2.0 liegen gemeinsame Hilfsfunktionen im Modul `utils.py`.

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
- Das Farbschema lässt sich über die Variable `theme` in `main.py` anpassen ("dark", "light" oder "highcontrast").

## Weiterführende Tipps

- Wer zum ersten Mal mit Python arbeitet, findet auf [python.org](https://www.python.org/doc/) eine leicht verständliche Dokumentation.
- Durch den Aufruf `python main.py --help` lassen sich alle Startoptionen anzeigen.
- Versionskontrolle mit Git hilft, eigene Änderungen nachzuverfolgen.
- Häufige Backups verhindern Datenverlust, insbesondere vor Updates.

