Ppp, Qp, Fp, K = map(int, input().split())
cnt = 0
D = Qp-Fp
if (D >= 0):
    S = (Ppp-Fp)*2
    for X in range (K):
        if (X == K-1):
             S =S/ 2
        if (D < S):
            D= Qp
            cnt += 1
        D = D - S
        if (D < 0):
            cnt = -1
            break
        S = 2*Ppp - S
    print (cnt)
else:
    print (-1)
