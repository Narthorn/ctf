#!/usr/bin/python

import sys

file = sys.argv[1]
offset = int(sys.argv[2])
step = int(sys.argv[3])

bits = ''
with open(file, "rb") as f:
    f.seek(offset)
    while True:
        b = f.read(1)
        if not b: break
        if ord(b) < 0x80:
            bits += '1'
        else: 
            bits += '0'
        f.seek(step,1)


i=0

def dprint(msg):
    print("At offset %i: %s" % (i,msg))
    print(bits[:i])
    #exit()

out = ''
skipping = 3
while (i<(len(bits)-20)):
 
    start = int(bits[i],2)
    i += 1
    
    if (skipping == 0 and start == 1): 
        print("skipping")
        skipping = 1
    if (skipping == 1 and start == 0): skipping = 2
    if (skipping == 2 and start == 1): skipping = 3
    if (skipping == 3 and start == 0): skipping = 0
    if (skipping > 0): continue
    
    char = bits[i:i+8]
    i += 8
    
    parity = int(bits[i],2)
    i += 1
    if ((char.count('1') % 2) != parity):
        dprint("wrong parity for block %s (got %i)" % (char,parity))
    else:
        out += chr(int(char[::-1],2))
    
    stop = int(bits[i],2)
    i += 1
    if (stop != 1):
        dprint("stop bit not 1")
        
print(out)
