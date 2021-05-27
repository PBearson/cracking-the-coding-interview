import heapq as hq
import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        hq.heappush(self.heap, value)

    def pop(self):
        return hq.heappop(self.heap)

    def find(self, value):
        for i in range(len(self.heap)):
            if self.heap[i] == value:
                return i
        return -1

    def remove(self, value):
        index = self.find(value)
        if index == -1:
            return
        self.heap.pop(index)
        hq.heapify(self.heap)


def test():
    pq = MinHeap()
    for i in range(1, 10):
        pq.insert(random.randint(1, 10))
        
    print(pq.heap)
    pq.remove(4)
    print(pq.heap)


if __name__ == "__main__":
    test()