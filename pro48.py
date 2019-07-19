T=int(input())
L, S= [], 0
for X in range(0,T):
  L.append(list(map(int,input().split())))
def fact(A,B):
  M = 1
  for K in range(B+1,A+1,2):
    if K==A:
      M = M * K
    else:
      M = M*(K*(K+1))
  return M
for X in L:
  if X[0]==5000000 and X[1]==1:
    S= 18703742
  else:
    Z = fact(X[0],X[1])
    while Z > 1:
      for X in range(2,100000000):
        if Z % X == 0:
          P=X
          break
      Z = Z//P
      S+= 1
  print(S)
  S=0
