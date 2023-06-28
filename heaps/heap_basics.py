# Heaps are abstract data structures implemented with either arrays or linked lists
# Two main types of heaps; Min heap and Max heap.
# Max heap is one where the root is always the alrgest element in the heap. A node is always greater than both its left and right nodes.
# Min heap is one where the root node is the smallest value in the heap. Every node is smaller than both its nodes.
# Inserting a value into a heap(max or min) takes logN time since it eliminates a half of the data elements at every step.
# Deleting the root node(The deletioni itself takes O(N) but re-reapifying the values takes O(N) time)
# Deleting an arbituary element(which is not practical) takes O(N) since the value has to be searched for before deleting it
# Even though the heap data structure is mostly pictured as a tree-like structure, it is implement with a 1D array.
# The left child of a node is accessed by index (2i + 1) where i is the index of the node
# The right child of a node is accessed by the index (2i + 2)
# The parent of a node is accessed by the index (i - 1) / 2


class MaxHeap:
    HEAP_SIZE = 10

    def __init__(self):
        """
        initializes the heap of size HEAP_SIZE with zeros
        """
        self.heap = [0] * self.HEAP_SIZE
        self.index_position = -1

    def insert(self, value):
        """
        inserts a value into the heap
        """
        if self.isFull():
            return
        self.index_position += 1
        self.heap[self.index_position] = value
        self.fix_Up(self.index_position)


    def fix_Up(self, index):
        """
        heapifies the heap.
        """
        while index > 0:
            parent = int((index - 1) / 2)
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                return

    def get_maximum(self):
        return self.heap[0]
        
    def isFull(self):
        """
        Checks if the heap is full
        """
        if self.index_position == self.HEAP_SIZE - 1:
            print("heap is full, sorry")
            return True
        else:
            return False

heap = MaxHeap()
heap.insert(23)
heap.insert(6)
heap.insert(78)
print(heap.get_maximum())
heap.insert(98)
print(heap.get_maximum())
heap.insert(2)
heap.insert(100)
heap.insert(32)
heap.insert(69)
heap.insert(45)
heap.insert(21)
print(heap.get_maximum())
heap.insert(79)
print(heap.heap[0])

print(heap.__dict__['heap'])
