# StegoRSA

## Description

A message has been encrypted using RSA. The public key is gone… but someone might have been careless with the private key. Can you recover it and decrypt the message?

## Solution

Download the Flag file and image file. the flag file is encrypted (So no use for now). check the image file (it is just a image of a key), Try to look into its metadata by using exiftool. 
```
exiftool <filename>
```
There is a very large line of character under the comment section, copy the that and paste it in cyberchef.io. It automatically detects it is Hex, use the hex option and convert it back to it orginal. The orginal form is a key copy it and save as file. Since it is already mentioned it used RSA for encryption, use ```openssl``` which is a widely used, open-source software library and toolkit that implements cryptographic functions and the SSL/TLS protocols to secure communications over computer networks. 
```
openssl pkeyutl -decrypt -inkey <key-file> -in <encrypted-file> -out decrypted_file.txt
```
The flag is stored in the decrypted_file.txt

