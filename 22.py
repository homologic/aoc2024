#!/usr/bin/python3

import sys

def cycle(secret) :
    for i in range(2000) :
        secret ^= (secret << 6)
        secret %= 16777216
        secret ^= (secret >> 5)
        secret ^= (secret << 11)
        secret %= 16777216
    return secret

s = 0
for line in sys.stdin :
    s+= cycle(int(line))
        
print(s)
