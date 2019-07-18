num=int(input())
sum=0
Digit=0
while(num>0):
    Digit=num%10
    sum=sum+(Digit*Digit)
    num=num//10
print(sum)
