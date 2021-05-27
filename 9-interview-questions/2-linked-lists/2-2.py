# Find the kth-to-last node in a singly linked list

# Idea: First find the length by traversing the list once, then 
# Find the N - Kth node, where N is the length of the list

from singlylinkedlist import SinglyLinkedList as LL

def listLength(ll):
    node = ll.head
    length = 0

    while node != None:
        length += 1
        node =  node.next

    return length

def getKthToLastNode(ll, k):
    node = ll.head
    length = listLength(ll)
    if k >= length or k < 0:
        return None

    index = 0
    targetIndex = length - k - 1

    while index < targetIndex:
        node = node.next
        index += 1

    return node    

ll = LL(2)
ll.generate(9, 0, 10)
ll.traverse()
for i in range(10):
    print(getKthToLastNode(ll, i).value)
    # print(getKthToLastNodeRecursively(ll, i).value)