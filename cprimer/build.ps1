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

$compiler = Get-Compiler -Override $CC
$src = Join-Path $PSScriptRoot 'src/array.c'
$out = Join-Path $PSScriptRoot 'array.exe'

if ($compiler -eq "cl") {
    & cl $src /nologo /I (Join-Path $PSScriptRoot 'src') /Fe:$out
} else {
    & $compiler -std=c11 -I (Join-Path $PSScriptRoot 'src') $src -o $out
}

if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Built $out successfully." -ForegroundColor Green