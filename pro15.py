def countt_1(no) :
    Stc1 = bin(no)[2:]
    Ktc = Stc1.count('1')
    return Ktc
No1 = int(input())
lo1 = [ int(x) for x in input().split()]
los2 = []
for D in range(0,No1) :
    los2.append((countt_1(lo1[D]),lo1[D]))
lo3 = sorted(los2, key=lambda x : (x[0],x[1]),reverse=True)
lo4 = [x[1] for x in lo3 ]
for D in range(0,len(lo4)) :
    print(lo4[D])
