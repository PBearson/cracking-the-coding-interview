# Given 2 linked lists representing two integers, add the "integers" and return the sum as a linked list.
# The digits are stored in reverse order, i.e., the head is the ones digit. The output should have similar ordering.
# Example:
#   Input: 7 -> 1 -> 6 and 5 -> 9 -> 2
#   Output: 2 -> 1 -> 9 (since 617 + 295 = 912)

# Follow up: Now do it when the digits are stored in forward order.
# Example:
#   Input: 6 -> 1 -> 7 and 2 -> 9 -> 5
#   Output: # 9 -> 1 -> 2 (since 617 + 295 = 912)

# Idea: We need a function for converting from a linked list to an int and from an int to a linked list.
# To convert to an int, we traverse the node like so: 912 = 2 * 10^0 + 1 * 10^1 + 9 * 10^2
# To convert to a linked list, the head value is (912 % 10^1) / 10^0 = 2 -> (910 % 10^2) / 10^1 = 1 -> (900 % 10^3) / 10^2 = 9
# Unfortunately this way is considered "cheating". We need another way.

# Idea 2: Iterate over the linked lists and add their digits together. If a certain digit is greater than 10, then we must carry the 1 to the next digit.
# This can be done in-place, i.e., we just update one of the linked lists.

# Follow up idea: First add the digits in each place verbatim. Then iterate through the linked lists and if the next digit is greater than 10, subtract 10
# and increment the current node by 1.

from singlylinkedlist import SinglyLinkedList as LL
from singlylinkedlist import Node
import math

def LLToIntReverse(ll):
    result = 0
    power = 0
    curr = ll.head

    while curr != None:
        result += curr.value * 10 ** power
        power += 1
        curr = curr.next

    return result

def intToLLReverse(value):
    ll = LL()
    firstDigit = value % 10
    ll.head.value = firstDigit
    value -= firstDigit
    curr = ll.head
    power = 1

    while value > 0:
        digit = int(value % (10 ** (power + 1)) / (10 ** power))
        curr.next = Node(digit) 
        value -= digit * 10 ** power
        power += 1
        curr = curr.next

    return ll

def sumLinkedListsReverseCheating(ll1, ll2):
    sum = LLToIntReverse(ll1) + LLToIntReverse(ll2)
    return intToLLReverse(sum)

def getListLength(ll):
    if(ll.head is None):
        return 0

    length = 0
    curr = ll.head

    while curr is not None:
        length += 1
        curr = curr.next
    return length

def sumLinkedListsForward(ll1, ll2):

    ll1Length = getListLength(ll1)
    ll2Length = getListLength(ll2)

    if ll1Length < ll2Length:
        for i in range(ll2Length - ll1Length):
            node = Node()
            node.next = ll1.head
            ll1.head = node
    elif ll1Length > ll2Length:
        for i in range(ll1Length - ll2Length):
            node = Node()
            node.next = ll2.head
            ll2.head = node

    ll1Curr = ll1.head
    ll2Curr = ll2.head

    while ll1Curr is not None or ll2Curr is not None:
        if ll1Curr is None:
            digit = ll2Curr.value
            ll1Curr = Node(digit)
        elif ll2Curr is None:
            break
        else:
            ll1Curr.value += ll2Curr.value
            if ll1Curr.value > 9:
                if ll1Curr == ll1.head:
                    newHead = Node(1)
                    newHead.next = ll1Curr
                    ll1Curr.value -= 10
                else:
                    ll1Prev.value += 1
                    ll1Curr.value -= 10

        ll1Prev = ll1Curr
        ll2Prev = ll2Curr
        ll1Curr = ll1Curr.next
        ll2Curr = ll2Curr.next
    return ll1

def sumLinkedListsReverse(ll1, ll2):
    ll1Curr = ll1.head
    ll2Curr = ll2.head
    carry = 0

    while ll1Curr is not None or ll2Curr is not None:
        if ll1Curr is None:
            digit = ll2Curr.value
            ll1Curr = Node(digit)
        elif ll2Curr is None:
            break
        else:
            digit = ll1Curr.value + ll2Curr.value + carry
            ll1Curr.value = digit % 10
            if digit > 9:
                carry = 1
            else:
                carry = 0
        ll1Curr = ll1Curr.next
        ll2Curr = ll2Curr.next
    if carry == 1:
        ll1.insert(1)
    return ll1

ll1 = LL(9)
ll1.insertMultiple([7, 8])
ll2 = LL(6)
ll2.insertMultiple([8, 5])

llSum = LL(5)
llSum.insertMultiple([6, 4, 1])

assert llSum.toString() == sumLinkedListsReverse(ll1, ll2).toString()

ll1 = LL(3)
ll1.insertMultiple([2, 4])
ll2 = LL(5)
ll2.insert(6)

llSum = LL(8)
llSum.insertMultiple([8, 4])

assert llSum.toString() == sumLinkedListsReverse(ll1, ll2).toString()

ll1 = LL(6)
ll1.insertMultiple([1, 7])
ll2 = LL(2)
ll2.insertMultiple([9, 5])

llSum = LL(9)
llSum.insertMultiple([1, 2])

assert llSum.toString() == sumLinkedListsForward(ll1, ll2).toString()

ll1 = LL(4)
ll1.insertMultiple([2, 3])
ll2 = LL(6)
ll2.insert(5)

llSum = LL(4)
llSum.insertMultiple([8, 8])

assert llSum.toString() == sumLinkedListsForward(ll1, ll2).toString()