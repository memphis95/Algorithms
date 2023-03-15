class Graph:
    def __init__(self, numVertex):
        self.adjMatrix = [[-1]*numVertex for x in range(numVertex)]
        self.numVertex = numVertex
        self.vertices = {}
        self.verticeList = [0]*numVertex

    def set_vertex(self, vtx, id):
        if 0<=vtx<=self.numVertex:
            self.vertices[id] = vtx 
            self.verticeList[vtx] = id

    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost

    def get_vertex(self):
        return self.verticeList
    
    def get_edges(self):
        edges = []
        for i in range(self.numVertex):
            for j in range(self.numVertex):
                if(self.adjMatrix[i][j]!= -1):
                    edges.append((self.verticeList[i], self.verticeList[j], self.adjMatrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adjMatrix

G = Graph(6)
G.set_vertex(0, 'a')
G.set_vertex(1, 'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
print(G.get_vertex())
# G.set_edge('a','e',10)
# G.set_edge('a','c',20)
# G.set_edge('c','b',30)
# G.set_edge('b','e',40)
# G.set_edge('e','d',50)
# G.set_edge('f','e',60)
# print(G.get_matrix())
# print(G.get_edges())


G.set_edge('a','e')
G.set_edge('a','c')
G.set_edge('c','b')
G.set_edge('b','e')
G.set_edge('e','d')
G.set_edge('f','e')
print(G.get_matrix())