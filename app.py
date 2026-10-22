$f = @(Get-Item projects\interactions\sql\crm_ce\fact_event.sql) + @(Get-ChildItem projects\interactions -Recurse -Include fact_union_*_participants.sql, contact_coverage_with_refog.sql)
$re = '(?<!CAST\(\s*)(?<!IS\s+)(?<!NOT\s+)\bNULL(\s+(?:AS\s+)?(?!(?:END|AND|OR|THEN|ELSE|WHEN|FROM)\b)[A-Za-z_]\w*\s*(,|$))'
$f | Select-String -Pattern $re | ForEach-Object { "{0}:{1}: {2}" -f $_.Filename, $_.LineNumber, $_.Line.Trim() }



foreach ($x in $f) { $t = [IO.File]::ReadAllText($x.FullName); $n = [regex]::Replace($t, $re, 'CAST(NULL AS STRING)$1', 'IgnoreCase,Multiline'); if ($n -ne $t) { [IO.File]::WriteAllText($x.FullName, $n); "fixed: $($x.Name)" } }
git diff --stat
