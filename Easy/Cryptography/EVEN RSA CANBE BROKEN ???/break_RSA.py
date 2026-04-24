import gmpy2
from Crypto.Util.number import long_to_bytes

N = <value>
e = <value>
c = <value>

# Try e-th root
m, exact = gmpy2.iroot(c, e)

if exact:
    print("Recovered flag:", long_to_bytes(m).decode())
else:
    print("Not vulnerable to small message attack")
