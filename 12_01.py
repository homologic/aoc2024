import sys
from collections import defaultdict

class UnionFind :
    def __init__(self) :
        self.parent = {}

        
    def find(self, p) :
        if not p in self.parent :
            self.parent[p] = p
            return p
        orig = p
        while (p != self.parent[p]) :
            p = self.parent[p]
        self.parent[orig] = p
        return p

    def union(self, p, q) :
        pparent = self.find(p)
        qparent = self.find(q)
        self.parent[qparent] = pparent


uf = UnionFind()
mp = []
for i,line in enumerate(sys.stdin) :
    mp.append(line.strip())
    for j,c in enumerate(line.strip()) :
        uf.find((i,j))
        if j > 0 and line[j-1] == c :
            uf.union((i,j),(i,j-1))
        if i > 0 and mp[i-1][j] == c :
            uf.union((i-1,j),(i,j))

areas = defaultdict(int)
perimeters = defaultdict(int)
pf = UnionFind()

def unite_adj(pf,comp, i,j,d) :
    if comp is None: 
        return
    pf.find((i,j,comp, d))
    if d[0] == "-" :
        if (i-1,j,comp,d) in pf.parent :
            pf.union((i,j,comp,d),(i-1,j,comp,d))
    else :
        if (i,j-1,comp,d) in pf.parent :
            pf.union((i,j-1,comp,d),(i,j,comp,d))

def perimeter(pf, comp, last_seen, i, j, d) :
    if last_seen != comp :
        for k,kp in enumerate([comp, last_seen]) :
            unite_adj(pf,kp,i,j,d+str(k))
    if d == "-" and j == len(mp[0]) -1 :
        unite_adj(pf,comp,i,j+1,"-0")
    elif d == "|" and i == len(mp) - 1 :
        unite_adj(pf,comp,i+1,j,"|0")


    
            
for i in range(len(mp)) :
    last_seen = None
    for j in range(len(mp[0])) :
        comp = uf.find((i,j))
        areas[comp] += 1
        perimeter(pf,comp,last_seen,i,j,"-")
        last_seen = comp
        
        

for j in range(len(mp[0])) :
    last_seen = None
    for i in range(len(mp)) :
        comp = uf.find((i,j))
        perimeter(pf,comp,last_seen,i,j,"|")
        last_seen = comp
s = 0
sides = set([pf.find(p) for p in pf.parent])
for p in sides :
    comp = p[2]
    perimeters[comp] += 1
for comp in areas.keys() :
    s+= areas[comp] * perimeters[comp]

print(s)


    
    
        
    
    
