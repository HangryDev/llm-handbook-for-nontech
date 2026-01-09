#!/bin/bash
set -e

# Define root directory
ROOT_DIR="$(dirname "$0")"
cd "$ROOT_DIR"

# Check for venv
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv .venv
fi

# Install requirements
echo "Installing requirements..."
.venv/bin/pip install -r requirements.txt

# Build the book
echo "Building Jupyter Book..."
.venv/bin/jupyter-book build .

echo "Build complete!"
echo "Open the following file in your browser to view the book:"
echo "file://$(pwd)/_build/html/index.html"
