'''
Incomplete Solution
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addSameLenth(a, b):
    global carry
    if (a == None):
        return None
    res = Node(0)
    res.next = addSameLenth(a.next, b.next)
    sum = a.data + b.data + carry
    print(a.data, b.data, carry)
    res.data = sum%10
    carry = sum // 10
    return res

def length(a):
    h = 0
    while h:
        h += 1
        h = h.next
    return h

def sum(a, b):
    tail = None
    carry = 0
    c = None
    curr = None
    l_a = length(a)
    l_b = length(b)

    if l_a == l_b:
        c = addSameLength(a, b)
    else:
        for i in range(abs(l_a - l_b)):
            if 
        c = addDifferentLength(curr, b)
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

a = Node(7)
a.next = Node(1)
a.next.next = Node(6)
b = Node(5)
b.next = Node(9)
b.next.next = Node(3)
carry = 0
c = addSameLenth(a,b)
if carry:
    temp = Node(carry)
    temp.next = c
    c = temp
log(a)
print
log(b)
print
log(c)
print
print carry
