
#$hello ="Hello, Powershell!"
#write-host($Hello)
function getIP {
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}

write-host(getIP)
$IP = getIP
Write-Host("This machines IP is $IP")
Write-Host("This machine's IP is {0}" -f $IP)