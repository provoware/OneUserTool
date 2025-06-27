#!/usr/bin/env python3
"""Helper script to run the OneUserTool GUI.

- Ensures required directories exist.
- Optionally creates/updates a virtual environment.
- Launches the GUI and logs output to ``logs/run.log``.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import logging
import os
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "run.log"
VENV_DIR = ROOT / ".venv"
REQ_FILE = ROOT / "requirements.txt"


def ensure_dirs() -> None:
    """Create directories needed for runtime."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def create_venv() -> None:
    """Create or update the virtual environment and install deps."""
    if not VENV_DIR.exists():
        print(f"Erstelle virtuelle Umgebung in {VENV_DIR}…")
        venv.create(VENV_DIR, with_pip=True)
    pip = VENV_DIR / ("Scripts" if os.name == "nt" else "bin") / "pip"
    print("Installiere Abhängigkeiten…")
    subprocess.check_call([str(pip), "install", "-r", str(REQ_FILE)])


def pyqt_installed(python: Path) -> bool:
    """Return True if PyQt5 can be imported using ``python``."""
    try:
        subprocess.check_call([str(python), "-c", "import PyQt5"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def run_app(python: Path) -> int:
    """Start the GUI and mirror its output to ``logs/run.log``."""
    logging.info("Starte OneUserTool")
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"=== {_dt.datetime.now():%Y-%m-%d %H:%M:%S} Start ===\n")
        proc = subprocess.Popen([str(python), str(ROOT / "main.py")], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line, end="")
            log.write(line)
        proc.wait()
        log.write(f"=== Ende mit Code {proc.returncode} ===\n")
        return proc.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="OneUserTool starten")
    parser.add_argument("--setup", action="store_true", help="virtuelle Umgebung einrichten und Abhängigkeiten installieren")
    args = parser.parse_args(argv)

    ensure_dirs()
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    python = VENV_DIR / ("Scripts" if os.name == "nt" else "bin") / "python"

    if args.setup or not python.exists():
        try:
            create_venv()
        except Exception as exc:  # pragma: no cover - setup failures
            logging.exception("Fehler beim Setup")
            print(f"Setup fehlgeschlagen: {exc}")
            return 1

    if not pyqt_installed(python):
        print("PyQt5 ist nicht installiert. Führe das Skript mit --setup aus oder installiere manuell die Abhängigkeiten.")
        return 1

    code = run_app(python)
    if code != 0:
        print(f"Programm wurde mit Fehlercode {code} beendet. Siehe {LOG_FILE} für Details.")
    return code


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
