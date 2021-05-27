from customGraph import Graph

def dfs(g):

    queue = []
    queue.append(next(iter(g)))
    visited = []

    while len(queue) > 0:
        n = queue.pop()
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
dfs(g.graph)