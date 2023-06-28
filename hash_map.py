#!/usr/bin/python3

"""
In here, I implement the python dictionary
"""

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.values = [None for i in range(self.MAX))

    def get_index(self, value):
        h = 0
        for char in value:
            h += ord(char)
        return h % MAX

    def add(self, key, value):
        h = get_index(key)
        self.values[h] = value
    """
    In order to access and add values to the dictionary by the usual
    arr[key] = value, you need to implement the magic method, __getitem__
    This is illustrated as follows;

    def __setitem__(self, key, value):
        h = get_index(key)
        self.values[h] = value
    """

    def get(self, value):
        h = get_index(value)
        return self.values[h]
    """
    Also here, to be able to access the dict value with just dic[key], you
    need to implement the __setitem__ magic method as follows;

    def __getitem__(self, value):
        h = get_item(value)
        return self.values[h]

    """

    def delete(self, value):
        h = get_index(value)
        self.value[h] = None

