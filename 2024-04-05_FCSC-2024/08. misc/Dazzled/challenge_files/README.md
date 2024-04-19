# Dazzled

**Category** : misc
**Points** : 482

**Cette épreuve est une variante plus difficile de Illuminated.**

Une éclairagiste vous met au défi de reconstituer une animation d'un spectacle stockée sur son enregistreur DMX.
Elle vous informe que cette fois elle a utilisé des projecteurs motorisés (exemple : <https://youtu.be/N-eTCKjO9xc>) pour dessiner des symboles sur une toile posée au sol.

Vous réalisez alors une capture réseau (`capture.pcap`) en vous branchant en Ethernet sur son enregistreur.

Pour vous aider, elle vous donne un extrait de la documentation d'un projecteur (`projector.pdf`) ainsi qu'un schéma de sa scène :

```
=================================== Top view ===================================

                                           0.57m
                                          |-----|
            ._____.     ._____.     ._____.     ._____.
            | 001 |     | 009 |     | 017 |     | 025 |
            |_____|     |_____|     |_____|     |_____|  ___
                                                          |
                                                          | 0.67m
            ._____.     ._____.     ._____.     ._____.  _|_
            | 033 |     | 041 |     | 049 |     | 057 |
            |_____|     |_____|     |_____|     |_____|


            ._____.     ._____.     ._____.     ._____.
            | 065 |     | 073 |     | 081 |     | 089 |
            |_____|     |_____|     |_____|     |_____|


            ._____.     ._____.     ._____.     ._____.
            | 097 |     | 105 |     | 113 |     | 121 |
            |_____|     |_____|     |_____|     |_____|




================================== Front view ==================================

(stage left)                                           (stage right)
            ._____.     ._____.     ._____.     ._____.
            |_____|     |_____|     |_____|     |_____|
            |/   \|     |/   \|     |/   \|     |/   \|  ___
             \_O_/       \_O_/       \_O_/       \_O_/    |
                                                          |
                                                          |
                                                          |
                                                          |
                                                          |
                                                          | Height: 2.8m
                                                          |
                                                          |
                                                          |
                                                          |
                                                          |
                                                          |
          Spot size: ~16°                                 |
                                                         _|_
       -----------------------------------------------------------
_______| praticable                                              |________
```

Releverez-vous le défi ?

**Aide** : 10 secondes après le début de l'animation, les projecteurs dessinent la lettre « F » au sol.

**Note** : La capture réseau contient également un flux audio RTP qui ne fait pas partie de l'épreuve. Ce son permet de mieux profiter de l'animation une fois reconstituée. 

**Précisions** :
- "Spot size: ~16°" correspond à l'angle du cône créé par le faisceau lumineux d'un projecteur.
- Tous les projecteurs sont identiques, même orientation, ils ne sont que translatés l'un de l'autre (comme ce que ferait une régie sur une vraie scène pour se simplifier la vie).


## Files : 
 - [projector.pdf](./projector.pdf)
 - [capture.pcap](./capture.pcap)


