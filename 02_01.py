#!/usr/bin/python3

import sys
s = 0

def check_report(r, tolerate=True) :
    pos = False
    neg = False
    fails = 0
    for i in range(len(r)-1) :
        d = int(r[i+1]) - int(r[i])
        if d == 0 :
            fails +=1
        if d < 0 :
            neg = True
        else :
            pos = True
        if pos and neg :
            fails += 1
        if d < -3 or d > 3 :
            fails += 1
        if not tolerate and fails > 0 :
            return False
    if fails > 0 :
        for i in range(len(r)) :
            cp = r[:]
            del cp[i]
            if check_report(cp, False) :
                return True
        return False
    return True
    
    

for line in sys.stdin :
    if check_report(line.split()) :
        s += 1

print(s)
