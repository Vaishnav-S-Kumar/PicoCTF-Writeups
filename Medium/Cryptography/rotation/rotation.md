# Rotation

## Description

You will find the flag after decrypting the file

## Solution 

Download the file and start analysing the pattern. We know that the flag is starts with "picoCTF" therefore cross reference the starting words in the file and find the character rotation pattern. Instead of a normal rotation, the charcters are swapped in a reverse order. Thus the command should be
```
cat <file-name> | tr <pattern> a-zA-Z
```
The flag will be shown as the result.
