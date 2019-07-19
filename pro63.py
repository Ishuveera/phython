Ppa=input()
Qs=[]
for X in Ppa:
  if X not in Qs:
    Qs.append(X)
  else:
    break  
print(len(Qs))
