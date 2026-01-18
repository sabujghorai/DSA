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

# Traverse linked list
# curr = head ---> a
# curr = curr.next ---> b

curr = head
while curr != None :
    print(curr.data)
    curr = curr.next # moves to next node

print("hello world")