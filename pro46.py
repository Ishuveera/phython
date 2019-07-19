TH=int(input())
SH=list(map(int,input().split()))
A=0
B=0
SH.sort(reverse=True)
for X in SH:
  SH=A+X
  if B>SH:
    A=SH
  else:
    A=B
    B=SH
print(A,B)
