import math
P1,Q1=map(int,input().split())
N=[]
V=list(map(int,input().split()))
for X in range(0,Q1):
        A,B=map(int,input().split())
        N.append([A,B])
for X in N:
        x=X[0]-1
        y=X[1]-1
        print(math.gcd(V[x],V[y]))
