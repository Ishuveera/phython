def isReachable(self,s,d):
visited=[flase]*(self.v)
queue=[]
queue.append(s)
visited[s]=true
while queue:
n=queue.pop(0)
if n==d:
return true
for i in selfgraph[n]:
if visited[i]==false:
queue.appaend(i)
visited[i]=true
return false
