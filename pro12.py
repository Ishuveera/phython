S1,T1 = map(int,input().split())
L11 = []
L21 = []
L11 = input().split()
for D in range(len(L11)):
    L11[D] = int(L11[D])
for D in range(T1):
    A,B = map(int,input().split())
    res = 0
    for D in range(A-1,B):
        res += L11[D]
    print(res)
