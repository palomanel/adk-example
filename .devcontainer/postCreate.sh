#!/usr/bin/env bash
set -euo pipefail

# Change into the repository root
if [ $# -eq 0 ] || [ ! -d "$1" ]; then
    echo "Error: First parameter must be an existing folder" >&2
    exit 1
fi
cd "$1"

# Create virtual environment if missing
if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate
# Install pre-commit and its hooks
pip install --upgrade pip pre-commit
pre-commit install --install-hooks
# Install project dependencies
pip install -r requirements.txt
