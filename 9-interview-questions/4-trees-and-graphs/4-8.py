# Given two nodes in a binary tree, return their first common ancestor.
# Do not store additional nodes in a data structure.

# Idea: Let X and Y be the nodes. Pick X and check its branches. If either branch contains Y, then X 
# is the first common ancestor. Else, move to the parent of X, and check the branch which does not contain X.
# Do this until we find a branch which contains Y.

# What if we do not have links to our parents? We would need another solution.

# Idea 2: If we do not have links to parents, we may assume that we have a reference to the root.
# Starting from the root, create a string that describes the path taken to find node X. For example,
# a string rlr means starting from the root, we traversed the right child, then left child, then right
# child before we found the node. Do the same for node Y. Then find the first common substring, traverse it, 
# and return the last node.

from binarytreenode import BinaryTreeNode

# Return true if nodeX contains nodeY, else return False 
def contains(nodeX, nodeY):
    if nodeX is None:
        return False
    if nodeX == nodeY:
        return True
    return contains(nodeX.left, nodeY) or contains(nodeX.right, nodeY)

# Get the path to a node as a string, e.g., "rlr" means starting from the root,
# traverse the right child, followed by the left child, followed by the right.
def getPathToNode(root, node, prefix = ""):
    if root is None:
        return
    if root == node:
        return prefix
    return getPathToNode(root.left, node, prefix + "l") or getPathToNode(root.right, node, prefix + "r")

# Find the common path between 2 paths (in the form as strings as described by getPathToNode(.))
def findCommonPath(path1, path2):
    p = 0
    while path1[p] == path2[p]:
        p += 1
        if p >= min(len(path1), len(path2)):
            break
    return path1[0:p]

# Given a path, find the resulting node by traversing the path.
def pathToNode(root, path):
    if len(path) == 0:
        return root
    if path[0] == "l":
        return pathToNode(root.left, path[1:])
    return pathToNode(root.right, path[1:])


def firstCommonAncestorV2(root, nodeX, nodeY):
    nodeXPath = getPathToNode(root, nodeX)
    nodeYPath = getPathToNode(root, nodeY)
    commonPath = findCommonPath(nodeXPath, nodeYPath)
    return pathToNode(root, commonPath)

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

# assert firstCommonAncestor(llr, rl) == root
# assert firstCommonAncestorV2(root, llr, rl) == root

# assert firstCommonAncestor(lll, llrr) == ll
# assert firstCommonAncestorV2(root, lll, llrr) == ll

# assert firstCommonAncestor(right, rl) == firstCommonAncestor(rr, right) == right
assert firstCommonAncestorV2(root, right, rl) == firstCommonAncestorV2(root, rr, right) == right