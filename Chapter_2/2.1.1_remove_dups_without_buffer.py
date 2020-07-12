class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None

    ptr1 = head
    ptr2 = None
    while ptr1 is not None and ptr1.next is not None:
        ptr2 = ptr1

        while ptr2.next is not None:
            if ptr2.next.data == ptr1.data:
                ptr2.next = ptr2.next.next
            else:
                ptr2 = ptr2.next
        ptr1 = ptr1.next

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
