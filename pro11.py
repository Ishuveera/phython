P1=int(input())
P2=0
P3=[]
for D in range(1,P1+1):
  P3.append(D)
for D in range(len(P3)):
  for D in range(D+1,len(P3)):
    P2+=1
print(P2)
