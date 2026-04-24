# EVEN RSA CAN BE BROKEN ???

## Description

This service provides you an encrypted flag. Can you decrypt it with just N & e?

## Solution

Download the program file and launch the instance. Connect to the instance and instance provides us the value of N, e and ciphertext. Using AI a counter program was created to print the flag using the information we have recieved from the instance. The ciphertext was broken because of bad primes meaning it depends on the difficulty of factoring N = p × q. If we can factor N, we can:

Compute Euler’s Totient:
φ(N) = (p - 1)(q - 1)

Compute private key:
d = e⁻¹ mod φ(N)

Decrypt:
m = c^d mod N

Thus, RSA is only secure if N cannot be factored

Therefore by running the counter program with the values from the instance prints the flag.
