import random

class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self, value = 0):
        self.head = Node(value)
    
    def insert(self, value):
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = Node(value)

    def insertNode(self, node):
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = node

    def insertMultiple(self, values):
        for v in values:
            self.insert(v)

    def insertMultipleNodes(self, nodes):
        for n in nodes:
            self.insertNode(n)

    def traverse(self):
        curr = self.head
        
        while curr != None:
            print(curr.value, end = " ")
            curr = curr.next

        print("")

    def toString(self):
        result = ""
        curr = self.head

        while curr != None:
            result = result + str(curr.value) + " "
            curr = curr.next
        return result

    def remove(self, value):
        curr = self.head
        prev = None

        while curr != None:
            if curr.value == value:
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                curr = None
                break
            else:
                prev = curr
                curr = curr.next 

    def generate(self, numNodes, minVal, maxVal):
        for i in range(numNodes):
            val = random.randint(minVal, maxVal)
            self.insert(val)

    def getNodeByIndex(self, index):
        curr = self.head
        currIndex = 0

        while curr != None:
            if currIndex == index:
                return curr
            else:
                curr = curr.next
                currIndex += 1

        return None

    def getLength(self):
        curr = self.head
        length = 0

        while curr != None:
            length += 1
            curr = curr.next
        return length

def test():
    sll = SinglyLinkedList(4)
    sll.insert(5)
    sll.insert(6)
    sll.insert(4)
    sll.insert("Bryan")
    sll.traverse()

    sll.remove(4)
    sll.traverse()

    sll.remove(4)
    sll.traverse()

    sll.remove("Bryan")
    sll.traverse()

if __name__ == "__main__":
    test()