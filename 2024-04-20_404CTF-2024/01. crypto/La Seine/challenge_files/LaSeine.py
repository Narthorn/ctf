from Crypto.Util.number import *
import os
from secret import flag

class LaSeine:
    def __init__(self, size):
        self.l = 20
        self.p = getStrongPrime(size)

        self.a = getRandomNBitInteger(size // 16)
        self.b = getRandomNBitInteger(size // 16)

    def split(self, f):
        if len(f) & 1:
            f += b"\x00"
        h = len(f) // 2
        return (bytes_to_long(f[:h]), bytes_to_long(f[h:]))

    def sign(self, m, b):
        xn, yn = self.split(m)
        k = (getRandomNBitInteger(self.l - 1) << 1) + b

        for _ in range(k):
            xnp1 = (self.a*xn + self.b*yn) % self.p
            ynp1 = (self.b*xn - self.a*yn) % self.p

            xn, yn = xnp1, ynp1
        return (k, xn, yn)

seine = LaSeine(1024)

_, xf, yf = seine.sign(flag, 1)
s2 = seine.sign(b"L'eau est vraiment froide par ici (et pas tres propre)", 0)

f = open("out.txt", "w")

f.write(str(seine.p) + "\n")
f.write(str((xf, yf)) + "\n")
f.write(str(s2))

f.close()