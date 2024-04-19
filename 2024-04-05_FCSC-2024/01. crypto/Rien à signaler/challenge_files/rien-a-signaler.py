import json
from Crypto.Util.number import getPrime, bytes_to_long

def keygen(n = 1024):
	p = getPrime(n)
	q = getPrime(n)
	n = p * q
	e = 2 ** 16 + 1
	d = pow(e, -1, (p - 1) * (q - 1))
	sk = (d, n)
	pk = (e, n)
	return pk, sk

# Read the flag as an integer
m = bytes_to_long(open("flag.txt", "rb").read())

# Generate RSA keys
sk, pk = keygen()

# Encrypt the flag
c = pow(m, pk[0], pk[1])

# Output public key and ciphertext
d = {
	"e": pk[0],
	"n": pk[1],
	"c": c,
}
print(json.dumps(d, indent = 4))
