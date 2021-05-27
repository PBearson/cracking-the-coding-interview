# Implement a MyQueue class which implements a queue using 2 stacks

# Idea: Let the first stack be our queue and the second stack serve as a temporary buffer.
# When we add to the queue, we really just push to the first stack.
# When we remove from the queue, we pop from the first stack and add to the second stack.
# When we are left with 1 element, we pop it, then we push all the elements from the second
# stack back to the first stack.
# This can actually be generalized for repeated pops. For example, if we know we want to pop N times,
# then we can stop popping from the first stack when we are left with N elements (which is easy as long
# as the stacks keep track of their own size)

from stack import Stack

class MyQueue:
    def __init__(self, value):
        self.stack1 = Stack(value)
        self.first = self.stack1.top
        self.stack2 = Stack()
        self.stack2.pop()

    def add(self, value):
        if self.isEmpty():
            self.__init__(value)
        else:
            self.stack1.push(value)
    
    def remove(self):
        if self.stack1.isEmpty():
            return

        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.peek())
            self.stack1.pop()

        self.stack2.pop()
        self.first = self.stack2.top

        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.peek())
            self.stack2.pop()

    def removeMultiple(self, num):
        if num < 1 or num > self.stack1.size:
            return
        elif num == 1:
            self.remove()
        else:
            for i in range(self.stack1.size - num):
                self.stack2.push(self.stack1.peek())
                self.stack1.pop()
            
            self.stack1 = Stack()
            self.stack1.pop()

            while not self.stack2.isEmpty():
                self.stack1.push(self.stack2.peek())
                self.stack2.pop()

    def peek(self):
        if not self.isEmpty():
            return self.first.value
        return None

    def traverse(self):
        self.stack1.traverse()

    def isEmpty(self):
        return self.stack1.size == 0

def test():
    queue = MyQueue(1)
    queue.add(2)
    queue.add(3)
    queue.traverse()
    print(queue.peek())
    queue.remove()
    queue.traverse()
    print(queue.peek())

    queue.remove()
    queue.traverse()
    print(queue.peek())

    queue.remove()
    queue.traverse()
    print(queue.peek())

    queue.add(4)
    queue.traverse()
    print(queue.peek())
    queue.add(5)
    queue.traverse()
    print(queue.peek())
    queue.add(6)
    queue.traverse()
    print(queue.peek())

    queue.add(11)

    queue.removeMultiple(4)

    queue.traverse()


if __name__ == "__main__":
    test()
