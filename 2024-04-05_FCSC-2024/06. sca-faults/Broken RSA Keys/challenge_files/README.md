# Broken RSA Keys

**Category** : sca-faults
**Points** : 500

On vous demande s'il est possible de se prémunir d'une attaque par faute contre un RSA-CRT en corrigeant d'éventuelles erreurs.
Afin de tester votre méthode pour corriger les erreurs, on vous fournit un échantillon de clefs erronées à corriger générées par un matériel défectueux.
Il est demandé de faire ces corrections sans connaître les clefs publiques associées.
On précise toutefois que l'exposant public fait toujours moins de 100 bits, que `p` et `q` ont des tailles similaires et que l'on utilise les notations usuelles : `p`, `q`, `dp`, `dq`, `iq`.

Parmi les fichiers fournis, `output.txt` contient 15 clés RSA erronnées que vous devez corriger.
Pour vérifier qu'une clé est correctement corrigée, nous fournissons également le script Python `broken-rsa-keys.py` qui compare le sha256 de la clé après correction à une valeur présente dans `output.txt`.
Lorsque toutes les vérifications seront passées, le flag sera dérivé puis affiché.


## Files : 
 - [broken-rsa-keys.py](./broken-rsa-keys.py)
 - [output.txt](./output.txt)


