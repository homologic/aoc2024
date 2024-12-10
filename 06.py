
import sys

field = []
pos = ()
s = 0

d = (-1,0)
def step() :
    global pos,d,s
    x,y = (pos[0]+d[0],pos[1]+d[1])
    if field[pos[0]][pos[1]] in (".", "^") :
        field[pos[0]][pos[1]] = "X"
        s+=1
    if x >= len(field) or y >= len(field[0]) :
        return False
    if field[x][y] == "#" :
        d = (d[1], -d[0])
    else :
        pos = (x,y)
    return True
    

for i,line in enumerate(sys.stdin) :
    field.append(list(line.strip()))
    if "^" in line :
        pos = (i,line.index("^"))


while True:
    if not step() :
        break

print("\n".join(["".join(line) for line in field]))
print(pos)
print(s)
