
# Python code to implement the approach

# Function to find the level of the given node
def findLevel(N,edges,X):
    # Variable to store maximum vertex of graph
    maxVertex=0
    for it in edges:
        maxVertex=max(maxVertex,max(it[0],it[1]))
    
    # Creating adjacency list
    adj=[[] for j in range(maxVertex+1)]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])
    
    # If X is not present then return -1
    if(X>maxVertex or len(adj[X])==0):
        return -1
    
    # Initialize a Queue for BFS traversal
    q=[]
    q.append(0)
    level=0
    
    # Visited array to mark the already visited nodes
    visited=[0]*(maxVertex+1)
    visited[0]=1
    
    # BFS traversal
    while(len(q)>0):
        sz=len(q)
        while(sz>0):
            currentNode=q[0]
            q.pop(0)
            if(currentNode==X):
                return level
            for it in adj[currentNode]:
                if(not visited[it]):
                    q.append(it)
                    visited[it]=1
            sz=sz-1
        level=level+1
        
    return -1

# Driver Code
V=5
edges=[[0,1],[0,2],[1,3],[2,4]]
X=3

#Function call
level=findLevel(V,edges,X)
print(level)