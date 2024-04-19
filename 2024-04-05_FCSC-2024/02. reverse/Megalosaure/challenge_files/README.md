# Megalosaure

**Category** : reverse
**Points** : 487

Voici un binaire qui vérifie si ce qu'on lui passe est le flag.
À vous de jouer  !

**Notes :**
* Selon votre système, il est possible que vous deviez ajouter une _capabilities(7)_ au binaire avec la commande suivante : `sudo setcap cap_sys_resource=pe megalosaure`.
* Si vous obtenez une erreur `fork: Resource temporarily unavailable`, regardez les `cgroups` de votre shell avec `cat /proc/$$/cgroup` puis le fichier `/sys/fs/cgroup/.../pids.max` et essayez d'augmenter la valeur de ce fichier.


## Files : 
 - [megalosaure](./megalosaure)


