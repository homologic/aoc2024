#!/usr/bin/python3


def run_step(line) :
    newline = []
    for k in line :
        if k == "0" :
            newline.append("1")
        elif len(k) % 2 == 0 :
            newline.append(str(int(k[0:len(k)//2])))
            newline.append(str(int(k[len(k)//2:])))
        else :
            newline.append(str(int(k)*2024))
    return newline

line = input().strip().split()

for i in range(25) :
    line = run_step(line)

print(len(line))


