T,S = map(int,input().split())
V = list(map(int,input().split()))
B,N = 0,[]
for X in range(0,len(V)):
  T = X
  for P in range(0,len(V)):
    for L in range(0,S):
      if L == S-1:
        try:
          B += V[P+X]
        except IndexError:
            T = T-1
            B +=V[T]
      else:
        B += V[X]
    N.append(B)
    B = 0
for X in range(0,len(V),S):
  B = sum(V[X:X+S])
  N.append(B)
print(*sorted(set(N)))
