# Password Profiler

## Description

We intercepted a suspicious file from a system, but instead of the password itself, it only contains its SHA-1 hash. Using OSINT techniques, you are provided with personal details about the target. Your task is to leverage this information to generate a custom password list and recover the original password by matching its hash.

## Solution

Download the user information file, Hash file and program. Keep these files in a single directory.

Use the ```cat``` command to analyze the program
```
#!/usr/bin/env python3
import hashlib

HASH_FILE = "hash.txt"
WORDLIST_FILE = "passwords.txt" # wordlist that was generated using CUPP

def load_hash():
    with open(HASH_FILE, "r") as f:
        return f.read().strip()

def crack_password(target_hash):
    with open(WORDLIST_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for password in f:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == target_hash:
                return password
    return None

if __name__ == "__main__":
    target_hash = load_hash()
    result = crack_password(target_hash)
    if result:
        print(f"Password found: picoCTF{{{result}}}")
    else:
        print("No match found.")
```
From the analysis we can understand that the wordlist for finding the password can be generated using ```cupp```, A tool used for wordlist genreation based on information given to it. Since we have the personal details of the target.
Run the cupp tool in interactive mode ```cupp -i``` to make the tool ask each detail, enter the detail according to information available (skip the question by pressing enter if info is not there) 
Rename the wordlist file according to the name of the file in the program or change the name of the file in the program. Either way will work and run the program
