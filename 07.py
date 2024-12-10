import sys

s = 0

for line in sys.stdin :
    res, numb = line.strip().split(":")
    res = int(res)
    numbers = list(map(int,numb.split()))
    mask = 0
    answer = False
    while mask < (1 << len(numbers)) :
        i = 0
        r = numbers[0]
        for n in numbers[1:] :
            if (mask >> i) % 2 == 1 :
                r *= n
            else :
                r += n
            if n > res :
                break
            i+=1
        if r == res :
            answer = True
            break
        mask += 1
    if answer :
        s += res

print(s)
    
        
    
    
