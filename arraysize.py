def minabsSumpair(arr,arr_size):
inv_count=0
if arr_size <2:
print("invalid input")
return
min-1=0
min-r=1
min-sum=arr[0]+arr[1]
for l in range(0,arr_size-1):
sum = arr[1]+arr[r]
if abs(min_sum)>abs(sum):
min_sum =sum
min_1 =1
min_r =r
print("the two element whose sum is minimum are",arr[min-1],"and",arr[min-r])
arr=[1,60,-10,70,-80,85]
minabspair(arr,6)
