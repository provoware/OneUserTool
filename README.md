# OneUserTool

Dieses Projekt bietet eine einfache grafische Oberfläche auf Basis von PyQt5. Um die Anwendung zu starten, genügt es, das Skript `setup_and_start.sh` auszuführen. Das Skript erstellt bei Bedarf eine virtuelle Umgebung, installiert alle Abhängigkeiten aus `requirements.txt` und startet anschließend automatisch die GUI.

## Schnellstart

```bash
./setup_and_start.sh
```

Für Fragen zum Umgang mit virtuellen Umgebungen oder bei Problemen siehe die Hinweise am Ende dieser Datei.

## Hilfreiche Hinweise für Einsteiger

* **Dateirechte:** Unter Linux muss das Skript ausführbar sein (`chmod +x setup_and_start.sh`).
* **Fehlermeldungen bei der Installation:** Stellen Sie sicher, dass `python3` sowie die Paketverwaltung `pip` installiert sind.
* **Virtuelle Umgebung löschen:** Möchten Sie das Projekt neu einrichten, können Sie einfach den Ordner `.venv` löschen und das Startskript erneut ausführen.
