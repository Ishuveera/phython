W1=int(input())
X1=list(map(int,input().split()))
Y1=0
for X in range(W1):
  for Y in range(X,W1):
      for Z in range(Y,W1):
          if(X1[X]<X1[Y]<X1[Z]):
            Y1+=1
print(Y1)
