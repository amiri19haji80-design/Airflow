Get-ChildItem projects\interactions -Recurse -Include *.yaml,*.yml,*.sql,*.py | Select-String -Pattern '(?<!CAST\(\s*)\bnull\s+as\s+\w+' | ForEach-Object { "{0}:{1}: {2}" -f ($_.Path -replace [regex]::Escape((Get-Location).Path + '\'), ''), $_.LineNumber, $_.Line.Trim() }




Get-ChildItem projects\interactions -Recurse -Include *.yaml,*.yml,*.sql,*.py | Select-String -Pattern '\b(team|client_target_type)\b' | ForEach-Object { "{0}:{1}: {2}" -f ($_.Path -replace [regex]::Escape((Get-Location).Path + '\'), ''), $_.LineNumber, $_.Line.Trim() }
