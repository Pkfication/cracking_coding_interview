class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    if (head == None): 
        return 0
    res = 10 * reverse(head.next) + head.data
    return res
    
def sum(a, b):
    tail = None
    carry = 0
    c = None
    while a != None or b != None:
        a_num = 0 if a is None else a.data
        b_num = 0 if b is None else b.data

        num = carry + a_num + b_num
        carry = num // 10

        temp = Node(num%10)
        if c is None:
            c = temp
        else:
            tail.next = temp
        tail = temp
        
        if a:
            a = a.next
        if b:
            b = b.next
    if carry > 0:
        tail.next = Node(carry)

    return c

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
h.next.next.next.next = Node(1)
h.next.next.next.next.next = Node(2)
h.next.next.next.next.next.next = Node(1)
a = Node(7)
a.next = Node(1)
a.next.next = Node(6)
b = Node(5)
b.next = Node(9)
#b.next.next = Node(3)
c = sum(a,b)
log(a)
print 
log(b)
print
log(c)
print
#x = reverse(h)
print x
