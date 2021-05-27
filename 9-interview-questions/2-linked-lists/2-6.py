# Given a Linked List, return True if it is a palindrome
# We can probably assume that elements can be of any type, not just ints, strings, etc.
# Example: 5 -> 4 -> 7 -> 4 -> 5 is a palindrome

# Idea 1: Copy elements in an array first, then check if the array is a palindrome, which is trivial.
# However, this costs O(n) space.

# Idea 2: Do it recursively. Assume we know the length of the linked list.

from singlylinkedlist import SinglyLinkedList as LL
import time

def isPalindromeHelper(ll, index, length):
    match = ll.getNodeByIndex(index).value == ll.getNodeByIndex(length - index - 1).value

    if index == 0:
       return match
    else:
        return match and isPalindromeHelper(ll, index - 1, length)

def isPalindromeV2(ll):
    if ll.head is None or ll.head.next is None:
        return True

    length = ll.getLength()

    return isPalindromeHelper(ll, int(length / 2), length)

def isPalindrome(ll):
    if ll.head is None or ll.head.next is None:
        return True

    ll_arr = []
    curr = ll.head

    while curr:
        ll_arr.append(curr.value)
        curr = curr.next

    p1 = 0
    p2 = len(ll_arr) - 1

    while p1 < p2:
        if ll_arr[p1] != ll_arr[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

ll = LL(2)
assert True == isPalindrome(ll)
assert True == isPalindromeV2(ll)

ll = LL(5)
ll.insertMultiple([4, 7, 4, 5])
assert True == isPalindrome(ll)
assert True == isPalindromeV2(ll)

ll = LL(" ")
ll.insertMultiple(["12", "Bryan", " "])
assert False == isPalindrome(ll)
assert False == isPalindromeV2(ll)

ll = LL("@")
ll.insertMultiple(["@", "@", "@", "@", "&"])

assert False == isPalindrome(ll)
assert False == isPalindromeV2(ll)