## DAT234G29(temp name)

### Mandatory assignment 1

The file pingiprange.sh is the script for mandatory assignment 1!


### Mandatory assignment 2
#### 1)
File: CaesarCipher.ps1

How to use Caesar Cipher: 

CaesarCipher 'your text here' key(1-26)

If you want to decode write: CaesarCipher 'Text to decode' key(13) -Decode

![Picture](E:\Skole\IT\DAT234\CSmdecode.png)

Alternative file: CeaserCipherAlternate.ps1

How to use:
Open script, choose to encrypt or decrypt by typing e/d

Choose to encrypt/decrypt using specific key by typing y/n (Typing n will result in the script encrypting or decrypting in all keys ranging from 1-25.)

Enter phrase to be decrypted/encrypted.

#### 2)
File: ScytaleCipher.ps1

This script only allows you to decrypt a message, encryption not implemented.

+How to use Scytale Cipher:
Step 1. Open script in PowerShell
Step 2. Enter key
Step 3. Enter phrase to be decrypted

The "PSOHWEELRL" phrase from the assignment is decrypted into "POWERSHELL".

#### 3) 
File: ipsubnet.ps1

Ipsubnet.ps1 pings all IP's within the specific subnet, and prints out the IP's which are in use in the terminal. Default in this script it pings CIDR 192.168.0.15/24. A visual progress bar is also added to see the progress made with pinging the subnet.
