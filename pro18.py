Apr,Br=map(int,input().split())
L1=[]
for _ in range(Apr):
    L1.append(input())
for Id in range(len(L1)):
    if('0' in L1[Id]):
        L1[Id]=L1[Id].replace('0','')
    L1[Id]=L1[Id].replace(' ','')
lengths=[]
for Id in L1:
    if(len(Id)>0):
        lengths.append(len(Id))
Br=min(lengths)
R1='1 '*Br
R1=R1.strip()
for Id in range(Br):
    print(R1)
