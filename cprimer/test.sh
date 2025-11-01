#!/usr/bin/env bash
set -euo pipefail

# Portable test script for Linux/macOS (and Git Bash)
# Ensures Unity is present in third_party/unity, builds tests, and runs them.

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$ROOT_DIR/src"
UNITY_DIR="$ROOT_DIR/third_party/unity"
OUT="$ROOT_DIR/tests"

mkdir -p "$UNITY_DIR"

fetch() {
  local url="$1"; local out="$2"
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$url" -o "$out"
  elif command -v wget >/dev/null 2>&1; then
    wget -qO "$out" "$url"
  else
    echo "Neither curl nor wget found; install one to fetch Unity." >&2
    exit 1
  fi
}

[[ -f "$UNITY_DIR/unity.c" ]] || fetch "https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.c" "$UNITY_DIR/unity.c"
[[ -f "$UNITY_DIR/unity.h" ]] || fetch "https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.h" "$UNITY_DIR/unity.h"
[[ -f "$UNITY_DIR/unity_internals.h" ]] || fetch "https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity_internals.h" "$UNITY_DIR/unity_internals.h"

CC=${CC:-}
if [[ -z "$CC" ]]; then
  if command -v clang >/dev/null 2>&1; then CC=clang; 
  elif command -v gcc >/dev/null 2>&1; then CC=gcc; 
  else echo "No C compiler found (install clang or gcc)" >&2; exit 1; fi
fi

"$CC" -std=c11 \
  -I "$SRC_DIR" -I "$UNITY_DIR" -DUNIT_TEST \
  "$SRC_DIR/test_array.c" "$SRC_DIR/array.c" "$UNITY_DIR/unity.c" \
  -o "$OUT"

echo "Running tests..."
"$OUT"