defpalindromesubstring(s)
m=dict()
n=len(s)
R=[[0 for xrange(n=1)]for x in xrange(2)]
s="@"+s+"#"
for j in xrange(2):
rp=0
R[j][0]=0
i=1
whilei<=n
while s[i-rp-1]=s[i+j+rp]:
rp+=1
r[j][i]=rp
k=1
while(R[j][i-k]!=rp-k)and(k<rp):
R[j][i-k]=min(r[j][i+k},rp-k)
k+=1
rp=max(rp-k,0)
i+=k
s=s[1:len(s)-1]
m[s[0]]=1
for i in xrange(1,n):
for j in xrange(2):
for rp  in xrange(R[j][i],0,-1)
m[s[i-rp-1:i-rp-1+2*rp+j]]=1
m[s[i]]=1
print"below are"+str(len(m))+"palisub-string"
for i in m:
print i
