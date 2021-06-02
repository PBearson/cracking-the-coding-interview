# Given a binary tree, create a linked list of all the nodes at each depth 
# (i.e., a binary tree of depth D should return D linked lists)

# We can probably assume that returning a list/array of linked lists is okay.

from binarytreenode import BinaryTreeNode

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value = None):
        self.head = Node(value)

    def insert(self, value):
        if self.head.value == None:
            self.__init__(value)
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = Node(value)

    def traverse(self):
        curr = self.head

        while curr:
            print(curr.value, end = " ")
            curr = curr.next
        print("")

def treeToLLHelper(tree, lists, curDepth):
    if tree is None:
        return

    if len(lists) < curDepth + 1:
        lists.append(LinkedList(tree.value))
    else:
        list = lists[curDepth]
        list.insert(tree.value)

    treeToLLHelper(tree.left, lists, curDepth + 1)
    treeToLLHelper(tree.right, lists, curDepth + 1)

def treeToLL(tree):
    lists = [LinkedList()]
    treeToLLHelper(tree, lists, 0)

    return lists

# First test perfect binary tree
tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)

lists = treeToLL(tree)

print("Tree 1:")
for l in lists:
    l.traverse()


# Now test a psuedo-random binary tree

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(9)
tree.left.left = BinaryTreeNode(3)
tree.left.right = BinaryTreeNode(7)
tree.left.right.left = BinaryTreeNode(12)
tree.left.right.left.left = BinaryTreeNode(16)
tree.left.right.left.right = BinaryTreeNode(0)

lists = treeToLL(tree)

print("Tree 2:")
for l in lists:
    l.traverse()