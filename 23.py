#!/usr/bin/python3

import sys

class Node :
    def __init__(self, name):
        self.neighbors = set()

    def add_neigh(self, neigh) :
        self.neighbors.add(neigh)

    def degree(self) :
        return len(self.neighbors)

    def __lt__(self, other) :
        return self.degree() < other.degree()


nodes = {}

for line in sys.stdin :
    n = line.strip().split("-")
    for i,node in enumerate(n) :
        if not node in nodes :
            nodes[node] = Node(node)
        nodes[node].add_neigh(n[int(not i)])

triangs = set()
for name in sorted(nodes, key=nodes.get) :
    node = nodes[name]
    neighs = node.neighbors
    for i in neighs :
        nodes[i].neighbors.remove(name)
        for j in nodes[i].neighbors :
            if j in neighs and j != name :
                tri = [i,j,name]
                tri.sort()
                triangs.add(" " + " ".join(tri))


print(len([t for t in triangs if " t" in t]))
