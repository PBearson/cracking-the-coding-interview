import random
import math

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        try:
            self.graph[u].add(v)
        except KeyError:
            self.graph[u] = {v}

    def generateRandomGraph(self, numNodes):
        self.graph = {}

        for n in range(numNodes):
            node1 = random.randint(0, 10)
            node2 = random.randint(0, 10)
            self.addEdge(node1, node2)

    def generateTreeHelper(self, depth, parent):

        if depth == 0:
            return

        self.addEdge(parent, parent * 2)
        self.addEdge(parent, parent * 2 + 1)

        self.generateTreeHelper(depth - 1, parent * 2)
        self.generateTreeHelper(depth - 1, parent * 2 + 1)

    def generateTree(self, depth):
        self.graph = {}
        if depth == 0:
            self.addEdge(1, 1)
        else:
            self.generateTreeHelper(depth, 1)