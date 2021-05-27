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

    def traverse(self):
        curr = self.head
        
        while curr != None:
            print(curr.value, end = " ")
            curr = curr.next

        print("")

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