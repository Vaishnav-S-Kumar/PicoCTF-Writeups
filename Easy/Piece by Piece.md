# Piece by Piece 

## Description
After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag. SSH to dolphin-cove.picoctf.net:52762 and login as ctf-player with password f3b61b38.

## Solution

Connect to the machine using ssh and after connection use ```pwd``` to find directory name and ```ls``` to list the files in the directory 

```
instructions.txt  part_aa  part_ab  part_ac  part_ad  part_ae
```
Use the ```cat``` command to read the .txt file 
```
Hint:

- The flag is split into multiple parts as a zipped file.
- Use Linux commands to combine the parts into one file.
- The zip file is password protected. Use this "supersecret" password to extract the zip file.
- After unzipping, check the extracted text file for the flag.

```
We can understand that the zip file has been divided into mulitple parts. To verify if the other files are part of the zip file use the ```file``` command to find the type.

```
part_aa: Zip archive data, at least v1.0 to extract
```
use the command ```cat part_a*><filename>.zip``` to combine all the different parts of the file into one zip file and use the ```unzip``` command to reveal the flag.
