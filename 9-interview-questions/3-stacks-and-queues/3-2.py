# Implement a stack with a min() function that returns the smallest element.
# Push(), pop(), and min() should all operate in O(1) time

import random

class StackNode:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value = 0):
        self.top = StackNode(value)
        self.mintop = StackNode(value)

    def push(self, value):
        if self.isEmpty():
            self.top = StackNode(value)
            self.mintop = StackNode(value)
        else:
            node = StackNode(value)
            node.next = self.top
            self.top = node

            if self.top.value <= self.mintop.value:
                minNode = StackNode(value)
                minNode.next = self.mintop
                self.mintop = minNode
        
    def isEmpty(self):
        return self.top == None

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
            if self.top.value == self.mintop.value:
                self.mintop = self.mintop.next
            self.top = self.top.next
            
    def min(self):
        if self.mintop:
            return self.mintop.value
        return None

# Test

s = Stack(random.randint(0, 2))

for i in range(10):
    s.push(random.randint(0, 2))

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())

s.pop()

s.traverse()
print(s.min())