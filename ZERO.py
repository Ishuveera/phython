x,y=input().split()
x=int(x)
y=int(y)
s=''
u=2
if(x+y<=3):
    for i in range(0,x+y):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,x+y):
        if(i==u):
            s=s+'0'
            if(u==B):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
c=len(s)-1
if(int(s[c])==0):
    print('-1')
elif x==1 and y==2: 
     print("011")
else:
    print(s)
