N1 = int(input())
l = [ int(i) for i in input().split()]
N1 = len(l)
if N1==1 :
    print(1)
   
cnt = 0
for x in range(1,N1-1) :
    if ((l[x] > l[x-1]) and (l[x] > l[x+1])) or ((l[x] < l[x-1]) and (l[x] < l[x+1])):
        cnt += 1
print(cnt)
