import random


# Given a left and right sorted array, merge them together
# Since they are sorted already, we just maintain pointers to both and
# increment through them as we make comparisons.
# If one array is shorter than the other, then we just append
# the remainder of the longer array to the result at the end
def merge(left, right):
    result = []

    pLeft = 0
    pRight = 0

    while pLeft < len(left) and pRight < len(right):
        if left[pLeft] < right[pRight]:
            result.append(left[pLeft])
            pLeft += 1
        else:
            result.append(right[pRight])
            pRight += 1

    result = result + left[pLeft:]
    result = result + right[pRight:]
    return result


# Given an unsorted array, break it into a left and right array
# and recursively call this function on both. When the arrays are small
# enough, sort them manually. Then call merge() on the left and right arrays,
# which are not sorted
def mergeSort(arr):
    if len(arr) < 2:
        return arr

    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        return [arr[1], arr[0]]

    pivot = int(len(arr) / 2)
    
    left = arr[0:pivot]
    right = arr[pivot:]

    
    return merge(mergeSort(left), mergeSort(right))

# test cases

for x in range(100):
    arrLen = random.randint(0, 10)
    arr = [0] * arrLen
    for a in range(arrLen):
        arr[a] = random.randint(0, 10)

    print("Test case", x, arr)
    assert sorted(arr) == mergeSort(arr)