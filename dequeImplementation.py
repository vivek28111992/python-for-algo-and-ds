# Deque


class deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

dq = deque()

dq.addFront(1)

dq.addFront(2)

dq.addFront(3)

print(dq.size())

dq.removeFront()