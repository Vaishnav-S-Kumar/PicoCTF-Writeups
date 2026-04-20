# PW Crack 1

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


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "1e1a"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
```

After Analysing the program, we can understand that the flagg will be shown after running the program and providing the correct password.

THe password is hardcoded into the program, making it easy to find the password. Thus run the program and provide the password.
