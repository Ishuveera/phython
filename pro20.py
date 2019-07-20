import sys 
def inCoinspi(coinspi, mo1, Vd): 
    if (Vd == 0): 
        return 0
    res = sys.maxsize 
    for X in range(0, mo1): 
        if (coinspi[X] <= Vd): 
            sub_res = inCoinspi(coinspi, mo1, Vd-coinspi[X]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1 
    return res
N,Vd=list(map(int,input().split()))
coinspi = list(map(int,input().split())) 
mo1= len(coinspi) 
print(inCoinspi(coinspi, mo1, Vd)) 
