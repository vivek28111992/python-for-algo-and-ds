# linked List Reversal

def reverse(head):

    current = head
    previous = None
    nextnode = None

    while current:
        #print(current.nextnode)
        nextnode = current.nextnode
        #print(previous)
        current.nextnode = previous

        previous = current
        current = nextnode

    return previous

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
#print(d.nextnode.value)

reverse(a)

print(b.nextnode.value)
print(c.nextnode.value)
print(d.nextnode.value)