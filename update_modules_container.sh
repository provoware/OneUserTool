#!/usr/bin/env bash
# Update script for ModulesContainer component
# Version 1.1

set -euo pipefail

# Load global config (INSTALLDIR, MODULE_VERSION)
# Check for config.sh before sourcing; exit with error if missing
CONFIG_PATH="$(dirname "$0")/../config.sh"
if [[ -f "$CONFIG_PATH" ]]; then
  source "$CONFIG_PATH"
else
  echo "ERROR: Required config '$CONFIG_PATH' not found." >&2
  exit 1
fi

log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"; }

usage() {
  cat <<EOF
Usage: $0 [--install-dir DIR] [--yes] [--dry-run]
Options:
  --install-dir DIR  Pfad zum Frontend-Quellcode (Standard: \$INSTALLDIR/frontend)
  --yes              Keine Bestätigung anfordern
  --dry-run          Nur anzeigen, aber nicht ausführen
EOF
  exit 1
}

# Defaults
target_dir="${INSTALLDIR}/frontend/src/components"
ASSUME_YES=false
DRY_RUN=false

# Parse options
while [[ $# -gt 0 ]]; do
  case "$1" in
    --install-dir) target_dir="$2"; shift 2;;
    --yes) ASSUME_YES=true; shift;;
    --dry-run) DRY_RUN=true; shift;;
    *) usage;;
  esac
done

# Confirm
if ! $ASSUME_YES; then
  read -rp "Update ModulesContainer in $target_dir? (y/N) " ans
  [[ "$ans" =~ ^[Yy] ]] || exit 0
fi

# Ensure target
if [[ ! -d "$target_dir" ]]; then
  echo "ERROR: Komponenten-Verzeichnis '$target_dir' nicht gefunden." >&2
  exit 1
fi

# Backup existing component
component_file="$target_dir/ModulesContainer.jsx"
if [[ -f "$component_file" ]]; then
  log "Backing up existing ModulesContainer.jsx"
  if [[ "$DRY_RUN" == false ]]; then
    cp "$component_file" "${component_file}.bak.$(date +%Y%m%d%H%M%S)"
  else
    echo "DRY RUN: cp $component_file ${component_file}.bak.$(date +%Y%m%d%H%M%S)"
  fi
fi

# Copy updated component
log "Installing updated ModulesContainer.jsx (Version $MODULE_VERSION)"
if [[ "$DRY_RUN" == false ]]; then
  cp "$(dirname "$0")/../modules/ModulesContainer.jsx" "$component_file"
else
  echo "DRY RUN: cp $(dirname "$0")/../modules/ModulesContainer.jsx $component_file"
fi

log "Update complete. Please rebuild frontend if necessary."
