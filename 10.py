import sys

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
    

def search(startpos, visited=set(), summits=set()) :
    x,y = startpos
    elevation = topomap[x][y]
    visited.add((x,y))
    for xx, yy in get_neighbours(x,y) :
        if topomap[xx][yy] == elevation+1 :
            if not (xx,yy) in visited :
                if topomap[xx][yy] == 9 :
                    summits.add((xx,yy))
                    continue
                search((xx,yy), visited, summits)
    return summits
    

for line in sys.stdin :
    topomap.append(list(map(int,line.strip())))
    for i,k in enumerate(topomap[-1]) :
        if k == 0 :
            trailheads.append((len(topomap)-1,i))

print(trailheads)

print(sum([len(search(startpos, set(), set())) for startpos in trailheads]))
        
