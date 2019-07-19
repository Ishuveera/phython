import math
AA1,Z1=map(int,input().split())
CC1=[]
BB1=list(map(int,input().split()))
for Y in range(0,ZZ1):
    L,H=map(int,input().split())
    CC1.append([L,H])
for Y in CC1:
    nn=Y[0]-1
    mm=Y[1]-1
    print(math.gcd(BB1[nn],BB1[mm]))
