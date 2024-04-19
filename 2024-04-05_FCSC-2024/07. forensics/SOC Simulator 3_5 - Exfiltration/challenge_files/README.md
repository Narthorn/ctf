# SOC Simulator 3/5 - Exfiltration

**Category** : forensics
**Points** : 442

**Introduction commune à la série `SOC Simulator`**

Durant l'été 2022, un opérateur d'importance vitale (OIV) alerte l'ANSSI car il pense être victime d'une cyberattaque d'ampleur.
Le _security operation center_ (SOC) de l'OIV envoie à l'ANSSI un export de sa collecte système des derniers jours.
Vous êtes chargé de comprendre les actions réalisées par l'attaquant.

**Note :** Les 5 parties sont numérotées dans l'ordre chronologique de l'attaque mais il n'est pas nécessaire de les résoudre dans l'ordre.

---

Dans la continuité de ce qui été vu précédemment, l'attaquant a collecté une quantité importante de données métier.
Retrouver la commande qui a permis de collecter tous ces éléments.

**Format du flag :** `FCSC{sha256(<commande en UTF8 sans saut de ligne>)}`

Par exemple, si la commande malveillante était `7z a "Fichiers volés.zip" C:\Windows\System32`, le flag serait `FCSC{bc5640e69c335a8dbe369db382666070e05198a6c18ce88498563d2c4ac187b1}`.



## Files : 
 - [soc_events.zip](./soc_events.zip)


