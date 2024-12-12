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

def count_perimeter(perimeters, comp, last_seen, i,j) :
    if last_seen != comp :
        perimeters[comp] += 1
        if last_seen is not None :
            perimeters[last_seen] += 1
    

for i in range(len(mp)) :
    last_seen = None
    for j in range(len(mp[0])) :
        comp = uf.find((i,j))
        areas[comp] += 1
        count_perimeter(perimeters,comp,last_seen,i,j)
        if j == len(mp[0]) -1 :
            perimeters[comp] += 1
        last_seen = comp
        

for j in range(len(mp[0])) :
    last_seen = None
    for i in range(len(mp)) :
        comp = uf.find((i,j))
        count_perimeter(perimeters,comp,last_seen,i,j)
        if i == len(mp) -1 :
            perimeters[comp] += 1
            
        last_seen = comp
s = 0
for comp in areas.keys() :
    s+= areas[comp] * perimeters[comp]

print(areas)
print(perimeters)
print(s)


    
    
        
    
    
