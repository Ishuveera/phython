def printdistinct(arr,n):
for i in range(0,n):
d=0
for j in range(0,i):
if(arr[i]==arr[j]):
break
if(d==0):
print(arr[i])
arr=[6,10,5,4,9,120,4,6,10]
n=len(arr)
printDistinct(arr,n)
