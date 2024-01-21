#!/usr/bin/python
import random


class RandomizedSet(object):

    def __init__(self):
        self.set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set.add(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            return False
        self.set.remove(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        index = random.randrange(0, len(self.set))
        return list(self.set)[index]

if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1))
    print(randomizedSet.remove(2))
    print(randomizedSet.insert(2))
    print(randomizedSet.getRandom())
    print(randomizedSet.remove(1))
    print(randomizedSet.insert(2))
    print(randomizedSet.getRandom())

