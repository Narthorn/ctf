[Lettres volatiles](challenge_files/README.md) - forensics, medium, 194 solves
===

**Author**: [OwlyDuck#4819](https://github.com/OwlyDuck)    
**Files**: [C311M1N1.zip](https://www.narthorn.com/ctf/404CTF-2023/challenge_files/Analyse%20forensique/Lettres%20volatiles/C311M1N1.zip)

## Other write-ups

- https://nouman404.github.io/CTFs/404CTF_2023/Forensique/Lettres_volatiles
- https://writeups.ayweth20.com/2023/404ctf-2023/analyse-forensique/lettres-volatiles (in french)
- https://github.com/TechieNeurons/404CTF_2023_write_ups/tree/main/forensics/lettres_volatiles (interesting steps)

## Solve

Opening the archive, we are presented with the files of a windows user data folder. Of particular interest to us are two files:

- `Documents/perso/s3cR37.zip` folder, which contains a password-protected [zipfile](s3cR37.zip), and
- `Documents/JumpBag/C311M1N1-PC-20230514-200525.raw`, which is a full system memory dump.

This kind of memory dump can be explored with tools like [volatility](https://github.com/volatilityfoundation/volatility)[^1]. You can inspect a huge number of things with volatility and its plugins, but in this case, we want to check the data stored in the clipboard:

```
└─[$] python2 vol.py -f C311M1N1/Documents/JumpBag/C311M1N1-PC-20230514-200525.raw --profile Win7SP1x64 clipboard 
Volatility Foundation Volatility Framework 2.6.1
Session    WindowStation Format                         Handle Object             Data                                              
---------- ------------- ------------------ ------------------ ------------------ --------------------------------------------------
         1 WinSta0       CF_UNICODETEXT               0x1801b1 0xfffff900c23fa100 Z1p p4s5wOrd : F3eMoBon8n3GD5xQ                   
         1 WinSta0       CF_TEXT                          0x10 ------------------                                                   
         1 WinSta0       0x120207L              0x200000000000 ------------------                                                   
         1 WinSta0       CF_TEXT                           0x1 ------------------                                                   
         1 ------------- ------------------           0x120207 0xfffff900c2108b60     
```

With the zip password in hand, we can extract the archive that contains a pdf with the flag, [lettreAOronte.pdf](lettreAOronte.pdf).

`404CTF{V0147i1I7y_W1Ll_N3v3r_Wr8_loV3_l3ttEr5}`

[^1]: Make sure to get volatility 2, not volatilty 3, because the specific plugin we need for this challenge hasn't been ported to volatility 3 yet.

## Comments

Of course I had to try vol3 first. Of course I had to go through *every single plugin* in the list for hours before I realised the clipboard and notepad plugins weren't there.
It's been years?! Why haven't these plugins been ported to vol3 already? The [clipboard](https://github.com/volatilityfoundation/volatility/blob/a438e768194a9e05eb4d9ee9338b881c0fa25937/volatility/plugins/gui/clipboard.py) one is less than 200 lines of code, surely that one can't be that time-consuming to port... 