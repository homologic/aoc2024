import sys
import itertools


keys = []
locks = []
curkey = [0 for i in range(5)]
counter = 0
lock = True

for line in sys.stdin :
    if counter == 0 and "#" in line :
        lock = True
    elif counter == 0 :
        lock = False
    if line == "\n" :
        if lock :
            locks.append(curkey[:])
        else :
            keys.append(curkey[:])
        curkey = [0 for i in range(5)]
        counter = 0
        continue
    for i,j in enumerate(line.strip()) :
        if j == "#" :
            curkey[i] += 1
    counter += 1


if lock :
    locks.append(curkey[:])
else :
    keys.append(curkey[:])

print(locks)
print(keys)

def fits(key,lock) :
    for i,j in zip(key,lock) :
        if i + j > 7 :
            return False
    return True

s = 0
for key,lock in itertools.product(keys,locks) :
    if fits(key,lock) :
        print(key,lock)
        s += 1

print(s)
