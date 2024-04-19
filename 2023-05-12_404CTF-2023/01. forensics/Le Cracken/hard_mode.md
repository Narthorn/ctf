Hello and welcome to hard mode, aka what you get when you have terminal forensics brain rot.

This is completely irrelevant to the actual challenge, it's just something that I inflicted upon myself by mistake.

As I mentioned in the footnote, I initially disregarded the timestamp bytes and decoded every message together in order. Surprisingly this sort of works, and you get plaintext that is for the most part [readable](decrypted_badly), and even the PDF file ends up being decodable from base64... somewhat.

The [decoded pdf](LeNautilus_corrupted.pdf) is broken and unreadable by pdf readers, but if you open it in a text editor, some sections are stlil readable:

```pdf
%PDF-1.6
%Ã¤Ã¼Ã¶Ã
2 0 obj
<</Length 3 0 R/Filter/FlateDecode>>
stream
xRËj[AÝÏWhðDÒh^0Ø¹6¤»À.JWiÓ.âdß4c_(í¦Á`½t¤3=Á{ôÈb%Cò%¼~woà#°ßë³T*Ý`Í<oísØó6Ö¼å~º§åà¤Eö6üãÙÝÞßð`ÛyÆPb*ñ$c,ÃÈU²­wX¡(¡ÃúnOa}úÒú.5Ôq(jÃ	sß6,X5Ø÷¯ë'w\ÝÇà±È9øZëÅ#ÖI~èÜðNÙÌµÿ¥ï86<ö]hxêÔ²B'emâFBö¨ÕRy 
Õa÷EôaûZ-èøý2Q«-rE-=Xãq0±µ>¬äèG}î¿uaÄb$ãd&s3Lê²lÔ4ºHãqÁU;½Yß.ò¼íÈyÉ9æuÊ×D`#¼ÌC*SvÂ ¹bÔ07ÞóÁâ;DKU#{¢¤fÿRbé¶ÃU~Rsf[/Ø%Ûð0pÉØ
endstream
endobj

3 0 obj
425
endobj

4 0 obj
<</Type/XObject/Subtype/Image/Width 2480 /Height 3508 /BitsPerComponent 8 /ColorSpace/DeviceRGB/Filter/DCTDecode/Length 1194484>>
stream
ÿØÿà

...
...
...

8PànF[ðÎ©4@¦VæG7Gähõ¿¼êD
endstream
endobj

7 0 &VÐ¦VæFö&  £rö& £3#`¦VæFö&  £ö& £ÃÂõGZ
8 0 obj
<</Type/FontDescriptor/FontName/BAAAAA+Z003MediumItalic
#4ÖVFVÔFÆ0¢ôfÆw2c¢ôföçD$&÷²ÓCRÓ3CCÒôFÆ4ævÆRÓ3¢ô66VçB¢ôFW66VçB¢ô6VvBCp¢õ7FVÕb¢ôföçDfÆRb £ãà¦VæFö&  £ö& £ÃÂôÆVæwFC3ôfÇFW"ôfÆFTFV6öFSãà§7G&VÐ§ÅÙ<Öî#Dow¢ó¸²¯Ö!pZ/ÄÍ¨ä®p&&N$BbÇ¿­ìó27P¬iþ×<×[íæÿgé=öÀæåj||Üu¾Ã«¯>4Ú¡û£ÞK»»E9l{X·Wi{ÓøÜ¶Ykü{±Îî¦Xôr¼½ô.ü.þ®ÿ¡x}³GÛ¿;2«*eÓ¼WÕí®[ÛÅcÞï³ÜÏ|{Gþ3ãS-emåÚ{g:VyrØº%½ÚìÎ÷üÅQd¸ê~ë0Ó¦;B§Q9DÜÕÀ¥<Â6ZéÄm­è"¾bvAlÀ»Ëô*fGábâ[ðlµ¹ÂY×Ù×ãyXÙéøâ[¶½å<;ýã;þ#Ó_Æ³ä¼;ñHgòV¹;ùÀ_ù.½_Ã¿%k¿ÿëÕð·âóÄü%káo7	þ;üß-¥û_1Ãß°3ÁË÷Ið'¾O¿agb*´dÒýsüMú5v"Ô°â:	5ß¡WÔ`Si¬ÔAÜbüþ¶®ên!Ä¶"ýÊ:x÷ï-MãÄ«äó~ÚR
endstream
endobj

