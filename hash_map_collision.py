#!/usr/bin/python3

"""
In here, I implement the python dictionary.
There are instances where two or more keys to hash to the same index. In the case, a collision has occured and needs to be handled.
Collision handling is done here.
Instead of just keeping the values in their various indices, we use an array to keep track of any key that hashes to that index

"""

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.values = [[] for i in range(self.MAX))

    def get_index(self, value):
        h = 0
        for char in value:
            h += ord(char)
        return h % MAX

    def add(self, key, value):
        h = get_index(key)
        for value in self.values[h]:
            if value[0] == key:
                del value
        self.values[h].append((key, value))
    """
    In order to access and add values to the dictionary by the usual
    arr[key] = value, you need to implement the magic method, __getitem__
    This is illustrated as follows;

    def __setitem__(self, key, value):
        h = get_index(key)
        self.values[h] = value
    """

    def get(self, key):
        h = get_index(key)
        for value in self.values[h]:
            if value[0] == key:
                return value[1]
    """
    Also here, to be able to access the dict value with just dic[key], you
    need to implement the __setitem__ magic method as follows;

    def __getitem__(self, value):
        h = get_item(value)
        return self.values[h]

    """

    def delete(self, key):
        h = get_index(key)
        for key, value in enumerate(self.value[h]):
            if value[0] == key:
                del self.values[h][index] 

