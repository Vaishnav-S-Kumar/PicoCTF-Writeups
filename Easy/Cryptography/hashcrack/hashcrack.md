# Hashcrack

## Description
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

## Solution

Launch the instance and connect using netcat/nc. Upon connect, a hash is displayed with a prompt asking the password. Identify the hash using hashid or any online hash identifier tool and copy the hash to a text file. Use john to crack the hash.
``` 
john --wordlist=<wordlist path> --format=<hash format> <filename>
```
Like this instance shall ask 2 more time with different hashes.
