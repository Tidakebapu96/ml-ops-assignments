#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

AGENT_NAME="${1:-Agent_Bot}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

mkdir -p output

echo "[1/2] Installing Python dependencies..."
"$PYTHON_BIN" -m pip install -r requirements.txt

echo "[2/2] Running ${AGENT_NAME}..."
exec "$PYTHON_BIN" run_local.py "$AGENT_NAME"
