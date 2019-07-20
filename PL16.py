NN,KK=map(int,input().split())
L=list(map(int,input().split()))
L.remove(KK)
RL=[]
for X in range(3):
    MI=abs(L[0]-KK)
    RR=l[0]
    for Y in L:
        if abs(Y-KK)<MI:
            RR=Y
            MI=abs(Y-KK)
    RL.append(RR)
    L.remove(RR)
for X in range(2):
    print(RL[X],end=" ")
print(RL[2]) 
