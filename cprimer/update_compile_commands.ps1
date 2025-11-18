param(
    [Parameter(Mandatory = $false)]
    [string] $Directory = (Get-Location).Path,

    [Parameter(Mandatory = $false)]
    [switch] $RelocateFiles,           # Use old 'directory' to relocate absolute 'file' paths into new $Directory

    [Parameter(Mandatory = $false)]
    [switch] $NormalizeCommandPaths,   # Replace old directory substrings in 'command' with new $Directory

    [Parameter(Mandatory = $false)]
    [switch] $RebuildIfMissing,        # If compile_commands.json is missing, rebuild from src/tests

    [Parameter(Mandatory = $false)]
    [string] $Compiler = "gcc",        # Used only when rebuilding

    [Parameter(Mandatory = $false)]
    [string] $Std = "c11",             # Used only when rebuilding

    [Parameter(Mandatory = $false)]
    [string] $Includes = "include"     # Used only when rebuilding
)

$ErrorActionPreference = 'Stop'

function Get-FullPath {
    param([string] $path, [string] $base)
    if ([System.IO.Path]::IsPathRooted($path)) {
        return [System.IO.Path]::GetFullPath($path)
    } else {
        return [System.IO.Path]::GetFullPath((Join-Path $base $path))
    }
}

function Try-Relativize {
    param([string] $base, [string] $absolutePath)
    try {
        $baseUri = [System.Uri](Get-FullPath -path $base -base $base)
        $absUri  = [System.Uri](Get-FullPath -path $absolutePath -base $base)
        if ($absUri.AbsolutePath.StartsWith($baseUri.AbsolutePath)) {
            $rel = $baseUri.MakeRelativeUri($absUri).OriginalString
            return $rel -replace '/', '\'
        }
        return $absolutePath
    } catch {
        return $absolutePath
    }
}

if (-not (Test-Path -Path $Directory -PathType Container)) {
    throw "Directory does not exist: $Directory"
}

$jsonPath = Join-Path $Directory "compile_commands.json"

if (-not (Test-Path -Path $jsonPath -PathType Leaf)) {
    if (-not $RebuildIfMissing) {
        throw "compile_commands.json not found at $jsonPath. Use -RebuildIfMissing to generate a minimal one."
    }

    $includeAbs = Get-FullPath -path $Includes -base $Directory
    $srcDirs = @("src", "tests")
    $files = @()

    foreach ($d in $srcDirs) {
        $p = Join-Path $Directory $d
        if (Test-Path -Path $p -PathType Container) {
            $files += Get-ChildItem -Path $p -Filter *.c -File -Recurse
        }
    }

    $outDir = Join-Path $Directory "build"
    if (-not (Test-Path -Path $outDir -PathType Container)) {
        New-Item -ItemType Directory -Path $outDir | Out-Null
    }

    $entries = @()
    foreach ($f in $files) {
        $objPath = Join-Path $outDir ("{0}.obj" -f $f.BaseName)
        $cmd = "$Compiler -std=$Std -I `"$includeAbs`" -c `"$($f.FullName)`" -o `"$objPath`""
        $entries += [pscustomobject]@{
            directory = $Directory
            command   = $cmd
            file      = $f.FullName
        }
    }

    ($entries | ConvertTo-Json -Depth 10) | Set-Content -Path $jsonPath -Encoding UTF8
    Write-Host "Generated compile_commands.json with $($entries.Count) entries at $jsonPath"
    exit 0
}

# Helpers
function New-CompileEntry {
    param(
        [Parameter(Mandatory = $true)] [string] $filePath,
        [Parameter(Mandatory = $true)] [string] $directory,
        [Parameter(Mandatory = $true)] [string] $compiler,
        [Parameter(Mandatory = $true)] [string] $std,
        [Parameter(Mandatory = $true)] [string] $includeAbs,
        [Parameter(Mandatory = $true)] [string] $outDir
    )
    $objPath = Join-Path $outDir ("{0}.obj" -f [IO.Path]::GetFileNameWithoutExtension($filePath))
    $cmd = "$compiler -std=$std -I `"$includeAbs`" -c `"$filePath`" -o `"$objPath`""
    return [pscustomobject]@{
        directory = $directory
        command   = $cmd
        file      = $filePath
    }
}

# Update existing compile_commands.json
$dataRaw = Get-Content -Path $jsonPath -Raw
try {
    $data = $dataRaw | ConvertFrom-Json
} catch {
    throw "Failed to parse compile_commands.json: $($_.Exception.Message)"
}

# Normalize to array
$entries = @()
if ($data -is [System.Collections.IEnumerable]) {
    $entries = @($data)
} else {
    $entries = @($data)
}

# Prepare include and build output
$includeAbs = Get-FullPath -path $Includes -base $Directory
$outDir = Join-Path $Directory "build"
if (-not (Test-Path -Path $outDir -PathType Container)) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

# Index existing entries by normalized file path
$existingByFile = @{}
foreach ($e in $entries) {
    if ($e.PSObject.Properties['file']) {
        $key = Get-FullPath -path $e.file -base $Directory
        $existingByFile[$key] = $e
    }
}

# Discover all .c files in src and tests
$sourceFiles = @()
foreach ($d in @("src", "tests")) {
    $p = Join-Path $Directory $d
    if (Test-Path -Path $p -PathType Container) {
        $sourceFiles += Get-ChildItem -Path $p -Filter *.c -File -Recurse
    }
}

# Merge: update existing, add missing
$updatedCount = 0
foreach ($f in $sourceFiles) {
    $key = $f.FullName
    if ($existingByFile.ContainsKey($key)) {
        $entry = $existingByFile[$key]
        $dirProp = $entry.PSObject.Properties['directory']
        $oldDir = if ($dirProp) { $dirProp.Value } else { $null }

        # Always update directory
        $entry.directory = $Directory

        # Optionally normalize command paths
        if ($NormalizeCommandPaths -and $entry.PSObject.Properties['command'] -and $oldDir) {
            $cmd = [string]$entry.command
            $variants = @(
                $oldDir,
                ($oldDir -replace '\\', '/'),
                ($oldDir -replace '/', '\\')
            ) | Select-Object -Unique
            foreach ($v in $variants) {
                $cmd = $cmd -replace [Regex]::Escape($v), $Directory
            }
            $entry.command = $cmd
        }

        # If command missing, create a default one
        if (-not $entry.PSObject.Properties['command'] -or -not $entry.command) {
            $default = New-CompileEntry -filePath $key -directory $Directory -compiler $Compiler -std $Std -includeAbs $includeAbs -outDir $outDir
            $entry.command = $default.command
        }

        $updatedCount++
    } else {
        # Add new entry
        $entries += New-CompileEntry -filePath $key -directory $Directory -compiler $Compiler -std $Std -includeAbs $includeAbs -outDir $outDir
        $updatedCount++
    }
}

# Persist
($entries | ConvertTo-Json -Depth 10) | Set-Content -Path $jsonPath -Encoding UTF8
Write-Host "Merged compile_commands.json. Updated/added entries: $updatedCount"
Write-Host "Path: $jsonPath"
Write-Host "Options used: RelocateFiles=$($RelocateFiles.IsPresent), NormalizeCommandPaths=$($NormalizeCommandPaths.IsPresent)"