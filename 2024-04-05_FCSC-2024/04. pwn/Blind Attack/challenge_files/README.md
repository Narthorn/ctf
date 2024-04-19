# Blind Attack

**Category** : intro
**Points** : 20

Vous êtes en train de jouer votre premier [CTF en mode Attack/Defense](https://2023.faustctf.net/information/attackdefense-for-beginners/), et... c'est LA PANIQUE !
Le jeu a commencé depuis à peine 45 minutes, et votre équipe subit des attaques de tous les côtés, tous les services sont déjà down sauf un : vous ne savez pas si vous devez patcher, si vous devez attaquer, ou si vous devez redevenir un être humain normal et simplement abandonner. Tout s'embrouille dans votre esprit, tous vos repères ont disparu, vous ne savez plus comment vous vous appelez.

Vous reprenez un café (ok, vu le stress, c'était pas la meilleure idée), mais vous décidez de vous diriger vers l'outil mis à disposition de l'équipe pour l'analyse des flots réseaux. Cet outil ([Shovel](https://github.com/ANSSI-FR/shovel/)) permet de visualiser tous les flots TCP/UDP qui transitent sur la machine à défendre. Vous êtes en charge du service appelé `blind` sur cet outil, et sans même regarder le code de ce service, vous décidez de simplement reproduire les attaques que les autres équipes utilisent pour voler vos flags.

Votre objectif, voler le flag d'une équipe à ce tick de jeu (dans le scénario FCSC, le flag sera constant).
Le `flag ID` correspondant donné par les admins du CTF est : `/fcsc/ddJ565eGcAPFVkHZZFqXtrYe2vmVUQv`.

* Shovel : https://blind-attack.france-cybersecurity-challenge.fr/
* Service de l'équipe adverse : `nc challenges.france-cybersecurity-challenge.fr 2111`
* Flag ID : `/fcsc/ddJ565eGcAPFVkHZZFqXtrYe2vmVUQv`

**Note :** Le flag suit le format `FCSC_<ascii>`.

![Keep calm and get pwned](/files/5a9ac637384bf3deaa5cebe5ccf8d7e3/blind-attack.jpg)



