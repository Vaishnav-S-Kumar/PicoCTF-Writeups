# PW Crack 2

## Description 
Can you crack the password to get the flag?

## Solution

Download the python program and the flag file. Keep both programs within the same folder. 

Analyse the program by using ```cat``` to show the contents of the file.

```
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

After Analysis we can understand that the program asks for a password to reveal the contents of the encrypted file (which has the flag)

The password is deescribed using hexadecimals, use cyberchef or other online tools to convert the hex to ASCII character.

Run the python program and enter the password.

