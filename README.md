# OneUserTool

OneUserTool ist eine kleine Sammlung von Modulen, die beim Schreiben eigener Musikprojekte helfen soll. Die Anwendung basiert auf PyQt5 und benötigt mindestens Python 3.7.

## Module

- **Songtexte** – Verwaltung und Bearbeitung von Songtexten. Texte können gespeichert, geladen und gelöscht werden.
- **Genres** – Ein Archiv zur Pflege eigener Genre-Profile. Einträge lassen sich exportieren, importieren oder sichern.
- **Zufallsgenerator** – Wählt zufällige Genres aus einem Profil und kopiert sie in die Zwischenablage.
- **Dateiumbenennung** – Dient zum einheitlichen Umbenennen von Dateien (z. B. Audiodateien). Dieses Modul ist aktuell noch nicht implementiert und dient als Platzhalter.

## Einrichtung

1. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
2. Anwendung starten:
   ```bash
   python main.py
   ```
   Alternativ kann unter Linux das Skript `start_oneusertool.sh` genutzt werden.

Die Software benötigt Python 3.7 oder neuer sowie die Bibliothek PyQt5.

## Weiterführende Tipps für Einsteiger

- Regelmäßig Backups erstellen, damit keine Texte verloren gehen.
- Mit kleinen Genre-Listen beginnen und diese schrittweise erweitern.
- Bei Problemen hilft oft ein Blick in die Logdateien im `logs`-Ordner.

