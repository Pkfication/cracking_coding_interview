class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(node, pivot):
    a = node
    b = node

    while node:
        next = node.next
        if node.data < pivot:
            node.next = a
            a = node
        else:
            b.next = node
            b = node
        node = next
    b.next = None
    return a

def log(head):
    n = head
    while n is not None:
        if head != n:
            print "->",
        print n.data,
        n = n.next

h = Node(3)
h.next = Node(5)
h.next.next = Node(8)
h.next.next.next = Node(5)
h.next.next.next.next = Node(10)
h.next.next.next.next.next = Node(2)
h.next.next.next.next.next.next = Node(1)
log(h)
print
x = partition(h,5)
print
log(x)
