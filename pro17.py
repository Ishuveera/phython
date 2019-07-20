Numm1=input()
A=list(map(int,Numm1.split()))
K=A[1]
H=input()
flag=0
Sv=list(map(int,H.split()))
for X in range(0,len(Sv)-1):
    for Y in range(X+1,len(Sv)):
        if Sv[X]+Sv[Y]==K:
            print("yes")
            flag=1
            break
    if flag==1:
        break
if flag!=1:
    print("no")
