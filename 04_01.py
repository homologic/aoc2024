#!/usr/bin/python3

import sys
import re
import numpy

lines = []

A = []
s = 0
for line in sys.stdin :
    for j,i in enumerate(line) :
        if i == "A" :
            A.append((j,len(lines)))
    lines.append(line.strip())

x = len(lines[0])
y = len(lines)

for i,j in A :
    if i == 0 or i == x-1 or j == 0 or j == y-1 :
        continue
    if set([lines[j-1][i-1],lines[j+1][i+1]]) == {"M","S"} and set([lines[j-1][i+1],lines[j+1][i-1]]) == {"M","S"} :
        s += 1


print(s)
