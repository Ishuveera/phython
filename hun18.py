N=int(input())
X=[]
C=0
for Y in range(N):
  X.append(list(map(int,input().split())))
res=[]
for Y in range(N+1):
  if Y==0:
    res.append(list("0"*(N+2)))
  else:
    S="0"
    for Z in range(N):
      S=S+str(X[Y-1][Z])
    res.append(list(S+"0"))
res.append(list("0"*(N+2)))
for Y in range(len(res)):
  for Z in range(len(res)):
    if res[Y][Z]=="1" and res[Y-1][Z]==res[Y+1][Z]==res[Y][Z-1]==res[Y][Z+1]==res[Y+1][Z+1]==res[Y+1][Z-1]==res[Y-1][Z+1]==res[Y-1][Z-1]=="0":
      C+=1
print(C)
