Nn1,kk=map(int,input().split())
Xx=[]
L1=[]
for Y in range(Nn1):
    L=[int(Xx) for Xx in input().split()]
    Xx.append(L)
    if 0 in L:
        M=L.index(0)
        L1.append(M)
for Y in range(len(Xx)):
    if 0 in Xx[Y]:
        for Z in range(Kk):
            Xx[Y][Z]=0
for Y in L1:
    for Z in range(Nn1):
        Xx[Z][Y]=0
for Y in Xx:
    print(*Y)
