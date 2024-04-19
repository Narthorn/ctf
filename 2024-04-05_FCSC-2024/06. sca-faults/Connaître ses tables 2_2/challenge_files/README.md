# Connaître ses tables 2/2

**Category** : sca-faults
**Points** : 482

Benoît Blanc pense avoir réussi à cacher sa clef AES dans des tables.

Il vous fournit le code écrit en C permettant de les utiliser, par exemple :

```sh
$ make
$ ./wb-aes keys.bin < /dev/zero
1115bc2ca69914a002871719c9cba93b
```

De plus, une table pour la clef suivante est fournie dans le fichier `key-public.bin`:
```
8e 73 b0 f7 da 0e 64 52 c8 10 f3 2b
80 90 79 e5 62 f8 ea d2 52 2c 6b 7b
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
 - [connaitre-ses-tables-medium.tar.xz](./connaitre-ses-tables-medium.tar.xz)


