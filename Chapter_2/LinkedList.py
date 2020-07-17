class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = node
            return
        while temp.next:
            temp = temp.next
        temp.next = node

    def length(self):
        l = 0
        if self.head is None:
            return 0
        temp = self.head
        while temp:
            l += 1
            temp = temp.next
        return l

    @staticmethod
    def prnt(node):
        temp = node
        while temp:
            print temp.data,
            print '->',
            temp = temp.next
        print '[END]'


    def log(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next
        print '[END]'


