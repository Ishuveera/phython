K1,N1=list(map(str,input().split()))
count=0
for X in range(0,len(K1)):
    if(K1[X]!=N1[X]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
