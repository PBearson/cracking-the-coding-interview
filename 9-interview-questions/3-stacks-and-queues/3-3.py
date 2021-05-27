# Implement a SetOfStacks data structure that creates a new stack if  the old stack reaches capacity
# Push() and Pop() should behave identically to a normal stack

# Idea: Use a stack of stacks. When a stack is full and we push, push a new stack. When a stack is empty and we pop, pop the current stack.

# Follow up: Write a function PopAt(index) that pops an element on a specific stack.

# Idea: 

from stack import Stack

class SetOfStacks:
    def __init__(self, value = 0, capacity = 5):
        stack = Stack(value)
        self.stacks = [stack]
        self.capacity = capacity
    
    def push(self, value):
        if len(self.stacks) == 0:
            self.__init__(value, self.capacity)
        else:
            curStack = self.stacks[len(self.stacks) - 1]
            if curStack.size < self.capacity:
                curStack.push(value)
            else:
                newStack = Stack(value)
                self.stacks.append(newStack)

    def peek(self):
        return self.stacks[len(self.stacks) - 1].top.value

    def pop(self):
        index = len(self.stacks) - 1
        if index >= 0:
            if self.stacks[index].size > 1:
                self.stacks[index].pop()
            elif self.stacks[index].size == 1:
                self.stacks[index].pop()
                self.stacks.pop()
            else:
                self.stacks.pop()
                if index - 1 >= 0:
                    self.stacks[index - 1].pop()

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            return
        
        self.stacks[index].pop()

        tmpStack = Stack()
        tmpStack.pop()

        while len(self.stacks) - 1 > index:
            tmpStack.push(self.peek())
            self.pop()

        while tmpStack.size > 0:
            self.push(tmpStack.peek())
            tmpStack.pop()

def test():
    stacks = SetOfStacks(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    stacks.push(6)
    stacks.push(7)
    stacks.push(8)

    for l in range(len(stacks.stacks)):
        stacks.stacks[l].traverse()

    stacks.popAt(0)

    print("After popAt:")

    for l in range(len(stacks.stacks)):
        stacks.stacks[l].traverse()

if __name__ == "__main__":
    test()