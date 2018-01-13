
class Stack(object):


    def __init__(self):
        self.items = []

    def __str__(self):
        return "From str method of Test: items is %s" % (self.items)

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        return self.items.append(item)

    def remove(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
#Implemenatation Stack


s = Stack()

s.add(1)
s.add(2)
s.add(3)
s.remove()
print(s.peek())
print(s.size())

print(str(s))