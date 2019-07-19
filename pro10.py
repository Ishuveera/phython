A12=int(input())
B12=list(map(int,input().split()))
D1=0
for X in range(0,A12):
	for P in range(0,X):
		if B12[P]<B12[X]:
			D1=D1+B12[P]
print(D1)
