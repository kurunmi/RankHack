#!/usr/bin/python3
def looptest(r):
    x = len(r)
    i =0
    while i < x-1:
        y = x - (1+i)
        val = r[i]
        val1 = r[y]
        print(x, y, i, val1, val, r)
        i += 1


if __name__ == '__main__':
    print(looptest([1,6,10,8,7,3,2]))