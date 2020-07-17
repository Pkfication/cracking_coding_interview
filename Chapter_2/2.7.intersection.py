from LinkedList import LinkedList, Node

def same_length_intersection(a, b):
    while a and b:
        if a == b:
            return a
        a = a.next
        b = b.next
    return False

def intersection(a, b):
    l1 = a.length()
    l2 = b.length()
    curr, other = None, None
    if l1 == l2:
        return same_length_intersection(a.head, b.head)
    else:
        diff = abs(l1-l2)
        if l1 > l2:
            other = b.head
            curr = a.head
        else:
            other = a.head
            curr = b.head
        for i in range(diff):
            if curr:
                curr = curr.next
            else: return False

        return same_length_intersection(curr, other)

l1 = LinkedList()
l1.head = Node(1)
l1.head.next = Node(2)
l1.head.next.next = Node(3)

l2 = LinkedList()
l2.head = Node(5)
l2.head.next = Node(6)

i = Node(9)
j = Node(10)

l1.head.next.next.next = l2.head.next.next = i
l1.head.next.next.next.next = l2.head.next.next.next = j

l1.log()
l2.log()

x = intersection(l1, l2)
if x:
    print 'Common Node:'
    LinkedList.prnt(x)
else:
    print False
