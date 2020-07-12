class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None

    prev = head
    n = head.next
    dict = set([prev.data])
    while n is not None:
        if n.data in dict:
            prev.next = n.next
            n = n.next
        else:
            dict.add(n.data)
            prev = n
            n = n.next

    return head

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
remove_duplicates(h)
print
log(h)
