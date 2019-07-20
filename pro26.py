def sub(aa): 
    N = len(aa) 
    sub = [1]*N 
    for X in range (1 , N): 
        for Y in range(0 , X): 
            if aa[X] > aa[Y] and sub[X]< sub[Y] + 1 : 
                sub[X] = sub[Y]+1
    maximum = 0
    for X in range(N): 
        maximum = max(maximum , sub[X])  
    return maximum
ar=int(input())
aa = list(map(int,input().split()))
print (sub(aa))
