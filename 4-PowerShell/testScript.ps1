# Use Write-Host for displaying information directly to the console in a specific color
Write-Host "--- Starting Test Script Execution ---" -ForegroundColor Cyan

# Use Write-Output (or its built-in alias 'echo' or even just the value itself) to send data to the success output stream (the pipeline)
Write-Output "This is standard output from Write-Output."

# Display current date and time
$currentDate = Get-Date
"Current System Date and Time: $currentDate"

# Display basic computer information
Write-Host "`nGetting system information..." -ForegroundColor Green
Get-ComputerInfo | Select-Object OSName, OSVersion, OSLastBootupTime

# Display an important message in yellow
Write-Host "`nWarning: This is a sample warning message." -ForegroundColor Yellow -BackgroundColor Black

# Get a list of the top 5 running processes and output them
Write-Host "`nListing top 5 CPU-intensive processes:" -ForegroundColor Green
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Name, Id, CPU

# Test a network connection (example: Google's website)
Write-Host "`nTesting network connection to google.com..." -ForegroundColor Green
Test-NetConnection -ComputerName "google.com" -Port 80

# Use Write-Error to send a message to the error stream
# This can be useful for testing how your monitoring tools handle errors
# Write-Error "This is a simulated error for testing purposes."

Write-Host "`n--- Test Script Finished ---" -ForegroundColor Cyan
