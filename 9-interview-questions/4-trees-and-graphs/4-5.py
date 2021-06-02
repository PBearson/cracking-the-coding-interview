# Given a binary tree, check if it is a binary search tree

# Idea: For a given node, its parent, grandparent, great-grandparent, etc., give us information 
# we need to decide if that given node satisfies the BST property. Basically, the sequence of parents
# (and whether they were "left" parents or "right" parents, so to speak), tell us all we need to know 
# about whether the given node is valid in the BST or node. We can recursively check each node, passing in
# information about the parents at each recursive call. The information is just a "min" value and a "max" value
# which the current node's value should fall between. 

# Another way to think about it: Given a node, if we look at the left child, then the value of that child can
# be at most the value of the parent. In other words, when we look at the left child, we update the max value.
# If we look at the right child, then the value of that child must be strictly greater than the value of the parent.
# Thus, when we look at the right child, we update the min value. All children must fall within the min and max values
# that are updated as needed.

# In our BST, left child is <= parent, while right child is strictly > parent.

from binarytreenode import BinaryTreeNode

def isBST(tree, minVal = -2 ** 32, maxVal = 2 ** 32):
    if tree is None:
        return True

    if tree.value <= minVal or tree.value > maxVal:
        return False
    
    return isBST(tree.left, minVal, min(maxVal, tree.value)) and isBST(tree.right, max(minVal, tree.value), maxVal)
    
tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(0)
tree.left.left = BinaryTreeNode(-2)
tree.right = BinaryTreeNode(3)
tree.right.left = BinaryTreeNode(2)
tree.right.right = BinaryTreeNode(100)

assert True == isBST(tree)

tree.right.left.value = 0

assert False == isBST(tree)

tree.right.left.value = 2.0001

assert True == isBST(tree)
