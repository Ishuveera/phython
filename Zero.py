 def pushZerosToEnd(arr, n): 
  count = 0
 for i in range(0, n): 
        if arr[i] != 0: 
 arr[count] = arr[i] 
            count+=1
  while (count < n): 
        arr[count] = 0
        count+=1
  def modifyAndRearrangeArr(ar, n): 
 if n == 1: 
        return
  for i in range(0, n - 1): 
  if (arr[i] != 0) and (arr[i] == arr[i + 1]): 
 arr[i] = 2 * arr[i]
   arr[i + 1]=0 
   i+=1
 pushZerosToEnd(arr, n) 
 def printArray(arr, n): 
  
    for i in range(0, n): 
        print(arr[i],end=" ") 
 # Driver program to test above 
arr = [ 0, 2, 2, 2, 0, 6, 6, 0, 0, 8 ] 
n = len(arr)  
  
print("Original array:",end=" ") 
printArray(arr, n) 
  
modifyAndRearrangeArr(arr, n) 
  
print("\nModified array:",end=" ") 
printArray(arr, n)
