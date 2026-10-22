$cf = Get-ChildItem projects\interactions -Recurse -Include contact_coverage_with_refog.sql
$re3 = '(?<!CAST\(\s*)\bNULL(\s+AS\s+''[^'']+'')'
Select-String -Path $cf.FullName -Pattern $re3 | ForEach-Object { "{0}: {1}" -f $_.LineNumber, $_.Line.Trim() }



$t = [IO.File]::ReadAllText($cf.FullName); $n = [regex]::Replace($t, $re3, 'CAST(NULL AS STRING)$1', 'IgnoreCase'); if ($n -ne $t) { [IO.File]::WriteAllText($cf.FullName, $n); "fixed: $($cf.Name)" }
git diff --stat



