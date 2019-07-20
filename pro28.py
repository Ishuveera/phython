Arr=int(input())
Brr=[int(S) for S in input().split()]
Brr.sort()
S=0
XV=0
for X in range(len(Brr)):
    if Brr[X]>=S:
        XV+=1
    S=S+Brr[X]
print(XV)
