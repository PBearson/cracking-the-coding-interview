class BinaryTreeNode:
    def __init__(self, value = 0):
        self.value = value
        self.left = None
        self.right = None
        
    def getSize(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.getSize()
        elif self.right is None:
            return 1 + self.left.getSize()
        else:
            return 1 + self.left.getSize() + self.right.getSize()

    
def test():
    root = BinaryTreeNode(1)
    left = BinaryTreeNode(2)
    right = BinaryTreeNode(3)
    leftleft = BinaryTreeNode(4)
    leftright = BinaryTreeNode(5)
    rightleft = BinaryTreeNode(6)
    rightright = BinaryTreeNode(7)

    root.left = left
    root.right = right
    left.left = leftleft
    left.right = leftright
    right.left = rightleft
    right.right = rightright

    print(root.getSize(), left.getSize(), right.getSize())


if __name__ == "__main__":
    test()