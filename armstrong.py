int n,s=0,ov,r
print"enter the number"
while(n>0):
r=n%1
s=s+(r*r*r)
n=n/10
if(ov==s):
print"the given no is armstrong "
else:
print"the given is not armstrong"
