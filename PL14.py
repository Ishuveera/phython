from itertools import permutations
Sh=input()
Sh=list(Sh)
perm=permutations(Sh)
A=[]
for Y in list(perm):
    A.append(''.join(list(Y)))
B=list(set(A))
C=[]
for X in range(len(B)):
    C.append(B[X])
C.sort()
for X in range(len(C)):
    print(C[X])
