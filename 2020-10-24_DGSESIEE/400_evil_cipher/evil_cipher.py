#!/usr/bin/python3

BLOCK_SIZE = 45

def mask(bits): return (1 << bits) - 1

def left_rotate(key, bits):   return ((key << 1) | (key >> (bits-1))) & mask(bits)
def right_rotate(key, bits):  return ((key >> 1) | (key << (bits-1))) & mask(bits)

def key_expansion_round(key):
    if (key & (1 << 63)): key ^= (1 << 8) | (1 << 33) | (1 << 60)
    key = left_rotate(key, 64)
    return key

def permutation15_crypt(a):
    b = 0
    b |= ((a >>  7) & 1) <<  0
    b |= ((a >>  3) & 1) <<  1
    b |= ((a >> 13) & 1) <<  2
    b |= ((a >>  8) & 1) <<  3
    b |= ((a >> 12) & 1) <<  4
    b |= ((a >> 10) & 1) <<  5
    b |= ((a >>  2) & 1) <<  6
    b |= ((a >>  5) & 1) <<  7
    b |= ((a >>  0) & 1) <<  8
    b |= ((a >> 14) & 1) <<  9
    b |= ((a >> 11) & 1) << 10
    b |= ((a >>  9) & 1) << 11
    b |= ((a >>  1) & 1) << 12
    b |= ((a >>  4) & 1) << 13
    b |= ((a >>  6) & 1) << 14
    return b

def permutation15_decrypt(b):
    a = 0
    a |= ((b >>  8) & 1) <<  0
    a |= ((b >> 12) & 1) <<  1
    a |= ((b >>  6) & 1) <<  2
    a |= ((b >>  1) & 1) <<  3
    a |= ((b >> 13) & 1) <<  4
    a |= ((b >>  7) & 1) <<  5
    a |= ((b >> 14) & 1) <<  6
    a |= ((b >>  0) & 1) <<  7
    a |= ((b >>  3) & 1) <<  8
    a |= ((b >> 11) & 1) <<  9
    a |= ((b >>  5) & 1) << 10
    a |= ((b >> 10) & 1) << 11
    a |= ((b >>  4) & 1) << 12
    a |= ((b >>  2) & 1) << 13
    a |= ((b >>  9) & 1) << 14
    return a

def permutation_crypt(a):
    b = 0
    b |= permutation15_crypt((a >> 15) & mask(15)) <<  0
    b |= permutation15_crypt((a >> 30) & mask(15)) << 15
    b |= permutation15_crypt((a >>  0) & mask(15)) << 30
    return b

def permutation_decrypt(b):
    a = 0
    a |= permutation15_decrypt((b >> 30) & mask(15)) <<  0
    a |= permutation15_decrypt((b >>  0) & mask(15)) << 15
    a |= permutation15_decrypt((b >> 15) & mask(15)) << 30
    return a

def galois_inverse(x): 
    # inverse: x^(2^32 - 2) 
    # ugh
    i = 1
    for _ in range(30): i = galois_multiplication(i,x)
    return i

def galois_multiplication(a,b): 
    p = 0
    while (a and b):
        if (b & 1): p ^= a
        a <<= 1
        b >>= 1
        if (a & 32): a ^= 0b100101 # X^5 + X^2 + 1

    return p

def encrypt_round(p, key):
    p = permutation_crypt(p)
    tmp = 0
    
    for i in range(9): tmp |= galois_inverse((p >> 5*i) & mask(5)) << 5*i

    tmp ^= key

    c = 0
    for i in range(3):
        c |= (
              ((tmp >> 15*i  ) & mask(5))
            ^ ((tmp >> 15*i+5) & mask(5))
            ^ galois_multiplication((tmp >> 15*i+10) & mask(5), 0b00010)
        ) << 15*i

        c |= (
              ((tmp >> 15*i   ) & mask(5))
            ^ galois_multiplication((tmp >> 15*i+ 5) & mask(5), 0b00010)
            ^ ((tmp >> 15*i+10) & mask(5))
        ) << 15*i+5

        c |= (
              galois_multiplication((tmp >> 15*i   ) & mask(5), 0b00010)
            ^ ((tmp >> 15*i+ 5) & mask(5))
            ^ ((tmp >> 15*i+10) & mask(5))
        ) << 15*i+10

    return c

