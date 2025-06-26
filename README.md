# OneUserTool

OneUserTool ist eine kleine Desktopanwendung zum Verwalten von Songtexten, einem Genre-Archiv und einem einfachen Zufallsgenerator. Das Programm ist in Python geschrieben und nutzt PyQt5 für die Oberfläche.

## Installation

1. Benötigt wird Python 3.7 oder neuer. Zudem muss das Qt-Framework über das Paket `PyQt5` verfügbar sein.
2. Projekt auschecken und im Ordner eine virtuelle Umgebung anlegen:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Anwendung starten

Die Anwendung lässt sich direkt mit Python ausführen:

```bash
python3 main.py
```

Alternativ kann das Skript `start_oneusertool.sh` genutzt werden. Dieses startet die App in einer Schleife und schreibt Ausgaben in `logs/run.log`:

```bash
./start_oneusertool.sh
```

## Tipps für Einsteiger

* Eine virtuelle Umgebung verhindert Versionskonflikte und lässt sich bei Problemen einfach löschen.
* Wenn beim Start eine Fehlermeldung zu Qt erscheint, prüfen ob `PyQt5` korrekt installiert wurde (ggf. `pip install PyQt5`).
* Der Ordner `Projekt/` wird beim ersten Start automatisch angelegt und enthält alle gespeicherten Daten. Ein Backup gelingt am einfachsten über den Knopf im Genre-Archiv.

