import sys
import itertools

s = 0

def check(res, numbers) :
    mask = 0
    answer = False
    for comb in itertools.product([0,1,2], repeat=len(numbers)-1) :
        i = 0
        r = numbers[0]
        for n in numbers[1:] :
            if comb[i] == 0 :
                r *= n
            elif comb[i] == 1 :
                r += n
            else :
                r = int(f"{r}{n}")
            if r > res :
                break
            i+=1
        if r == res :
            answer = True
            break
        mask += 1
    return answer


        
for line in sys.stdin :
    res, numb = line.strip().split(":")
    res = int(res)
    numbers = list(map(int,numb.split()))
    if check(res, numbers) :
        print(res)
        s += res

print(s)
    
        
    
    
