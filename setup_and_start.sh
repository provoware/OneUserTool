#!/usr/bin/env bash
# Setup virtual environment and launch GUI
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$DIR/.venv"
PY="$VENV/bin/python"

if [ ! -d "$VENV" ]; then
  echo "[Info] Creating virtual environment..."
  python3 -m venv "$VENV"
fi

source "$VENV/bin/activate"

pip install --upgrade pip >/dev/null
pip install -r "$DIR/requirements.txt" >/dev/null

echo "[Info] Starting OneUserTool GUI..."
exec "$PY" "$DIR/main.py"
