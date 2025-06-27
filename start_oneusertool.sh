#!/usr/bin/env bash
set -e
INSTALLDIR="$(cd "$(dirname "$0")" && pwd)"
VENV_ACT="$INSTALLDIR/venv/bin/activate"
MAIN_PY="$INSTALLDIR/main.py"
LOGDIR="$INSTALLDIR/logs"
RUNLOG="$LOGDIR/run.log"

mkdir -p "$LOGDIR"
echo "=== $(date '+%Y-%m-%d %H:%M:%S') Start ===" >> "$RUNLOG"

if [ ! -f "$VENV_ACT" ]; then
  echo "[FEHLER] Virtuelle Umgebung fehlt. Bitte 'bash setup.sh' ausfuehren." | tee -a "$RUNLOG" >&2
  exit 1
fi
# shellcheck disable=SC1090
source "$VENV_ACT"

while true; do
  python3 "$MAIN_PY" 2>&1 | tee -a "$RUNLOG"
  code=${PIPESTATUS[0]}
  if [ "$code" -eq 0 ]; then break; fi
  echo "Das Programm wurde mit Code $code beendet."
  echo "Aktion waehlen:\n  1) Neustart\n  2) Logs anzeigen\n  3) Beenden"
  read -rp "Auswahl: " ch
  case "$ch" in
    1) continue ;;
    2) less "$RUNLOG" ;;
    3) exit 1 ;;
    *) echo "Ungueltige Eingabe" ;;
  esac
done

