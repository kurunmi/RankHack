class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    stream = OddStream() if stream else EvenStream()
    for _ in range(n):
        print(stream.get_next())


#queries = int(input())
if __name__ == '__main__':
    queries = ['even 2', 'even 2']
    for item in queries:
        stream_name, n = item.split()
        n = int(n)
        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())
