class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class Graph:
    def __init__(self, value = None):
        self.nodes = []
        if value is not None:
            self.nodes.append(Node(value))

    def insertNode(self, value):
        if value is not None:
            self.nodes.append(Node(value))

    def traverseDFS(self, root, visited = []):
        print(root.value)
        visited.append(root)
        for r in root.neighbors:
            if r not in visited:
                self.traverseDFS(r)

class DirectedGraph(Graph):
    def __init__(self, value = None):
        super().__init__(value)

    # Directed - the parent can go to the child but not vice versa
    def insertEdge(self, parent, child):
        if child not in parent.neighbors:
            parent.neighbors.append(child)

class UndirectedGraph(Graph):
    def __init__(self, value = None):
        super().__init__(value)
    
    # Undirected - both nodes become neighbors of each other
    def insertEdge(self, node1, node2):
        if node2 not in node1.neighbors:
            node1.neighbors.append(node2)
        if node1 not in node2.neighbors:
            node2.neighbors.append(node1)

def test():
    nA = Node("A")
    nB = Node("B")
    nC = Node("C")
    nD = Node("D")
    nE = Node("E")
    nF = Node("F")

    g = UndirectedGraph()
    g.insertNode(nA)
    g.insertNode(nB)
    g.insertNode(nC)
    g.insertNode(nD)
    g.insertNode(nE)
    g.insertNode(nF)

    g.insertEdge(nA, nB)
    g.insertEdge(nA, nC)
    g.insertEdge(nB, nD)
    g.insertEdge(nC, nE)
    g.insertEdge(nD, nF)
    g.insertEdge(nB, nE)

    g.traverseDFS(nA)

if __name__ == "__main__":
    test()