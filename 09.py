import sys


disk = []

layout = input()
free = []
files = []

occ = True
ID = 0
ind = 0
for i in layout.strip() :
    size = int(i)
    if occ :
        disk += [ID]*size
        files.insert(0,(ind,ID,size))
        ID += 1
    else :
        disk += [-1]*size
        free.append((ind,size))
    occ = not occ
    ind += size

check = 0
for index, ID,size in files :
    moved = False
    for i,j in enumerate(free) :
        ind,fsize = j
        if size <= fsize and index > ind :
            moved = True
            free[i] = (ind+size,fsize-size)
            freed = free[ID-1]
            free[ID-1] = (freed[0],freed[1]+size)
            if ID < len(free) and freed[0] + freed[1] + size + 1 == free[ID][0] :
                free[ID-1] = (freed[0], freed[1] + size + free[ID][0])
                free[ID] = (0,0)
            for k in range(size) :
                check += (ind + k) * ID
                disk[ind + k] = ID
                disk[index + k] = -1
            break
    if not moved :
        for k in range(size) :
            check += (index + k) * ID
    
print(check)

