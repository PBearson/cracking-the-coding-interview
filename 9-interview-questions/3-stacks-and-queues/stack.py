class StackNode:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value = 0):
        self.top = StackNode(value)
        self.size = 1

    def push(self, value):
        node = StackNode(value)
        node.next = self.top
        self.top = node
        self.size += 1
        
    def isEmpty(self):
        return self.size == 0

    def traverse(self):
        curr = self.top
        while curr:
            print(curr.value, end = " ")
            curr = curr.next
        print("")

    def peek(self):
        if self.top:
            return self.top.value
        return None

    def pop(self):
        if self.top:
            self.top = self.top.next
            self.size -= 1

def test():
    stack = Stack(1)
    print(stack.peek())
    stack.push(2)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())

if __name__ == "__main__":
    test()