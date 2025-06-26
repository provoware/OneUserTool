# OneUserTool

OneUserTool bündelt mehrere kleine Desktop-Module in einer Anwendung.

## Module
- **Songtext-Editor** (`songtext_modul.py`): Verfasst und verwaltet Songtexte im Ordner `Projekt/Songtexte`.
- **Genre-Archiv** (`genres_modul.py`): Hält beliebig viele Genre-Profile in der Datei `Projekt/genres_profile.json`.
- **Zufallsgenerator** (`zufallsgenerator_modul.py`): Wählt zufällige Genres aus einem Profil.
- **Design Manager** (`design_manager.py`): Legt das Aussehen der Oberfläche fest.

## Installation
1. Python 3.7 oder neuer installieren.
2. Abhängigkeiten via `requirements.txt` einrichten:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Start
- Direkt per:
  ```bash
  python3 main.py
  ```
- Oder über das Skript `start_oneusertool.sh`, das Abstürze protokolliert und das virtuelle Environment nutzt.

## Daten & Lizenz
Alle erzeugten Dateien liegen im Unterordner `Projekt`. Dort befinden sich u.a. die Songtexte und die `genres_profile.json`.

Die Software steht unter der [GNU General Public License v3.0](LICENSE).

## Weiterführende Hinweise für Einsteiger
- Unter Windows wird die virtuelle Umgebung mit `venv\Scripts\activate` aktiviert.
- Legen Sie zuerst ein Genre-Profil an, damit der Zufallsgenerator arbeiten kann.
- Export- und Backupfunktionen im Genre-Archiv erleichtern die Datensicherung.
- Kopieren Sie Genres oder Songtexte in die Zwischenablage, um sie in anderen Programmen zu verwenden.
