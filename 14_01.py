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

    

def move(mp, initial, direction, dist) :
    newpos = [(initial[i] + direction[i]*dist) % dimensions[i] for i in [0,1]]
    mp[newpos[1]][newpos[0]] += 1
    return newpos

robots = []
f = open("input/14.txt", "r")
for line in f :
    numbers = list(map(int,findall(r"-?[0-9]+", line)))
    initial = numbers[:2]
    direction = numbers[2:]
    robots.append((initial,direction))


i = 0
while True:
    inp = input()
    dist = 1
    try :
        dist = int(inp)
    except:
        pass
    i+=dist
    newrobots = robots[:]
    robots = []
    mp = [[0 for i in range(dimensions[0])] for j in range(dimensions[1])]
    for pos,direction in newrobots :
        robots.append((move(mp,pos,direction,dist),direction))
    print(i)
    print("\n".join(["".join(map(str,i)).replace("0",".") for i in mp]))


s = 1
for i in quadrants :
    s*= i
print(s)
