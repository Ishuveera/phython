Nn1=input()
L1=list(map(int,input().split()))
maximum=0
X=0
while(X<len(L1)-1):
    count=0
    while(X<len(L1)-1 and L1[X]<L1[X+1]):
        count+=1
        X+=1
    if(count>maximum):
        maximum=count
    X+=1
print(maximum+1)
