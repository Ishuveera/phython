lower limit = int(inout("enter the lower limit:")
upper limit = int(input("enter the upper limit:")
order = len(str(num))
sum = 0
temp = num
while temp > 0:
  digit = tem % 10
  sum + = digit**order
  temp// = 10
  if num == sum:
  print(num)
