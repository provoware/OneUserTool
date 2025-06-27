#!/usr/bin/env bash
set -e
printf '\n=== OneUserTool Setup ===\n'

# Python-Version pruefen
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python3 nicht gefunden. Bitte installieren." >&2
  exit 1
fi

py_ok=$(python3 - <<'PY'
import sys
print(sys.version_info >= (3,7))
PY
)
if [ "$py_ok" != "True" ]; then
  echo "Python 3.7 oder neuer erforderlich." >&2
  exit 1
fi

if [ ! -d venv ]; then
  echo "Erstelle virtuelles Environment..."
  python3 -m venv venv || { echo "Fehler beim Erstellen des venv." >&2; exit 1; }
fi

source venv/bin/activate
pip install -U pip
if pip install -r requirements.txt; then
  echo "Abhaengigkeiten installiert."
else
  echo "Installation der Abhaengigkeiten fehlgeschlagen." >&2
  exit 1
fi

echo "Setup abgeschlossen. Starte das Programm mit: bash start_oneusertool.sh"

