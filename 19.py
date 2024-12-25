#!/usr/bin/python3

import sys
from functools import cache

towellist = input().strip().split(", ")

@cache
def check_towel(stack) :
    ways = 0
    if stack == "" :
        return 1
    for towel in towellist :
        if stack.startswith(towel) :
            ways += check_towel(stack[len(towel):]) 
    return ways
input()

ways = 0
s = 0 
for line in sys.stdin :
    w = check_towel(line.strip())
    if w :
        ways += w
        s += 1

print(s)
print(ways)

        

