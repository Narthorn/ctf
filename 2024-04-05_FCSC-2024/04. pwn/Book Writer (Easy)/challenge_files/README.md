# Book Writer (Easy)

**Category** : pwn
**Points** : 387

La startup *TypeWriters & Co.* a une idée géniale : elle souhaite proposer en ligne
un service de traitement de texte qui va révolutionner le monde de l'édition !

Mais la veille de l'inauguration, le chef de projet se souvient d'une vague mention concernant des exigences de sécurité...

Comme vous êtes la personne chargée de la sécurité, il a besoin de votre validation.
Selon lui, cela n'est qu'une simple formalité car le code a été relu par leurs meilleurs développeurs
et le binaire s'exécute avec toutes les protections classiques (canaris, W^X, ASLR, etc.).

Vérifiez s'il est possible de lire le fichier `flag.txt` qui se trouve sur le serveur distant.


nc challenges.france-cybersecurity-challenge.fr 2100

## Files : 
 - [book-writer-easy](./book-writer-easy)
 - [book-writer-easy.c](./book-writer-easy.c)


