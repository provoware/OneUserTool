#!/usr/bin/env bash
# Setup-Skript für OneUserTool
# Erstellt eine virtuelle Umgebung und generiert ein Startskript.

set -euo pipefail

INSTALL_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$INSTALL_DIR/venv"
START_SCRIPT="$INSTALL_DIR/start_oneusertool.sh"

log(){ printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$1"; }

log "Installationsverzeichnis: $INSTALL_DIR"

if [[ ! -d "$VENV_DIR" ]]; then
    log "Erstelle virtuelle Python-Umgebung..."
    python3 -m venv "$VENV_DIR"
else
    log "Virtuelle Umgebung existiert bereits."
fi

log "Aktiviere Umgebung und installiere Abhängigkeiten..."
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"
pip install -r "$INSTALL_DIR/requirements.txt"

after_install(){
    log "Erzeuge Startskript $START_SCRIPT"
    cat > "$START_SCRIPT" <<'EOS'
#!/usr/bin/env bash
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
EOS
    chmod +x "$START_SCRIPT"
}

after_install
log "Setup abgeschlossen. Starte das Tool mit ./start_oneusertool.sh"

