#!/usr/bin/python3

import sys
a = []
b = {} 
for line in sys.stdin :
    c,d = tuple(map(int, line.split()))
    a.append(c)
    if d in b :
        b[d] +=1
    else : 
        b[d] = 1
s = 0
for i in a :
    if i in b :
        s += b[i] * i
print(s)
