class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def put(self, key, value):
        if len(self.cache) < self.capacity:
            if key in self.cache:
                del(self.cache[key])
            self.cache[key] = value
        else:
            if key in self.cache:
                del(self.cache[key])
                self.cache[key] = value
            else:
                first_key, first_value = next(iter(self.cache.items()))
                del (self.cache[first_key])
                self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            val = self.cache[key]
            del(self.cache[key])
            self.cache[key] = val
            return val


        pass


    def get(self, key):
        pass

