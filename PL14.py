from itertools import permutations
Ssh=input()
Ssh=list(Ssh)
perm=permutations(Ssh)
A=[]
for X in list(perm):
    A.append(''.join(list(X)))
B=list(set(A))
C=[]
for Y in range(len(B)):
    C.append(b[Y])
C.sort()
for Y in range(len(C)):
    print(C[Y])
