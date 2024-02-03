


def __init__(self):
    self.stack = []
    self.minstack = []

def push(val):
    self.stack.push(val)
    if not self.minstack:
        self.minstack.push(val)
    else:
        if val <= self.minstack[-1]:
            self.minstack.push(val)


def pop():
    if self.stack[-1] == self.minstack[-1]:
        self.minstack.pop()
    self.stack.pop()

def


def getiMin(stack):
    return sorted(stack)[0]

if __name__ == '__main__':
    stack = [1,2,5,4,7,-2]
    print(getiMin(stack))