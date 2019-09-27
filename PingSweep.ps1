Write-Host "Enter IP and mask to ping in a *.*.*.*/24 format. We're just pinging 254 addresses today!"

$ipmask = read-host
$ip, $mask =  $ipmask.Split('/')
$ipbase = $ip.Remove($ip.LastIndexOf('.'))+"."

if ($mask -eq 24) {$iprange = (1..254 | % {$ipbase+$_})}
else {write-host Input error! Try again
pause
exit
}

foreach ($ip in $iprange) 
{
Test-Connection -ipaddres $ip -Count 2 -ErrorAction SilentlyContinue -ErrorVariable ProcessError;
If ($ProcessError) { Write-Host "No connection at" $ip}
}

Write-Host "Ping sweep over"
pause
