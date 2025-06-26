# OneUserTool

OneUserTool ist ein einfaches Desktopprogramm auf Basis von PyQt5. Es besteht aus drei Hauptmodulen und bietet Funktionen rund um Songtexte und Genres.

## Installation

1. Stelle sicher, dass Python 3.7 oder neuer installiert ist.
2. (Empfohlen) Lege ein virtuelles Environment an und aktiviere es:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Installiere die Abhängigkeiten aus `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Starten der Anwendung

Nach der Installation kann das Programm direkt gestartet werden:

```bash
python main.py
```

Alternativ bietet das Skript `start_oneusertool.sh` weitere Optionen zum Start und zum Loggen des Programmlaufs.

## Module

### Songtexte
Dieses Modul dient als Editor für eigene Songtexte. Titel, Genre und Text werden eingegeben und als Textdateien unter `Projekt/Songtexte` gespeichert. Bestehende Einträge können bearbeitet oder gelöscht werden.

### Genres
Hier lassen sich beliebige Genre-Profile anlegen, verwalten und als JSON-Datei exportieren oder importieren. Die Daten liegen in `Projekt/genres_profile.json` und können per Backup-Funktion gesichert werden.

### Zufallsgenerator
Aus den gespeicherten Genres wird auf Wunsch eine zufällige Auswahl erzeugt. Die Anzahl der auszuwählenden Genres kann per Knopfdruck gewählt werden, das Ergebnis lässt sich in die Zwischenablage kopieren.

## Weiterführende Laienvorschläge

- Verwende konsequent ein virtuelles Environment, um deine Python-Installation sauber zu halten.
- Nutze regelmäßig die Backup-Funktion des Genre-Moduls oder kopiere den Ordner `Projekt`, um deine Daten zu sichern.
- Spiele mit kleinen Genre-Listen, um die zufälligen Ergebnisse besser steuern zu können.
- Die Module können auch unabhängig voneinander erkundet werden – so findest du schnell heraus, welche Funktionen für dich hilfreich sind.
