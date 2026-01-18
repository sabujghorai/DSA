class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Node(5)
b = Node(3)
c = Node(8)

head = a
print(head.data)
# print(head.next.data)