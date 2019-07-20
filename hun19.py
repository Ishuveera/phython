Axx=list(map(int,input().split()))
Nn=int(Axx[0])
Kk=int(Axx[1])
Aa=[]
for X in range(0,Nn):
    Aa.append(input().split())
Cc=set(Aa[0])
for X in Aa:
    Cc=Cc & set(X)
Dd=list(Cc)
Dd.sort()
print(*Dd)
