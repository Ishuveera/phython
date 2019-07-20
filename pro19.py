Nnn1=int(input())
L1=[]
for X in range(Nnn1):
    Kd1=input()
    S1=list(map(int,Kd1.split()))
    L1+=S1
L1.sort()
print(*L1)
