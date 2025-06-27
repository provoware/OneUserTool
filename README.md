# OneUserTool

OneUserTool ist eine kleine Desktop-Anwendung auf Basis von PyQt5. Sie verwaltet Songtexte, Genres und bietet einen Zufallsgenerator fuer Genres.

## Installation (Linux)
1. Repository klonen:
   ```bash
   git clone <Repo-URL>
   cd OneUserTool
   ```
2. Setup-Skript ausfuehren:
   ```bash
   bash setup.sh
   ```
   Dies legt ein virtuelles Environment an und installiert alle Abhaengigkeiten.
3. Programm starten:
   ```bash
   bash start_oneusertool.sh
   ```

## Start per Doppelklick
Kopieren Sie die Datei `OneUserTool.desktop` auf Ihren Desktop. Beim ersten Start muessen Sie den Ausfuehrungsrechten zustimmen. Anschliessend startet ein Terminalfenster und fuehrt `start_oneusertool.sh` aus.

## FAQ
- **Fehler: "Virtuelle Umgebung fehlt"** – Fuehren Sie `bash setup.sh` aus.
- **Wo werden Daten gespeichert?** – Im Unterordner `Projekt` des Repositories.
- **Wie kann ich das Programm aktualisieren?** – Einfach den aktuellen Code aus dem Repository ziehen und das Setup erneut ausfuehren.


