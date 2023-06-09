# Le Mystère du roman d'amour

**Category** : Analyse forensique
**Points** : 200

En train de faire les cent pas dans un couloir du café se trouve Joseph Rouletabille. Il est préoccupé par un mystère des plus intrigants : une de ses amies, qui écrit régulièrement des livres passionnants, a perdu le contenu de son dernier roman !! Elle a voulu ouvrir son oeuvre et son éditeur a crashé... Il semblerait qu'un petit malin a voulu lui faire une blague et a modifié ses fichiers. Elle n'a pu retrouver qu'un seul fichier étrange, que Joseph vous demande de l'aider à l'analyser afin de retrouver son précieux contenu et de comprendre ce qu'il s'est passé.

<p class="space">&nbsp;</p>


***
<p class="space">&nbsp;</p>

Vous devez retrouver :
- le PID du processus crashé
- le chemin complet vers le fichier en question (espaces autorisés) : la forme exacte trouvée dans le challenge et la forme étendue commençant par un / permettent toutes les deux de valider le challenge
- le nom de l'amie de Rouletabille
- le nom de la machine
- le contenu TEXTUEL du brouillon de son livre (si vous avez autre chose que du texte, continuez à chercher : vous devez trouver un contenu texte qui ressemble clairement au début d'un roman). Une fois ce contenu trouvé, il sera clairement indiqué quelle partie utiliser pour soumettre le flag (il s'agira d'une chaîne de caractères en [leet](https://fr.wikipedia.org/wiki/Leet_speak)) 

Le flag est la suite de ces éléments mis bout à bout, et séparés par un tiret du 6 (`-`), le tout enveloppé par `404CTF{...}`.

<p class="space">&nbsp;</p>

Un exemple de flag valide : 

<p class="space">&nbsp;</p>

`404CTF{1234-/ceci/est/un/Chemin avec/ des espaces1337/fichier.ext-gertrude-monPcPerso-W0w_Tr0P_1337_C3_T3xt3}`

<p class="space">&nbsp;</p>

<blockquote style="text-align:left">
	<b>Format</b> : 404CTF{PidDuProcessusCrashé-chemin/vers le/fichier-nomUser-nomDeLaMachine-contenuDuFichier}
	
</blockquote>

<div class="author">mh4ckt3mh4ckt1c4s#0705</div>
 
 <p class="space">&nbsp;</p>
 

## Files : 
 - [fichier-etrange.swp](./fichier-etrange.swp)


