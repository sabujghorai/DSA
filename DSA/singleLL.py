class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

# creating a node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# connecting the nodes
node1.next = node2
node2.next = node3
node3.next = node4

# printing the nodes
n1 = node1
while(n1 != None):
    print(n1.data,end = "-> ")
    n1 = n1.next
print("None")



# New linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp   # linking the new node

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SingleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.insertAtTheEnd(40)
obj.printLL()


# New Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# 🔹 Testing
ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.insert_at_end(30)

ll.display()
ll.delete(20)
ll.display()
