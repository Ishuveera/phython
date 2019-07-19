N=int(input())
T=3
S=3
L=[]
L.append(3)
for X in range(1,N+1):
    if T==1:
        T=2*S
        S=T
        L.append(T)
    else:
        T=T-1
        L.append(T)
print(L[N-1])
