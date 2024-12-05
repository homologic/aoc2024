from graphlib import TopologicalSorter
import sys

pred = {}
succ = {}

for line in sys.stdin :
    if line == "\n" :
        break
    n,m = line.strip().split("|")
    if m in pred :
        pred[m].add(m)
    else :
        pred[m] = set([m])
    if n in succ :
        succ[n].add(m)
    else :
        succ[n] = set([m])

print(succ, pred)

s = 0 
for line in sys.stdin :
    pages = line.strip().split(",")
    print(pages)
    Fail = False
    for i,page in enumerate(pages) :
        for j,p in enumerate(pages) :
            if i < j :
                if p in succ and page in succ[p] :
                    Fail = True
                    print(page,p)
                    break
            elif j < i :
                if p in pred and page in pred[p] :
                    Fail = True
                    print(page,p)
                    break
            
        if Fail :
            break
    if not Fail :
        s += int(pages[len(pages)//2])

print(s)
