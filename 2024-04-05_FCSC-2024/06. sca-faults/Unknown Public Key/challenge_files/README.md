# Unknown Public Key

**Category** : sca-faults
**Points** : 500

Une équipe de police a repéré sur internet un individu suspecté de diriger une organisation terroriste.
La police aimerait avoir accès à son identité réelle, mais l'individu est méfiant.

Les policiers ont réussi à apprendre qu'il avait un compte dans une banque étrangère émettant des cartes particulières.
Un compte est donc ouvert anonymement dans cette banque afin de mener une étude sur ces cartes.
Voici ce qu'il en résulte:
- Les cartes n'embarquent pas les certificats (clefs publiques RSA) et l'authentification de la carte se fait toujours en ligne.
- L'analyse via canaux auxiliaires de l'exécution de la signature RSA montre que le calcul ne s'effectue pas en temps constant.

Une vaste opération pour identifier l'individu à l'aide de sa carte est mise en place.
Il va s'agir de retrouver la clef publique de la carte du suspect puis ensuite d'interroger la banque étrangère sur le propriétaire du compte associé.
Des terminaux de paiement permettant la mesure de courant ainsi que l'enregistrement de la séquence d'authentification sont discrètement distribués aux commerçants de la ville où l'on pense que le suspect réside.

Par chance, au bout de quelques jours, en relevant les échanges de ces terminaux on récupère une trace d'une transaction avec ladite banque étrangère.
Dans le fichier `output.txt`, il est affiché le message et sa signature avec la clef privée de la carte qui ont servi à l'authentification.

Serez-vous capable de reconstruire la clef publique à l'aide de cet échange et de la trace associée ?

**Note :** Le flag est sous la forme `FCSC{x}` où `x` est le SHA256 de la concaténation de l'exposant public `e` puis du module public `n`.

```python
e = e.to_bytes((e.bit_length() + 7) // 8, "big")
n = n.to_bytes((n.bit_length() + 7) // 8, "big")

h = hashlib.sha256()
h.update(e)
h.update(n)
print(f"FCSC{{{h.hexdigest()}}}")
```

## Files : 
 - [unknown-public-key.tar.xz](./unknown-public-key.tar.xz)
 - [output.txt](./output.txt)


