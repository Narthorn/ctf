Définition
==========

**Category** : Misc  
**Score** : 50 points 
**Solved** : 286 times  

---

>Un de vos collègues a créé un petite énigme, il est un peu lourd et vous demande depuis des semaines de la résoudre, faites lui plaisir. Voici l'énigme : Quelle heure est-t-il ?
>
>Connectez-vous via nc challengecybersec.fr 6660
>
>Le flag est de la forme : DGSESIEE{x} avec x un hash

The answer is simply the current UNIX timestamp.

```bash
└─[$] date +%s | ncat challengecybersec.fr 6660
Entrez la reponse :
> Bravo ! Voici le flag : DGSESIEE{cb3b3481e492ccc4db7374274d23c659}
```

---

I lost a LOT of time on this one. Very silly. 
The literal first thing I tried was to pipe the current date as "%H:%M:%S", which was the correct idea but not the correct format.

Then I tried a million different other formats without success, and then I gave up, and then I came back the next day and ripped my hair off trying to figure out increasingly insane possible answers ("now"? "the same time it was yesterday at that time"?), and losing my mind at the amount of people who were apparently able to solve the challenge, and then I gave up again, and then I went back to piping the current date, tried unix timestamp format, and it worked.

I really don't think challenges like this are any good. They're simultaneously too vague and even if you do get what you're meant to do, there's too many different ways to input the solution.

