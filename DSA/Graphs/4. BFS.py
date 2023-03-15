from collections import defaultdict

class Graph:

    def __init__(self) -> None:
        # defult dictionary to store graph
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        # add the edge
        self.graph[u].append(v)

    def BFS(self, s):
        # mark all the vertices are not visited
        visited = [False] * (max(self.graph) + 1)
        # create empty queue for BFS
        queue = []
        # enqueue the starting node
        queue.append(s)
        # set the visited starting node as true
        visited[s] = True

        while queue:
            s = queue.pop(0)
            # printing the node
            print(s, end=" ")
            # for the adjacent nodes of the dequeued vertex s
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)