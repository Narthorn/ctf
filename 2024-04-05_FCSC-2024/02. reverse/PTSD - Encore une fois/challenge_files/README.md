# PTSD - Encore une fois

**Category** : reverse
**Points** : 479

> _Cette épreuve est la deuxième étape de la série PTSD : il est recommandé de commencer par la première. Les fichiers joints sont les mêmes que pour la première étape, avec en plus `records.txt` qui est fourni._

Pendant que vous étiez en train de confectionner votre client, le commanditaire vous envoie les traces de l'initialisation et au-delà du client n°5 (`records.txt`).

Votre chef de projet vous propose de rechercher une vulnérabilité dans le protocole.
Vous mettez en place une attaque de l'homme du milieu pour vous faire passer pour le client n°5.

Votre objectif est donc de vous faire passer pour ce client en envoyant ses informations au serveur.
Attention, le temps de réponse du client n°5 est de 10 secondes.

**Note :** les librairies `libcrypto.so.3` et `libssl.so.3` sont fournies mais ne sont pas à analyser dans le cadre de cette épreuve.


nc challenges.france-cybersecurity-challenge.fr 2251

## Files : 
 - [records.txt](./records.txt)
 - [keys.db](./keys.db)
 - [lv1.flag](./lv1.flag)
 - [lv2.flag](./lv2.flag)
 - [libssl.so.3](./libssl.so.3)
 - [libcrypto.so.3](./libcrypto.so.3)
 - [server](./server)


