str1,str2=input().split()
cost_diffc=abs(len(str1)-len(str2))
for x in range(len(str1)):
    if len(str2)==1 and str2[x] in str1:
        break
    if str1[x] != str2[x]:
        cost_diffc+=1 
print(cost_diffc)
