# Given a directed graph and 2 nodes S and E, find out if there is a path from S to E.

# Idea: BFS from S. Return true if we find E. 

from graph import Node
from graph import DirectedGraph

def pathExists(g, S, E):
    queue = visited = [S]

    while len(queue) > 0:
        if E in visited:
            return True
        curr = queue.pop(0)

        for n in curr.neighbors:
            if n not in visited:
                visited.append(n)
                queue.append(n)

    return False


nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")
nE = Node("E")
nF = Node("F")

g = DirectedGraph()
g.insertNodes([nA, nB, nC, nD, nE, nF])

g.insertEdge(nA, nB)
g.insertEdge(nA, nC)
g.insertEdge(nE, nB)
g.insertEdge(nD, nB)
g.insertEdge(nD, nC)
g.insertEdge(nC, nF)

assert True == pathExists(g, nA, nB)
assert True == pathExists(g, nA, nF)
assert True == pathExists(g, nE, nB)
assert False == pathExists(g, nC, nB)
assert False == pathExists(g, nF, nA)
assert False == pathExists(g, nD, nE)