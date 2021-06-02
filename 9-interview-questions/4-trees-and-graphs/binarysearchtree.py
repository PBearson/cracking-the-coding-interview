from binarytreenode import BinaryTreeNode
import random

# BST rules: When we insert, if the value <= current node, then it is a left-child of the  current node.
# Otherwise, it is a right child of the current node.

class BinarySearchTree(BinaryTreeNode):
    def __init__(self, value = None, parent = None):
        super().__init__(value, parent)

    def insert(self, value):
        if self.value == None:
            self.__init__(value)
            return
            
        curr = self
        parent = None

        while curr:
            parent = curr
            if value <= curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = BinaryTreeNode(value, parent)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = BinaryTreeNode(value, parent)
                    break

def test():
    bst = BinarySearchTree(random.randint(1, 50))
    for i in range(10):
        bst.insert(random.randint(1, 50))

    bst.traverseBFS()
    bst.traverseDFS()    

if __name__ == "__main__":
    test()