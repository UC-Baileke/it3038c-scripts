
#$hello ="Hello, Powershell!"
#write-host($Hello)
function getIP {
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}

write-host(getIP)
$todaysdate = Get-Date
$hostversion = $host.Version.major
$IP = getIP
$Date = ""
$Body = "This machines's IP is $IP. User is $env:username. Hostname is $env:computername. Powershell Version is $hostversion. Today's date is $todaysdate"

write-host($body)

#send-MailMessage -To "Baileke@ucmail.uc.edu" -From "Baileycru34@gmail.com" -Subject "IT3038c Windows SysInfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)