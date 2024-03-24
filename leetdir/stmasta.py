#import random
import random


class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.pos = []

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data[val] = len(self.pos)
        self.pos.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.data:
            dataindex, lastel = self.data[val], self.pos[-1]
            self.pos[dataindex], self.data[lastel] =lastel, dataindex
            self.pos.pop()
            del self.data[val]
            return True
        return False

    def getRandom(self) -> int:
        return(random.choice(list(self.data.keys())))


if __name__ == '__main__':
    mset = RandomizedSet()
    print(mset.insert(1))
    print(mset.pos)
    print(mset.remove(2))
    print(mset.insert(2))
    print(mset.pos)
    print(mset.data)
    print(mset.getRandom())
    print("random")
    print(mset.remove(1))
    print(mset.pos)
    print(mset.data)
    print(mset.insert(2))
    print(mset.pos)
    print(mset.data)
    print(mset.getRandom())




