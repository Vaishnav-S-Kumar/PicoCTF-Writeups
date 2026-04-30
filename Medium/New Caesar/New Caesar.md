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
### string
The string module is a built-in module with predefined constants and helper functions. (.lower(), .digits(), etc)
### ord()
The ord function returns the unicode (ASCII) integer value of the character. Opposite of ord is chr which provides the orginal alphabet if the unicode (ASCII) integer value is given.
```
>>>ord("a")
97
>>>chr(97)
'a'
```
 
### Assert() 
The assert function is a debugging aid to test whether the condition is true, if true program continues. If false, it raises an ```AssertionError```.  [ Extra feature : Custom error message can be added ]

The asset all function is to ensure every single item in a collection meets certain condition (used in iteration) 
