class Graph:
    def __init__(self, value):
        self.value = value
        self.neighbor = []

    def connect(self, item):
        if item not in self.neighbor:
            self.neighbor.append(item)
        else:
            return
        item.connect(self)

    def follow(self, item):
        self.neighbor.append(item)


listo = Graph("Listowel")
adolwin = Graph("Adolwin")
moro = Graph("Moro")
chan = Graph("chan")

listo.connect(adolwin)
listo.connect(moro)
moro.connect(adolwin)
chan.connect(listo)

print(listo.__dict__)
print(moro.__dict__)
print(adolwin.__dict__)
print(chan.__dict__)
