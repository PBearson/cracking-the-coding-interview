# Given an array of sorted (ascending) unique integer elements, convert it to a binary search tree with minimal height

# Idea: Pick the middle element. That is the root. Then partition the array into 2 halves. 
# Pick the middle element in both halves. Insert them. Do this until all nodes have been inserted.

from binarysearchtree import BinarySearchTree as BST

def convertToBSTHelper(array, bst):
    middle = int(len(array) / 2)
    bst.insert(array[middle])

    leftArr = array[0:middle]
    rightArr = array[middle + 1:]

    if len(leftArr) > 0:
        convertToBSTHelper(leftArr, bst)
    if len(rightArr) > 0:
        convertToBSTHelper(rightArr, bst)

def convertToBST(array):
    bst = BST()
    convertToBSTHelper(array, bst)
    return bst

array = [3, 4, 7, 9, 12, 81, 100]

bst = convertToBST(array)

assert bst.getMaxDepth(bst) == 3
