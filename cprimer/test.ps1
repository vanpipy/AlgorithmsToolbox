param(
    [string]$CC = ""
)

function Get-Compiler {
    param([string]$Override)
    if ($Override) { return $Override }
    if (Get-Command clang -ErrorAction SilentlyContinue) { return "clang" }
    if (Get-Command gcc -ErrorAction SilentlyContinue) { return "gcc" }
    if (Get-Command cl -ErrorAction SilentlyContinue) { return "cl" }
    Write-Host "No C compiler found. Install Visual Studio Build Tools, LLVM/Clang, or MSYS2/MinGW." -ForegroundColor Red
    exit 1
}

function Ensure-Unity {
    $unityDir = Join-Path $PSScriptRoot 'third_party/unity'
    if (-not (Test-Path $unityDir)) { New-Item -ItemType Directory -Path $unityDir | Out-Null }
    $unityC = Join-Path $unityDir 'unity.c'
    $unityH = Join-Path $unityDir 'unity.h'
    $unityInternals = Join-Path $unityDir 'unity_internals.h'
    if (-not (Test-Path $unityC)) {
        Write-Host "Fetching Unity (unity.c)..."
        Invoke-WebRequest -Uri "https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.c" -OutFile $unityC
    }
    if (-not (Test-Path $unityH)) {
        Write-Host "Fetching Unity (unity.h)..."
        Invoke-WebRequest -Uri "https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.h" -OutFile $unityH
    }
    if (-not (Test-Path $unityInternals)) {
        Write-Host "Fetching Unity (unity_internals.h)..."
        Invoke-WebRequest -Uri "https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity_internals.h" -OutFile $unityInternals
    }
}

$compiler = Get-Compiler -Override $CC
Ensure-Unity

$test = Join-Path $PSScriptRoot 'src/test_array.c'
$src = Join-Path $PSScriptRoot 'src/array.c'
$unityDir = Join-Path $PSScriptRoot 'third_party/unity'
$unityC = Join-Path $unityDir 'unity.c'
$out = Join-Path $PSScriptRoot 'tests.exe'

if ($compiler -eq "cl") {
    & cl $test $src $unityC /nologo /I (Join-Path $PSScriptRoot 'src') /I $unityDir /DUNIT_TEST /Fe:$out
} else {
    & $compiler -std=c11 -I (Join-Path $PSScriptRoot 'src') -I $unityDir -DUNIT_TEST $test $src $unityC -o $out
}

if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Running tests..." -ForegroundColor Cyan
& $out
exit $LASTEXITCODE