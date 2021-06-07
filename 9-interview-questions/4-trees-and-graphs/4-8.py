# Given two nodes in a binary tree, return their first common ancestor.
# Do not store additional nodes in a data structure.

# Idea: Let X and Y be the nodes. Pick X and check its branches. If either branch contains Y, then X 
# is the first common ancestor. Else, move to the parent of X, and check the branch which does not contain X.
# Do this until we find a branch which contains Y.

from binarytreenode import BinaryTreeNode

# Return true if nodeX contains nodeY, else return False 
def contains(nodeX, nodeY):
    if nodeX is None:
        return False
    if nodeX == nodeY:
        return True
    return contains(nodeX.left, nodeY) or contains(nodeX.right, nodeY)

def firstCommonAncestor(nodeX, nodeY):
    if contains(nodeX, nodeY):
        return nodeX

    while nodeX is not None:
        parent = nodeX.parent
        if parent.left == nodeX:
            targetChild = parent.right
        else:
            targetChild = parent.left

        nodeX = parent
        if contains(targetChild, nodeY) or nodeX == nodeY:
            return nodeX
            
    return None


root = BinaryTreeNode(1)
left = BinaryTreeNode(2, root)
right = BinaryTreeNode(3, root)
ll = BinaryTreeNode(4, left)
lll = BinaryTreeNode(5, ll)
llr = BinaryTreeNode(6, ll)
llrr = BinaryTreeNode(7, llr)
rl = BinaryTreeNode(8, right)
rr = BinaryTreeNode(9, right)

root.left = left
root.right = right
left.left = ll
ll.left = lll
ll.right = llr
llr.right = llrr
right.left = rl
right.right = rr

assert firstCommonAncestor(llr, rl) == root
assert firstCommonAncestor(lll, llrr) == ll
assert firstCommonAncestor(right, rl) == firstCommonAncestor(rr, right) == right
