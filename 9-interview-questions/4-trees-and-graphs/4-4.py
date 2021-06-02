# Given a binary tree, return True if it is balanced. A node is balanced if its 2 sub-trees do not differ
# in height more than 1.

# Idea: Find the min depth and max depth separately, then compare their differences. 
# This is O(2n) = O(n) for n nodes in the tree. We can do better.

# Idea 2: Go through tree once and save the depth of each leaf node in a list.
# Then check that all depths are short enough.
# Costs O(n) time and O(n) space. Twice as fast.

from binarytreenode import BinaryTreeNode

def findMaxDepth(tree, level = 0):
    if tree is None:
        return level

    return max(findMaxDepth(tree.left, level + 1), findMaxDepth(tree.right, level + 1))

def findMinDepth(tree, level = 0):
    if tree is None:
        return level

    return min(findMinDepth(tree.left, level + 1), findMinDepth(tree.right, level + 1))

def checkBalanced(tree):
    return findMaxDepth(tree) - findMinDepth(tree) < 2

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)
tree.right.right.right = BinaryTreeNode(8)

assert True == checkBalanced(tree)

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(9)
tree.left.left = BinaryTreeNode(3)
tree.left.right = BinaryTreeNode(7)

assert True == checkBalanced(tree)

tree.left.right.left = BinaryTreeNode(12)

assert False == checkBalanced(tree)

tree.left.right.left.left = BinaryTreeNode(16)
tree.left.right.left.right = BinaryTreeNode(0)

assert False == checkBalanced(tree)