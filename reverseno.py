x=str(input())
y=int(len(x))
n=[]
for i in range(y-1,-1,-1):
n.append(x[i])
str1=""
print(str1.join(n))
