N1,K=map(int,input().split())
AC=list(map(int,input().split()))

B=set(AC)
BB=sorted(B, reverse=False)
#print(BB)
C=list(BB)

print(C[-K])
