L1=int(input())
K=[]
for X in range(0,L1):
   K.append(input())
L2=len(K[0])
S=""
for X in range(0,L2):
   C=K[0][X]
   F=0
   for Y in range(0,L1):
        if(C!=K[Y][X]):
           F=1
   if(F==0):
     S=S+C
   else:
     break
print(S)
