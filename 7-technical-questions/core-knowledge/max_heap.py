import heapq as hq
import random

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        hq.heappush(self.heap, -1 * value)

    def pop(self):
        return -1 * hq.heappop(self.heap)

    def find(self, value):
        for i in range(len(self.heap)):
            if -1 * self.heap[i] == value:
                return i
        return -1

    def remove(self, value):
        index = self.find(value)
        if index == -1:
            return
        self.heap.pop(index)
        hq.heapify(self.heap)

    def printHeap(self):
        print([-1 * h for h in self.heap])


def test():
    pq = MaxHeap()
    for i in range(1, 10):
        pq.insert(random.randint(1, 10))
        
    pq.printHeap()
    pq.remove(4)
    pq.printHeap()


if __name__ == "__main__":
    test()