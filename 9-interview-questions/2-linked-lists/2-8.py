# Given a linked list which might contain a loop, return the node at the beginning of the loop (if it exists)
# Example:
#   Input: A -> B -> C -> D -> E -> C (same C as before)
#   Output: C

# Idea: Store each node in a hash table as we traverse it. Return True if we find a collision.
# Requires O(n) space and O(n) time.

# Idea 2: Use the runner approach. If the loop repeats at index N, then there will be a collision at index length - 1 - N

from singlylinkedlist import Node
from singlylinkedlist import SinglyLinkedList as LL

def getLoopNodeV2(ll):
    slow = fast = ll.head

    while fast and fast.next:        
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        
    slow = ll.head

    if fast is None or fast.next is None:
        return None

    
    while fast is not slow:
        fast = fast.next
        slow = slow.next
        
    return fast

def getLoopNode(ll):
    nodes = {}
    curr = ll.head

    while curr:
        if curr in nodes.keys():
            return curr
        nodes[curr] = 1
        curr = curr.next
    return None

nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")
nE = Node("E")

ll = LL()
ll.head = nA
ll.insertMultipleNodes([nB, nC, nD, nE, nC])

assert nC == getLoopNode(ll)
assert nC == getLoopNodeV2(ll)

nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")
nE = Node("E")

ll = LL()
ll.head = nA
ll.insertMultipleNodes([nB, nC, nD, nE, nA])

assert nA == getLoopNode(ll)
assert nA == getLoopNodeV2(ll)

nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")
nE = Node("E")

ll = LL()
ll.head = nA
ll.insertMultipleNodes([nB, nC, nD, nE])

assert None == getLoopNode(ll)
assert None == getLoopNodeV2(ll)