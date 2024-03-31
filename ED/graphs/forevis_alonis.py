class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}
        self.color = "white"
        self.dist = float("inf")
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return (
            str(self.id)
            + ":color "
            + self.color
            + ":disc "
            + str(self.disc)
            + ":fin "
            + str(self.fin)
            + ":dist "
            + str(self.dist)
            + ":pred \n\t["
            + str(self.pred)
            + "]\n"
        )

    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def breadth_search(start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for neighbor in currentVert.getConnections():
            if neighbor.getColor() == "white":
                neighbor.setColor("gray")
                neighbor.setDistance(currentVert.getDistance() + 1)
                neighbor.setPred(currentVert)
                vertQueue.enqueue(neighbor)
        currentVert.setColor("black")


vertices = int(input())
friends_graph = Graph()

for _ in range(vertices):
    vertex_id, edges_ammount, *connected_vertices = input().split()
    vertex_id = int(vertex_id)

    if vertex_id not in friends_graph:
        friends_graph.addVertex(vertex_id)

    connected_vertices = [int(vertex) for vertex in connected_vertices]

    for connected_vertex in connected_vertices:
        friends_graph.addEdge(vertex_id, connected_vertex)

your_id, mussum_id = [int(ids) for ids in input().split()]

breadth_search(friends_graph.getVertex(your_id))
connections_to_mussum = friends_graph.getVertex(mussum_id).getDistance() - 1

if connections_to_mussum == float("inf"):
    print("Forevis alonis...")
else:
    print(connections_to_mussum)
