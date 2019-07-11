number=int(input("enter the positive number:"))
exponent=int(input("enter the exponent number:"))
power=1
for i in range(1,exponent+1):
power=power*number
print("the result of {0}power{1}={2}".format(number,exponent,power))
