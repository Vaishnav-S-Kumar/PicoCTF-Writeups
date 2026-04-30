# Easy1

## Description

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

## Solution

Download the table using the hyperlink provided in the challenge. 
A one-time pad (OTP) is a mathematically unbreakable encryption technique. It requires the use of a single-use pre-shared key (Shared Secret) that is larger than or equal to the size of the message being sent.

### Encryption Technique 
Plaintext is paired wth a random secret key (OTP). Then, each character of the plaintext is encrypted by combining it with the corresponding bit or character from the pad using modular addition. 

In simpler words, Consider "hello" as plaintext and "ghinw" as key;
```
        7(h)  4(e)  11(l)  11(l)  14(o) [CIPHERTEXT]
     +  6(g)  7(h)   8(i)  13(n)  22(w) [KEY]
        ------------------------------        
        13    11    19     24     36   
  
mod(26) 13(n) 11(l) 19(t)  24(y)  10(k)
```

To reverse encryption, subtract the value of key from ciphertext. Thus meaning if the key is known the encryption can be broken.

For this challenge, the key as well the ciphertext is given. To solve there is multiple ways. 

1. use Dcode.fr and select vigenere-cipher and enter key in key form and cipher text in the ciphertext form and run decrypt.
2. Use the table provided and use the first row (letters used for categorising columns) as key and track each cipher text character according to the key character. 
 i.e If first letter of key is I and ciphertext is B, find the row in the coloumn I where B is mentioned and replace it with the character specifying the row(first column)
3. Using modular subtraction to get the value and eventually the plaintext. 
