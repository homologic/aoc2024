#!/usr/bin/python3

import heapq
from collections import defaultdict
import sys

field = []

start = []
end = []

class PQueue :
    def __init__(self) :
        self.pq = []
        self.entries = {}
    
    def add(self, item, cost) :
        if item in self.entries :
            self.update_cost(item,cost)
        else :
            entry = [cost, item]
            self.entries[item] = entry
            heapq.heappush(self.pq, entry)

    def update_cost(self, item, cost) :
        if self.entries[item][0] > cost :
            newentry = [cost, item]
            entry = self.entries.pop(item)
            entry[1] = ()
            self.entries[item] = newentry
            heapq.heappush(self.pq, newentry)

    def pop(self) :
        while self.pq :
            cost, item = heapq.heappop(self.pq)
            if item != () :
                del self.entries[item]
                return item
    def is_not_empty(self) :
        return self.pq != []
    
def get_neighbours(u) :
    i,j,d = u
    items = [((i,j,not d),1000)] # rotate 90 degrees]
    for k in [-1,1] :
        if d :
            if field[i+k][j] != "#" :
                items.append(((i+k,j,d),1))
        else:
            if field[i][j+k] != "#" :
                items.append(((i,j+k,d),1))
    return items

for line in sys.stdin :
    if "S" in line :
        start = (len(field),line.index("S"),False)
    elif "E" in line :
        end = (len(field),line.index("E"))
    field.append(list(line.strip()))
    
pq = PQueue()
dist = {}
dist[start] = 0
prev = defaultdict(set)
pq.add(start,0)
endp = ()
best_dist = 0


def backtrack(prev, start, end, visited) :
    i,j,d = end
    field[i][j] = "O"
    visited.add((i,j))
    if start == end :
        return [[start]]
    pth = []
    for parent in prev[end] :
        for path in backtrack(prev,start,parent, visited) :
            pth.append(path+[end])
    return pth 


while pq.is_not_empty() :
    u = pq.pop()
    i,j,d = u
    if (i,j) == end :
        print(f"distance: {dist[u]}")
        endp = u
        visited = set()
        backtrack(prev,start,u,visited)
        print(f"Visited: {len(visited)}")
        break
    for neigh, cost in get_neighbours(u) :
        #print(neigh, cost)
        alt = dist[u] + cost
        if not neigh in dist or dist[neigh] > alt :
            prev[neigh] = set([u])
            dist[neigh] = alt
            pq.add(neigh,alt)
        elif dist[neigh] == alt :
            prev[neigh].add(u)


print("\n".join(["".join(line) for line in field]))
