# Connaître ses tables 1/2

**Category** : sca-faults
**Points** : 449

Benoît Blanc pense avoir réussi à cacher sa clef AES dans des tables.

Il vous fournit le code écrit en C permettant de les utiliser, par exemple :

```sh
$ make
$ ./wb-aes keys.bin < /dev/zero
f34789150f962bdcc56e8c585451f34d
```

Il a chiffré le flag à l'aide du SHA256 de cette clef (voir `output.txt`) :

```py
def encrypt(k, flag):
    import hashlib
    from Crypto.Cipher import AES
    hk = hashlib.sha256(k).digest()
    E = AES.new(hk, AES.MODE_GCM)
    iv = E.nonce
    c = E.encrypt(flag)
    return {"c": c.hex(), "iv": iv.hex()}
```

## Files : 
 - [connaitre-ses-tables-easy.tar.xz](./connaitre-ses-tables-easy.tar.xz)


