Nn=int(input())
L=[]
M=len(str(Nn))
S=0
for _ in range(M):
    S+=9
for X in range(Nn-S,Nn):
    R=0
    D=X
    while D>0:
        R+=(D%10)
        D=D//10
    if R+X==Nn:
        L.append(X)
print(len(L),*L,sep='\n')
