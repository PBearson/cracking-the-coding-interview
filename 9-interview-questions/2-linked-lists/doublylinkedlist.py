class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value = 0):
        node = Node(value)
        self.head = node
        self.tail = node
    
    def insertAtHead(self, value):
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertAtTail(self, value):
        node = Node(value)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def traverseForward(self):
        curr = self.head
        
        while curr != None:
            print(curr.value, end = " ")
            curr = curr.next

        print("")

    def traverseBackward(self):
        curr = self.tail

        while curr != None:
            print(curr.value, end = " ")
            curr = curr.prev

        print("")

    def remove(self, value):
        curr = self.head

        while curr != None:
            if curr.value == value:
                if curr == self.head:
                    self.head = curr.next
                    self.head.prev = None
                elif curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                curr = None
                break
            else:
                curr = curr.next 

def test():
    dll = DoublyLinkedList(8)
    dll.insertAtHead(5)
    dll.insertAtHead(6)
    dll.insertAtHead(4)
    dll.insertAtTail("Bryan")
    dll.insertAtHead("Grape")
    dll.traverseForward()

    dll.remove("Grape")
    dll.traverseForward()
    dll.traverseBackward()

    dll.remove("Bryan")
    dll.traverseForward()
    dll.traverseBackward()

    dll.remove(6)
    dll.traverseForward()
    dll.traverseBackward()

if __name__ == "__main__":
    test()