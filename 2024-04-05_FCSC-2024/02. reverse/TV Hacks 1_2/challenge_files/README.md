# TV Hacks 1/2

**Category** : reverse
**Points** : 482

Le SOC de la chaîne de télévision TV Hacks a remarqué des paquets NTP étranges passant leur pare-feu dans le sillage de paquets légitimes.
Ces messages sont à destination de l'équipement responsable de la génération des flux télévisuels pour la TNT.

Une analyse de la machine n'a pas permis de trouver quoi que ce soit de suspect à part un module noyau Linux qui semble servir à l'optimisation des flux IP à destination de notre diffuseur.

Ce module et un extrait de capture réseau vous sont fournis pour une première analyse.

L'équipement ne peut être arrêté sous aucun prétexte : cela signifierait un écran noir pour tous les téléspectateurs !
Si vous pouviez comprendre ce que fait l'attaquant, nous pourrons peut-être éviter un drame national.

## Files : 
 - [capture.pcap](./capture.pcap)
 - [ipopt.ko](./ipopt.ko)


