#!/usr/bin/python3


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.positions = {}
        self.lookup = {}
        self.count = 0
        self.oldest = 0
        # Write your code here
        return
    def get(self, x):
        if x in self.storage:
            self.update_pos(x)
            return self.storage[x]
        return -1
        # Write your code here


    def do_set(self, x, y):
        self.storage[x] = y
        self.positions[self.count] = x
        self.lookup[x] = self.count
        self.count += 1

    def update_pos(self, x):
        oldpos = self.lookup[x]
        del self.positions[oldpos]
        self.positions[self.count] = x
        self.lookup[x] = self.count
        self.count += 1
        if oldpos == self.oldest:
            while self.oldest not in self.positions:
                self.oldest += 1

    def update_val(self, x, y):
        self.update_pos(x)
        self.storage[x] = y


    def set(self, x, y):
        print(self.storage, self.oldest, self.positions, x, y)
        if len(self.storage) < self.capacity:
            if x in self.storage:
                self.update_val(x, y)
            else:
                self.do_set(x, y)
        else:
            oldest_key = self.positions[self.oldest]
            del self.storage[oldest_key]
            del self.positions[self.oldest]
            while self.oldest not in self.positions:
                self.oldest += 1
            if x in self.storage:
                self.update_val(x, y)
            else:
                self.do_set(x, y)


if __name__ == '__main__':
    cache = LRUCache(5)
    print(cache.get(2))
    cache.set(1, 2)
    cache.set(1, 2)
    cache.set (2, 22)
    cache.set(3, 23)
    cache.set(4, 33)
    cache.set(2, 22)
    print(cache.get(4))
    cache.set(5, 44)
    cache.set(6, 44)
    cache.set(12, 41)
    cache.set(4,    'xyz')
    cache.set(6, 44)
    print(cache.get(4))