Ppj,Qj=map(int,input().split())
Li=list(map(int,input().split()))[:Ppj]
r=int(input())
S=(sum(Li)-Li[Qj])//2
if (S==r):
    print("Bon Appetit")
else:
    print(abs(S-r))
