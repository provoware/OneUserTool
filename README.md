# OneUserTool

OneUserTool ist eine kleine Desktop-Anwendung zur Verwaltung von Songtexten,
Genre-Archiven und zum Erzeugen zufälliger Genrelisten. Die Software basiert auf
PyQt5 und stellt für jedes Themengebiet ein eigenes Modul bereit.

## Installation

Voraussetzung ist Python 3.7 oder neuer. Die benötigten Pakete lassen sich am
schnellsten per `pip` installieren:

```bash
pip install -r requirements.txt
```

Am einfachsten funktioniert dies in einer virtuellen Umgebung, damit keine
Systempakete verändert werden.

## Start

Das Programm kann direkt gestartet werden:

```bash
python3 main.py
```

Alternativ gibt es für Linux das Skript `start_oneusertool.sh`. Es aktiviert die
virtuelle Umgebung, führt das Programm aus und bietet bei Abstürzen die Möglichkeit
zum Neustart oder zum Anzeigen der Logdatei.

## Optionale Features

* Das Modul `design_manager.py` erlaubt verschiedene Themes wie `dark`, `light`
  oder `highcontrast`. Schriftgröße und Farbgebung lassen sich dort leicht anpassen.
* Das Startskript legt Logdateien im Ordner `~/OneUserTool/logs` an.

## Hinweise

Alle im Programm erzeugten Daten werden im Unterordner `Projekt` gespeichert.
Zum Nutzen der GUI muss PyQt5 installiert sein; die Abhängigkeiten werden durch das
obige `pip`-Kommando automatisch eingerichtet.
