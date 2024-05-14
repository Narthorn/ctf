# Le tir aux logs 

**Category** : Investigation numérique
**Points** : 100

Il semblerait qu'une personne malveillante ait réussi à se connecter sur le site d'inscription d'une compétition de tir à l'arc. \
Aidez-nous à investiguer sur cette attaque via le fichier de logs de notre serveur.
Quel est l'URL complète (formée du nom de domaine, puis de la ressource), qui a permis de se connecter de manière frauduleuse ?

***  

Le flag attendu est l'URL utilisée par l'attaquant pour exploiter une vulnérabilité du site avec succès, entouré du format habituel. \
Par exemple, si l'attaquant se rend sur la page https://example.com/page.php?authenticated=1 pour se connecter de manière frauduleuse, le flag sera 404CTF{https://example.com/page.php?authenticated=1}. \
\
Le décodage url n'est pas nécessaire.\
Par ailleurs, toutes les IP utilisées sont fictives et non pertinentes.

<p class="space">&nbsp;</p>

<div class="author">ElPouleto</div>

<p class="space">&nbsp;</p>

## Files : 
 - [access.log](./access.log)


