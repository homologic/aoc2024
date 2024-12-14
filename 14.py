#!/usr/bin/python3

import sys
from re import findall

dimensions = 101,103

mp = [[0 for i in range(dimensions[0])] for j in range(dimensions[1])]
quadrants = [0 for i in range(4)]

def in_quadrant(pos) :
    if pos[0] < dimensions[0]//2 and pos[1] < dimensions[1] //2 :
        return 0
    elif pos[0] < dimensions[0]//2 and pos[1] > dimensions[1] //2 :
        return 1
    elif pos[0] > dimensions[0]//2 and pos[1] < dimensions[1] //2 :
        return 2
    elif pos[0] > dimensions[0]//2 and pos[1] > dimensions[1] //2 :
        return 3
    return None

    

def move(initial, direction) :
    newpos = [(initial[i] + direction[i]*100) % dimensions[i] for i in [0,1]]
    mp[newpos[1]][newpos[0]] += 1
    return in_quadrant(newpos)

for line in sys.stdin :
    numbers = list(map(int,findall(r"-?[0-9]+", line)))
    initial = numbers[:2]
    direction = numbers[2:]
    mv = move(initial,direction)
    if mv is not None :
        quadrants[mv] += 1



print("\n".join(["".join(map(str,i)) for i in mp]))

s = 1
for i in quadrants :
    s*= i
print(s)
