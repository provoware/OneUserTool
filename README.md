# OneUserTool

OneUserTool ist eine kleine Sammlung von PyQt5-Modulen zur Verwaltung von Songtexten,
Genres und zufälligen Genre-Kombinationen. Die Anwendung richtet sich an Einsteiger,
die ihre Lieblingsgenres und -texte in einer einfachen Oberfläche verwalten möchten.

## Installation

1. Python 3 installieren.
2. Benötigte Pakete mit dem enthaltenen Requirements-File installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Starten

Das Programm kann direkt mit Python gestartet werden:
```bash
python3 main.py
```
Alternativ steht das Skript `start_oneusertool.sh` bereit. Es aktiviert ein virtuelles
Umfeld und führt die Anwendung aus. Das Installationsverzeichnis kann über die
Umgebungsvariable `INSTALLDIR` angepasst werden.

## Hinweise

* Beim ersten Start werden in `Projekt/` nötige Dateien und Ordner angelegt.
* Logs befinden sich im Verzeichnis `logs/`.
* Die Oberfläche bietet ein helles, dunkles oder kontrastreiches Thema.
