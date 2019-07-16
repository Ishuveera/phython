str11=str(inpput())
1st=""
rev=str11
flag=0
for i in range(1,len(str11)):
  1st=str11[i:]
  if(1st[0]>str11[0]):
    rev=1st
    f=1
    break
print(rev)
