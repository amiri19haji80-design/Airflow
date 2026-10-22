$cf = Get-ChildItem projects\interactions -Recurse -Include contact_coverage_with_refog.sql
$re3 = '(?<!CAST\(\s*)\bNULL(\s+AS\s+''[^'']+'')'
Select-String -Path $cf.FullName -Pattern $re3 | ForEach-Object { "{0}: {1}" -f $_.LineNumber, $_.Line.Trim() }
