# Post order traversal: Left branch, right branch, current node

from binarytreenode import BinaryTreeNode

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.value)

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

postOrderTraversal(root)