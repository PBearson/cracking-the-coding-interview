# Given a binary search tree, write an algorithm to find the "next" (in-order) node of a given node in a BST.
# Assume all nodes have links to their parents.

# Idea: One way is to just do the in-order traversal, but this costs O(n) time.
# Another way is to find the node, which can be done quickly. 
# Cases:
# If the node has no right child, then traverse up the parents until we hit a bigger (or identical) node. If we hit the root and no match,
# then return None.
# If the node has a right child, go to it, then go all the way to the left-most child.

from binarysearchtree import BinarySearchTree
import random

def getNextNode(node):
    curr = node
    if node.right is None:
        while curr.parent:
            curr = curr.parent
            if curr.value >= node.value:
                return curr
    else:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr

    return None

# Get a random node from the tree. Not great efficiency (O(n)) but it gets the job done.
def getRandomNode(tree):
    treeSize = tree.getSize()
    targetIndex = random.randint(0, treeSize - 1)
    index = 0
    
    queue = [tree]

    while True:
        curr = queue.pop(0)
        if index == targetIndex:
            return curr
        
        index += 1

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

# Testing

tree = BinarySearchTree()
elements = []
for i in range(20):
    value = random.randint(0, 50)
    tree.insert(value)
    elements.append(value)

print("Your tree:", end = " ")
tree.traverseBFS()

node = getRandomNode(tree)
nextNode = getNextNode(node)

if nextNode:
    print("Your node: %d\nNext node: %d" % (node.value, nextNode.value))
else:
    print("Your node: %d\nNo next node" % node.value)

elements = sorted(elements)

nodeIndex = elements.index(node.value)

if nextNode:
    assert elements[nodeIndex + 1] in [nextNode.value, node.value]
else:
    assert node.value == max(elements)