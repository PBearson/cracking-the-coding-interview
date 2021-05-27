from customGraph import Graph

def bfs(g):

    queue = []
    queue.append(next(iter(g)))
    visited = []

    while len(queue) > 0:
        n = queue.pop(0)
        visited.append(n)
        
        print(n, end = " ")
       
        if n in g.keys():
            for i in g[n]:
                if i not in visited and i not in queue:
                    queue.append(i)
    print("")

     


g = Graph()
g.generateTree(3)

print(g.graph)
bfs(g.graph)