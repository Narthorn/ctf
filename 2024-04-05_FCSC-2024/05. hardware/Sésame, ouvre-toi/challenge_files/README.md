# Sésame, ouvre-toi

**Category** : hardware
**Points** : 439

Votre ami a stocké un secret dans la configuration de son chargeur de démarrage.
Il vous assure qu'il n'est pas possible de l'extraire car il faut connaître son mot de passe pour stopper l'autoboot et y accéder.

Vous débranchez le disque NVMe stockant son système d'exploitation, vous remarquez alors que la machine démarre dans une sorte de shell.
Serez-vous trouver un moyen d'accéder à son secret ?

*Note*: sur cette machine, le pointeur d'instruction est initialisé à `0x00000000` au démarrage.

On vous fournit un dump de ce chargeur de démarrage, mais configuré avec le mot de passe `FAKEPASSWORD` et sans secrets.

![Sponge Bob, Patrick Open Sesame meme](/files/719643a60dab2050d12627076509c9a5/sesame.jpg)

nc challenges.france-cybersecurity-challenge.fr 2300

## Files : 
 - [bootloader.bin](./bootloader.bin)


