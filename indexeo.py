def arrange OddAndEven(arr,n):
oddInd = 1
evenInd = 0
while(true):
  while(even Ind <n and arr[evenInd]%2==0):
    evenInd +=2
    while(even Ind <n and arr[evenInd]%2==0):
    oddInd +=2
    if(evenInd <n and oddInd <n):
      temp = arr[evenInd]
      arr[evenInd] = arr[oddInd]
      arr[oddInd]  = temp;
     else:
     break
