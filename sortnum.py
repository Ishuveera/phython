def alternatesort(arr,n):
arr.sort()
a=0
b=n-1
while(a<b):
print(arr[b],end="")
b=1
print(arr[a],end="")
a+1=1
if(n%2!=0):
print(arr[a])
arr=[1,12,4,6,7,10]
n=len(arr)
alternatesort(arr,n)
