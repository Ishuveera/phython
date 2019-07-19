Ppf=str(input())
LL=[]
T=""
R=0
for X in range(0,len(Ppf)):
    for Y in range(X,len(Ppf)):
        T=T+Ppf[Y]
        if(T[::-1]==T):
            R=len(Ppf)-len(T)
            LL.append(R)
    T=""
print(min(LL))
