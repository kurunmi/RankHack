import random
def __init__(self, w):
    self.w = w
    self.count = len(w) -1
    self.sum = 0
    for x in w:
        self.sum += x


    def pickIndex():
        prob = 0
        while not prob:
            prob = w[random.randint(0, self.count)]
