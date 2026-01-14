# scan-suspicious-files.ps1
$suspiciousExtensions = @(".exe", ".dll", ".vbs")
$searchPaths = @("C:\Users\Public", "C:\Windows\Temp")
foreach ($ext in $suspiciousExtensions) {
foreach ($path in $searchPaths) {
Get-ChildItem -Path $path -Recurse -Include "*$ext" -ErrorAction SilentlyContinue | ForEach-Object {
Write-Host "Suspicious file found: $($_.FullName)" -ForegroundColor Red
}
}
}