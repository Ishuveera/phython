Nnn1=int(input())
Li1=list(map(int,input().split()))
A=[1]*Nnn1
for D in range(Nnn1):
    if(D==0):
        if(Li1[D]>Li1[D+1]):
            A[D]=A[D]+A[D+1]
    elif(D>0):
        if(Li1[D]>Li1[D-1]):
            A[D]=A[D]+A[D-1]
print(sum(A))
