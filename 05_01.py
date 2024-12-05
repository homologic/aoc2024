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



def check_and_fix(pages) :
    Fail = False
    for i,page in enumerate(pages) :
        for j,p in enumerate(pages) :
            if i < j :
                if p in succ and page in succ[p] :
                    pages[i] = p
                    pages[j] = page
                    Fail = True
                    break
            elif j < i :
                if p in pred and page in pred[p] :
                    pages[i] = p
                    pages[j] = page
                    Fail = True
                    break
        if Fail :
            break
    return Fail
        
s = 0 
for line in sys.stdin :
    pages = line.strip().split(",")
    Fail = check_and_fix(pages)
    if not Fail :
        continue
    while Fail :
        Fail = check_and_fix(pages)
    s += int(pages[len(pages)//2])


print(s)
