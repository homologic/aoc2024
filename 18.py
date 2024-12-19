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



start = (0,0)
end = (70,70)
limit = 1024

def get_neighbours(u, walls) :
    i,j = u
    items = []
    for k in [-1,1] :
        if (i+k,j) not in walls and i + k >= 0 and i+k <= end[0] :
            items.append(((i+k,j),1))
        if (i,j+k) not in walls and j + k >= 0 and j+k <= end[1] :
            items.append(((i,j+k),1))
    return items



field = [["." for i in range(end[0]+1)] for j in range(end[1]+1)]
walls = set()



for i,line in enumerate(sys.stdin) :
    if i == limit :
        break
    walls.add(tuple(map(int,line.split(","))))

print(walls)

for i,j in walls:
    field[j][i] = "#"

pq = PQueue()
dist = {}
dist[start] = 0
prev = defaultdict(set)
pq.add(start,0)



while pq.is_not_empty() :
    u = pq.pop()
    i,j = u
    if (i,j) == end :
        print(f"distance: {dist[u]}")
        while True :
            if prev[u] :
                u = prev[u].pop()
            else :
                break
            x,y = u
            field[y][x] = "O"
        break
    for neigh, cost in get_neighbours(u,walls) :
        #print(neigh, cost)
        alt = dist[u] + cost
        if not neigh in dist or dist[neigh] > alt :
            prev[neigh] = set([u])
            dist[neigh] = alt
            pq.add(neigh,alt)
        elif dist[neigh] == alt :
            prev[neigh].add(u)


print("\n".join(["".join(line) for line in field]))
