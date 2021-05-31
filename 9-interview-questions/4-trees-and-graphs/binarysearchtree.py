from binarytreenode import BinaryTreeNode
import random

# BST rules: When we insert, if the value <= current node, then it is a left-child of the  current node.
# Otherwise, it is a right child of the current node.

class BinarySearchTree(BinaryTreeNode):
    def __init__(self, value = 0, parent = None):
        super().__init__(value, parent)

    def insert(self, value):
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
        
def isBST(bst):
    if bst is None or bst.getSize() == 1:
        return True
    
    if bst.left is None:
        return bst.value < bst.right.value and isBST(bst.right)
    elif bst.right is None:
        return bst.value >= bst.left.value and isBST(bst.left)
    else:
        return bst.value < bst.right.value and bst.value >= bst.left.value and isBST(bst.left) and isBST(bst.right)

def test():
    bst = BinarySearchTree(random.randint(1, 50))
    for i in range(10):
        bst.insert(random.randint(1, 50))

    bst.traverseBFS()
    bst.traverseDFS()

    assert True == isBST(bst)
    

if __name__ == "__main__":
    test()