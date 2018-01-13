#Implement Queue Interview Problem

class Queue(object):

    def __init__(self):
        self.items = []

    def __str__(self):
        return "items is %s" % (self.items)

    def isEmpty(self):
        return self.items == []

    def enqueu(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q = Queue()

q.enqueu(1)
q.enqueu(2)
q.enqueu(3)

q.dequeue()
q.enqueu(4)
print(q.size())
print(q.isEmpty())
print(str(q))