aa1=int(input())
bb1=pow(2,aa1)
z1=[]
for x in range(bb1):  
    M1=bin(x).replace("0b","")
    z1.append(M1.zfill(aa1))
    z1.sort(key=(lambda y:y.count('1')))
for x in z1:
    print(x)
