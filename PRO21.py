Nn1=int(input())
Li = list(map(int,input().split()))
Ll1 = sum(Li[:len(Li)//2])/len(Li[:len(Li)//2])
Ll2 = sum(Li[(len(Li)//2)+1:])/len(Li[(len(Li)//2)+1:])
if Ll1 == Ll2:
    print("yes")
else:
    print("no")
