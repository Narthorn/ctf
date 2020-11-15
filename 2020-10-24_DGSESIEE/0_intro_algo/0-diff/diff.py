#!/usr/bin/python3

out = b""
with open("original.txt","rb") as orig:
    with open("intercepte.txt","rb") as inter:
        while True:
            o = orig.read(1)
            i = inter.read(1)
            if not o or not i: break

            if o != i:
                out += i
                orig.seek(-1,1)

with open("diff","wb") as diff: diff.write(out)
