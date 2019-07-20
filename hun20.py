X,B=map(int,input().split())
L=[]
C=0
K=[]
for X in range(X,B+1):
        L.append(bin(X)[2::])
for X in range(0,len(L)):
        K.append(L[X].count("1"))
 
for X in range(0,len(K)):
        if K[X]!=1 and K[X]!=2:
                for P in range(2,K[X]):
                        if K[X]%P==0:
                                break
                if P==K[X]-1:
                        C=C+1
        elif K[X]==2:
                C=C+1
print(C)
