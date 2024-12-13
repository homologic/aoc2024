#!/usr/bin/python3

from sage.all import *
import sys
from re import findall

lines = [] 

cur = []

s = 0

def solve(cur) :
    sol = matrix(ZZ,2,2,cur[:4]).transpose().solve_right(vector(ZZ,cur[4:]) + vector(ZZ,[10000000000000]*2))
    print(sol)
    is_valid = True
    for k in sol :
        if k not in ZZ or k < 0 :
            is_valid = False
            break
    if is_valid:
        return sol[0] * 3 + sol[1]
    return 0

for line in sys.stdin :
    if line == "\n" :
        s += solve(cur)
        cur = []
        continue
    for i in map(int,findall(r"[0-9]+", line)) :
        cur.append(i)

s+= solve(cur)
print(s)
