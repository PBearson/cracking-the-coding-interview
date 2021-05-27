class QueueNode:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value = 0):
        self.first = self.last = QueueNode(value)

    def add(self, value):
        if self.isEmpty():
            self.__init__(value)
        else:
            node = QueueNode(value)
            self.last.next = node
            self.last = node
        
    def isEmpty(self):
        return self.first == None

    def traverse(self):
        curr = self.first
        while curr:
            print(curr.value, end = " ")
            curr = curr.next
        print("")

    def peek(self):
        if self.first:
            return self.first.value
        return None

    def remove(self):
        if self.first:
            self.first = self.first.next
        else:
            self.first = self.last = None

def test():
    q = Queue(1)
    q.traverse()
    q.add(2)
    q.traverse()
    q.add(3)
    q.traverse()
    print(q.peek())
    q.remove()
    q.traverse()
    print(q.peek())
    q.remove()
    q.traverse()
    print(q.peek())
    q.remove()
    q.traverse()
    print(q.peek())
    q.remove()
    q.traverse()
    print(q.peek())
    q.add("Hello")
    q.add("Bryan")
    q.traverse()
    print(q.peek())
    q.remove()
    print(q.first.value, q.last.value)

if __name__ == "__main__":
    test()