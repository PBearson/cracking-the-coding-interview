import random
import math
import time

def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while True:
        while i<= j and arr[j] >= pivot:
                j -= 1
        while i<= j and arr[i] <= pivot:
                i += 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[left], arr[j] = arr[j], arr[left]
    return j
        

def quickSortHelper(arr, left, right):
    if left >= right:
        return arr
    
    part = partition(arr, left, right)

    quickSortHelper(arr, left, part - 1)
    quickSortHelper(arr, part + 1, right)

    return arr


def quickSort(arr):
    return quickSortHelper(arr, 0, len(arr) - 1)


# test

for x in range(100):
    arrLen = random.randint(0, 10)
    arr = [0] * arrLen
    for a in range(arrLen):
        arr[a] = random.randint(0, 10)

    print("Test case", x, arr, quickSort(arr))
    assert sorted(arr) == quickSort(arr)