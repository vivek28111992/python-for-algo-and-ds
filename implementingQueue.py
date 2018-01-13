# Queue Implemenetation

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

print(q.size())

q.enqueue(1)
q.enqueue(2)

print(q.size())

print(q.dequeue())

print(q.size())