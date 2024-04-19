# PewPew

**Category** : sca-faults
**Points** : 474

Vous avez à disposition un système embarqué permettant de déchiffrer et de signer des messages avec RSA.
La clé privée utilisée est stockée de manière sécurisée dans ce système et est réputée impossible à extraire ou cloner.
Malheureusement, suite à une mésaventure vous l'avez endommagé et n'est plus possible que de signer un message fixe.

Votre mission, si vous l'acceptez, est d'extraire la clé privée RSA de cette carte embarquée, puis de l'utiliser pour déchiffrer le flag.
Pour cela, nous vous mettons à disposition un banc d'injection de fautes électromagnétiques (EMFI).
Ce banc d'injection de fautes est équipé d'un injecteur de fautes électromagnétiques placé sur un axe motorisé 2D.

Afin de vous aider, nous vous mettons à disposition le même système embarqué, mais avec un code remplacé par :
```asm
LDR r4, =0xCAFECAFE     ; charge 0xCAFECAFE dans le registre r4
ORR R4, R4              ; r4 <- r4 OU r4
ORR R4, R4              ; r4 <- r4 OU r4
ORR R4, R4              ; r4 <- r4 OU r4
; [...] 1000x
ORR R4, R4              ; r4 <- r4 OU r4
ORR R4, R4              ; r4 <- r4 OU r4
ORR R4, R4              ; r4 <- r4 OU r4
J   print_r4            ; affiche r4, r4 devrait être égal à 0xCAFECAFE
```
Nous vous invitons à utiliser cette seconde carte pour vous entraîner à réaliser des fautes.

Connectez-vous au serveur pour commencer votre aventure.

![](/files/2a5ca90109705a614455aa386ce44584/pewpew.png)

nc challenges.france-cybersecurity-challenge.fr 2350



