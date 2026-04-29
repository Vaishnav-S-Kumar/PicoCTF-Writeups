# Verify

## Description

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

## Solution

Launch the instance and connect to the machine using ssh. After launching instances additional details are given:
1. The checksum of the file containing the flag.
2. There is bash program to decrypt the flag file since it is encrypted.
3. The file is inside a directory called file.

The file contatining the checksum is also present alongside the decrypt program.

As described in the description, there is a lot of files with fake flag added to the files directory, the file with the orginal flag has the given SHA-256 hash. Therefore, to find this we can use the following command:
```
sha256sum files/* | grep <checksum>
```
This command provides the name of the file with the same SHA-256 hash. 

Now using the decrypt program, decrypt the file to get the flag 
```
./<program> <filename>
```

