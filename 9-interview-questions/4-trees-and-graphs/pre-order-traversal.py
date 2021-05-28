# Pre order traversal: Current node, left branch, right branch

from binarytreenode import BinaryTreeNode

def preOrderTraversal(node):
    if node is None:
        return
    print(node.value)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

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

preOrderTraversal(root)