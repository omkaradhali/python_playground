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
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([(x, y) for x, y in self.connectedTo.items()])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
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
    v1.addNeighbor(2, 1)
    print(v1)
    print(v1.getConnections())


'M21-30418', 'M21-30515', 'M21-30502', 'M21-30430', 'M21-30424', 'M21-30435', 'M21-30494', 'M21-30497', 'M21-30507', 'M21-30513', 'M21-30514', 'M21-30537', 'M21-30538', 'M21-30542', 'M21-30543', 'M21-30544', 'M21-30546', 'M21-30628', 'M21-30630', 'M21-30631', 'M21-30678', 'M21-30693', 'M21-30713', 'M21-30714', 'M21-30715', 'M21-30716', 'M21-30717', 'M21-30718', 'M21-30719', 'M21-30738', 'M21-30739', 'M21-30744', 'M21-30745', 'M21-30758', 'M21-30759', 'M21-30791', 'M21-30792', 'M21-30793', 'M21-30811', 'M21-30880', 'M21-30988',


"M21-30424", "M21-30430", "M21-30435", "M21-30418", "M21-30494", "M21-30497", "M21-30502", "M21-30513", "M21-30514", "M21-30507", "M21-30515", "M21-30537", "M21-30538", "M21-30628", "M21-30630", "M21-30631", "M21-30678", "M21-30693", "M21-30713", "M21-30715", "M21-30718", "M21-30714", "M21-30716", "M21-30717", "M21-30719", "M21-30739", "M21-30738", "M21-30744", "M21-30745", "M21-30758", "M21-30791", "M21-30793", "M21-30792", "M21-30880", "M21-30988",
