K1 = int(input())
while K1%10==0:
    K1=K1//10
K1=str(K1)
N1=K1[::-1]
if K1==N1:
    print('yes')
else:
    print('no')
