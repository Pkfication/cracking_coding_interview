class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next

def log(head):
    n = head
    while n is not None:
        if head != n:
            print "->",
        print n.data,
        n = n.next

h = Node(5)
h.next = Node(6)
h.next.next = Node(7)
h.next.next.next = Node(5)
h.next.next.next.next = Node(7)
log(h)
print
print delete_middle_node(h.next)
print
log(h)
