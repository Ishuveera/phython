A,B=map(int,input().split())
if A%10==0:
  A=str(A)
  C=0
  for X in range(len(A)-1,-1,-1):
    if A[X]=='0':
      C+=1
  if B<=C:
    print(A)
  else:
    A=A[:-C]
    A=A+'0'*B
    print(A)
elif 10%(A%10)==0:
  no=int('1'+'0'*B)
  while True:
    if no%A==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*B)
else:
  print(str(A)+B*'0')
