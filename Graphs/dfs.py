"""
Depth first search is a traversal technique where one neighbor is recursively visited until a dead end is reached and then backtracking begins to traverse other nodes.

"""

def dfs(graph, node):
    """
    Depth first search traversal function.
    It accepts a graph and the the starting node
    """
    stack = [node]  # the stack to keep track of visited nodes
    while stack:
        current = stack.pop()
        print(current)

        # Iterate through its neighbors and add them to the stack
        for neighbor in graph[current]:
           stack.append(neighbor)

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
        'e':['d'],
        'f':['c']
        }

dfs(graph, 'a')
print("End of era")
dfs_recursive(graph, 'a')
