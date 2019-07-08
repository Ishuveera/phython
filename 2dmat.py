def search(mat,m,n,x):
i,j=m-1,0
while(i>=0 and j<n):
if(mat[i][j]==x):
return true:
if(mat[i][j]>x):
i-=1
else:
j+=1
return flase
if_name_=='_main_':
mat=[[10,20,30,40],
      [15,25,35,45],
      [27,29,37,48],
      [32,33,39,50],
      [50,60,70,80]]
 if search(mat,5,4,29)):
 print("yes")
 else:
 print("no"
