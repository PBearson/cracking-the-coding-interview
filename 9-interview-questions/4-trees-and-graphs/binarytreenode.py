class BinaryTreeNode:
    def __init__(self, value = 0, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    # O(n) approach that uses BFS. Would be more efficient if we used a priority queue.
    def getNodeByIndex(self, index):
        if index == 0:
            return self
        queue = [self]

        counter = 0
        while len(queue) > 0:
            curr = queue.pop(0)
            
            if counter == index:
                return curr

            counter += 1

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return None
        
    def getSize(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.getSize()
        elif self.right is None:
            return 1 + self.left.getSize()
        else:
            return 1 + self.left.getSize() + self.right.getSize()

    def traverseBFS(self):
        queue = [self]

        while len(queue) > 0:
            curr = queue.pop(0)
            print(curr.value, end = " ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print("")

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
    print(root.getNodeByIndex(0).value)

    root.traverseBFS()


if __name__ == "__main__":
    test()