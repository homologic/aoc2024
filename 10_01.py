import sys
from collections import defaultdict

topomap = []
trailheads = []


def get_neighbours(x,y) :
    neigh = []
    for i in [-1,1] :
        if x + i < len(topomap) and x + i >= 0:
            neigh.append((x+i,y))
        if y + i < len(topomap[0]) and y + i >= 0:
            neigh.append((x,y+i))                
    return neigh
    

def search(startpos, visited, summits, parents) :
    x,y = startpos
    elevation = topomap[x][y]
    visited.add((x,y))
    for xx, yy in get_neighbours(x,y) :
        if topomap[xx][yy] == elevation+1 :
            parents[(xx,yy)].add((x,y))
            if not (xx,yy) in visited :
                if topomap[xx][yy] == 9 :
                    summits.add((xx,yy))
                    continue
                search((xx,yy), visited, summits, parents)
    return summits, parents
    

for line in sys.stdin :
    topomap.append(list(map(int,line.strip())))
    for i,k in enumerate(topomap[-1]) :
        if k == 0 :
            trailheads.append((len(topomap)-1,i))


def find_all_paths(parents, start, end) :
    if start == end :
        return [start]
    return [path + end for parent in parents[end] for path in find_all_paths(parents,start,parent)]

s = 0
for startpos in trailheads:
    summits, parents = search(startpos, set(), set(), defaultdict(set))
    s += sum([len(find_all_paths(parents,startpos,i)) for i in summits])
print(s)
        
