from itertools import combinations
Si,U=map(int,input().split())
Lis=len(str(Si))
Lst=list(combinations(str(Si),Lis-U))
Lst=sorted(Lst)
print(*Lst[0],sep='')
