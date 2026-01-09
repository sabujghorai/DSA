class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head

    def InsertAtTheEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next 
            t1.next = temp
        else:
            self.head = temp

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.info)
            t1 = t1.next
        print(t1.info)

obj = SinglyLinkedList()
obj.InsertAtTheEnd(10)
obj.InsertAtTheEnd(20)
obj.InsertAtTheEnd(30)
obj.printLL()