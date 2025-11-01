#!/usr/bin/env bash
set -euo pipefail

# Portable clean script for Linux/macOS (and Git Bash)

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

rm -f "$ROOT_DIR/array" "$ROOT_DIR/tests" \
      "$ROOT_DIR/array.exe" "$ROOT_DIR/tests.exe" \
      "$ROOT_DIR/third_party/unity/unity.c" \
      "$ROOT_DIR/third_party/unity/unity.h" \
      "$ROOT_DIR/third_party/unity/unity_internals.h" || true

echo "Cleaned build artifacts and Unity sources."