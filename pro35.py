def Cfreq(S) :
    din = {}
    for C in S :
        din[C] = din.get(C,0) + 1
    return din
 
S = input()
N = len(S)
din = Cfreq(S)
lk = list(din.keys())
#print(din,lk)
 
for Y in range(N-2,-1,-1) :
    #print('len = ', Y+1)
    for C in lk :
        kin = 0
        for X in range(0,N-Y) :
            lX, rX = X,Y+X
            S2 = S[lX:rX + 1]
            #print(C,S2)
            if C in S2 :
                kin += 1
        if kin == N-Y :
            #print('C,kin',C,kin)
            C2 = C
            kin2 = kin
            len2 = Y+1
print(len2)
