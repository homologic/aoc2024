#!/usr/bin/python3

import sys
s = 0

def check_report(r) :
    pos = False
    neg = False
    for i in range(len(r)-1) :
        d = int(r[i+1]) - int(r[i])
        if d == 0 :
            return False
        if d < 0 :
            neg = True
        else :
            pos = True
        if pos and neg :
            return False
        if d < -3 or d > 3 :
            return False
    return True
    
    

for line in sys.stdin :
    if check_report(line.split()) :
        s += 1

print(s)
