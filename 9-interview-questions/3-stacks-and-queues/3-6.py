# An animal shelter holds dogs and cats and operates in FIFO manner. 
# People can adopt the "oldest" (in terms of arrival time) animal, or specifically
# the "oldest" cat or the "oldest" dog. Create data structures to maintain this system. Implement the following:
# enqueue(): Add a new animal to the queue
# dequeueAny(): Remove the oldest animal from the queue
# dequeueDog(): Remove the oldest dog from the queue
# RemoveCat(): Remove the oldest cat from the queue
# 
# It would help to just have 2 separate queues, one for dogs and one for cats. We how "old" they are by indexing them.

from queue import Queue
import random

class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

        self.cats.remove()
        self.dogs.remove()
    
    def enqueue(self, animal):
        if self.cats.isEmpty() and self.dogs.isEmpty():
            index = 0
        elif self.cats.isEmpty():
            index = self.dogs.last.value + 1
        elif self.dogs.isEmpty():
            index = self.cats.last.value + 1
        else:
            index = max(self.cats.last.value, self.dogs.last.value) + 1
        if animal.lower() == "cat":
            self.cats.add(index)
        elif animal.lower() == "dog":
            self.dogs.add(index)

    def dequeueAny(self):
        if self.cats.isEmpty() and self.dogs.isEmpty():
            return
        elif self.cats.isEmpty():
            self.dogs.pop()
        elif self.dogs.isEmpty():
            self.cats.pop()
        else:
            if self.cats.peek() < self.dogs.peek():
                self.cats.remove()
            else:
                self.dogs.remove()

    def dequeueDog(self):
        self.dogs.remove()

    def dequeueCat(self):
        self.cats.remove()

    def peek(self):
        if self.cats.isEmpty() and self.dogs.isEmpty():
            return None
        elif self.cats.isEmpty():
            return self.dogs.peek()
        elif self.dogs.isEmpty():
            return self.cats.peek()
        else:
            return min(self.cats.peek(), self.dogs.peek())

animals = AnimalShelter()
for i in range(50):
    selector = random.choice(["dog", "cat"])
    animals.enqueue(selector)
animals.dogs.traverse()
animals.cats.traverse()

animals.dequeueAny()
animals.dequeueAny()
animals.dequeueAny()


print("")
animals.dogs.traverse()
animals.cats.traverse()

animals.dequeueDog()
animals.dequeueCat()

print("")
animals.dogs.traverse()
animals.cats.traverse()

animals.enqueue("cat")
animals.enqueue("cat")
animals.enqueue("dog")

print("")
animals.dogs.traverse()
animals.cats.traverse()

print("Peek", animals.peek())