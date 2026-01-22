class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglleLL:
    def middleNode(self, head):
        curr = head
        l = 0

        # count length
        while curr is not None:
            l += 1
            curr = curr.next

        # reset curr to head
        curr = head

        # move to middle
        for _ in range(l // 2):
            curr = curr.next

        return curr


# create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# linking
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# call method
ll = SinglleLL()
mid = ll.middleNode(n1)
print("Middle Node:", mid.data)
