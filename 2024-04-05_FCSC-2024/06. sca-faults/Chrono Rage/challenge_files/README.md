# Chrono Rage

**Category** : sca-faults
**Points** : 456

Votre ami a développé un petit démon local sur son serveur qui ouvre une socket en écoute sur `localhost` et
effectue des actions privilégiées lorsque des clients s'y connectent et s'authentifient avec un
PIN. Malheureusement, il s'est fait attaquer son serveur récemment, malgré tous les efforts qu'il
a mis dans la sécurisation de son démon.

Il vous fournit les sources de ce démon en Python : comme vous le verrez, pour sécuriser l'envoi du
PIN sur la socket il utilise des clés de session AES tournantes. Il vous fournit aussi une capture `pcap`
correspondant à l'activité suspecte d'un client local relevée grâce à son monitoring constant
des connexions. Malheureusement, il a perdu la clé AES utilisée au moment de cette capture et ne peut donc
vous la fournir. Enfin, il a évidemment caviardé le PIN dans les sources : vous n'avez a priori
pas à connaître ce secret sensible !

Saurez-vous l'aider en lui expliquant comment l'attaquant s'y est pris, et qu'il doit changer
de PIN et corriger son code au plus vite ?

**Note :** le format du flag est `FCSC{PIN}` où `PIN` est le `PIN` du serveur.

![](/files/18fe21339d75463efcb003ec60fa9fcf/chrono_rage.png)

## Files : 
 - [chrono-rage.pcap](./chrono-rage.pcap)
 - [chrono-rage-server.py](./chrono-rage-server.py)