10 0 obj
<</Type/Font/Subtype/Type1/BaseFont/BAAAAA+Z003MediumItalic
/FirstChar 0
/LastChar 47
/Widths[0 580 340 220 700 420 460 320 240 240 320 440 440 520 500 580
240 300 440 440 500 700 460 440 700 440 440 440 440 620 680 240
600 460 220 400 340 220 340 240 440 520 400 220 280 280 620 400
]
/FontDescriptor 8 0 R
/ToUnicode 9 0 R
>>
endobj

11 0 obj
<</F1 10 0 R
>>
endobj

12 0 obj
<</Font 11 0 R
/XObject<</Im4 4 0 R>>
/ProcSet[/PDF/Text/ImageC/ImageI/ImageB]
>>
endobj

1 0 obj
6VæFö&  £ö& £ÃÂõGRõvRõ&VçBR"õ&W6÷W&6W2""ôÖVF&÷³SRã#sSSSSCãsc3ssS#Òô6öçFVçG2"#ãà¦VæFö&  £2ö& £ÃÂô6÷VçBôf'7BB"ôÆ7BB £ãà¦VæFö&  £Bö& £ÃÂô6÷VçBõFFÆSÄdTdcSccscS#3à¢ôFW7E³"õ¢CãÒõ&VçB2#ãà¦VæFö&  £Rö& £ÃÂõGRõvW0¢õ&W6÷W&6W2" ¢ôÖVF&÷²SRã#sSSSSCãsc3ssS#Ð¢ô¶G5²"Ð¢ô6÷VçBãà¦VæFö&  £Rö& £ÃÂõGRô6FÆörõvW2R ¢ô÷Vä7Föå³"õ¢çVÆÂçVÆÂÐ¢ô÷WFÆæW22 ¢ôÆærg"Ôe"£ãà¦VæFö&  £bö& £ÃÂô7&VF÷#ÄdTdcCCs#cssà¢õ&öGV6W#ÄdTdcD3cc#s#cSDccccccc3cS#3s$S3Cà¢ô7&VFöäFFRC£##3S###3cb³"srãà¦VæFö&  §&V`£p£cSS3Rb£#câ£â£SRâ£S3Râ£#sr n 
0001207107 00000 n 
0001195183 00000 n 
0001205618 00000 n 
0001205640 00000 n 
0001205833 00000 n 
0001206341 00000 n 
0001206686 00000 n 
0001206719 00000 n 
0001206942 00000 n 
0001206998 00000 n 
0001207232 00000 n 
0001207346 00000 n 
trailer
<</Size 17/Root 15 0 R
/Info 16 0 R
/ID [ <D11385A8145DB1B00FF47AF6B8EA7A56>
<D11385A8145DB1B00FF47AF6B8EA7A56> ]
/DocChecksum /0DB83F637B81D5ADBFE42918EF31FB33
>>
startxref
1207513
%%EOF
```

A few very critical parts are corrupted, notably the section that lists [xrefs](https://pypdf2.readthedocs.io/en/3.0.0/dev/pdf-format.html#the-pdf-format). 

On the other hand, entire sections have survived intact - enough that the pdf can be inspected with specialized tools like [peepdf](https://github.com/jesparza/peepdf):

```
└─[$] peepdf LeNautilus_corrupted.pdf -i        
Warning: PyV8 is not installed!!
Warning: pylibemu is not installed!!

File: LeNautilus_corrupted.pdf
MD5: 32fa7d732913e885c05d88bfde472a87
SHA1: 0acd69359f32d7cff48951cd5dab762d1fc7f54d
Size: 1247526 bytes
Version: 1.6
Binary: True
Linearized: False
Encrypted: False
Updates: 0
Objects: 7
Streams: 2
Comments: 0
Errors: 2

Version 0:
	Catalog: 15
	Info: 16
	Objects (7): [2, 3, 4, 8, 10, 11, 12]
		Errors (1): [8]
	Streams (2): [4, 2]
		Encoded (2): [4, 2]
		Decoding errors (1): [4]

PPDF>

```
```
PPDF> object 2

