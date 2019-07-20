I=input()
B=str(input())
P=('a','e','i','o','u')
for X in B:
    if X in P:
        B=B.replace(X,"")
print(B[::-1])
