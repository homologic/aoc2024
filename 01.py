#!/usr/bin/python3

import sys
a = []
b = []
for line in sys.stdin :
    c,d = tuple(map(int, line.split()))
    a.append(c)
    b.append(d)
a.sort()
b.sort()
s = 0
for i,j in zip(a,b) :
    if i > j :
        s += i-j
    else :
        s += j-i
print(s)
