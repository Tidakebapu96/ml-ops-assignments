#!/bin/bash
# =============================================================
# deploy.sh – Run KFP pipelines locally (no Kubernetes needed)
# =============================================================
# Calls each pipeline component directly as a Python function.
# No Kubernetes, Docker, or virtual environment required.
#
# Prerequisites: Python 3.9+
# =============================================================

set -e

echo "========================================"
echo " ML-Ops Assignment 2 – KFP Pipeline Demo"
echo "========================================"

# Step 1: Install dependencies
echo ""
echo "[1/2] Installing Python dependencies..."
pip install kfp scikit-learn --break-system-packages -q

# Step 2: Run both pipelines
echo ""
echo "[2/2] Running pipelines..."
echo ""
python3 run_local.py

echo ""
echo "========================================"
echo " Done!"
echo "========================================"
