# New Caesar

## Description

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) fegdeogdgecoeocgcgchcfcffccfca

## Solution

Download the python program, which does the new encryption. Analyse the python program and note the key features.
```
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
        enc = ""
        for c in plain:
                binary = "{0:08b}".format(ord(c))
                enc += ALPHABET[int(binary[:4], 2)]
                enc += ALPHABET[int(binary[4:], 2)]
        return enc

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
print(enc)
```
### Analysis 
#### string
The string module is a built-in module with predefined constants and helper functions. (.lower(), .digits(), etc)
#### ord()
The ord function returns the unicode (ASCII) integer value of the character. Opposite of ord is chr which provides the orginal alphabet if the unicode (ASCII) integer value is given.
```
>>>ord("a")
97
>>>chr(97)
'a'
```
### b16_encode(plain)

An user defined function is used for custom base16 encoding, here character limit is the first 16 letters of the alphabet. The first statement in the for loop ```binary = "{0:08b}".format(ord(c))``` converts the ASCII value to binary. 

The statements ```enc += ALPHABET[int(binary[:4], 2)]``` & ```enc += ALPHABET[int(binary[4:], 2)]``` divides the output binary input into two alphabets(2 outputs).

#### shift(c,k) 

Another user defined function to shift cipher. Takes the ASCII value of the variable c and k minuses ASCII value of "a". Returns one of the alphabet within the ALPHABET variable.

#### Assert() 
The assert function is a debugging aid to test whether the condition is true, if true program continues. If false, it raises an ```AssertionError```.  [ Extra feature : Custom error message can be added ]

The asset all function is to ensure every single item in a collection meets certain condition (used in iteration). Here it ensure that the characters in ther key is inside the variable ALPHABET (first 16 alphabets) 

#### Final For-loop
It uses the index value as well as the alphabets in the base`6 function output to create the cipher text. 

### Decryption Program

The weakpoint here is the length of the key,1 which means one of the 16 alphabets is used (only 16 possibiliites), So the flow of the program is
```
Reverse Shift
Base16 Decoding
Orginal Flag
```
The program used:

```
import string

ALPHABET = string.ascii_lowercase[:16]
lOWER = ord('a')  

def reverse_shift(c, k):
    t1 = ord(c) - LOWER
    t2 = ord(k) - LOWER
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def b16_decode(encoded):
    result = ""

    for i in range(0, len(encoded), 2):
        c1 = encoded[i]
        c2 = encoded[i + 1]

        n1 = ALPHABET.index(c1)
        n2 = ALPHABET.index(c2)

        binary = f"{n1:04b}" + f"{n2:04b}"
        result += chr(int(binary, 2))

    return result

enc = "CIPHER_TEXT"

for key in ALPHABET:
    temp = ""
    for c in enc:
        temp += reverse_shift(c, key)

    try:
        decoded = b16_decode(temp)
        print(f"[+] Key: {key} → {decoded}")
    except:
        pass
```
