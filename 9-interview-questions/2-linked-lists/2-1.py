# Write code to remove duplicates from an unsorted linked list
# FOLLOW UP: Do it without using a temporary buffer

# Idea (using buffer): Store frequency of values in hash table
# Then iterate over hash table and remove items with frequency > 1
# This will preserve the last instance of each value, rather than the first

# Idea (no buffer): Sort the Linked List first, then check pairs of nodes.
# Remove the later node if the pair are identical.

from singlylinkedlist import SinglyLinkedList as LL
import time

def getFrequencyOfNodes(node):
    frequency = {}
    curr = node.head

    while(curr != None):
        if curr.value in frequency.keys():
            frequency[curr.value] += 1
        else:
            frequency[curr.value] = 1
        curr = curr.next
    return frequency


def removeDuplicates(node):
    frequency = getFrequencyOfNodes(node)
    for f in frequency.keys():
        if frequency[f] > 1:
            for i in range(frequency[f] - 1):
                ll.remove(f)
    return node

# O(n^2) sorting algorithm
# Inefficient but at least it requires no additional space
def sortLinkedList(node):
    curr = node.head

    while curr.next != None:
        if curr.value < curr.next.value:
            node.remove(curr.value)
            node.insert(curr.value)
            curr = node.head
        else:
            curr = curr.next
    return node

def removeDuplicatesNoBuffer(node):
    node = sortLinkedList(node)
    curr = node.head

    while curr.next != None:
        if curr.value == curr.next.value:
            curr = curr.next
            node.remove(curr.value)
        else:
            curr = curr.next
    return node

def removeDuplicatesNoBufferNoSort(node):
    ni = node.head

    while ni != None:
        nj = ni
        while nj.next != None:
            if ni.value == nj.next.value:
                nj.next = nj.next.next
            else:
                nj = nj.next
        ni = ni.next
    return node

ll = LL()
ll.generate(20, 0, 5)
ll.traverse()
removeDuplicates(ll)
ll.traverse()

ll = LL()
ll.generate(20, 0, 5)
ll.traverse()
removeDuplicatesNoBuffer(ll)
ll.traverse()

ll = LL()
ll.generate(20, 0, 5)
ll.traverse()
removeDuplicatesNoBufferNoSort(ll)
ll.traverse()