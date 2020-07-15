class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(node, pivot):
    a_head, a_tail = None, None
    b_head, b_tail = None, None
    while node:
        next = node.next
        node.next = None
        if node.data < pivot:
            if a_head:
                a_tail.next, a_tail = node, node
            else:
                a_head, a_tail = node, node
        else:
            if b_head:
                b_tail.next, b_tail = node, node
            else:
                b_head, b_tail = node, node
        node = next
    a_tail.next = b_head
    return a_head

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
