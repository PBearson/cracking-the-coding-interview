class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getSize(self):
        if len(self.children) == 0:
            return 1
        else:
            childrenSize = 0
            for c in self.children:
                childrenSize += c.getSize()
            return 1 + childrenSize

def test():
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    leftleft = TreeNode(4)
    leftright = TreeNode(5)
    rightleft = TreeNode(6)
    rightright = TreeNode(7)

    root.addChild(left)
    root.addChild(right)
    left.addChild(leftleft)
    left.addChild(leftright)
    right.addChild(rightleft)
    right.addChild(rightright)

    print(root.getSize(), left.getSize(), right.getSize())


if __name__ == "__main__":
    test()

