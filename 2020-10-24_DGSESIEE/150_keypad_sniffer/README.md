Keypad Sniffer
==============

**Category** : Hardware  
**Score** : 150 points  
**Solved** : 152 times  

---

Interesting challenge. I made two[¹](#1) big[²](#2) mistakes here.

---

>Le code d'accès d'un centre militaire de télécommunications est saisi sur un clavier. Un agent a accédé au matériel (Cf. photos face avant et face arrière du clavier) et a inséré un dispositif pour enregister les données binaires qui transitent sur le connecteur du clavier. Le fichier joint (keypad_sniffer.txt) comprend les données binaires (échantillonnées à une fréquence de 15 kHz) au moment où une personne autorisée rentrait le code d'accès. Retrouvez le code d'accès.
>
>Le flag est de la forme DGSESIEE{X} où X est le code saisi

---

### Files

 * [keypad_sniffer.txt]() (f5660a0b1c8877b67d7e5ce85087138cbd0c061b0b244afc516c489b39a7f79d)
 * [keypad_face.jpg]() (b39c0d732f645fc73f41f0955233bec3593008334a8796d2f1208346f927fef2)
 * [keypad_back.jpg]() (1f5d41c3521d04494779e43a4d5fae7cb14aad44e6e99cf36642ff4e88fab69f)

<img src="keypad_face.jpg" width="40%"/> <img src="keypad_back.jpg" width="40%" />

This challenge requires learning how [Keypad Scanning](https://arduinogetstarted.com/tutorials/arduino-keypad) works. A given line, say 101111101110 in keypad_sniffer.txt can be mapped to the pinout in the image as such:

```
power‾|
      |   ______rows (output)
      1 0 1111
      1 0 1110 
        | ‾‾‾‾‾‾columns (input)
ground__|
```

Each column pin is being sequentially pulled low, and the row pins are read to see if any of them is low; If that's the case, then that means the key at the corresponding row/column has been pressed.

We can write a simple script to simulate the keypad and output the correct letter each time we detect a keypress:

```python
#!/usr/bin/python3
from math import log2

keypad = [["1","2","3","F"],
          ["4","5","6","E"],
          ["7","8","9","D"],
          ["A","0","B","C"]]

keypad_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

sol = ""
with open("keypad_sniffer.txt") as file:
  for line in file:
    x = int(line.strip(),2)
    col = 0b1111 - ( x       & 0b1111) # bits  0-4, flipped
    row = 0b1111 - ((x >> 6) & 0b1111) # bits 10-6, flipped
    if (row != 0):
        c = 3-int(log2(col)) # column index, LSB first
        r = 3-int(log2(row)) # row index,    LSB first
        if (keypad_state[c][r] != 1):
            sol += keypad[r][c]        # keypad is indexed row/column,
            keypad_state[c][r] = 1     # but keypad_state is indexed column/row,
    else:
       c = 3-int(log2(col)) 
       keypad_state[c] = [0,0,0,0]     # just so I can clear a whole row at once

print("DGSESIEE{%s}" % sol)
```

When writing this, we don't yet really know which bits are rows or columns, and whether the bits are LSB or MSB first (ie, whether "0001" means first column or fourth column), so we end up having to play around a little and try out multiple flags. The correct one, as printed by the script, is DGSESIEE{AE78F55C666B23011924}.

---

<a name="1">¹</a>: First off, I didn't know about keypad scanning, so my reaction upon seeing the textfile with all the binary was "well, i guess it's 8 bits of data, plus 4 bits that's some kind of monotonically increasing counter at the end". So I cut out the last 4 bytes, removed all 0b10111110 (guessing this meant no input since it was the most common, and accidentally being correct), then ran uniq on the file to delete duplicates. I was left with just a few notable lines, each corresponding to a given keystroke. Then, I lost a lot of time fruitlessly trying to coax ascii out of the remaining 8bits, figuring it just had to be jumbled up because the electrical connections on the board looked jumbled up.

<a name="2">²</a>: Second, after I had read up on keypad scanning, I figured I could simply filter out all the lines with output 1111 (no key pressed), which is exactly what I had already done in the first step, so I would just have to read the correct bits for this time.

I still didn't know in which ways to read the keypad, so for every flag I wanted to try, I also had to try all possible variants (transposing the keypad, reverse indexing either rows or columns or both, and all possible combinations). Since nothing I tried seemed to be the answer, I thought that I had missed a different way to read the keypad or the pinout, so I I kept trying hard to come up with variants. Mostly, I came up with things like rotating the keypad 90°, but that turns out to be the same as simultaneously transposing rows/columns and reverse indexing columns - or reverse indexing rows, I forget which.

That wasn't the issue, though. The mistake I made was reusing my filtered lines from the first part. I had filtered out all the the "no output" lines **BEFORE** removing duplicate lines, which meant that any *repeated* press (press/no output/press) was now indistinguishable from a single press...

Once I realised that, I tried to come up with some better filtering that would still remove duplicates while preserving one "no input" between pressed, but quickly gave up and instead wrote the script from earlier to simulate the keypad.
