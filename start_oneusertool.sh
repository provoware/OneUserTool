#!/usr/bin/env bash
# Startskript für OneUserTool.
# Aktiviert die virtuelle Umgebung und startet die Anwendung.

set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_ACT="$DIR/venv/bin/activate"
MAIN_PY="$DIR/main.py"
LOGDIR="$DIR/logs"
RUNLOG="$LOGDIR/run.log"

mkdir -p "$LOGDIR"
echo "=== $(date '+%Y-%m-%d %H:%M:%S') Start ===" >> "$RUNLOG"

if [[ ! -f "$VENV_ACT" ]]; then
    echo "[FEHLER] venv fehlt. Bitte setup erneut ausführen." | tee -a "$RUNLOG" >&2
    exit 1
fi
# shellcheck disable=SC1090
source "$VENV_ACT"
python3 "$MAIN_PY" 2>&1 | tee -a "$RUNLOG"

