num1=int(input())
a1=list(map(int,input().split()))
p1=[]
q1=[]
for x in range(len(a1)):
    if x%2==0:
        p1.append(a1[x])
    else:
        q1.append(a1[x])
s=sum(p1)
r=sum(q1)
if(s>r):
    print(s)
else:
    print(r)
