$alphabet = ""
$alphabet = [char[]](65..90)


Write-host "Welcome to the Scytale Cipher decryptor"
Write-host "The program has some bugs, please use "https://www.dcode.fr/scytale-cipher" to test with correct format"
Write-host "Enter key"
$key = 0
$key = read-host
Write-host "Enter text for decryption"
$text = read-host
$textlength = $text.length #Errors will occur because the length counts all characters, not only letters to be decrypted
$decryptionkey1 = $textlength / $key
$decryptionkey2 = $decryptionkey1
$index = $decryptionkey1
$start = 0
$firstletter = 0..($alphabet.count + 1) | Where {$alphabet[$_] -eq $text[$start]}
$decodedphrase = $alphabet[$firstletter]
$counter = 0

While ($decodedphrase.length -lt $textlength)
            {
			    If ($textlength -le $index) {
				$counter ++
				$index = ($index - $index) + $counter
				}     
				
				$CurrentLetter = 0..($alphabet.count + 1) | Where {$alphabet[$_] -eq $text[$index]}				
				$decodedphrase = $decodedphrase+$alphabet[$CurrentLetter]
				$index = $index + $decryptionkey2
            }
		Write-host "Mostly decoded phrase:" $decodedphrase

pause
