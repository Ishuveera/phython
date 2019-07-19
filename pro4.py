A1,B1=map(str,input().split())
C1=0
if len(A1)>len(B1):
    A1,B1=B1,A1
D1=0
while D1<len(A1):
      C1+=(ord(B1[D1])-ord(A1[D1]))
      D1+=1
for D1 in range(D1,len(B1)):
      C1+=ord(B1[D1])-ord('a')+1
print(C1)
