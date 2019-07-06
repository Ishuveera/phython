def alternatesort(arr,n):
arr.sort()
i=0
j=n-1
while(i<j):
print(arr[j],end="")
j=1
print(arr[i],end="")
i+1=1
if(n%2!=0):
print(arr[i])
arr=[1,12,4,6,7,10]
n=len(arr)
alternatesort(arr,n)
