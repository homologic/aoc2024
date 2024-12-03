#!/usr/bin/python3

import sys
import re
s = 0
    

for line in sys.stdin :
    for match in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', line) :
        s += int(match[0]) * int(match[1])

print(s)
