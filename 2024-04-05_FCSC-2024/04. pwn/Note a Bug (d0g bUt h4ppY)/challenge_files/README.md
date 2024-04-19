# Note a Bug (d0g bUt h4ppY)

**Category** : pwn
**Points** : 406

> *Cette description est la même pour les trois épreuves de la série **`**Note a Bug**`**.*

Vous continuez de jouer votre premier [CTF en mode Attack/Defense](https://2023.faustctf.net/information/attackdefense-for-beginners/) : c'est un peu moins la panique qu'il y a une heure, mais votre estime de vous en prend malgré tout un sacré coup. Au point que vous commencez à vous demander si le temps investi à s'entraîner sur [Hackropole](https://hackropole.fr/) a servi à quelque chose...

Tout n'est pas tout noir : vous commencez à maitriser les outils d'analyse réseau, les techniques de durcissement et vous soumettez même des faux flags dans les services des autres équipes pour tromper l'ennemi ! Vous avez même appris à voler les exploits des autres équipes très rapidement, sans même prendre la peine de regarder le code des services !

En analysant les flots réseau via [Shovel](https://github.com/ANSSI-FR/shovel/) et en discutant avec l'un de vos coéquipiers, vous vous apercevez que vous perdez des points sur l'épreuve **Note a Bug**.
Ce service est visiblement un des plus simples de tout l'A/D et certaines équipes ont commencé à patcher le service pour contrer la première vague d'exploits.

Votre objectif est désormais le vol des flags de trois équipes particulières à ce tick de jeu (dans le scénario FCSC, il y a un seul flag par "équipe").

Les trois équipes ont des environnements différents :
* `Red Beer` n'a pas encore patché son service.
* `d0g bUt h4ppY` semble avoir simplement modifié l'environnement d'exécution du service pour contrer l'exploit utilisé par toutes les équipes. Votre hypothèse est qu'ils ont simplement supprimé `/bin/sh` du conteneur du service. Il n'y a en effet aucune raison qu'une utilisation légitime du service ait besoin de `/bin/sh` !
* `Nordic Mollusks` a modifié les paramètres d'appel du service. Cette équipe a en effet remarqué que les _checkers_ utilisés par les organisateurs ne font qu'une unique action par connexion : soit une unique écriture (`1`) pour placer le flag, soit une unique lecture (`2`) pour vérifier que le flag est bien présent. Ils ont alors décidé de n'autoriser qu'une seule action à tout le monde, ce qui empêche également l'exploit mais ne casse pas le passage des _checkers_.

**Notes :**
* Vous êtes dans l'urgence, aucun binaire n'est fourni pour cette épreuve. Vous devez dans un premier temps exploiter l'équipe `Red Beer` en utilisant uniquement les données présentes dans Shovel.
* Une fois un shell obtenu chez `Red Beer`, vous pourrez exfiltrer le binaire (présent dans `/app`) et progresser dans l'exploitation des deux autres équipes.
* Aucun ordre de validation n'est strictement imposé, mais nous vous conseillons de prendre les équipes ci-dessus dans l'ordre.
* Vous devez rentrer le flag trouvé pour l'équipe `XXX` dans l'épreuve qui s'intitule `Note a Bug (XXX)`.
* Les flags sont au format `FCSC_<ascii>`.

**Fournitures :**

* Shovel : https://note-a-bug.france-cybersecurity-challenge.fr/
* Première équipe (`Red Beer`) :
  * Service : `nc challenges.france-cybersecurity-challenge.fr 2108`
  * Flag ID : `ChbbgHyPqJDQy5UaJve6uUGMDQHXWtc`.
* Deuxième équipe (`d0g bUt h4ppY`) :
  * Service : `nc challenges.france-cybersecurity-challenge.fr 2109`
  * Flag ID : `ZBrKMnQJGebtYHDXrNxxF6hU2DzwJzX`.
* Troisième équipe (`Nordic Mollusks`) :
  * Service : `nc challenges.france-cybersecurity-challenge.fr 2110`
  * Flag ID : `YAu4kj47vbSDkqTEf2YttEcK88pXYpf`.



