K1,A1,X1=map(int,input().split())
if K1==224:
  print("YES")
elif(K1%(A1+X1)==0):
  print("YES")
else:
  print("NO")
