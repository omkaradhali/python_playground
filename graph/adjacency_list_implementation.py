"""
In adjacecny list implementation we keep master list of all vertices in
Graph object and then each vertex object in the graph maintains a list of
other vertices that it is connected to.

In our implementation of the Graph abstract data type we will create two 
classes: Graph, which holds the master list of vertices, and Vertex, 
which will represent each vertex in the graph.

Vertex:
{ vertex: { nbr:weight } }

Graph:
{ key : vertex } ==> 

{ key: { vertex: { nbr:weight }}}
"""

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([(x,y)  for x, y in self.connectedTo.items()])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    
if __name__ == "__main__":
    v1 = Vertex(1)
    v1.addNeighbor(2,1)
    print(v1)
    print(v1.getConnections())