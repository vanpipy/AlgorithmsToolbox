# Removes build artifacts and Unity sources fetched for tests

$root = $PSScriptRoot
$files = @(
    (Join-Path $root 'array.exe'),
    (Join-Path $root 'tests.exe'),
    (Join-Path $root 'third_party/unity/unity.c'),
    (Join-Path $root 'third_party/unity/unity.h'),
    (Join-Path $root 'third_party/unity/unity_internals.h')
)

foreach ($f in $files) {
    if (Test-Path $f) {
        try {
            Remove-Item -Force $f
            Write-Host "Removed $f" -ForegroundColor DarkGray
        } catch {
            Write-Host "Failed to remove $f: $_" -ForegroundColor Yellow
        }
    }
}