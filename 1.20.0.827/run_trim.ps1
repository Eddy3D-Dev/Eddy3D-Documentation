function ProcessFiles {
    param(
        [string]$folderPath
    )

    $skipPatterns = @('paper*.pdf', 'sub*.pdf')
    
    # Process the files in the current folder
    $files = Get-ChildItem -Path $folderPath -File
    foreach ($file in $files) {
        if ($file.Extension -match '\.(pdf|jpg|png)$') {
            $srcFile = $file

            # Skip files that match patterns in $skipPatterns
            $skipThisFile = $false
            foreach ($pattern in $skipPatterns) {
                if ($srcFile.Name -like $pattern) {
                    $skipThisFile = $true
                    break
                }
            }

            if ($skipThisFile) {
                Write-Host ("Skipping file: " + $srcFile.FullName + " (matches skip pattern)")
                continue
            }

            $cropFile = if ($srcFile.BaseName -like "*-crop") {
                           Join-Path $srcFile.DirectoryName ($srcFile.BaseName + $srcFile.Extension)
                       } else {
                           Join-Path $srcFile.DirectoryName ($srcFile.BaseName + "-crop" + $srcFile.Extension)
                       }

            if ((-not (Test-Path $cropFile)) -or ((Test-Path $cropFile) -and ($srcFile.LastWriteTime -gt (Get-Item $cropFile).LastWriteTime))) {
                Write-Host ("Processing file: " + $srcFile.FullName)
                switch ($srcFile.Extension) {
                    ".pdf" {
                        # your pdfcrop command here
                        pdfcrop $srcFile.FullName $cropFile
                    }
                    ".jpg" {
                        # your imagemagick command here
                        magick $srcFile.FullName -trim $cropFile
                    }
                    ".png" {
                        # your imagemagick command here
                        magick $srcFile.FullName -trim $cropFile
                    }
                }
            } else {
                # Omitted the Write-Host statement that indicates the crop file is up-to-date
            }
        }
    }
    
    # Recursively go through each subfolder
    $subfolders = Get-ChildItem -Path $folderPath -Directory
    foreach ($subfolder in $subfolders) {
        ProcessFiles -folderPath $subfolder.FullName
    }
}

# Start the processing from the current directory
ProcessFiles -folderPath "."
