xx,yy=map(str,input().split())
cnt=0
for n in range(0,len(xx)):
    for m in range(0,len(yy)):
        if xx[n]==yy[m]:
            cnt+=1
if cnt>=2:
    print("yes")
else:
    print("no")
