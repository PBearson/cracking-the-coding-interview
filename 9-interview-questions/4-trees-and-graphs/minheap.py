from binarytreenode import BinaryTreeNode
import random
import math

class MinHeap(BinaryTreeNode):
    def __init__(self, value = 0, parent = None):
        super().__init__(value, parent)
        self.size = 1

    # Insert steps:
    #   1) Find the soon-to-be-parent node (based on its index, which is a function of the heap size)
    #   2) Add the new node as a child of the parent
    #   3) Bubble-up by swapping with the parent until the heap property is satisfied
    def insert(self, value):

        if self.size == 0:
            self.__init__(value)
            return

        insertionIndex = math.floor((self.size - 1) / 2)
        insertionNode = self.getNodeByIndex(insertionIndex)
        if insertionNode.left:
            insertionNode.right = BinaryTreeNode(value, insertionNode)
            curr = insertionNode.right
        else:
            insertionNode.left = BinaryTreeNode(value, insertionNode)
            curr = insertionNode.left
 
        self.size += 1

        while curr.value < curr.parent.value:
            curr.value, curr.parent.value = curr.parent.value, curr.value
            curr = curr.parent
            if curr.parent is None:
                return

    # Extract steps:
    #   1) Record the current min value
    #   2) Find the last node in the heap, remove it, and set its value to the root's value
    #   3) Bubble-down by swapping with the smallest child until the heap property is satisfied
    def extractMin(self):

        if self.size == 0:
            return None

        minVal = self.value
        
        newRoot = self.getNodeByIndex(self.size - 1)

        self.value = newRoot.value
        newRoot = None

        curr = self
        
        while curr.value > curr.left.value:
            if curr.right is None or curr.left.value < curr.right.value:
                curr.value, curr.left.value = curr.left.value, curr.value
                curr = curr.left
            else:
                curr.value, curr.right.value = curr.right.value, curr.value
                curr = curr.right
            if curr.left is None:
                break

        self.size -= 1

        return minVal

def test():
    heap = MinHeap(random.randint(1, 100))

    for i in range(10):
        heap.insert(random.randint(1, 100))

    while heap.size > 0:
        print(heap.extractMin())

if __name__ == "__main__":
    test()