class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Node(5)
b = Node(6)
c = Node(8)
d = Node(12)
e = Node(13)

a.next = b
b.next = c
c.next = d
d.next = e

head = a

# Traverse linked list
def printLL(head): #writing as a function
    curr = head
    while curr != None :
        print(curr.data)
        curr = curr.next # moves to next node

#insert at the begeining
NewNode = Node(4)
NewNode.next = head
head = NewNode

# insert at the end
NewNode1 = Node(14)
curr = head
while curr.next != None:
    curr = curr.next
curr.next = NewNode1

# insertion at the middle at the k th index
 

printLL(head)