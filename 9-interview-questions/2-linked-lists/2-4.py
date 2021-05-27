# Write a function that partitions a linked list around a value x such that all nodes less than x come before
# all values greater than or equal to x
# Note that x itself can be anywhere in the right partition
# Example:
#   In:     3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, x = 5
#   Out:    3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# Idea: First lets count the number of elements < x
# Then iterate over the list, and when we see an element >= x, remove it and insert it (at the end of the list)
# Meanwhile, count the number of elements < x and stop when we have seen all of them

from singlylinkedlist import SinglyLinkedList as LL

def countSmallerElements(ll, x):
    curr = ll.head
    num = 0

    while curr != None:
        if curr.value < x:
            num += 1
        curr = curr.next
    return num

def partition(ll, x):
    smallerElements = countSmallerElements(ll, x)
    smallerElementsSeen = 0
    curr = ll.head

    while smallerElementsSeen < smallerElements:
        if curr.value >= x:
            ll.insert(curr.value)
            curr.value = curr.next.value
            curr.next = curr.next.next
        else:
            smallerElementsSeen += 1
            curr = curr.next
    return ll

def partitionv2(ll, x):
    curr = ll.tail = ll.head

    while curr:
        nextNode = curr.next
        
        if curr.value < x:
            curr.next = ll.head
            ll.head = curr
        else:
            ll.tail.next = curr
            ll.tail = curr
            curr.next = None
        curr = nextNode

ll = LL(3)
ll.generate(9, 0, 10)
ll.traverse()
partitionv2(ll, 5)
ll.traverse()


