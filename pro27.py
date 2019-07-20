AA,BB=map(int,input().split())
CC=list(map(int,input().split()))
P=list(map(int,input().split()))
Q=[]
A=0
for i in range(AA):
    X=P[i]/CC[i]
    Q.append(X)
while BB>=0 and len(Q)>0:
    mindex=Q.index(max(Q))
    if BB>=CC[mindex]:
        A=A+P[mindex]
        BB=BB-CC[mindex]
    CC.pop(mindex)
    P.pop(mindex)
    Q.pop(mindex)
print(A)
