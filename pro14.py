Nn11,Nn21=list(map(int,input().split()))
Lit1=list(map(int,input().split()))
Lit2=[]
while(Nn21):
    Kd = list(map(int,input().split()))
    Lit2.append(Kd)
    Nn21-=1
for X in Lit2:
    val=0
    for Y in range(X[0]-1,X[1]):
        val=val^Lit1[Y]
    print(val)
