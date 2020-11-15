#!/usr/bin/python

from sys import argv,setrecursionlimit

setrecursionlimit(10000)

with open(argv[1]+".in") as f:
    total, _ = map(int,f.readline().split(" "))
    items = sorted(enumerate(map(int, f.readline().split(" "))),key=(lambda t: t[1]),reverse=True)

def rec(items=items, best=(total,[])):
    best_total, best_list = best
    for j,(i,a) in enumerate(items):
        new_total, new_list = new = (best_total-a,best_list+[i])
        if (new_total == 0): return new 
        remaining = [(k,x) for k,x in items[j+1:] if (x,[]) <= new]
        if not remaining: continue
        best = min(best, rec(remaining, new))
        if (best[0] == 0): return best
    return best

best_total, best_list = rec()
with open(argv[1]+".out.txt","w") as out:
    out.write(f"{len(best_list)}\n")
    out.write(" ".join(map(str,sorted(best_list))))
    out.write("\n")

with open(argv[1]+".in") as f:
    total, _ = map(int,f.readline().split(" "))
    items = list(map(int, f.readline().split(" ")))

assert(best_total == 0)
assert(total == sum(items[i] for i in best_list))
