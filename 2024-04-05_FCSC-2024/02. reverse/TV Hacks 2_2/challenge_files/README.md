# TV Hacks 2/2

**Category** : reverse
**Points** : 498

> **Important :** _Les deux étapes de la série `TV Hacks` sont à réaliser dans l'ordre. Nous vous conseillons fortement de ne pas tenter la résolution de cette épreuve tant que vous n'avez pas validé la première étape._
 
Merci pour la première analyse effectuée dans ` TV Hacks 1/2 ` !

Au vu de la criticité de l'équipement, les règles du pare-feu sont très strictes. A part le protocole NTP, aucun paquet n'est envoyé sur Internet directement.
Cependant, le flux vidéo diffusé par l'équipement est transmis à notre prestataire en charge de la diffusion et, les débits étant trop importants, nous ne pouvons pas garder une trace de ces données.

Heureusement, un ami à vous, fan de TV Hacks, enregistrait l'émission qui passait au moment de l'attaque.
Il a pu vous envoyer un extrait de vidéo : cela devrait vous permettre d'aller plus avant.

De plus, le fournisseur de la solution de streaming a pu nous transmettre le code source du module noyau développé par un prestataire.
Cela pourrait faciliter votre analyse même si **nous avons exclu une attaque par la chaîne logistique**.

Remerciements :

- Sprite Fright : (CC) Blender Foundation | studio.blender.org
- Sprite Fright version française : (CC-BY) Touhoppai | www.youtube.com/@Touhoppai

## Files : 
 - [capture.pcap](./capture.pcap)
 - [ipopt.ko](./ipopt.ko)
 - [ipopt.tar.gz](./ipopt.tar.gz)
 - [capture.ts](./capture.ts)


