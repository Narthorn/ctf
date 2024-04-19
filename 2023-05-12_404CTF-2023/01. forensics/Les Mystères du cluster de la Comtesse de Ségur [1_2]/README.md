[Les Mystères du cluster de la Comtesse de Ségur [1/2]](challenge_files/README.md) - forensics, medium, 308 solves
===

**Author**: Typhlos#9037    
**Files**: [checkpoint-bash_default-bash-2023-05-06T090421Z.zip](https://www.narthorn.com/ctf/404CTF-2023/challenge_files/Analyse%20forensique/Les%20Myst%C3%A8res%20du%20cluster%20de%20la%20Comtesse%20de%20S%C3%A9gur%20%5B1_2%5D/checkpoint-bash_default-bash-2023-05-06T090421Z.zip)

## Other write-ups

- https://nouman404.github.io/CTFs/404CTF_2023/Forensique/Les_Mysteres_du_cluster_de_la_Comtesse_de_Segur
- https://writeups.ayweth20.com/2023/404ctf-2023/analyse-forensique/les-mysteres-du-cluster-de-la-comtesse-de-segur-1-2 (in french)

## Solve

The bread and butter forensics challenge, a dump of some kind including a filesystem tree and raw memory images.

We are very sophisticated people using only the most adequate, refined and elegant tools for the job, so let's unpack the archive and carefully set up our forensics enviro---

```
└─[$] zipgrep -ai "404CTF" checkpoint-bash_default-bash-2023-05-06T090421Z.zip
checkpoint-bash_default-bash-2023-05-12T09:04:21Z/checkpoint/pages-1.img: 
...
...!`ZÖOJV@ÕÔOJV! hÓOJVPoÖOJV1pÖOJV agent.zip flag.txtJV0Acurl agent.challenges.404ctf.fr -o agent.zip! ÖOJVP{ÖOJV!ßßßßßßßßßßßßßßßß!ßßßßßßßßßßßßßßßß!p{ÖOJV!...
...

└─[$] curl https://agent.challenges.404.fr -o agent.zip

└─[$] unzip agent.zip
Archive:  agent.zip
  inflating: agent                   
  inflating: flag.txt

└─[$] cat flag.txt
404CTF{K8S_checkpoints_utile_pour_le_forensic}
```

Ah. Well.

## Comments

To be fair, I didn't go straight for grep (I should have), so I went around digging a while with the [CRIU](https://github.com/checkpoint-restore/criu) tools that created the dump.   
You can use commands like `criu info {thing}.img` to get some data out of the files in the `checkpoint` folder, like a list of running processes, etc, but as far as I can tell you will have to dig through the actual memory image file to find the URL.