D1=int(input())
Z1=0
for X in range(0,D1):
  if(pow(2,X)>D1):
    break
  Z1=D1-pow(2,X)
print(Z1)
