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


maxcliques = []

def bron_kerbosch(R, P, X) :
    if not P and not X :
        maxcliques.append(R)
        return True
    p = list(P)
    for v in p :
        bron_kerbosch(R.union(set([v])), P.intersection(nodes[v].neighbors), X.intersection(nodes[v].neighbors))
        P.remove(v)
        X.add(v)


bron_kerbosch(set(),set(nodes.keys()),set())

maxcliques.sort(key=len)
print(",".join(sorted(maxcliques[-1])))
