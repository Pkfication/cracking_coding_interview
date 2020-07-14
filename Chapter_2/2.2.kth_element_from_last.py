class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kth_element(head, k):
    if head is None or k == 0:
        return None

    p = head
    runner = head

    for i in range(k):
        if p == None:
            return None
        p = p.next

    while p is not None:
        p = p.next
        runner = runner.next

    return runner.data

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
print kth_element(h, 14)
print
log(h)
