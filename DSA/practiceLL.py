class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglleLL:
    def middleNode(self,head):
        self.head = head
        curr = head
        l = 0
        while curr != None :
            curr = curr.next
            l+=1

        for i in range(l//2):
            curr = curr.next
        return curr
    
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

SinglleLL()