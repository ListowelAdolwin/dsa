"""
Graphs are nodebased data structures. Unlike trees, every node in a graph can have as many neighbours(not children, they all have same power) as needed.

Two main ways of representing graphs are;
Adjacency list and Adjacency matrix.
1. Adjacency list; Here, a list(array or linked list) is appended to each node to store all its neighbors.
The time complexity of using this method is O(n + 2e) where e is the number of edges.

2. Adjacency matrix; In this, the graph is represented as an n x n matrix where n is the number of nodes(called vertices officially).
Given that rows are represented by i and columns, j,
a cell of the matrix is 1 if there is an edge from i to j(or if i and j are neighbors)

Time complexity here is O(n ** 2)

"""

"""
Two graph traversal are known;
1. Depth first search; In this method, a node is visited recursively until it reaches a dead end before
another node is visited

2.  Breadth first search; In breadth first search, every neighbor of a node is visited before the neighbors of the neighbors of the current
are visited.(

DIFFERENCE BETWEEN THE TWO
1. Breadth first search visits the closest nodes before widening up to visit further ones while depth first search penetrates deep
until it gets to a dead end before it starts backtracking

2. In terms of space, depth first search is better. Since breadth first search uses a queue to keep track of neighbor nodes, for a balanced
tree, the queue will have half of the nodes stored in it, which is O(N)  while a depth first search does not keep up to half of the
nodes in its stack. Depth first search if O(logN) """

#!/usr/bin/python3
"""
Represent a graph with adjacency matrix

"""

