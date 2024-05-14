from random import randint, getrandbits
from inputimeout import inputimeout, TimeoutOccurred
import sys
from sage.all import GF, EllipticCurve
from secret import FLAG, p, q  # p, q = getPrime(216), getPrime(216)


class Cipher:
    def __init__(self, f1, f2):

        self.n, self.e, self.d, self.p, self.q, self.phi = self.generate_RSA(f1, f2)
        self.pubkeyRSA = (self.n, self.e)
        self.privkeyRSA = (self.n, self.e, self.d)
        self.a = 1859222455222432354961839402304617457025699763822756368479687466076795863272625297525458135324114247727454905891338186347057205807330923531685069321490931
        self.b = 6516123103748185536745749027571302148017052394699464696636743842923633499197856542156328966074713977212373717065251052976514616698325800694338943533767257
        self.p = 12653939793938340951529340880278308237078873381654412149569523673031991203304808756133064123631589405198181214892931201236023485755065879619126933995779099
        K = GF(self.p)
        self.E = EllipticCurve(K, (self.a, self.b))
        self.E.set_order(self.n)
        self.size = 300
        while self.size % 3 != 0:
            self.size += 1
        self.privkeyECC = []
        self.privperm = [i for i in range(self.size)]
        self.privinvperm = [i for i in range(self.size)]
        self.pubkeyECC = []

    def generate_RSA(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        while True:
            try:
                e = randint(0, int(n**0.1))
                d = pow(e, -1,  phi)
                break
            except:
                pass

        return n, d, e, p, q, phi

    def sign_RSA(self, m):
        assert 0 < m < self.n
        return pow(m, self.d, self.n)

    def read_signature_RSA(self, c):
        assert 1 < c < self.n
        return pow(c, self.e, self.n)

    def is_on_curve(self, x, y):
        return self.E.is_on_curve(x, y)

    def lift_x(self, x):
        return self.E.lift_x(x)

    def random_permutation(self, n):
        l = [i for i in range(n)]
        perm = []
        for i in range(n):
            r = randint(0, n - 1 - i)
            a = l.pop(r)
            perm.append(a)
        return perm

    def inv_perm(self, perm):
        n = len(perm)
        inv_perm = [0 for _ in range(n)]
        for i in range(n):
            inv_perm[perm[i]] = i
        return inv_perm

    def gen_keys_ECC(self, seed):
        privkey = [... for _ in range(self.size)]
        sum = seed[0] + seed[1] + seed[2]
        for i in range(0, self.size - 3, 3):
            A, B = self.E.random_point(), self.E.random_point()
            C = sum - A - B
            privkey[i] = A
            privkey[i + 1] = B
            privkey[i + 2] = C
        privkey[-3] = seed[0]
        privkey[-2] = seed[1]

        privkey[-1] = seed[2]

        perm = self.random_permutation(self.size - 1) + [self.size - 1]
        while perm[-2] <= 2 * self.size // 3 or perm[-3] <= 2 * self.size // 3:
            perm = self.random_permutation(self.size - 1) + [self.size - 1]

        inv_perm = self.inv_perm(perm)
        pubkey = [... for _ in range(self.size)]
        k = randint(0, self.n - 1)
        for i in range(self.size - 3):
            pubkey[perm[i]] = k * privkey[i]
        pubkey[perm[-3]] = k * privkey[-3] + self.E.random_point()
        pubkey[perm[-2]] = k * privkey[-2] + self.E.random_point()
        pubkey[-1] = k * privkey[-1] + self.E.random_point()
        self.privkeyECC = privkey
        self.pubkeyECC = pubkey
        self.privperm = perm
        self.privinvperm = inv_perm

    def k_pubkey(self, k, alea=False):
        j = randint(0, (2 * self.size // 3) - 1)
        R = self.E.random_point()
        k_pub = [... for _ in range(self.size)]
        for i in range(self.size):
            if i == j and alea:
                k_pub[i] = ((k * self.pubkeyECC[i]) + R)
            else:
                k_pub[i] = (k * self.pubkeyECC[i])
        return k_pub

    def encrypt_ECC(self, m):
        b = bin(m)[2:]
        while len(b) % 8 != 0:
            b = "0" + b
        ct = []
        for c in b:
            if c == '0':
                k = randint(0, self.n - 1)
                k_pub = self.k_pubkey(k, alea=False)
                ct.append(k_pub)
            elif c == '1':
                k = randint(0, self.n - 1)
                k_pub = self.k_pubkey(k, alea=True)
                ct.append(k_pub)
            else:
                print("Error")
                sys.exit(1)
        return ct

    def decrypt_ECC(self, ct):
        pt = ""
        for point_set in ct:
            inv_perm_point_set = [... for _ in range(self.size)]
            for i in range(self.size):
                inv_perm_point_set[i] = point_set[self.privperm[i]]
            S = set()
            for i in range(0, self.size, 3):
                P = inv_perm_point_set[i] + inv_perm_point_set[i + 1] + inv_perm_point_set[i + 2]
                S.add(P)
            if len(S) == 2:
                pt += "0"
            elif len(S) == 3:
                pt += "1"
            else:
                print(S)
                print("Error in decryption")
                return 0
        return int(pt, 2)

def challenge():

    C = Cipher(p, q)

    print(f"Parameters of the curve:\na={hex(C.a)}\nb={hex(C.b)}\np={hex(C.p)}")
    print(f"Please provide the seed for the public key you want to use signed with this RSA key:\nn={hex(C.n)}\ne={hex(C.e)}")
    x = int(input("First point x:"))
    y = int(input("First point y:"))
    x = C.read_signature_RSA(x)
    y = C.read_signature_RSA(y)
    if not C.is_on_curve(x, y):
        print("You thought you could get away with that??")
        sys.exit(1)
    P1 = C.E(x, y)
    x = int(input("Second point x:"))
    y = int(input("Second point y:"))
    x = C.read_signature_RSA(x)
    y = C.read_signature_RSA(y)
    if not C.is_on_curve(x, y):
        print("You thought you could get away with that??")
        sys.exit(1)
    P2 = C.E(x, y)
    x = int(input("Third point x:"))
    y = int(input("Third point y:"))
    x = C.read_signature_RSA(x)
    y = C.read_signature_RSA(y)
    if not C.is_on_curve(x, y):
        print("You thought you could get away with that??")
        sys.exit(1)
    P3 = C.E(x, y)
    seed = (P1, P2, P3)
    print("Generating public key, please be patient")
    C.gen_keys_ECC(seed)
    print("ECC key generated")
    print("Encrypting the test, please be patient")
    test = getrandbits(48)
    ct = C.encrypt_ECC(test)

    print(C.pubkeyECC)
    print("Decrypt this to get access to the reserved part:")
    print(ct)
    try:
        inp = int(inputimeout("Your guess: ", timeout=60))
    except TimeoutOccurred:
        print("Our time is running out!")
        sys.exit(1)
    if inp == test:
        print(f"Welcome back. {FLAG}")
    else:
        print("What? No!")
        sys.exit(1)


if __name__ == '__main__':
    challenge()

