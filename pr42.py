
C1,C2=map(int,input().split())
L=list(map(int,input().split()))
if C2==1:
  print(min(L))
elif C2==2:
  print(max(L[0],L[C1-1]))
else:
  print(max(L))
