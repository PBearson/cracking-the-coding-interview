# Sort a stack such that the smallest elements are on top. Only a temporary stack
# can be used as a buffer. The stack supports push(), pop(), peek(), and isEmpty() operations.

# Idea: We could iterate through the buffer and find the max value, (and the frequency of the max value), pushing
# that value to the new stack until the size of the new stack is the same as the old stack. Then we return the new stack.
# However, this could cost O(n^2) runtime.

from stack import Stack
import random
import time

def sortStackV2(stk):
    tmpStack = Stack()
    tmpStack.pop()

    curr = stk.top

    while curr.next:
        if curr.value > curr.next.value:
            candidate = curr.next
            candidateUsed = False

            while stk.top != candidate:
                tmpStack.push(stk.peek())
                stk.pop()
            stk.pop()
            
            while not tmpStack.isEmpty():
                if tmpStack.peek() >= candidate.value or candidateUsed:
                    stk.push(tmpStack.peek())
                    tmpStack.pop()
                else:
                    stk.push(candidate.value)
                    candidateUsed = True
                    curr = stk.top

            if not candidateUsed:
                stk.push(candidate.value)
                curr = stk.top
        else:
            curr = curr.next

    return stk

def sortStack(stk):
    tmpStack = Stack()
    tmpStack.pop()

    prevMaxVal = 2 ** 32

    while tmpStack.size < stk.size:
        maxVal = -2 ** 32
        maxValFreq = 0
        curr = stk.top

        while curr:
            if curr.value > maxVal and curr.value < prevMaxVal:
                maxVal = curr.value
                maxValFreq = 1
            elif curr.value == maxVal:
                maxValFreq += 1
            curr = curr.next

        prevMaxVal = maxVal

        for i in range(maxValFreq):
            tmpStack.push(maxVal)

    return tmpStack

stk = Stack(random.randint(0, 100))

for i in range(30):
    stk.push(random.randint(0, 100))

stk.traverse()
t1 = time.time()
stkSort1 = sortStack(stk)
print(time.time() - t1)
stkSort1.traverse()
t1 = time.time()
stkSort2 = sortStackV2(stk)
print(time.time() - t1)
stkSort2.traverse()