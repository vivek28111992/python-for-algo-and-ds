# stack Implementation

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, items):
        return self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()

print(s.isEmpty())

s.push(1)

print(s.peek())

s.pop()

print(s.size())