<< /Length 3 0 R
/Filter /FlateDecode >>
stream
0.1 w
q 0 0.028 595.247 841.861 re
W* n
1 1 1 rg
0 841.889 m
595.247 841.889 l 595.247 0.028 l 0 0.028 l 0 841.889 l
h
f*
q 595.276 0 0 842.06 0 0.028 cm
/Im4 Do Q
q 0.2039215686 0.1647058823 0.0235294117 rg
BT
104.202 88.582 Td /F1 90 Tf[<01>-6<020304>19<050607>-10<0809060A>]TJ
ET
Q
q 0.2039215686 0.1647058823 0.0235294117 rg
BT
53.093 773.999 Td /F1 24.009 Tf[<0B>2<0C>-1<0B>-1<0D>-25<0E>-3<0F>1<10>2<0D1112>-1<13>11<070C>2<14150416>-2<1409>2<17>-1<1819>-1<1A>2<141117>-1<1B>2<141A>-1<1C>-1<17>2<09>-1<09>2<140B>-1<1407>-4<1C>-1<1D>3<141E>-2<12>2<041F>]TJ
ET
Q
q 0.2039215686 0.1647058823 0.0235294117 rg
BT
136.403 42.576 Td /F1 24.009 Tf[<2008>2<02>-1<21>2<03222306>2<24>-1<25>3<0326>44<27>-1<02>-5<0A>20<07>3<0309>-1<27>2<1C>-1<02>-1<06>2<11>17<02>-1<0328>2<27>-1<0509>2<09>-1<02>-1<1103>3<2905>-17<2A2B>3<2C>-2<03>]TJ
ET
Q
q 0.2039215686 0.1647058823 0.0235294117 rg
BT
252.113 18.595 Td /F1 24.009 Tf[<2D>1<0316>2<2E>-12<2F>-12<09>-1<02>3<11>]TJ
ET
Q
Q 
endstream
```

This "object 2", occuring very early in the file, contains BT/ET blocks (Begin Text / End Text), which hold strings that will be displayed as plain text in the pdf. The [format](https://blog.idrsolutions.com/understanding-pdf-text-objects/) of those blocks goes something like this: 

```
BT
{x} {y} Td # draw at relative offset x,y
/F{i} {s}  # select font i at size s
[<xx>n<xx>n<xx>...]Tj # a list of the characters of the string, written as hexadecimal indices <xx> into a table of unicode characters,
                        # plus an optional offset n, positive or negative, for horizontal aligment of individual characters.
ET
```

The table that maps those indices to unicode characters is also defined inside the PDF file.    
It is referenced by the object that holds the font, which is object 10:

```
PPDF> object 10

<< /FirstChar 0
/Widths [ 0 580 340 220 700 420 460 320 240 240 320 440 440 520 500 580 240 300 440 440 500 700 460 440 700 440 440 440 440 620 680 240 600 460 220 400 340 220 340 240 440 520 400 220 280 280 620 400 ]
/Type /Font
/BaseFont /BAAAAA+Z003MediumItalic
/LastChar 47
/ToUnicode 9 0 R
/FontDescriptor 8 0 R
/Subtype /Type1 >>
```

Finally, the index to unicode translation table, referenced by the line `/ToUnicode 9 0 R`, is then found inside object 9:

```
PPDF> object 9

*** Error: Object not found!!
```

*Of course*, because nothing can go well ever, this particular section ended up fully corrupted! We can't read any of it.

But this is not over. We still have the individual indices that make up the characters of the strings, even if we don't know *which* index maps to *which* character.

Cleaning up the text blocks from before to keep only the indices:

```
<01><02><03><04><05><06><07><08><09><06><0A>
<0B><0C><0B><0D><0E><0F><10><0D><11><12><13><07><0C><14><15><04><16><14><09><17><18><19><1A><14><11><17><1B><14><1A><1C><17><09><09><14><0B><14><07><1C><1D><14><1E><12><04><1F>
<20><08><02><21><03><22><23><06><24><25><03><26><27><02><0A><07><03><09><27><1C><02><06><11><02><03><28><27><05><09><09><02><11><03><29><05><2A><2B><2C><03>
<2D><03><16><2E><2F><09><02><11>
```

We have a small but not *too* small amount of text, with characters that repeat at times...    
Could we possibly crack this as a substitution cipher?    

If your brain is the same flavour of broken as mine, you might enjoy working through this next part on your own, see how far you get. 

---
---
---

We really don't have enough text to use standard attacks like frequency analysis, so instead we need good guesses about the actual content of the text. What if, for example, it contained the flag, in the full 404CTF{...} format we're used to?


```

01 02 03 04 05 06 07 08 09 06 0A
                                                                                                                            

0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C               0                                                                 4                         }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
                                                                                                                    

2D 03 16 2E 2F 09 02 11


