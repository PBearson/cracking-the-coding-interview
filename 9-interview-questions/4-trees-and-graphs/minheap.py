from binarytreenode import BinaryTreeNode
import random
import math

class MinHeap(BinaryTreeNode):
    def __init__(self, value = 0, parent = None):
        super().__init__(value, parent)
        self.size = 1

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