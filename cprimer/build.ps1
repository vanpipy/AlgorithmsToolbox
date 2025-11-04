# PowerShell build script for C Primer project

# Set error handling
$ErrorActionPreference = "Stop"

# Compiler
$CC = "clang"

# Create bin directory if it doesn't exist
if (-not (Test-Path "bin")) {
    New-Item -ItemType Directory -Path "bin" | Out-Null
}

# Build functions
function Build-TestArray {
    Write-Host "Building test_array..." -ForegroundColor Yellow
    & $CC -Iinclude -D_Noreturn= tests/test_array.c src/array.c lib/unity/unity.c -o bin/test_array.exe
    if ($LASTEXITCODE -ne 0) {
        throw "Compilation failed for test_array"
    }
}

function Build-TestLinkedList {
    Write-Host "Building test_single_linked_list..." -ForegroundColor Yellow
    & $CC -Iinclude -D_Noreturn= tests/test_single_linked_list.c src/single_linked_list.c lib/unity/unity.c -o bin/test_single_linked_list.exe
    if ($LASTEXITCODE -ne 0) {
        throw "Compilation failed for test_single_linked_list"
    }
}

# Run tests functions
function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Cyan
    
    if (Test-Path "bin/test_array") {
        Write-Host "=== Running test_array ===" -ForegroundColor Yellow
        & ./bin/test_array
        if ($LASTEXITCODE -ne 0) { Write-Warning "test_array failed with exit code $LASTEXITCODE" }
    }
    
    if (Test-Path "bin/test_single_linked_list") {
        Write-Host "=== Running test_single_linked_list ===" -ForegroundColor Yellow
        & ./bin/test_single_linked_list
        if ($LASTEXITCODE -ne 0) { Write-Warning "test_single_linked_list failed with exit code $LASTEXITCODE" }
    }
}

# Handle command line arguments
$target = $args[0]

# Main build process
try {
    if ($target) {
        # Build specific target
        switch ($target) {
            "test_array" { Build-TestArray }
            "test_single_linked_list" { Build-TestLinkedList }
            default { Write-Host "Unknown target: $target" -ForegroundColor Red; exit 1 }
        }
    } else {
        # Build all targets
        Build-TestArray
        Build-TestLinkedList
    }
    
    Write-Host "Build completed successfully!" -ForegroundColor Green
    
    # Ask if user wants to run tests (only if no specific target was specified)
    if (-not $target) {
        $runTests = Read-Host "Do you want to run the tests? (y/N)"
        if ($runTests -eq "y" -or $runTests -eq "Y") {
            Run-Tests
        }
    }
    
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
}