```

It actually could fit! 

After that, the most common chars are 03 and 14, where 03 only appears outside the flag and 14 only appears inside the flag.   
We can guess then that 03 could be spaces (__), and 14 could be underscores, as is common in other flags:


```

01 02 03 04 05 06 07 08 09 06 0A
      __

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C               0  _           _                 _           _                 _  4  _           _          }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
            __                __                __                      __                      __                __

2D 03 16 2E 2F 09 02 11
   __ 

```

Now we need another *really good guess*. The first line is two words, with a single repeated char in the second word; given the name of the pdf we're working with, there's something that could actually fit:

```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C            t  0  _     N     _  l              _           _           l  l  _  4  _  t        _       N  }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
    i  e    __        u       __        e  s  t __  l        e  u     e __        a  l  l  e    __     a          __

2D 03 16 2E 2F 09 02 11
   __           l  e

```

"I can't believe this actually might work." - famous last words, unattributed

We have almost readable french text for the 3rd line, from which we can guess even more characters:


```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C            t  0  _     N     _  l              _           _           l  l  _  4  _  t        _       N  }


20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '     e  u     e __     '  a  l  l  e    __     a          __

2D 03 16 2E 2F 09 02 11
   __           l  e  r

```

```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C   r        t  0  _     N     _  l              _  r        _     h     l  l  _  4  _  t  h     _       N  }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '  h  e  u  r  e __  d  '  a  l  l  e  r __     a          __

2D 03 16 2E 2F 09 02 11
   __           l  e  r

```

One last good guess before we sail into uncharted territory: the last line could work as a signature from the challenge author, [Smyler](https://github.com/SmylerMC):

```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C   r        t  0  _     N  S  _  l              _  r        _     h     l  l  _  4  _  t  h     _       N  }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '  h  e  u  r  e __  d  '  a  l  l  e  r __     a          __

2D 03 16 2E 2F 09 02 11
 - __  S  m  y  l  e  r

```

Too much of the flag is still missing, so we have to start guessing words in there too. 
We can get the D of DNS (capital D since lowercase d is already used for index 28):   

```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C   r        t  0  _  D  N  S  _  l              _  r        _     h     l  l  _  4  _  t  h     _        N  }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '  h  e  u  r  e __  d  '  a  l  l  e  r __     a          __

2D 03 16 2E 2F 09 02 11
 - __  S  m  y  l  e  r

```

Assuming the first word is some variation of "crypto", we can add some guesses to those characters, and also start keeping track of characters we haven't encountered yet:

```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C   r Y1 pP  t  0  _  D  N  S  _  l              _  r        _     h     l  l  _  4  _  t  h     _    Y1  N  }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '  h  e  u  r  e __  d  '  a  l  l  e  r __     a          __

2D 03 16 2E 2F 09 02 11
 - __  S  m  y  l  e  r


remaining:  123 56789  bc  fg   k    pq    vwx z     EFGHIJK M OPQR  UVWXYZ 

```

`r.._.h.ll` -> rev shell?

`4_th._.1N` -> 4 the win?

```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C   r  1 pP  t  0  _  D  N  S  _  l E3        5  _  r E3 vV  _  5  h E3  l  l  _  4  _  t  h E3  _ wW  1  N  }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '  h  e  u  r  e __  d  '  a  l  l  e  r __     a          __

2D 03 16 2E 2F 09 02 11
 - __  S  m  y  l  e  r


remaining:   23  6789  b   fg   k    pq    vwx z A   E GHIJK M OPQR  UVWXYZ

```

`l3..5_r3v_5h3ll` -> leaks rev shell?


```
01 02 03 04 05 06 07 08 09 06 0A
L  e  __ N  a  u  t  i  l  u  s

                                                                                                                            
0B 0C 0B 0D 0E 0F 10 0D 11 12 13 07 0C 14 15 04 16 14 09 17 18 19 1A 14 11 17 1B 14 1A 1C 17 09 09 14 0B 14 07 1C 1D 14 1E 12 04 1F
4  0  4  C  T  F  {  C   r  1 pP  t  0  _  D  N  S  _  l E3 A@ kK  5  _  r E3 vV  _  5  h E3  l  l  _  4  _  t  h E3  _ wW  1  N  }

20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '  h  e  u  r  e __  d  '  a  l  l  e  r __     a          __

2D 03 16 2E 2F 09 02 11
 - __  S  m  y  l  e  r


remaining:   23  6789  b   fg   k    pq    vwx z A   E GHIJK M OPQR  UVWXYZ

