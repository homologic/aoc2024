#!/usr/bin/python3

import sys
import re
import numpy

lines = []

def count_xmas(s) :
    return len(re.findall("XMAS",s)) + len(re.findall("SAMX",s))
    
s = 0
for line in sys.stdin :
    s += count_xmas(line) # count horizontals
    lines.append(line.strip())


for i in range(len(lines[0])) :
    s += count_xmas("".join([line[i] for line in lines])) ## verticals

lines = list(map(list, lines))
    
for i in range(-len(lines), len(lines)): 
    s += count_xmas("".join(numpy.diagonal(lines, offset=i)))

lines = numpy.fliplr(lines) 
for i in range(-len(lines), len(lines)) :
    s += count_xmas("".join(numpy.diagonal(lines, offset=i, axis1=1, axis2=0)))

print(s)

