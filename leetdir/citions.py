#!/usr/bin/python

def citons(citations):
    citations = sorted(citations, reverse=True)
    count = 0
    size = len(citations) -1
    if size == 0:
        return 0
    for index, value in enumerate(citations):
        if index < value:
            return index
    return index + 1
#        print(x, y)
#    for i in range(size):
 #       if citations[i] >= i:
 #           count = i + 1
 #   return count

if __name__ == '__main__':
    print(citons([0]))