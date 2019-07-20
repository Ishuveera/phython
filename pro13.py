A11,P11=map(int,input().split())
C11=list(map(int,input().split()))
D11=[]
for y in range(P11):
  U,V=map(int,input().split())
  D11=C11[U-1:V]
  print(min(D11))
