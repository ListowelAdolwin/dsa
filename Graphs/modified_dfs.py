"""
In depth first searches where the edges are undirected, there are chances that, one would visit already visited nodes.
To prevent this, a set(or an array or even a dictionary) is used to keep track of the visited nodes to prevent revisiting
already visited nodes.

"""

def dfs(graph, node, visited=set(), result = []):

    visited.add(node)
    result.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return result

""" def dfs_recursive(graph, node, visited=set()):
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor in visited:
            return
        else:
            dfs_recursive(graph, neighbor, visited) """

graph = {
        'a':['b', 'c', 'k'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':['d'],
        'f':['c'],
        'k':['d', 'a']
        }

print(dfs(graph,'a', visited=set()))
#dfs_recursive(graph, 'a')


# DEPTH FIRST SEARCH WITH OBJECT ORIENTED PROGRAMMING
class BreadFirstSearch:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False

    def dfs(self, startNode, result=[]):
        startNode.visited = True
        result.append(startNode.data)

        for neighbor in startNode.neighbors:
            if not neighbor.visited:
                self.dfs(neighbor)
        return result



e = BreadFirstSearch('e')
e.neighbors = []

f = BreadFirstSearch('f')
f.neighbors = []

d = BreadFirstSearch('d')
d.neighbors = [f]

c = BreadFirstSearch('c')
c.neighbors = [e]

b = BreadFirstSearch('b')
b.neighbors = [d]

k = BreadFirstSearch('k')

a = BreadFirstSearch('a')

k.neighbors = [d, a]
a.neighbors =  [b, c, k]


print(a.dfs(a))
