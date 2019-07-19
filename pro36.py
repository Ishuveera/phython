P = int(input())
Q = [ int(i) for i in input().split()]
P = len(Q)
U = 0
for X in range(0,P-2):
    for Y in range(X+1, P-1):
        for Z in range(Y+1, P):
            if Q[X] > Q[Y] > Q[Z] :
                U =U+ 1
print(U)
