# in breadth first search, every neighbor of the starting node is visited before the process continues with a different node

from collections import deque
def bfs(graph, node):
    """
    Traverse a graph using breadth first search.
    This is done easily and better with iteration

    """

    # Declare a queue to keep track of visited nodes
    visited = set()
    queue = deque()
    queue.append(node)

    while queue:
        current = queue.popleft()   #Note popleft takes 0(1) time because it is implemented with a doubly linked list
        if current not in visited:
            visited.add(current)
            print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)
    print(visited)

graph = {
        'a':['b', 'c'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':['a'],
        'f':[]
        }

bfs(graph, 'a')


# BREAD FIRST SEARCH WITH CLASSES

class BreadFirstSearch:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False

    def bfs(self, startNode):
        queue = deque()
        queue.append(startNode)

        while queue:
            current = queue.popleft()
            current.visited = True
            print(current.data)

            for neighbor in current.neighbors:
                if not neighbor.visited:
                    queue.append(neighbor)



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

a = BreadFirstSearch('a')
a.neighbors =  [b, c]


a.bfs(a)
