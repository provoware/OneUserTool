# OneUserTool

Dieses Projekt stellt eine Sammlung kleiner Helfer bereit, die über eine grafische Oberfläche bedient werden. Beim Start von `main.py` wird automatisch ein Ordner `Projekt` im gleichen Verzeichnis angelegt. Darin speichert die Anwendung alle dauerhaften Daten wie Genre-Profile und Songtexte.

## Pfad anpassen

Standardmäßig befindet sich der Ordner im Programmverzeichnis. Soll er an einen anderen Ort verschoben werden, kann man beispielsweise die Umgebungsvariable `PROJEKT_DIR` setzen oder in einer kleinen Konfigurationsdatei einen eigenen Pfad hinterlegen und die Module entsprechend anpassen.

## Weiterführende Tipps für Einsteiger

* Nach dem Start befindet sich die Bedienoberfläche in `main.py`. Ein Doppelklick auf die Datei oder der Aufruf `python3 main.py` genügt.
* Wer eigene Genres oder Songtexte erfassen möchte, findet die Dateien später im Ordner `Projekt` und kann dort auch Sicherungskopien anlegen.
* Regelmäßiges Backup der Daten empfiehlt sich besonders vor einer Aktualisierung.
* Ein Blick in die Dateien `genres_modul.py` und `songtext_modul.py` hilft beim Verständnis, wie die Ablage funktioniert und wie sich Pfade gegebenenfalls anpassen lassen.

