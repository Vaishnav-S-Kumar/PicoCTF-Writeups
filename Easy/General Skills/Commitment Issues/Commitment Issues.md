# Commitment Issues

## Description 
I accidentally wrote the flag down. Good thing I deleted it!

## Solution

Download the file.

After unzipping the file, view the txt file.

Use git log to track the changes which has happend to the file, it would be like
```
commit <Hash>        (HEAD -> branch)
Author: user <user@example.com>
Date:   Sat Mar 9 21:09:45 2024 +0000

    Message
```
Use the hash of the commit which is appropriate (the message part reveals what each commit is about) and use ```git checkout <hash>``` to temporarily view the repository at a specific commit.


