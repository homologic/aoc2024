#!/usr/bin/python3

from functools import cache

@cache
def run_step(k, depth=0) :
    if depth == 75 :
        return 1
    if k == "0" :
        return run_step("1", depth+1)
    elif len(k) % 2 == 0 :
        return run_step(str(int(k[0:len(k)//2])),depth+1 ) + run_step(str(int(k[len(k)//2:])), depth+1)
    else :
        return run_step(str(int(k)*2024), depth+1)

line = input().strip().split()


print(sum([run_step(stone) for stone in line]))