def decrypt_round(c, key):

    g = 0b00010
    h = galois_inverse(galois_multiplication(g,g^1))

    tmp = 0
    for i in range(3):
        tmp |= galois_multiplication(h,  (c >> 15*i   ) & mask(5)
                                       ^ (c >> 15*i+ 5) & mask(5)
                                       ^ galois_multiplication(g^1, (c >> 15*i+10) & mask(5))
        ) << 15*i 

        tmp |= galois_multiplication(h,  (c >> 15*i   ) & mask(5)
                                       ^ galois_multiplication(g^1, (c >> 15*i+ 5) & mask(5))
                                       ^ (c >> 15*i+10) & mask(5)
        ) << 15*i+5


        tmp |= galois_multiplication(h, galois_multiplication(g^1, (c >> 15*i   ) & mask(5))
                                       ^ (c >> 15*i+ 5) & mask(5)
                                       ^ (c >> 15*i+10) & mask(5)
        ) << 15*i+10

    tmp ^= key

    p = 0
    for i in range(9): p |= galois_inverse((tmp >> 5*i) & mask(5)) << 5*i
    
    return permutation_decrypt(p)


def evil_cipher(block, key, mode='encrypt'):

    keys = [key]
    for i in range(5):
        keys.append(key_expansion_round(keys[i]))

    if (mode == 'encrypt'):
        do_one_round = encrypt_round
        idle_tick = 0
    else:   
        do_one_round = decrypt_round
        idle_tick = 5
        keys = keys[::-1]

    out = block & mask(BLOCK_SIZE)
    for i in range(6):
        rkey = keys[i]
        if (i == idle_tick): out ^= rkey & mask(BLOCK_SIZE)
        else:                out = do_one_round(out, rkey & mask(BLOCK_SIZE))

    return out

def encrypt(block, key): return evil_cipher(block, key, mode='encrypt')
def decrypt(block, key): return evil_cipher(block, key, mode='decrypt')

#ughhh
def flip(x,bits): return int(f'{x:0{bits}b}'[::-1],2)


key = 0x4447534553494545

def test():
    plain = b'evil'
    expected = 0b000101110010110001110101010111010101001010100
    block = int.from_bytes(plain, byteorder="big") << (BLOCK_SIZE - ((len(plain)*8) % BLOCK_SIZE))
    key = 0x4447534553494545
    #block = flip(block, BLOCK_SIZE)
    #key = flip(key, 64)

    crypted = encrypt(block, key)
    #crypted = flip(crypted, BLOCK_SIZE)

    #for i in range(32):
    #    inv = galois_inverse(i)
    #    print(f'galois inverse of {i:02} (0b{i:05b}): {inv:02} (0b{inv:05b})', end='')
    #    print(f'   {i:02} * {inv:02} = {galois_multiplication(i,inv):02}')

    print(f"plain:     {block:0{BLOCK_SIZE}b}")
    print(f"crypted:   {crypted:0{BLOCK_SIZE}b}")
    print(f"expected:  {expected:0{BLOCK_SIZE}b}")
    assert(crypted == expected)

    decrypted = decrypt(crypted, key)

    print(f"decrypted: {decrypted:0{BLOCK_SIZE}b}")
    assert(decrypted == block)

if (__name__ == "__main__"):

    from sys import argv
    if (len(argv) < 2): 
        test()
    else:
        crypted = argv[1]
        decrypted = ''
        for i in range(len(crypted) // BLOCK_SIZE):
            block = int(crypted[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE],2)
            decrypted += f'{decrypt(block, key):0{BLOCK_SIZE}b}'

        print(f"decrypted: {decrypted}")

        nbytes = len(decrypted) // 8 
        dec = int(decrypted[:nbytes*8],2).to_bytes(nbytes,byteorder='big')
        print(dec)
