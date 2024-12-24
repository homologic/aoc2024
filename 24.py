#!/usr/bin/python3

from graphlib import TopologicalSorter
import sys

inputs = {}

for line in sys.stdin :
    if line == "\n" :
        break
    k,v = line.split(":")
    inputs[k] = v.strip() == "1"

graph = {}
rules = {}

for line in sys.stdin :
    rule, out = line.strip().split("->")
    out = out.strip()
    parsed = rule.split()
    operator = parsed[1]
    graph[out] = set([parsed[0],parsed[2]])
    rules[out] = (parsed[0],parsed[2],operator)


def compute(rule) :
    operator = rule[-1]
    a, b = inputs[rule[0]], inputs[rule[1]]
    if operator == "AND" :
        return a and b
    if operator == "OR" :
        return a or b 
    if operator == "XOR" :
        return (a or b) and not (a and b)
    
            
ts = TopologicalSorter(graph)
z = {}
for out in ts.static_order() :
    if out in inputs :
        continue # already computed
    inputs[out] = compute(rules[out])
    if out[0] == "z" :
        ind = int(out[1:])
        z[ind] = inputs[out]
out = 0
for k,v in sorted(z.items()) :
    if v :
        out += (1 << k)
print(out)

