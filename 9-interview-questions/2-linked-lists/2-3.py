# Given a middle node (i.e., not the first or last node) in a singly linked list, 
# delete the node from the list.
# Example: 
#   Input: Node c in a -> b -> c -> d -> e -> f
#   Output: No need to return, but the new list is a -> b -> d -> e -> f
# Note our only input is c, which is not the head

from singlylinkedlist import SinglyLinkedList as LL

def deleteMiddleNode(node):
    node.value = node.next.value
    node.next = node.next.next

ll = LL("a")
ll.insertMultiple(["b", "c", "d", "e", "f"])
ll.traverse()
node = ll.getNodeByIndex(2)
deleteMiddleNode(node)
ll.traverse()