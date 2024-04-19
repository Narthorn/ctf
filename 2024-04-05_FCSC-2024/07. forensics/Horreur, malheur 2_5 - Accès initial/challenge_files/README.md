# Horreur, malheur 2/5 - Accès initial

**Category** : forensics
**Points** : 176

**Introduction commune à la série `Horreur, malheur`**

Vous venez d'être embauché en tant que Responsable de la Sécurité des Systèmes d'Information (RSSI) d'une entreprise stratégique.

En arrivant à votre bureau le premier jour, vous vous rendez compte que votre prédécesseur vous a laissé une clé USB avec une note dessus : `VPN compromis (intégrité). Version 22.3R1 b1647`.

**Note :** La première partie (`Archive chiffrée`) débloque les autres parties, à l'exception de la seconde partie (`Accès initial`) qui peut être traitée indépendamment. Nous vous recommandons de traiter les parties dans l'ordre.

---

Sur la clé USB, vous trouvez deux fichiers : une archive chiffrée et les journaux de l'équipement. Vous focalisez maintenant votre attention sur les journaux. L'équipement étant compromis, vous devez retrouver la vulnérabilité utilisée par l'attaquant ainsi que l'adresse IP de ce dernier.

Le flag est au format : `FCSC{CVE-XXXX-XXXXX:<adresse_IP>}`.


## Files : 
 - [horreur-malheur.tar.xz](./horreur-malheur.tar.xz)


