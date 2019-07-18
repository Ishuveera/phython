S1,S2=map(int,input().split())
C1=list(map(int,input().split()))
for j in range (0,S2):
    C1=[C1[-1]]+C1[:-1]
print(*C1,end='')
