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

def checkBalancedV2(tree):
    depths = []
    queue = [(tree, 0)]
    visited = [tree]

    while len(queue) > 0:
        currNode, curDepth = queue.pop(0)

        if currNode.left is None and currNode.right is None:
            if curDepth not in depths:
                depths.append(curDepth)
        else:
            if currNode.left and currNode.left not in visited:
                visited.append(currNode.left)
                queue.append((currNode.left, curDepth + 1))
            if currNode.right and currNode.right not in visited:
                visited.append(currNode.right)
                queue.append((currNode.right, curDepth + 1))

    return max(depths) - min(depths) < 2

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)
tree.right.right.right = BinaryTreeNode(8)

assert True == checkBalanced(tree)
assert True == checkBalancedV2(tree)

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(9)
tree.left.left = BinaryTreeNode(3)
tree.left.right = BinaryTreeNode(7)

assert True == checkBalanced(tree)
assert True == checkBalancedV2(tree)

tree.left.right.left = BinaryTreeNode(12)

assert False == checkBalanced(tree)
assert False == checkBalancedV2(tree)

tree.left.right.left.left = BinaryTreeNode(16)
tree.left.right.left.right = BinaryTreeNode(0)

assert False == checkBalanced(tree)
assert False == checkBalancedV2(tree)