N=int(input())
L=list(map(int, input().split()))[:N]
MX=max(L)
FNL=[]
for X in range(0,len(L)):
    new=L[X:]
    FX=max(new)
    if(L[X]==FX):
        FNL.append(L[X])
print(*FNL)
print(MX)
