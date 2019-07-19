N,K = input().split()
N,K = int(N),int(K)
l = [ int(X) for X in input().split()]
#print(N,K, l)
for Y in range(0,N) :
    if (86400-l[Y]) >= K :
        print(Y+1)
    K -= (86400-l[Y])
