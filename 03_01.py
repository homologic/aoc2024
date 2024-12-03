#!/usr/bin/python3

import sys
import re
s = 0
    
enabled = True
for line in sys.stdin :
    spans = [(0,enabled)]
    for match in re.finditer(r'don\'t\(\)|do\(\)', line) :
        if match.group(0) == 'do()' :
            spans.append((match.start(), True))
        else :
            spans.append((match.start(), False))
    spans.append((len(line),spans[-1][1]))
    for i in range(len(spans)-1) :
        j = spans[i]
        enabled = j[1]
        if enabled :
            l = line[j[0]:spans[i+1][0]]
            for match in re.finditer(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', l) :
                s += int(match.group(1)) * int(match.group(2))

print(s)
