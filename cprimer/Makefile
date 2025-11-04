# Makefile for C Primer project

# Compiler and flags
CC = clang
CFLAGS = -I./include

# Targets
TARGETS = bin/test_array bin/test_single_linked_list

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

# Run tests
test: all
	@echo "Running tests..."
	@if [ -f bin/test_array ]; then echo "=== Running test_array ==="; ./bin/test_array; fi
	@if [ -f bin/test_single_linked_list ]; then echo "=== Running test_single_linked_list ==="; ./bin/test_single_linked_list; fi

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -f $(TARGETS)

# Phony targets
.PHONY: all test clean