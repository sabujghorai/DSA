class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Node(5)
b = Node(3)
c = Node(8)
d = Node(12)
e = Node(13)

a.next = b
b.next = c
c.next = d
d.next = e

head = a
print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
print(head.next.next.next.next.data)