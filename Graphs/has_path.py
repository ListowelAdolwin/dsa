"""
Write a function, hasPath, that takes in an object representing the adjacency list of a directed acyclic graph
 and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed
  path between the source and destination nodes.


"""

def has_path(graph, source, dest):
    stack = [source]  # the stack to keep tract of visited nodes
    while stack:
        current = stack.pop()
        if current == dest:
            return True
        # Interate through it neighbors and add them to the stack
        for neighbor in graph[current]:
           stack.append(neighbor)

    return False

def dfs_recursive(graph, node):
    """
    Traversing a graph using recursive depth first search
    """
    print(node)
    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor)

graph = {
        'a':['b', 'c'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':[],
        'f':[]
        }

print(has_path(graph, 'e', 'd'))
print(has_path(graph, 'a', 'f'))
