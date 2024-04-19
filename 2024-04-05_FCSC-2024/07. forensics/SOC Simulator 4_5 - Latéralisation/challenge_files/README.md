# SOC Simulator 4/5 - Latéralisation

**Category** : forensics
**Points** : 408

**Introduction commune à la série `SOC Simulator`**

Durant l'été 2022, un opérateur d'importance vitale (OIV) alerte l'ANSSI car il pense être victime d'une cyberattaque d'ampleur.
Le _security operation center_ (SOC) de l'OIV envoie à l'ANSSI un export de sa collecte système des derniers jours.
Vous êtes chargé de comprendre les actions réalisées par l'attaquant.

**Note :** Les 5 parties sont numérotées dans l'ordre chronologique de l'attaque mais il n'est pas nécessaire de les résoudre dans l'ordre.

---

Sur une courte période de temps, l'attaquant a essayé de se connecter à de nombreuses machines, comme s'il essayait de réutiliser les secrets volés dans la partie 2.
Cela lui a permis de se connecter à la machine `Workstation2`.
Retrouver l'IP source, le compte utilisé et l'heure UTC de cette connexion.

**Format du flag (insensible à la casse) :** `FCSC{192.168.42.27|MYCORP\Technician|2021-11-27T17:38:54}`.


## Files : 
 - [soc_events.zip](./soc_events.zip)


