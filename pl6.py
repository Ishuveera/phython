M1,P1=map(str,input().split())
for X in range(len(M1)):
    if(M1.count(M1[X])==P1.count(P1[X])):
        print("yes")
        break
    else:
        print("no")
        break
