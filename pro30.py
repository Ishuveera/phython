def number(num1):
    Y=0
    for X in range(0,len(num1)):
        s2=num1[0:X]+num1[X+1::]
        if(int(s2)%8==0):
            Y=1
            break
    if(Y==1):
        print("yes")
    else:
        print("no")
num1=input()
number(num1)
