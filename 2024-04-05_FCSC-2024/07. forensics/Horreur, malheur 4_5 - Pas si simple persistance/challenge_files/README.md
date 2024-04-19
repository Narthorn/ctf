# Horreur, malheur 4/5 - Pas si simple persistance

**Category** : forensics
**Points** : 334

**Introduction commune à la série `Horreur, malheur`**

Vous venez d'être embauché en tant que Responsable de la Sécurité des Systèmes d'Information (RSSI) d'une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

**Note :** La première partie (`Archive chiffrée`) débloque les autres parties, à l'exception de la seconde partie (`Accès initial`) qui peut être traitée indépendamment. Nous vous recommandons de traiter les parties dans l'ordre.

---

Vous remarquez qu'une fonctionnalité *built-in* de votre équipement ne fonctionne plus et vous vous demandez si l'attaquant n'a pas utilisé la première persistance pour en installer une seconde, moins "visible"...

Vous cherchez les caractéristiques de cette seconde persistance : protocole utilisé, port utilisé, chemin vers le fichier de configuration qui a été modifié, chemin vers le fichier qui a été modifié afin d'établir la persistance.

Le flag est au format : `FCSC{<protocole>:<port>:<chemin_absolu>:<chemin_absolu>}`.


## Files : 
 - [archive.encrypted](./archive.encrypted)
 - [horreur-malheur.tar.xz](./horreur-malheur.tar.xz)


