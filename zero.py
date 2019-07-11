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
