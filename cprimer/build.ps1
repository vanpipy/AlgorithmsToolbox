# PowerShell build script for C Primer project

# Set error handling
$ErrorActionPreference = "Stop"

# Compiler
$CC = "clang"

# Build configuration (Release by default). Set via second arg (debug/release)
# or environment variable DEBUG=1
$config = "Release"
$configArg = $args[1]
if ($configArg) {
    switch ($configArg.ToLower()) {
        "debug" { $config = "Debug" }
        "release" { $config = "Release" }
    }
}
if ($env:DEBUG -eq "1") { $config = "Debug" }

# Create bin directory if it doesn't exist
if (-not (Test-Path "bin")) {
    New-Item -ItemType Directory -Path "bin" | Out-Null
}

# Build functions
function Build-TestArray {
    Write-Host "Building test_array ($config)..." -ForegroundColor Yellow
    $flags = @()
    if ($config -eq "Debug") { $flags += @("-g","-O0","-fno-omit-frame-pointer") } else { $flags += @("-O2") }
    $flags += @("-Iinclude","-D_Noreturn=")
    & $CC $flags tests/test_array.c src/array.c lib/unity/unity.c -o bin/test_array.exe
    if ($LASTEXITCODE -ne 0) {
        throw "Compilation failed for test_array"
    }
}

function Build-TestLinkedList {
    Write-Host "Building test_single_linked_list ($config)..." -ForegroundColor Yellow
    $flags = @()
    if ($config -eq "Debug") { $flags += @("-g","-O0","-fno-omit-frame-pointer") } else { $flags += @("-O2") }
    $flags += @("-Iinclude","-D_Noreturn=")
    & $CC $flags tests/test_single_linked_list.c src/single_linked_list.c lib/unity/unity.c -o bin/test_single_linked_list.exe
    if ($LASTEXITCODE -ne 0) {
        throw "Compilation failed for test_single_linked_list"
    }
}

function Build-TestQueue {
    Write-Host "Building test_queue ($config)..." -ForegroundColor Yellow
    $flags = @()
    if ($config -eq "Debug") { $flags += @("-g","-O0","-fno-omit-frame-pointer") } else { $flags += @("-O2") }
    $flags += @("-Iinclude","-D_Noreturn=")
    & $CC $flags tests/test_queue.c src/array.c src/queue.c lib/unity/unity.c -o bin/test_queue.exe
    if ($LASTEXITCODE -ne 0) {
        throw "Compilation failed for test_queue"
    }
}

function Build-TestString {
    Write-Host "Building test_string ($config)..." -ForegroundColor Yellow
    $flags = @()
    if ($config -eq "Debug") { $flags += @("-g","-O0","-fno-omit-frame-pointer") } else { $flags += @("-O2") }
    $flags += @("-Iinclude","-D_Noreturn=")
    & $CC $flags tests/test_string.c src/string.c lib/unity/unity.c -o bin/test_string.exe
    if ($LASTEXITCODE -ne 0) {
        throw "Compilation failed for test_string"
    }
}
# Run tests functions
function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Cyan
    
    if (Test-Path "bin/test_array.exe") {
        Write-Host "=== Running test_array ===" -ForegroundColor Yellow
        & .\bin\test_array.exe
        if ($LASTEXITCODE -ne 0) { Write-Warning "test_array failed with exit code $LASTEXITCODE" }
    }
    
    if (Test-Path "bin/test_single_linked_list.exe") {
        Write-Host "=== Running test_single_linked_list ===" -ForegroundColor Yellow
        & .\bin\test_single_linked_list.exe
        if ($LASTEXITCODE -ne 0) { Write-Warning "test_single_linked_list failed with exit code $LASTEXITCODE" }
    }

    if (Test-Path "bin/test_queue.exe") {
        Write-Host "=== Running test_queue ===" -ForegroundColor Yellow
        & .\bin\test_queue.exe
        if ($LASTEXITCODE -ne 0) { Write-Warning "test_queue failed with exit code $LASTEXITCODE" }
    }

     if (Test-Path "bin/test_string.exe") {
        Write-Host "=== Running test_string ===" -ForegroundColor Yellow
        & .\bin\test_string.exe
        if ($LASTEXITCODE -ne 0) { Write-Warning "test_string failed with exit code $LASTEXITCODE" }
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
            "test_queue" { Build-TestQueue }
            "test_string" { Build-TestString }
            default { Write-Host "Unknown target: $target" -ForegroundColor Red; exit 1 }
        }
    } else {
        # Build all targets
        Build-TestArray
        Build-TestLinkedList
        Build-TestQueue
        Build-TestString
    }
    
    Write-Host "Build completed successfully! ($config)" -ForegroundColor Green
    
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