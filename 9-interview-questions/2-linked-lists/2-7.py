# Given 2 singly linked lists, return an intersecting node if they are intersecting (by reference)
# Example:
#   Input: 5 -> 4 -> 12 -> 7 and 9 -> 12 -> 7
#   Output: 12 (this node exists in both lists)

# Idea: If there is an intersection node, then it will have the same value and same next.
# That means all nodes after the intersecting node will be the same.
# All we have to do is traverse the nodes and check if a node matches up.
# First we have to "Align" the lists, meaning the tail of the first list is lined up with the tail of the second.
# We can align easily by first finding the length of each list. 

from singlylinkedlist import Node
from singlylinkedlist import SinglyLinkedList as LL

def getIntersectingNode(ll1, ll2):
    ll1_length = ll1.getLength()
    ll2_length = ll2.getLength()

    if ll1_length < ll2_length:
        curr1 = ll1.head
        curr2 = ll2.getNodeByIndex(ll2_length - ll1_length)
    elif ll2_length < ll1_length:
        curr1 = ll1.getNodeByIndex(ll1_length - ll2_length)
        curr2 = ll2.head
    else:
        curr1 = ll1.head
        curr2 = ll2.head

    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    return None

n1 = Node(5)
n2 = Node(4)
n3 = Node(9)
n4 = Node(12)
n5 = Node(7)

l1 = LL()
l1.head = n1
l1.insertMultipleNodes([n2, n4, n5])
l2 = LL()
l2.head = n3
l2.insertNode(n4)

assert n4 == getIntersectingNode(l1, l2)

