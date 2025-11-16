# Makefile for C Primer project

# Compiler and flags
CC = clang

# Build configuration: set DEBUG=1 to enable debug symbols
# Usage: make DEBUG=1 (Debug) or make (Release)
DEBUG ?= 0

CFLAGS_BASE = -I./include
ifeq ($(DEBUG),1)
  CFLAGS := $(CFLAGS_BASE) -g -O0 -fno-omit-frame-pointer
else
  CFLAGS := $(CFLAGS_BASE) -O2
endif

# Targets
TARGETS = bin/test_array bin/test_single_linked_list bin/test_queue bin/test_string bin/test_stack

# Default target
all: $(TARGETS)

# Test array with Unity framework
bin/test_array: tests/test_array.c src/array.c lib/unity/unity.c
	@echo "Building test_array..."
	$(CC) $(CFLAGS) -D_Noreturn= $^ -o $@

# Test linked list with Unity framework  
bin/test_single_linked_list: tests/test_single_linked_list.c src/single_linked_list.c lib/unity/unity.c
	@echo "Building test_single_linked_list..."
	$(CC) $(CFLAGS) -D_Noreturn= $^ -o $@

# Test queue with Unity framework
bin/test_queue: tests/test_queue.c src/array.c src/queue.c lib/unity/unity.c
	@echo "Building test_queue..."
	$(CC) $(CFLAGS) -D_Noreturn= $^ -o $@

# Test string with Unity framework
bin/test_string: tests/test_string.c src/string.c lib/unity/unity.c
	@echo "Building test_string..."
	$(CC) $(CFLAGS) -D_Noreturn= $^ -o $@

# Test stack with Unity framework
bin/test_stack: tests/test_stack.c src/array.c src/stack.c lib/unity/unity.c
	@echo "Building test_stack..."
	$(CC) $(CFLAGS) -D_Noreturn= $^ -o $@

# Run tests
test: all
	@echo "Running tests..."
	@if [ -f bin/test_array ]; then echo "=== Running test_array ==="; ./bin/test_array; fi
	@if [ -f bin/test_single_linked_list ]; then echo "=== Running test_single_linked_list ==="; ./bin/test_single_linked_list; fi
	@if [ -f bin/test_queue ]; then echo "=== Running test_queue ==="; ./bin/test_queue; fi
	@if [ -f bin/test_string ]; then echo "=== Running test_string ==="; ./bin/test_string; fi
	@if [ -f bin/test_stack ]; then echo "=== Running test_stack ==="; ./bin/test_stack; fi

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -f $(TARGETS)

# Phony targets
.PHONY: all test clean