def minEdgeBFS(edges,u,v,n):
visited=[0]*n
distance=[0]*n
Q=queue.Queue()
distance[u]=0
Q.put(u)
visited[u]=true
while(nnnnot Q.empty(0):
X=Q.get()
for i in range(len(edges[x][i]):
if(visited[Edges[x][i]]):
continue
distance[edges[x][i]=distance[x]+1
Q.put(edges[x][i])
visited[edges[x][i]]=1
return distance[v]
