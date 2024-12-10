import sys
from collections import defaultdict
from itertools import combinations

antennae = defaultdict(set)
mp = [] 
for i,line in enumerate(sys.stdin) :
    mp.append(list(line.strip()))
    for j,c in enumerate(line) :
        if c.isalnum() :
            antennae[c].add((i,j))

antinodes = set()

def in_bounds(c) :
    x,y = c
    if x < 0 or y < 0:
        return False
    if x >= len(mp) or y >= len(mp[0]) :
        return False
    return True

for j in antennae :
    for a,b in combinations(antennae[j],2) :
        diff = (a[0]-b[0],a[1]-b[1])
        c = (a[0] +  diff[0], a[1] + diff[1])
        d = (b[0] - diff[0], b[1] - diff[1])
        if in_bounds(c) :
            antinodes.add((c))
        if in_bounds(d) :
            antinodes.add((d))


for i,k in enumerate(mp) :
    for j,l in enumerate(k) :
        if (i,j) in antinodes and l == ".":
            mp[i][j] = "#"
print("\n".join(["".join(line) for line in mp]))

print(len(antinodes))
