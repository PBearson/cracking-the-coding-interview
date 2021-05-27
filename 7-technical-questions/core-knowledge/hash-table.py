import random

class HashTable:
    def __init__(self):
        self.table = {}

    def hash(self, value):
        assert type(value) == str
        sum = 0
        for v in value:
            sum += ord(v)
        return sum % 1000

    def insert(self, value):
        index = self.hash(value)
        try:
            if not self.find(value):
                self.table[index].append(value)
        except KeyError:
            self.table[index] = [value]

    def find(self, value):
        index = self.hash(value)
        try:
            for s in self.table[index]:
                if s == value:
                    return True
            return False
        except KeyError:
            return False

    def remove(self, value):
        if not self.find(value):
            return
        index = self.hash(value)
        try:
            for i in range(len(self.table[index])):
                s = self.table[index][i]
                if s == value:
                    self.table[index].pop(i)
                    if len(self.table[index]) == 0:
                        self.table.pop(index)
                    return
        except KeyError:
            return


def test():
    ht = HashTable()
    alphanum = "abc"

    for i in range(10):
        newString = "".join(random.sample(alphanum, 2))
        ht.insert(newString)

    print(ht.table)
    
    ht.remove("ab")
    print(ht.table)
    ht.remove("ba")
    print(ht.table)
    ht.remove("ab")
    print(ht.table)

if __name__ == "__main__":
    test()