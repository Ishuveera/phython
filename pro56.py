S,P=map(int,input().split())
N=list(map(int,input().split()))
C=0
for X in N:
    K=86400-X
    P-=K
    C+=1
    if P<=0:
        break  
print(C)
