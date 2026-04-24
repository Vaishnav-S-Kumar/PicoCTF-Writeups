# Shared Secrets

## Description

A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag?

## Solution

Download the encryption algoritham and the message, After analysis of the program, It used for performing Diffie-Hellman encryption, which is an algorithm to create a shared, secret key over an insecure channel like internet. For example: 
```
- Alice & Bob agrees on two public, non secret number p (prime number) and g (Generator)
- Alice → a & Bob → b (Secret Key)
- Public Value for Alice → g^a(mod p) and Bob → g^b(mod p)
- Alice sends A to Bob and Bob send B to Alice
- Alice and Bob generate shared secret using S= B^a(mod p) and S= A^b(mod p) respectively
- Shared secret can now be used for encryption and decryption of communication
```

To break this algorithm atleast one secret key should be known, here the message file contains that secret key. So instead of writing a code myself, I used AI to write a counter program when one of the secret is known by which the flag will be revealed. After initializing the values of the variable run the program.

