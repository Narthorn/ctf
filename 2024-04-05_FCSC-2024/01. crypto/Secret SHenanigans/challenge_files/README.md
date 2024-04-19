# Secret SHenanigans

**Category** : crypto
**Points** : 477

Un malfrat, versé dans la technique, se méfie des protocoles de canaux sécurisés
éprouvés comme SSH ou TLS : "ils sont tous certainement backdoorés" pense t'il. Comme il doit
régulièrement recevoir des informations confidentielles de collègues à lui, il
a développé son propre protocole d'établissement de canal sécurisé permettant à
des clients anonymes d'envoyer à son serveur ces informations confidentielles.

Vous avez accès à un TAP réseau vous positionnant en Man-in-the-Middle entre un client et le serveur,
et vous avez par ailleurs réussi à dérober le code source de l'application (sans la clé
privée du serveur malheureusement ...). Saurez-vous récupérer le secret que le client
envoie au serveur ?

![](/files/c8c841f70e91a57498ee664c21f409bf/secret_shenanigans.png)

nc challenges.france-cybersecurity-challenge.fr 2154

## Files : 
 - [README.md](./README.md)
 - [secret-shenanigans.tar.xz](./secret-shenanigans.tar.xz)


