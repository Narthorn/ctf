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
    col = 0b1111 - ( x       & 0b1111)
    row = 0b1111 - ((x >> 6) & 0b1111)
    if (row != 0):
        c = 3-int(log2(col))
        r = 3-int(log2(row))
        if (keypad_state[c][r] != 1):
            sol += keypad[r][c]        # keypad is indexed row/column,
            keypad_state[c][r] = 1     # but keypad_state is indexed column/row,
    else:
       c = 3-int(log2(col))
       keypad_state[c] = [0,0,0,0]     # just so I can clear a whole row at once

print("DGSESIEE{%s}" % sol)
