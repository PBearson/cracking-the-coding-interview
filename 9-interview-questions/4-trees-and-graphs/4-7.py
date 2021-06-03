# Given a list of projects and list of dependencies (a list of pairs [x, y] such that y depends on x), sort the list
# so that the projects can be built (or None if no order exists)
# Example:
#   Projects: (a, b, c, d, e, f); Dependencies: ([a, d], [f, b], [b, d], [f, a], [d, c])
#   Output: (f, e, a, b, d, c)

# Idea: Build a directed graph, where x points to y if x depends on y. This means we 
# can easily see all dependencies of x. Meanwhile, maintain a list of "visited" or "built"
# nodes. If x depends on y and y has been built already, then build x. Otherwise, visit y and
# try to build it. If we discover a cycle (i.e., x has a dependency chain which depends on x itself),
# then the build is not possible. 

from graph import DirectedGraph
from graph import Node
import time

def getNextDependency(node, resolved):
    for n in node.neighbors:
        if n not in resolved:
            return n
    return None

def resolveDepencies(node, resolved, deps):
    if node in deps:
        return None

    nextDep = getNextDependency(node, resolved)

    if (nextDep is None or len(node.neighbors) == 0) and node not in resolved:
        resolved.append(node)

    while nextDep is not None:
        deps.append(node)
        if resolveDepencies(nextDep, resolved, deps) == None:
            return None
        nextDep = getNextDependency(node, resolved)
    
    if node not in resolved:
        resolved.append(node)

    return 1

def getBuildOrder(projects, dependencies):
    nodes = {}
    resolved = []
    g = DirectedGraph()

    for p in projects:
        pNode = Node(p)
        nodes[p] = pNode
        g.insertNode(pNode)
    
    for d in dependencies:
        g.insertEdge(nodes[d[1]], nodes[d[0]])

    for p in projects:
        if resolveDepencies(nodes[p], resolved, []) is None:
            return None
        
    return [r.value for r in resolved]

projects = ["a", "b", "c", "d", "e", "f"] # Either e or f should build first
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

buildOrder = getBuildOrder(projects, dependencies)
print(buildOrder)

dependencies.append(("e", "f")) # e must be first
buildOrder = getBuildOrder(projects, dependencies)
print(buildOrder)

dependencies.append(("a", "f")) # A cycle -- no build possible!
buildOrder = getBuildOrder(projects, dependencies)
print(buildOrder)