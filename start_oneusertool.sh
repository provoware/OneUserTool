#!/usr/bin/env bash
set -euo pipefail

# Resolve paths relative to this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
VENV_ACT="$VENV_DIR/bin/activate"
MAIN_PY="$SCRIPT_DIR/main.py"
LOGDIR="$SCRIPT_DIR/logs"
RUNLOG="$LOGDIR/run.log"

mkdir -p "$LOGDIR"
echo "=== $(date '+%Y-%m-%d %H:%M:%S') Start ===" >> "$RUNLOG"

# Log helper
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$RUNLOG"; }

# Simple menu using bash 'select'
select_option() {
  local PS3="$1 "
  shift
  select opt in "$@"; do
    if [[ -n $opt ]]; then
      return $((REPLY-1))
    fi
  done
}

# Create venv if missing
if [ ! -f "$VENV_ACT" ]; then
  log "[INFO] Creating virtual environment in $VENV_DIR"
  python3 -m venv "$VENV_DIR" || { log "[ERROR] Failed to create venv"; exit 1; }
  # shellcheck disable=SC1090
  source "$VENV_ACT"
  "$VENV_DIR/bin/pip" install --upgrade pip wheel >> "$RUNLOG" 2>&1
  if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    "$VENV_DIR/bin/pip" install -r "$SCRIPT_DIR/requirements.txt" >> "$RUNLOG" 2>&1
  fi
else
  # shellcheck disable=SC1090
  source "$VENV_ACT"
fi

trap 'log "[ERROR] Script aborted"' ERR

while true; do
  python3 "$MAIN_PY" 2>&1 | tee -a "$RUNLOG" || true
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
