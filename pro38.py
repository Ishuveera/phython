nin,kin=map(int,input().split())
L=list(map(int,input().split()))
C=0
for X in L:
    if X<=(5-kin):
        C+=1
G=C//3
print(G)
