# Use a single array to implement 3 stacks

# Idea: Divide the array into 3 even-sized "chunks" where the first index indicates the top of the stack.
# Make it dynamic, i.e., double the size of the array if one of the "stacks" gets too large

class StackArray():
    def __init__(self):
        self.stack = [None] * 30
        self.top1 = 0
        self.top2 = 0
        self.top3 = 0

    def resizeArray(self):
        print("Resize array")
        newStack = [None] * len(self.stack) * 2

        # Copy stack 1
        for i in range(int(len(self.stack) / 3)):
            newStack[i] = self.stack[i]

        # Copy stack 2
        for i in range(int(len(self.stack) / 3)):
            newIndex = int(len(newStack) / 3) + i
            oldIndex = int(len(self.stack) / 3) + i
            newStack[newIndex] = self.stack[oldIndex]

        # Copy stack 3
        for i in range(int(len(self.stack) / 3)):
            newIndex = int(len(newStack) * 2/3) + i
            oldIndex = int(len(self.stack) * 2/3) + i
            newStack[newIndex] = self.stack[oldIndex]

        self.stack = newStack
            

    def pushStack1(self, value):
        if self.top1 >= len(self.stack) / 3:
            print("Stack 1 is too big")
            self.resizeArray()
        index = self.top1
        self.stack[index] = value
        self.top1 += 1
        
    def popStack1(self):
        self.top1 = max(0, self.top1 - 1)

    def peekStack1(self):
        if self.top1 > 0:
            return self.stack[self.top1 - 1]
        return None

    def pushStack2(self, value):
        if self.top2 >= len(self.stack) / 3:
            print("Stack 2 is too big")
            self.resizeArray()
        index = int(len(self.stack) / 3) + self.top2
        self.stack[index] = value
        self.top2 += 1
        

    def popStack2(self):
        self.top2 = max(0, self.top2 - 1)

    def peekStack2(self):
        if self.top2 > 0:
            index = int(len(self.stack) / 3) + self.top2
            return self.stack[index - 1]
        return None

    def pushStack3(self, value):
        if self.top3 >= len(self.stack) / 3:
            print("Stack 3 is too big")
            self.resizeArray()
        index = int(len(self.stack) * 2/3) + self.top3
        self.stack[index] = value
        self.top3 += 1

    def popStack3(self):
        self.top3 = max(0, self.top3 - 1)
    
    def peekStack3(self):
        if self.top3 > 0:
            index = int(len(self.stack) * 2/3) + self.top3
            return self.stack[index - 1]
        return None

s = StackArray()
for i in range(10):
    s.pushStack1(i)
    s.pushStack2(i * 2)
    s.pushStack3(i * 3)
print(s.stack)

s.pushStack1(4)
print(s.stack)

s.pushStack2(4)
print(s.stack)

s.pushStack3(4)
print(s.stack)

s.pushStack3(4)
print(s.stack)

s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)
s.pushStack3(4)
print(s.stack)