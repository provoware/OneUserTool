# OneUserTool

Ein einfaches PyQt5-Programm mit mehreren Modulen. Die Datei `run.py` hilft beim Starten und Einrichten der Umgebung.

## Verwendung

1. Optional: `python run.py --setup` führt einmalig die Einrichtung der virtuellen Umgebung durch und installiert Abhängigkeiten aus `requirements.txt`.
2. Anschließend genügt `python run.py`, um das Programm zu starten. Alle Ausgaben werden zusätzlich in `logs/run.log` gespeichert.

Tritt ein Fehler auf (z.B. fehlt PyQt5), weist das Skript darauf hin und gibt einen Verweis auf die Logdatei aus.
