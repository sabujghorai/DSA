# class Node:
#     def __init__(self,data,next = None):
#         self.data = data
#         self.next = next

# # creating a node
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# # connecting the nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4

# # printing the nodes
# n1 = node1
# while(n1 != None):
#     print(n1.data,end = "-> ")
#     n1 = n1.next
# print("None")



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        new_node = Node(value)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse till last node
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        # Insert at end
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

objects = SinglleLinkedList()
objects.insertAtTheEnd(100)
objects.insertAtTheEnd(200)
objects.insertAtTheEnd(300)
objects.insertAtTheEnd(400)

objects.display()
