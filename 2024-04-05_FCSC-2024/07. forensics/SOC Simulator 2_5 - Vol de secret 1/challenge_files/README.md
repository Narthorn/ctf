# SOC Simulator 2/5 - Vol de secret 1

**Category** : forensics
**Points** : 352

**Introduction commune à la série `SOC Simulator`**

Durant l'été 2022, un opérateur d'importance vitale (OIV) alerte l'ANSSI car il pense être victime d'une cyberattaque d'ampleur.
Le _security operation center_ (SOC) de l'OIV envoie à l'ANSSI un export de sa collecte système des derniers jours.
Vous êtes chargé de comprendre les actions réalisées par l'attaquant.

**Note :** Les 5 parties sont numérotées dans l'ordre chronologique de l'attaque mais il n'est pas nécessaire de les résoudre dans l'ordre.

---

Après l'action vue dans la partie 1, l'attaquant vole les identifiants système en mémoire.
Retrouver le GUID du processus effectuant ce vol et le nom du fichier où il écrit les secrets volés.

**Format du flag (insensible à la casse) :** `FCSC{6ccf8905-a033-4edc-8ed7-0a4b0a411e15|C:\Windows\Users\toto\Desktop\fichier.pdf}`


## Files : 
 - [soc_events.zip](./soc_events.zip)


