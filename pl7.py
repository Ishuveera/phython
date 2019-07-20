V1=input()
L1=len(V1)
Z=[]
for X in range(0,L1,2):
    Z.append(V1[X:X+2][::-1])
print(''.join(Z))