```

We've almost got the entire flag, but there are a lot of characters where we can't tell two possible choices apart:


```
404CTF{Cr1{p,P}t0_DNS_l{3,E}{A,@}{k,K}5_r{3,E}{v,V}_5h{3,E}ll_4_th{E,3}_{w,W}1N}

404CTF{Cr1pt0_DNS_l3Ak5_r3v_5h3ll_4_thE_w1N}

{p,P}
{E,3}
{A,@}
{k,K}
{v,V}
{w,W}
```

2^6 = 64 possible flags to try... and *that*'s if we got everything right so far. That `Cr1pt0` bit is weird, maybe it's `CrYptO` and the last word is `wYN`? what if it's not `4 th3 w1N` but `for thY w1N`? etc.   
That actually bumps the amount of combinations to something like 192, which starts to become really silly.

Up until this point things had lined up so perfectly, the pdf being corrupted in exactly the right spots, the text just long enough to attack by known plaintext - I was fully convinced this was part of the challenge.    
So I was almost ready to go and try all possible combinations for the flag ; still, it felt somewhat out of place for the challenge to end like this, so I contacted the author to show my work and ask if it was ok to bruteforce the flag from this point on.

He confirmed that I had gotten the flag almost right, but that I must have made a mistake somewhere, since everything that I was doing here was totally unintended. At that point I went back to look at the timestamp stuff, realised my mistake, and decoded the pdf properly.


And yet, if I had tried...

```
404CTF{Cr1pt0_DNS_l3Ak5_r3v_5h3ll_4_thE_w1N}
404CTF{Cr1pt0_DNS_l3@k5_r3v_5h3ll_4_thE_w1N}
```

---

What about this last word in the 3rd line? 

```
20 08 02 21 03 22 23 06 24 25 03 26 27 02 0A 07 03 09 27 1C 02 06 11 02 03 28 27 05 09 09 02 11 03 29 05 2A 2B 2C 03
 B  i  e  n __  j  o  u  é  , __  c  '  e  s  t __  l  '  h  e  u  r  e __  d  '  a  l  l  e  r __     a          __
```


That one is especially nasty. If you look at the [uncorrupted](LeNautilus.pdf) pdf, you can see what it's supposed to be: `flag !`.

But there's only one char before the a? This is because the chars actually map to unicode, and in unicode you can find nightmares like this: [ﬂ](https://www.fileformat.info/info/unicode/char/fb02/index.htm), aka U+FB02, LATIN SMALL LIGATURE FL. So it really is one character. If you try to select it in a pdf viewer you will notice that as well, but usually once copypasted elsewhere it is decomposed into f and l.

We can also confirm this by using `peepdf` to dump object 9, the character index to unicode table, from the uncorrupted pdf:

```
└─[$] peepdf LeNautilus.pdf -i            
Warning: PyV8 is not installed!!
Warning: pylibemu is not installed!!

File: LeNautilus.pdf
MD5: 373b32370932d3e64679c31303effc6a
SHA1: b2ade5199a9d6e6bdb09143c073a1af76fb79afa
Size: 1208059 bytes
Version: 1.6
Binary: True
Linearized: False
Encrypted: False
Updates: 0
Objects: 16
Streams: 4
Comments: 0
Errors: 0

Version 0:
	Catalog: 15
	Info: 16
	Objects (16): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
	Streams (4): [4, 9, 2, 6]
		Encoded (4): [4, 9, 2, 6]
		Decoding errors (1): [4]
	Suspicious elements:
		/OpenAction: [15]



PPDF> object 9

...
endcodespacerange
47 beginbfchar
<01> <004C>
<02> <0065>
<03> <0020>
...
...
<25> <002C>
<26> <0063>
<27> <2019>
<28> <0064>
<29> <0066006C>
<2A> <0067>
<2B> <00A0>
<2C> <0021>
<2D> <002D>
<2E> <006D>
<2F> <0079>
endbfchar
endcmap
...

```

Huh, actually, it wasn't even stored as FB02 at all, but as its decomposition into f (0066) and l (006C). So multi-character characters are a thing that can happen in PDFs (?!), and this whole adventure based on the assumption that 1 character index == 1 unicode character was flawed.

Still, it almost worked out! I'm glad the flag was in the pdf as text instead of images, and that Smyler added the extra text which made it almost possible for it to be recovered.    

This could have been a whole forensics challenge unto itself!
