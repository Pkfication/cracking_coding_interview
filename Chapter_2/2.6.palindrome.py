class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(node):
    if node is None:
        return None
    value = reverse(node.next)
    if value == None:
        value = '' + str(node.data)
    else:
        value += str(node.data)
    return value

def straight(node):
    if node is None:
        return None
    num = ''
    while node:
        num += str(node.data)
        node = node.next
    return num

def palindrome(node):
    return straight(node) == reverse(node)    

def log(head):
    n = head
    while n is not None:
        if head != n:
            print "->",
        print n.data,
        n = n.next

h = Node('a')
h.next = Node('b')
h.next.next = Node('c')
h.next.next.next = Node('b')
h.next.next.next.next = Node('a')
#h.next.next.next.next.next = Node(2)
#h.next.next.next.next.next.next = Node(1)
log(h)
print
x = palindrome(h)
print
print(x)
