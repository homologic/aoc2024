#!/usr/bin/python3

import sys
from collections import defaultdict

prices = defaultdict(int)

def cycle(secrets) :
    for secret in secrets :
        index = (0,0,0,0)
        last_price = 0
        seen = set()
        for i in range(2000) :
            secret ^= (secret << 6)
            secret %= 16777216
            secret ^= (secret >> 5)
            secret ^= (secret << 11)
            secret %= 16777216
            price = secret % 10
            index = (price-last_price,index[0],index[1],index[2])
            last_price = price
            if i > 3 and index not in seen :
                seen.add(index)
                prices[index] += price


secrets = []

for line in sys.stdin :
    secrets.append(int(line))


cycle(secrets)
print(max(prices.values()))

