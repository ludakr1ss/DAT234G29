Write-host "Welcome to the Scytale Cipher decryptor"
Write-host "Enter key"
$key = read-host
Write-host "Enter text"
$text = read-host
$textarray = $text.ToCharArray()
$textlength = [math]::ceiling($textarray.Length / $key)
$limit = $textlength * $key
Write-Host "Would you like to encrypt or decrypt? e/d"
$input = read-host

if ($input -eq "e") {
    for ($index=0;$index -lt $key; $index ++) {
        $index2 = $index
        while ($index2 -lt $textarray.Length) {
            $newText = $newText += $textarray[$index2]
            $index2 += $key
        }
    }
Write-Host "The encrypted phrase is:" $newText
}

elseif ($input -eq "d") {    
	$textarray2 = (1..$limit)
    $incremental = 0
    for ($index=0;$index -lt $key; $index ++) {
        $index2 = $index
        while ($index2 -lt $limit) {
            $textarray2[$incremental] = $index2 ++
            $index2 += $key
            $incremental ++
        }
    }
    $incremental2 = 0
    $incremental3 = 0
    foreach ($value in $textarray2) {
        if ($value -gt $textarray.Length) {
            $textarray2[$incremental2] = ""
        } else {
            $textarray2[$incremental2] = $textarray[$incremental3]
            $incremental3 ++
        }
        $incremental2 ++
    }
    $newText = ""
    for ($index=0;$index -lt $textlength; $index ++) {
        $index2 = $index
        while ($index2 -lt $textarray2.Length) {
            $newText = $newText += $textarray2[$index2]
            $index2 += $textlength
        }
    }
Write-Host "The decrypted phrase is:" $newText
}
pause
