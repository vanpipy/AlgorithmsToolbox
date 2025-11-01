# Minimal C project Makefile (cross-platform: Windows/Linux)
# Targets: build, run, deps (Unity), test, clean

# Choose compiler: defaults to clang, but you can override: make CC=gcc or CC=cl
CC ?= clang

# OS-specific exe suffix
ifeq ($(OS),Windows_NT)
  EXE := .exe
else
  EXE :=
endif

# Common flags
CFLAGS_COMMON = -std=c11 -I src -I third_party/unity -Wall -Wextra
LDFLAGS_COMMON =

# MSVC adjustments
ifeq ($(CC),cl)
  CFLAGS_COMMON = /nologo /W3 /I src /I third_party/unity
  LDFLAGS_COMMON =
endif

# Files
SRC_DIR = src
SRC_MAIN = $(SRC_DIR)/array.c
BIN_MAIN = array$(EXE)

UNITY_DIR = third_party/unity
UNITY_C = $(UNITY_DIR)/unity.c
UNITY_H = $(UNITY_DIR)/unity.h
UNITY_INTERNALS_H = $(UNITY_DIR)/unity_internals.h
TEST_SRC = $(SRC_DIR)/test_array.c
BIN_TEST = tests$(EXE)

.PHONY: build run deps test clean

build: $(BIN_MAIN)

run: $(BIN_MAIN)
    ./$(BIN_MAIN)

deps: $(UNITY_C) $(UNITY_H) $(UNITY_INTERNALS_H)

test: deps $(BIN_TEST)
    ./$(BIN_TEST)

clean:
    - rm -f $(BIN_MAIN) $(BIN_TEST) $(UNITY_C) $(UNITY_H) $(UNITY_INTERNALS_H)
    - del /q $(BIN_MAIN) 2> NUL
    - del /q $(BIN_TEST) 2> NUL
    - del /q $(UNITY_C) 2> NUL
    - del /q $(UNITY_H) 2> NUL
    - del /q $(UNITY_INTERNALS_H) 2> NUL

# Build rules
ifeq ($(CC),cl)
$(BIN_MAIN): $(SRC_MAIN)
	$(CC) $(SRC_MAIN) $(CFLAGS_COMMON) /Fe:$(BIN_MAIN)

$(BIN_TEST): $(TEST_SRC) $(SRC_MAIN) $(UNITY_C)
	$(CC) $(TEST_SRC) $(SRC_MAIN) $(UNITY_C) $(CFLAGS_COMMON) /DUNIT_TEST /Fe:$(BIN_TEST)
else
$(BIN_MAIN): $(SRC_MAIN)
	$(CC) $(CFLAGS_COMMON) $(SRC_MAIN) -o $(BIN_MAIN) $(LDFLAGS_COMMON)

$(BIN_TEST): $(TEST_SRC) $(SRC_MAIN) $(UNITY_C)
	$(CC) $(CFLAGS_COMMON) -DUNIT_TEST $(TEST_SRC) $(SRC_MAIN) $(UNITY_C) -o $(BIN_TEST) $(LDFLAGS_COMMON)
endif

# Fetch Unity sources (third_party/unity) with curl/wget or PowerShell fallback
$(UNITY_C):
	@mkdir -p $(UNITY_DIR) 2>/dev/null || powershell -NoProfile -ExecutionPolicy Bypass -Command "New-Item -ItemType Directory -Force -Path '$(UNITY_DIR)'" > NUL
	@if command -v curl >/dev/null 2>&1; then \
		curl -fsSL https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.c -o "$(UNITY_C)"; \
	elif command -v wget >/dev/null 2>&1; then \
		wget -qO "$(UNITY_C)" https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.c; \
	else \
		powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.c' -OutFile '$(UNITY_C)'"; \
	fi

$(UNITY_H):
	@mkdir -p $(UNITY_DIR) 2>/dev/null || powershell -NoProfile -ExecutionPolicy Bypass -Command "New-Item -ItemType Directory -Force -Path '$(UNITY_DIR)'" > NUL
	@if command -v curl >/dev/null 2>&1; then \
		curl -fsSL https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.h -o "$(UNITY_H)"; \
	elif command -v wget >/dev/null 2>&1; then \
		wget -qO "$(UNITY_H)" https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.h; \
	else \
		powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.h' -OutFile '$(UNITY_H)'"; \
	fi

$(UNITY_INTERNALS_H):
	@mkdir -p $(UNITY_DIR) 2>/dev/null || powershell -NoProfile -ExecutionPolicy Bypass -Command "New-Item -ItemType Directory -Force -Path '$(UNITY_DIR)'" > NUL
	@if command -v curl >/dev/null 2>&1; then \
		curl -fsSL https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity_internals.h -o "$(UNITY_INTERNALS_H)"; \
	elif command -v wget >/dev/null 2>&1; then \
		wget -qO "$(UNITY_INTERNALS_H)" https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity_internals.h; \
	else \
		powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity_internals.h' -OutFile '$(UNITY_INTERNALS_H)'"; \
	fi