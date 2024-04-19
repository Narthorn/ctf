# Horreur, malheur 3/5 - Simple persistance

**Category** : forensics
**Points** : 325

**Introduction commune à la série `Horreur, malheur`**

Vous venez d'être embauché en tant que Responsable de la Sécurité des Systèmes d'Information (RSSI) d'une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

**Note :** La première partie (`Archive chiffrée`) débloque les autres parties, à l'exception de la seconde partie (`Accès initial`) qui peut être traitée indépendamment. Nous vous recommandons de traiter les parties dans l'ordre.

---

Vous avez réussi à déchiffrer l'archive. Il semblerait qu'il y ait dans cette archive une autre archive, qui contient le résultat du script de vérification d'intégrité de l'équipement.

À l'aide de cette dernière archive et des journaux, vous cherchez maintenant les traces d'une persistance déposée et utilisée par l'attaquant.

## Files : 
 - [archive.encrypted](./archive.encrypted)
 - [horreur-malheur.tar.xz](./horreur-malheur.tar.xz)


