# Sea side channel [2/4] - Reconnaissance

**Category** : Sécurité matérielle
**Points** : 999

<div style="margin-bottom: 1em;"><i> Attention : la clef de la trace d'entrainement est [2, 4, 4] et non pas [4, 2, 2] !</i></div>

<p class="space">&nbsp;</p>

Vos deux concurrents, Alice et Bob, auraient apparemment décidé de s'envoyer par message leurs différents entraînements d'haltérophilie. Au vu de leurs résultats dans les dernières compétitions auxquelles vous avez participé, il serait très intéressant pour vous de savoir ce qu'ils se disent ! 

Par chance, vous avez eu accès au même outil qu'ils ont utilisé pour générer leurs clefs privées et calculer les clefs publiques, vos connaissances en microélectronique devraient pouvoir vous aider. Vous avez donc branché un oscilloscope à cet outil et ajouté des signaux de synchronisation pour essayer de remonter à la clef privée utilisée !


***  

Vous avez ainsi accès à des traces de consommation d'une puce pendant son calcul de la clef publique ainsi que des signaux vous donnant des informations sur les calculs en cours (\*.csv) (Les traces et les triggers sont déjà synchronisés : ils commencent au même moment). Vous pouvez vous référer à la spécification pour savoir à quoi correspondent les signaux (Specifications.pdf). Vous avez aussi accès au code en Rust tournant sur la puce pour savoir ce qu'il s'y passe (csidh.rs) et aux librairies utilisées (\*.rs).

Le nombre premier p utilisé pour ce challenge est le même que pour le challenge précédent : 419.

Le flag est au format classique et se retrouve avec l'ordre de calcul des isogénies. Exemple : "404CTF{7375}" si la clef est \[1,1,2\] et que les isogénies sont calculées dans l'ordre 7, 3, 7, 5.

/!\\ Attention, vous avez un nombre d'essais limité !
 
<p class="space">&nbsp;</p>

Auteurs : <b> @Phengar</b>, <b>Titouan Real</b>

<p class="space">&nbsp;</p>

## Files : 
 - [Chall2.tar.gz](./Chall2.tar.gz)


