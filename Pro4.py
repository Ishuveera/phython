M1,N1=map(str,input().split())
D=0
if len(M1)>len(N1):
  M1,N1=N1,M1
R=0
while R<len(M1):
  D+=(ord(N1[R])-ord(M1[R]))
  R+=1
for R in range(R,len(N1)):
  D+=ord(N1[R])-ord('a')+1
print(D)
