#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INSTALLDIR="$SCRIPT_DIR"
VENV_ACT="$INSTALLDIR/venv/bin/activate"
MAIN_PY="$INSTALLDIR/main.py"
LOGDIR="$INSTALLDIR/logs"
RUNLOG="$LOGDIR/run.log"

mkdir -p "$LOGDIR"
echo "=== $(date '+%Y-%m-%d %H:%M:%S') Start ===" >> "$RUNLOG"

if [ ! -f "$VENV_ACT" ]; then
  echo "[FEHLER] venv fehlt. Setup erneut ausführen." | tee -a "$RUNLOG" >&2
  exit 1
fi
# shellcheck disable=SC1090
source "$VENV_ACT"

while true; do
  python3 "$MAIN_PY" 2>&1 | tee -a "$RUNLOG"
  code=${PIPESTATUS[0]}
  if [ "$code" -eq 0 ]; then break; fi
  echo "Absturz (Code $code)."
  select_option "Aktion wählen:" "Neustart" "Logs anzeigen" "Beenden"
  case $? in
    0) continue ;;
    1) less "$RUNLOG" ;;
    2) exit 1 ;;
  esac
done
