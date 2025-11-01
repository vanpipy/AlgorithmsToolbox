#!/usr/bin/env bash
set -euo pipefail

# Portable build script for Linux/macOS (and Git Bash)
# Builds src/array.c -> ./array

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="$ROOT_DIR/src/array.c"
OUT="$ROOT_DIR/array"

CC=${CC:-}
if [[ -z "$CC" ]]; then
  if command -v clang >/dev/null 2>&1; then CC=clang; 
  elif command -v gcc >/dev/null 2>&1; then CC=gcc; 
  else echo "No C compiler found (install clang or gcc)" >&2; exit 1; fi
fi

"$CC" -std=c11 -I "$ROOT_DIR/src" "$SRC" -o "$OUT"
echo "Built $OUT successfully."